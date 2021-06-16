from app import models
from background_task import background
from django.db.models import Q
import numpy as np
import pandas as pd
from scipy import sparse
from sklearn.metrics.pairwise import cosine_similarity
import subprocess
import shlex
from app.models import Role, Status
from surprise import Reader, Dataset, KNNBasic


# Calculate hotel similarity
class CollaborativeFiltering():
    def __init__(self, train_data, neighbors, similarity_function=cosine_similarity):
        self.train_data = train_data
        self.normalized_data = None
        self.similarity_function = similarity_function
        self.neighbors = neighbors
        self.n_items = int(np.max(self.train_data[:, 1])) + 1
        self.n_users = int(np.max(self.train_data[:, 0])) + 1

    def fit(self):
        self.normalized_data = self.train_data.copy().astype('float64')
        users = self.train_data[:, 0]
        self.mean_rating_matrix = np.zeros((self.n_users,))
        for u in range(self.n_users):
            indices = np.where(users == u)[0].astype(np.int32)
            ratings = self.train_data[indices, 2]
            self.mean_rating_matrix[u] = np.mean(ratings) if indices.size > 0 else 0
            self.normalized_data[indices, 2] = ratings - self.mean_rating_matrix[u]

        self.normalized_data = sparse.coo_matrix((self.normalized_data[:, 2], (self.normalized_data[:, 1], self.normalized_data[:, 0])),
                                                 (self.n_items, self.n_users)).tocsr()

        self.similarity_matrix = self.similarity_function(self.normalized_data.T, self.normalized_data.T)


@background(schedule=60)
def demo_task():
    # Get user and hotel list
    hotels = models.Hotel.objects.all()
    users = models.User.objects.filter(role=Role.USER)
    # Create dicts to mapping uuid to positive integer number
    hotels_ids = dict()
    users_ids = dict()
    count = 0
    for hotel in hotels:
        count = count + 1
        hotels_ids[hotel.uuid] = count

    count = 0
    for user in users:
        count = count + 1
        users_ids[user.uuid] = count

    # Get review list
    reviews_list = []
    reviews = models.Review.objects.filter(hotel__isnull=False, user__isnull=False)
    # Save tuple of user id, hotel id and rating to a list
    for review in reviews:
        user_id = review.user.uuid
        hotel_id = review.hotel.uuid
        latest_created = review.created
        temp_reviews = models.Review.objects.filter(user_id=user_id, hotel_id=hotel_id)
        for temp in temp_reviews:
            if latest_created < temp.created:
                latest_created = temp.created
        latest_review = models.Review.objects.filter(user_id=user_id, hotel_id=hotel_id, created=latest_created)[0]
        tup = (users_ids[user_id], hotels_ids[hotel_id], latest_review.rating)
        reviews_list.append(tup)

    reviews_list = list(set(reviews_list))

    if reviews_list:
        # Change list to dataframe, and then to numpy array
        ratings_dataset = pd.DataFrame(reviews_list, columns=['user_id', 'item_id', 'rating'])
        ratings_train = ratings_dataset.to_numpy()
        # index starts from 0
        ratings_train[:, :2] -= 1

        # Swap user id column and hotel id column for item-item CF
        ratings_train = ratings_train[:, [1, 0, 2]]
        # Run item-item CF with neighbors = 40
        recommend_model = CollaborativeFiltering(ratings_train, neighbors=40)
        recommend_model.fit()
        # Get similarity matrix of hotels
        sim_matrix = recommend_model.similarity_matrix

        n_rows, n_cols = sim_matrix.shape
        tmp_data = {}
        key_hotels_ids = list(hotels_ids.keys())
        val_hotels_ids = list(hotels_ids.values())
        # Save similarity matrix to database
        null_hotels = models.Recommendation.objects.filter(hotel__isnull=True)
        for null_hotel in null_hotels:
            null_hotel.delete()

        null_collation_hotels = models.Recommendation.objects.filter(collation_hotel__isnull=True)
        for null_collation_hotel in null_collation_hotels:
            null_collation_hotel.delete()

        for i in range(n_rows - 1):
            for j in range(i + 1, n_cols):
                pos = val_hotels_ids.index(i + 1)
                tmp_data['hotel_id'] = key_hotels_ids[pos]
                pos = val_hotels_ids.index(j + 1)
                tmp_data['collation_hotel_id'] = key_hotels_ids[pos]
                tmp_data['similarity'] = float(sim_matrix[i, j])
                current_recommendation = models.Recommendation.objects.filter(
                    Q(hotel_id=tmp_data['hotel_id']) & Q(collation_hotel_id=tmp_data['collation_hotel_id'])
                ).first()
                if not current_recommendation:
                    # Create similarity
                    recommendation = models.Recommendation(**tmp_data)
                    recommendation.save()
                else:
                    # Or update if existed
                    current_recommendation.similarity = tmp_data['similarity']
                    current_recommendation.save()


