import random
from app.models import User, Role, Hotel, Review, Status
from app.migrations.seeders.user_seeder import UserSeeder
from app.migrations.seeders.hotel_seeder import HotelSeeder
from app.utils.seeder_maker import BaseSeeder
from faker import Faker
from faker_enum import EnumProvider
import os
import pandas as pd
import re
import math


# Seed data for review
class ReviewSeeder(BaseSeeder):
    OBJECT_NUMBER = 5000
    REQUIRED_SEEDERS = [UserSeeder, HotelSeeder]

    def run(self, stdout, _):
        filename = 'data/data.csv'
        dataset = pd.read_csv(filename)
        data_len = dataset.shape[0]
        regex = re.compile('^[a-zA-Z0-9.,!\t\n\r ]*$')
        faker = Faker()
        faker.add_provider(EnumProvider)
        hotels = Hotel.objects.filter(status=Status.ACTIVE)
        users = User.objects.filter(role=Role.USER, is_active=True)

        for i in range(self.OBJECT_NUMBER):
            row = random.randrange(2, data_len + 1)
            while regex.search(str(dataset.iloc[row]['reviews.title'])) is None \
                    or regex.search(str(dataset.iloc[row]['reviews.text'])) is None \
                    or math.isnan(dataset.iloc[row]['reviews.rating']):
                row = random.randrange(2, data_len + 1)
            title = dataset.iloc[row]['reviews.title']
            content = dataset.iloc[row]['reviews.text']
            rating = int(dataset.iloc[row]['reviews.rating'])
            if rating < 1:
                rating = 1
            if rating > 5:
                rating = 5
            hotel = random.choice(hotels)
            user = random.choice(users)
            created = faker.date_time_between(hotel.created, 'now')
            review = Review(title=title, content=content, rating=rating,
                            user_id=user.uuid, hotel_id=hotel.uuid, created=created, updated=created)
            review.save()
            stdout.write(str(review))
