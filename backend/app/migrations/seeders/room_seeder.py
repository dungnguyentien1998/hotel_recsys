import random
import exrex
from app.models import Hotel, Room, Type
from app.migrations.seeders.hotel_seeder import HotelSeeder
from app.migrations.seeders.type_seeder import TypeSeeder
from app.utils.seeder_maker import BaseSeeder
from faker import Faker
from faker_enum import EnumProvider


# Seed data for room
class RoomSeeder(BaseSeeder):
    OBJECT_NUMBER = 500
    REQUIRED_SEEDERS = [HotelSeeder, TypeSeeder]

    def run(self, stdout, _):
        faker = Faker()
        faker.add_provider(EnumProvider)
        hotels = Hotel.objects.all()

        for hotel in hotels:
            room_types = Type.objects.filter(hotel_id=hotel.uuid)
            for room_type in room_types:
                room_number = exrex.getone(r'\d{3}')
                while Room.objects.filter(room_number=room_number, hotel_id=hotel.uuid):
                    room_number = exrex.getone(r'\d{3}')
                created = faker.date_time_between(hotel.created, 'now')
                room = Room(room_number=room_number, hotel_id=hotel.uuid, type_id=room_type.uuid,
                            created=created, updated=created)
                room.save()
                self.image_maker(name=f'{faker.word()}.png', obj=room, folder='room')
                stdout.write(str(room))

        # for i in range(self.OBJECT_NUMBER):
        #     hotel = random.choice(hotels)
        #     room_types = Type.objects.filter(hotel_id=hotel.uuid)
        #     room_type = random.choice(room_types)
        #     room_number = exrex.getone(r'\d{3}')
        #     while Room.objects.filter(room_number=room_number):
        #         room_number = exrex.getone(r'\d{3}')
        #     created = faker.date_time_between(hotel.created, 'now')
        #     room = Room(room_number=room_number, hotel_id=hotel.uuid, type_id=room_type.uuid,
        #                 created=created, updated=created)
        #     room.save()
        #     self.image_maker(name=f'{faker.word()}.png', obj=room, folder='room')
        #     stdout.write(str(room))