@background(schedule=60)
def calculate_sim():
    # Get user and hotel list
    hotels = models.Hotel.objects.filter(status=Status.ACTIVE)
    users = models.User.objects.filter(role=Role.USER)
    # Create dicts to mapping uuid to positive integer number
    hotels_ids = dict()
    users_ids = dict()
    count = 0
    for hotel in hotels:
        count = count + 1
        hotels_ids[hotel.uuid] = count

    count = 0
    for user in users:
        count = count + 1
        users_ids[user.uuid] = count

    reviews_list = []
    reviews = models.Review.objects.filter(hotel__isnull=False, user__isnull=False)
    # Save tuple of user id, hotel id and rating to a list
    for review in reviews:
        user_id = review.user.uuid
        hotel_id = review.hotel.uuid
        latest_created = review.created
        temp_reviews = models.Review.objects.filter(user_id=user_id, hotel_id=hotel_id)
        for temp in temp_reviews:
            if latest_created < temp.created:
                latest_created = temp.created
        latest_review = models.Review.objects.filter(user_id=user_id, hotel_id=hotel_id, created=latest_created)[0]
        # tup = (user_id, hotel_id, latest_review.rating)
        tup = (users_ids[user_id], hotels_ids[hotel_id], latest_review.rating)
        reviews_list.append(tup)

    reviews_list = list(set(reviews_list))

    if reviews_list:
        # Change list to dataframe, and then to numpy array
        ratings = pd.DataFrame(reviews_list, columns=['user_id', 'item_id', 'rating'])

        # Add for calculate pearson using cosine
        train_data = ratings.to_numpy()
        n_rows, n_cols = train_data.shape

        # normalized_data = train_data.copy()
        normalized_data = np.ndarray((n_rows, n_cols), dtype=object)
        for r in range(n_rows):
            normalized_data[r, 0] = train_data[r, 0]
            normalized_data[r, 1] = train_data[r, 1]
            normalized_data[r, 2] = float(train_data[r, 2])

        # User mean, for adjust cosine
        # users = train_data[:, 0]
        # n_users = int(np.max(train_data[:, 0]))
        # mean_rating_matrix = np.zeros((n_users + 1,))
        # for u in range(1, n_users + 1):
        #     indices = np.where(users == u)[0].astype(np.int32)
        #     temp_ratings = train_data[indices, 2]
        #     # temp_ratings = [float(temp) for temp in train_data[indices, 2]]
        #     mean_rating_matrix[u] = np.mean(temp_ratings) if indices.size > 0 else 0
        #     normalized_data[indices, 2] = temp_ratings - mean_rating_matrix[u]

        # Item mean, for pearson
        items = train_data[:, 1]
        n_items = int(np.max(train_data[:, 1]))
        mean_rating_matrix = np.zeros((n_items + 1,))
        for i in range(1, n_items + 1):
            indices = np.where(items == i)[0].astype(np.int32)
            temp_ratings = train_data[indices, 2]
            # temp_ratings = [float(temp) for temp in train_data[indices, 2]]
            mean_rating_matrix[i] = np.mean(temp_ratings) if indices.size > 0 else 0
            normalized_data[indices, 2] = temp_ratings - mean_rating_matrix[i]

        key_hotels_ids = list(hotels_ids.keys())
        val_hotels_ids = list(hotels_ids.values())
        key_users_ids = list(users_ids.keys())
        val_users_ids = list(users_ids.values())
        for r in range(n_rows):
            pos = val_users_ids.index(normalized_data[r, 0])
            normalized_data[r, 0] = key_users_ids[pos]
            pos = val_hotels_ids.index(normalized_data[r, 1])
            normalized_data[r, 1] = key_hotels_ids[pos]

        new_ratings = pd.DataFrame(normalized_data, columns=['user_id', 'item_id', 'rating'])

        reader = Reader()

        # ratings --> new_ratings
        data = Dataset.load_from_df(new_ratings[['user_id', 'item_id', 'rating']], reader)
        trainset = data.build_full_trainset()

        # pearson --> cosine
        sim_options = {'name': 'cosine', 'user_based': False}
        algo = KNNBasic(sim_options=sim_options)
        algo.fit(trainset)
        sim_matrix = algo.sim

        null_hotels = models.Recommendation.objects.filter(hotel__isnull=True)
        for null_hotel in null_hotels:
            null_hotel.delete()

        null_collation_hotels = models.Recommendation.objects.filter(collation_hotel__isnull=True)
        for null_collation_hotel in null_collation_hotels:
            null_collation_hotel.delete()

        n_rows, n_cols = sim_matrix.shape
        tmp_data = {}
        for i in range(n_rows - 1):
            for j in range(i + 1, n_cols):
                tmp_data['hotel_id'] = algo.trainset.to_raw_iid(i)
                tmp_data['collation_hotel_id'] = algo.trainset.to_raw_iid(j)
                tmp_data['similarity'] = float(sim_matrix[i, j])
                first_current_recommendation = models.Recommendation.objects.filter(
                    Q(hotel_id=tmp_data['hotel_id']) & Q(collation_hotel_id=tmp_data['collation_hotel_id'])
                ).first()
                second_current_recommendation = models.Recommendation.objects.filter(
                    Q(hotel_id=tmp_data['collation_hotel_id']) & Q(collation_hotel_id=tmp_data['hotel_id'])
                ).first()
                if (not first_current_recommendation) and (not second_current_recommendation):
                    # Create similarity
                    recommendation = models.Recommendation(**tmp_data)
                    recommendation.save()
                else:
                    # Or update if existed
                    if first_current_recommendation:
                        first_current_recommendation.similarity = tmp_data['similarity']
                        first_current_recommendation.save()
                    else:
                        second_current_recommendation.similarity = tmp_data['similarity']
                        second_current_recommendation.save()


# Run background task without command
def process_tasks():
    process_tasks_cmd = "python manage.py process_tasks"
    process_tasks_args = shlex.split(process_tasks_cmd)
    process_tasks_subprocess = subprocess.Popen(process_tasks_args)
