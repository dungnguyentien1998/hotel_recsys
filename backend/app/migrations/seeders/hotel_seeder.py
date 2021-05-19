import random
from app.models import Hotel, HotelAmenity, User, Role
from app.migrations.seeders.user_seeder import UserSeeder
from app.utils.seeder_maker import BaseSeeder
from faker import Faker


# Seed data for hotel
class HotelSeeder(BaseSeeder):
    OBJECT_NUMBER = 100
    REQUIRED_SEEDERS = [UserSeeder]

    def run(self, stdout, _):
        faker = Faker()
        hoteliers = User.objects.filter(role=Role.HOTELIER, is_active=True)
        addresses = [{'city': 'Thành phố Hà Nội', 'district': 'Quận Ba Đình', 'ward': 'Phường Phúc Xá', 'address': ''},
                     {'city': 'Thành phố Hà Nội', 'district': 'Quận Cầu Giấy', 'ward': 'Phường Nghĩa Đô', 'address': ''},
                     {'city': 'Thành phố Hà Nội', 'district': 'Quận Tây Hồ', 'ward': 'Phường Nhật Tân', 'address': ''},
                     {'city': 'Thành phố Hà Nội', 'district': 'Quận Hai Bà Trưng', 'ward': 'Phường Bạch Đằng', 'address': ''},
                     {'city': 'Thành phố Hà Nội', 'district': 'Quận Đống Đa', 'ward': 'Phường Văn Miếu', 'address': ''},
                     ]

        for i in range(self.OBJECT_NUMBER):
            hotelier = random.choice(hoteliers)
            created = faker.date_time_between(hotelier.created, 'now')
            address = random.choice(addresses)
            hotel = Hotel(name=faker.name(), star=random.randrange(2, 5) + 1, city=address['city'],
                          district=address['district'], ward=address['ward'], address=address['address'],
                          amenities=[amenity[0] for amenity in
                                     random.sample(HotelAmenity.choices, k=random.randrange(len(HotelAmenity.choices)) + 1)],
                          user_id=hotelier.uuid, created=created, updated=created,
                          is_active=random.choices(population=[True, False], weights=(90, 10)))
            hotel.save()
            # hotel.image.save(f'{faker.word()}.png', self.image_maker())
            self.image_maker(name=f'{faker.word()}.png', obj=hotel)
            stdout.write(str(hotel))
