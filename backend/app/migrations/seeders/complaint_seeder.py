# import random
# from app.models import User, Role, Complaint, Hotel, Status
# from app.migrations.seeders.user_seeder import UserSeeder
# from app.migrations.seeders.hotel_seeder import HotelSeeder
# # from app.migrations.seeders.booking_seeder import BookingSeeder
# from app.utils.seeder_maker import BaseSeeder
# from faker import Faker
# from faker_enum import EnumProvider
#
#
# # Seed data for complaint
# class ComplaintSeeder(BaseSeeder):
#     OBJECT_NUMBER = 50
#     REQUIRED_SEEDERS = [UserSeeder, HotelSeeder]
#
#     def run(self, stdout, _):
#         faker = Faker()
#         faker.add_provider(EnumProvider)
#         users = User.objects.filter(role=Role.USER, is_active=True)
#         # hotels = Hotel.objects.filter(is_active=True)
#         hotels = Hotel.objects.filter(status=Status.ACTIVE)
#
#         for i in range(self.OBJECT_NUMBER):
#             user = random.choice(users)
#             # while user.bookings.count() == 0:
#             #     user = random.choice(users)
#             hotel = random.choice(hotels)
#             created = faker.date_time_between(hotel.created, 'now')
#             complaint = Complaint(title=faker.paragraph(), content=faker.text(),
#                                   user_id=user.uuid, hotel_id=hotel.uuid, created=created, updated=created)
#             complaint.save()
#             self.image_maker(name=f'{faker.word()}.png', obj=complaint)
#             stdout.write(str(complaint))
