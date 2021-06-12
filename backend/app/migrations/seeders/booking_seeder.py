import random
from app.models import User, Role, Room, Booking, Hotel, Status, Type, BookingType
from app.migrations.seeders.user_seeder import UserSeeder
from app.migrations.seeders.room_seeder import RoomSeeder
from app.migrations.seeders.type_seeder import TypeSeeder
from app.migrations.seeders.hotel_seeder import HotelSeeder
from app.utils.seeder_maker import BaseSeeder
from faker import Faker
from faker_enum import EnumProvider
import datetime


# Seed data for booking
class BookingSeeder(BaseSeeder):
    OBJECT_NUMBER = 500
    REQUIRED_SEEDERS = [UserSeeder, HotelSeeder, TypeSeeder, RoomSeeder]

    def run(self, stdout, _):
        faker = Faker()
        faker.add_provider(EnumProvider)
        hotels = Hotel.objects.filter(status=Status.ACTIVE)
        hotel = random.choice(hotels)
        users = User.objects.filter(role=Role.USER, is_active=True)
        # now = datetime.datetime.now()
        start_date = datetime.date(year=2021, month=1, day=1)
        end_date = datetime.date(year=2021, month=4, day=29)
        for i in range(self.OBJECT_NUMBER):
            now = faker.date_time_between(start_date, end_date)
            microsecond = datetime.datetime.now().microsecond
            now = now + datetime.timedelta(microseconds=microsecond)
            now_string = now.strftime("%Y-%m-%d %H:%M:%S")
            year = str(now.year)
            month = str(now.month)
            day = str(now.day)
            year = year[2:len(year)]
            if len(month) == 1:
                month = "0" + month
            if len(day) == 1:
                day = "0" + day
            hour = str(now.hour)
            minute = str(now.minute)
            second = str(now.second)
            microsecond = str(now.microsecond)
            if len(hour) == 1:
                hour = "0" + hour
            if len(minute) == 1:
                minute = "0" + minute
            if len(second) == 1:
                second = "0" + second
            microsecond = microsecond[0:4]
            code = year + month + day + hour + minute + second + microsecond
            user = random.choice(users)
            start_date = datetime.date(year=2021, month=4, day=30)
            end_date = datetime.date(year=2021, month=5, day=1)
            check_in_time = faker.date_time_between(start_date, end_date)
            start_date = datetime.date(year=2021, month=5, day=2)
            end_date = datetime.date(year=2021, month=5, day=3)
            check_out_time = faker.date_time_between(start_date, end_date)

            booking_count = 1
            total_price = 0
            delta = check_out_time - check_in_time
            room_type = Type.objects.filter(name='single', hotel_id=hotel.uuid)[0]
            total_price = total_price + room_type.price * booking_count * delta.days

            booking = Booking(check_in_time=check_in_time, check_out_time=check_out_time, user_id=user.uuid,
                              created=now, updated=now, code=code, hotel_id=hotel.uuid, total_price=total_price)
            booking.save()

            booking_type = BookingType(booking_id=booking.uuid, type_id=room_type.uuid, count=booking_count)
            booking_type.save()
            stdout.write(str(booking))
