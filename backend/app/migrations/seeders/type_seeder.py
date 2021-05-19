from app.models import Hotel, RoomAmenity, Type
from app.migrations.seeders.hotel_seeder import HotelSeeder
from app.utils.seeder_maker import BaseSeeder
from faker import Faker
from faker_enum import EnumProvider


class TypeSeeder(BaseSeeder):
    REQUIRED_SEEDERS = [HotelSeeder]

    def run(self, stdout, _):
        faker = Faker()
        faker.add_provider(EnumProvider)
        hotels = Hotel.objects.filter(is_active=True)
        capacity = {'single': '1', 'double': '2', 'twin': '3', 'double double': '4'}
        price = {'single': '1000000', 'double': '2000000', 'twin': '3000000', 'double double': '4000000'}
        amenities = {'single': [RoomAmenity.WIFI, RoomAmenity.BATHROBES],
                     'double': [RoomAmenity.WIFI, RoomAmenity.BATHROBES, RoomAmenity.TISSUE_BOX],
                     'twin': [RoomAmenity.WIFI, RoomAmenity.BATHROBES, RoomAmenity.TISSUE_BOX, RoomAmenity.COFFEE_KIT],
                     'double double': [RoomAmenity.WIFI, RoomAmenity.BATHROBES, RoomAmenity.TISSUE_BOX,
                                       RoomAmenity.COFFEE_KIT, RoomAmenity.PERSONAL_CARE]}
        for hotel in hotels:
            created = faker.date_time_between(hotel.created, 'now')
            for key in capacity:
                room_type = Type(room_type=key, capacity=capacity[key], price=price[key], amenities=amenities[key],
                                 hotel_id=hotel.uuid, created=created, updated=created)
                room_type.save()
                stdout.write(str(hotel))

