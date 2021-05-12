import random
import exrex
from app.models import User, Role
from app.utils.seeder_maker import BaseSeeder
from faker import Faker
from faker_enum import EnumProvider


# Seed data for user
class UserSeeder(BaseSeeder):
    OBJECT_NUMBER = 1000
    ROLE_SEEDING_WEIGHTS = [0.7, 0.02, 0.28]
    REQUIRED_SEEDERS = []

    def run(self, stdout, _):
        faker = Faker()
        faker.add_provider(EnumProvider)
        addresses = [{'city': 'Thành phố Hà Nội', 'district': 'Quận Ba Đình', 'ward': 'Phường Phúc Xá', 'address': ''},
                     {'city': 'Thành phố Hà Nội', 'district': 'Quận Cầu Giấy', 'ward': 'Phường Nghĩa Đô', 'address': ''},
                     {'city': 'Thành phố Hà Nội', 'district': 'Quận Tây Hồ', 'ward': 'Phường Nhật Tân', 'address': ''},
                     {'city': 'Thành phố Hà Nội', 'district': 'Quận Hai Bà Trưng', 'ward': 'Phường Bạch Đằng', 'address': ''},
                     {'city': 'Thành phố Hà Nội', 'district': 'Quận Đống Đa', 'ward': 'Phường Văn Miếu', 'address': ''},
                     ]
        for i in range(self.OBJECT_NUMBER):
            email = faker.email()
            while User.objects.filter(email=email):
                email = faker.email()
            address = random.choice(addresses)
            birthday = faker.date_time()
            created = faker.date_time_between(birthday, 'now')

            user = User(email=email, name=faker.name(), tel=exrex.getone(r'0\d{9}'), birthday=birthday,
                        last_login=None, city=address['city'], district=address['district'],
                        ward=address['ward'], address=address['address'], password='',
                        role=random.choices(population=Role.choices, weights=self.ROLE_SEEDING_WEIGHTS)[0][0],
                        is_active=faker.boolean(), created=created, updated=created)
            self.image_maker(name=f'{faker.word()}.png', obj=user, folder='user')
            user.set_password('123456')
            user.save()
            stdout.write(str(user))
