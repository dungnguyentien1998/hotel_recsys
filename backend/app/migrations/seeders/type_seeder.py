from app.models import Hotel, RoomAmenity, Type, Status
from app.migrations.seeders.hotel_seeder import HotelSeeder
from app.utils.seeder_maker import BaseSeeder
from faker import Faker
from faker_enum import EnumProvider


class TypeSeeder(BaseSeeder):
    REQUIRED_SEEDERS = [HotelSeeder]

    def run(self, stdout, _):
        faker = Faker()
        faker.add_provider(EnumProvider)
        hotels = Hotel.objects.filter(status=Status.ACTIVE)
        capacity = {'single': 1, 'double': 2, 'twin': 3, 'double double': 4}
        adult_number = {'single': 1, 'double': 2, 'twin': 3, 'double double': 4}
        children_number = {'single': 0, 'double': 0, 'twin': 1, 'double double': 2}
        price = {'single': '1000000', 'double': '2000000', 'twin': '3000000', 'double double': '4000000'}
        area = {'single': 50, 'double': 60, 'twin': 65, 'double double': 70}
        amenities = {
            'single': [RoomAmenity.WIFI, RoomAmenity.BATHROBES, RoomAmenity.CLOTHES_RACK,
                       RoomAmenity.TOILETRIES, RoomAmenity.REFRIGERATOR, RoomAmenity.ELECTRIC_KETTLE],
            'double': [RoomAmenity.WIFI, RoomAmenity.BATHROBES, RoomAmenity.COFFEE_KIT, RoomAmenity.CLOTHES_RACK,
                       RoomAmenity.TOILETRIES, RoomAmenity.BATHTUB, RoomAmenity.REFRIGERATOR, RoomAmenity.ELECTRIC_KETTLE],
            'twin': [RoomAmenity.WIFI, RoomAmenity.BATHROBES, RoomAmenity.COFFEE_KIT, RoomAmenity.CLOTHES_RACK,
                     RoomAmenity.TOILETRIES, RoomAmenity.BATHTUB, RoomAmenity.REFRIGERATOR,
                     RoomAmenity.HAIR_DRYER, RoomAmenity.ELECTRIC_KETTLE],
            'double double': [RoomAmenity.WIFI, RoomAmenity.BATHROBES, RoomAmenity.TISSUE_BOX, RoomAmenity.COFFEE_KIT,
                              RoomAmenity.CLOTHES_RACK, RoomAmenity.TOILETRIES, RoomAmenity.BATHTUB,
                              RoomAmenity.REFRIGERATOR, RoomAmenity.HAIR_DRYER, RoomAmenity.ELECTRIC_KETTLE]}
        for hotel in hotels:
            created = faker.date_time_between(hotel.created, 'now')
            for key in capacity:
                room_type = Type(name=key, price=price[key], amenities=amenities[key],
                                 hotel_id=hotel.uuid, created=created, updated=created,
                                 children_number=children_number[key], adult_number=adult_number[key], area=area[key])
                room_type.save()
                stdout.write(str(hotel))

