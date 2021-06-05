from app.utils.seeder_maker import BaseSeeder
from django.core.management.base import CommandError, BaseCommand
from app.migrations.seeders import *


class Command(BaseCommand):
    help = 'Seed database'

    # Identify which seeder run first
    def dependency_resolver(self, _cls, _resolved, _unresolved):
        _unresolved.append(_cls)
        for dependency in _cls.REQUIRED_SEEDERS:
            if dependency not in _resolved:
                if dependency in _unresolved:
                    raise CommandError(f'Circular reference detected: {_cls.__name__} -> {dependency.__name__}')
                self.dependency_resolver(_cls=dependency, _resolved=_resolved, _unresolved=_unresolved)
        _resolved.append(_cls)

    # Run seeder after identify order
    def handle(self, *args, **options):
        _classes = BaseSeeder.__subclasses__()
        orders = []
        for _cls in _classes:
            if _cls not in orders:
                self.dependency_resolver(_cls, orders, [])
        self.stdout.write()
        for _cls in orders:
            _cls().run(self.stdout, self.stderr)
        # ReviewSeeder().run(self.stdout, self.stderr)
