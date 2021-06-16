import random
from app.models import Hotel, HotelAmenity, User, Role, Status
from app.migrations.seeders.user_seeder import UserSeeder
from app.utils.seeder_maker import BaseSeeder
from faker import Faker
import exrex
import json
import pandas as pd


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
        cities_code = ['01', '79', '92']
        cities_name = ['Thành phố Hà Nội', 'Thành phố Hồ Chí Minh', 'Thành phố Cần Thơ']
        f = open('data/db_vi.txt', )
        data = json.load(f)

        filename = 'data/data.csv'
        dataset = pd.read_csv(filename)
        data_len = dataset.shape[0]
        for i in range(self.OBJECT_NUMBER):
            row = random.randrange(2, data_len - 1)
            name = dataset.iloc[row]['name']
            email = faker.email()
            while Hotel.objects.filter(email=email):
                email = faker.email()
            hotelier = random.choice(hoteliers)
            # while hotelier.hotels.count() > 5:
            #     hotelier = random.choice(hoteliers)
            created = faker.date_time_between(hotelier.created, 'now')
            index = random.randrange(0, 3)
            city_code = cities_code[index]
            city_name = cities_name[index]
            district = random.choice([d for d in data['district'] if d['idProvince'] == city_code])
            district_code = district['idDistrict']
            district_name = district['name']
            ward = random.choice([w for w in data['commune'] if w['idDistrict'] == district_code])
            ward_name = ward['name']

            address = random.choice(addresses)
            hotel = Hotel(name=faker.name(), star=random.randrange(2, 5) + 1, city=city_name,
                          district=district_name, ward=ward_name, address='',
                          amenities=[amenity[0] for amenity in
                                     random.sample(HotelAmenity.choices, k=random.randrange(5, len(HotelAmenity.choices)) + 1)],
                          user_id=hotelier.uuid, created=created, updated=created,
                          status=random.choices(population=[Status.ACTIVE, Status.PENDING], weights=(90, 10))[0],
                          email=email, tel=exrex.getone(r'0\d{9}'))
            hotel.save()
            # hotel.image.save(f'{faker.word()}.png', self.image_maker())
            self.image_maker(name=f'{faker.word()}.png', obj=hotel)
            stdout.write(str(hotel))
