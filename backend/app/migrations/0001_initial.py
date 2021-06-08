# Generated by Django 3.1.7 on 2021-06-08 01:39

import app.models.user
import app.utils.security
from django.conf import settings
import django.contrib.postgres.fields
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('last_login', models.DateTimeField(blank=True, null=True, verbose_name='last login')),
                ('deleted', models.DateTimeField(editable=False, null=True)),
                ('uuid', models.CharField(default=app.utils.security.generate_uuid, max_length=32768, primary_key=True, serialize=False)),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('updated', models.DateTimeField(auto_now=True)),
                ('email', models.EmailField(error_messages={'unique': 'An user with that email already exists.'}, max_length=32768, unique=True, verbose_name='email')),
                ('password', models.CharField(max_length=32768)),
                ('name', models.CharField(blank=True, max_length=32768)),
                ('tel', models.CharField(blank=True, max_length=10, null=True)),
                ('city', models.CharField(blank=True, max_length=32768, null=True)),
                ('district', models.CharField(blank=True, max_length=32768, null=True)),
                ('ward', models.CharField(blank=True, max_length=32768, null=True)),
                ('address', models.CharField(blank=True, max_length=32768, null=True)),
                ('image', models.ImageField(null=True, upload_to='')),
                ('birthday', models.DateField(null=True)),
                ('role', models.CharField(choices=[('user', 'user'), ('hotelier', 'hotelier'), ('admin', 'admin')], default='user', max_length=8)),
                ('is_active', models.BooleanField(default=False)),
                ('deactivate_reason', models.CharField(max_length=32768, null=True)),
            ],
            options={
                'db_table': 'user',
            },
            managers=[
                ('objects', app.models.user.UserManager()),
            ],
        ),
        migrations.CreateModel(
            name='Booking',
            fields=[
                ('deleted', models.DateTimeField(editable=False, null=True)),
                ('uuid', models.CharField(default=app.utils.security.generate_uuid, max_length=32768, primary_key=True, serialize=False)),
                ('check_in_time', models.DateTimeField(null=True)),
                ('check_out_time', models.DateTimeField(null=True)),
                ('code', models.CharField(max_length=32768, null=True)),
                ('created', models.DateTimeField(blank=True)),
                ('updated', models.DateTimeField(blank=True)),
                ('total_price', models.PositiveBigIntegerField(null=True)),
                ('hotel_id', models.CharField(max_length=32768, null=True)),
            ],
            options={
                'db_table': 'booking',
            },
        ),
        migrations.CreateModel(
            name='Complaint',
            fields=[
                ('deleted', models.DateTimeField(editable=False, null=True)),
                ('uuid', models.CharField(default=app.utils.security.generate_uuid, max_length=32768, primary_key=True, serialize=False)),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('updated', models.DateTimeField(auto_now=True)),
                ('title', models.CharField(blank=True, max_length=32768)),
                ('image', models.ImageField(null=True, upload_to='')),
                ('content', models.TextField(blank=True, max_length=65536)),
                ('is_processed', models.BooleanField(default=False)),
            ],
            options={
                'db_table': 'complaint',
            },
        ),
        migrations.CreateModel(
            name='Hotel',
            fields=[
                ('deleted', models.DateTimeField(editable=False, null=True)),
                ('uuid', models.CharField(default=app.utils.security.generate_uuid, max_length=32768, primary_key=True, serialize=False)),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('updated', models.DateTimeField(auto_now=True)),
                ('name', models.CharField(blank=True, max_length=32768)),
                ('star', models.PositiveIntegerField(blank=True)),
                ('city', models.CharField(blank=True, max_length=32768)),
                ('district', models.CharField(blank=True, max_length=32768)),
                ('ward', models.CharField(blank=True, max_length=32768)),
                ('address', models.CharField(blank=True, max_length=32768, null=True)),
                ('image', models.ImageField(blank=True, upload_to='')),
                ('amenities', django.contrib.postgres.fields.ArrayField(base_field=models.CharField(choices=[('free parking', 'Free Parking'), ('fitness center', 'Fitness Center'), ('breakfast', 'Breakfast'), ('swimming pool', 'Swimming Pool'), ('bar', 'Bar'), ('spa', 'Spa'), ('room service', 'Room Service'), ('non smoking room', 'Non Smoking Room')], max_length=32768), size=None)),
                ('status', models.CharField(choices=[('active', 'Active'), ('reject', 'Reject'), ('pending', 'Pending')], default='pending', max_length=8)),
                ('reject_reason', models.CharField(max_length=32768, null=True)),
                ('email', models.EmailField(error_messages={'unique': 'Email already exists.'}, max_length=32768, null=True, unique=True, verbose_name='email')),
                ('tel', models.CharField(blank=True, max_length=10, null=True)),
                ('user', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='hotels', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'db_table': 'hotel',
            },
        ),
        migrations.CreateModel(
            name='Type',
            fields=[
                ('deleted', models.DateTimeField(editable=False, null=True)),
                ('uuid', models.CharField(default=app.utils.security.generate_uuid, max_length=32768, primary_key=True, serialize=False)),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('updated', models.DateTimeField(auto_now=True)),
                ('name', models.CharField(blank=True, max_length=32768)),
                ('capacity', models.IntegerField(default=1)),
                ('adult_number', models.IntegerField(default=1)),
                ('children_number', models.IntegerField(default=0)),
                ('price', models.IntegerField(blank=True)),
                ('area', models.IntegerField(blank=True)),
                ('amenities', django.contrib.postgres.fields.ArrayField(base_field=models.CharField(choices=[('bathrobes', 'Bathrobes'), ('coffee kit', 'Coffee Kit'), ('clothes rack', 'Clothes Rack'), ('wifi', 'Wifi'), ('tissue box', 'Tissue Box'), ('toiletries', 'Toiletries'), ('bathtub', 'Bathtub'), ('refrigerator', 'Refrigerator'), ('hair dryer', 'Hair Dryer'), ('electric kettle', 'Electric Kettle')], max_length=32768), blank=True, size=None)),
                ('hotel', models.ForeignKey(null=True, on_delete=django.db.models.deletion.DO_NOTHING, related_name='types', to='app.hotel')),
            ],
            options={
                'db_table': 'type',
            },
        ),
        migrations.CreateModel(
            name='Room',
            fields=[
                ('deleted', models.DateTimeField(editable=False, null=True)),
                ('uuid', models.CharField(default=app.utils.security.generate_uuid, max_length=32768, primary_key=True, serialize=False)),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('updated', models.DateTimeField(auto_now=True)),
                ('room_number', models.CharField(blank=True, max_length=32768)),
                ('image', models.ImageField(blank=True, upload_to='')),
                ('hotel', models.ForeignKey(null=True, on_delete=django.db.models.deletion.DO_NOTHING, related_name='rooms', to='app.hotel')),
                ('type', models.ForeignKey(null=True, on_delete=django.db.models.deletion.DO_NOTHING, related_name='rooms', to='app.type')),
            ],
            options={
                'db_table': 'room',
            },
        ),
        migrations.CreateModel(
            name='Review',
            fields=[
                ('deleted', models.DateTimeField(editable=False, null=True)),
                ('uuid', models.CharField(default=app.utils.security.generate_uuid, max_length=32768, primary_key=True, serialize=False)),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('updated', models.DateTimeField(auto_now=True)),
                ('rating', models.PositiveIntegerField(blank=True)),
                ('title', models.CharField(blank=True, max_length=32768)),
                ('content', models.TextField(blank=True, max_length=65536)),
                ('hotel', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='reviews', to='app.hotel')),
                ('user', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='reviews', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'db_table': 'review',
            },
        ),
        migrations.CreateModel(
            name='Reply',
            fields=[
                ('deleted', models.DateTimeField(editable=False, null=True)),
                ('uuid', models.CharField(default=app.utils.security.generate_uuid, max_length=32768, primary_key=True, serialize=False)),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('updated', models.DateTimeField(auto_now=True)),
                ('title', models.CharField(blank=True, max_length=32768)),
                ('image', models.ImageField(null=True, upload_to='')),
                ('content', models.TextField(blank=True, max_length=65536)),
                ('complaint', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='replys', to='app.complaint')),
            ],
            options={
                'db_table': 'reply',
            },
        ),
        migrations.CreateModel(
            name='Recommendation',
            fields=[
                ('deleted', models.DateTimeField(editable=False, null=True)),
                ('uuid', models.CharField(default=app.utils.security.generate_uuid, max_length=32768, primary_key=True, serialize=False)),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('updated', models.DateTimeField(auto_now=True)),
                ('similarity', models.FloatField(blank=True)),
                ('collation_hotel', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='collated_recommendations', to='app.hotel')),
                ('hotel', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='recommendations', to='app.hotel')),
            ],
            options={
                'db_table': 'recommendation',
            },
        ),
        migrations.CreateModel(
            name='Favorite',
            fields=[
                ('deleted', models.DateTimeField(editable=False, null=True)),
                ('uuid', models.CharField(default=app.utils.security.generate_uuid, max_length=32768, primary_key=True, serialize=False)),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('updated', models.DateTimeField(auto_now=True)),
                ('hotel', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='favorites', to='app.hotel')),
                ('user', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='favorites', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'db_table': 'favorite',
            },
        ),
        migrations.AddField(
            model_name='complaint',
            name='hotel',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='complaints', to='app.hotel'),
        ),
        migrations.AddField(
            model_name='complaint',
            name='user',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='complaints', to=settings.AUTH_USER_MODEL),
        ),
        migrations.CreateModel(
            name='BookingType',
            fields=[
                ('deleted', models.DateTimeField(editable=False, null=True)),
                ('uuid', models.CharField(default=app.utils.security.generate_uuid, max_length=32768, primary_key=True, serialize=False)),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('updated', models.DateTimeField(auto_now=True)),
                ('count', models.IntegerField(blank=True)),
                ('booking', models.ForeignKey(null=True, on_delete=django.db.models.deletion.DO_NOTHING, to='app.booking')),
                ('type', models.ForeignKey(null=True, on_delete=django.db.models.deletion.DO_NOTHING, to='app.type')),
            ],
            options={
                'db_table': 'booking_type',
            },
        ),
        migrations.CreateModel(
            name='BookingRoom',
            fields=[
                ('deleted', models.DateTimeField(editable=False, null=True)),
                ('uuid', models.CharField(default=app.utils.security.generate_uuid, max_length=32768, primary_key=True, serialize=False)),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('updated', models.DateTimeField(auto_now=True)),
                ('booking', models.ForeignKey(null=True, on_delete=django.db.models.deletion.DO_NOTHING, to='app.booking')),
                ('room', models.ForeignKey(null=True, on_delete=django.db.models.deletion.DO_NOTHING, to='app.room')),
            ],
            options={
                'db_table': 'booking_room',
            },
        ),
        migrations.AddField(
            model_name='booking',
            name='rooms',
            field=models.ManyToManyField(through='app.BookingRoom', to='app.Room'),
        ),
        migrations.AddField(
            model_name='booking',
            name='types',
            field=models.ManyToManyField(through='app.BookingType', to='app.Type'),
        ),
        migrations.AddField(
            model_name='booking',
            name='user',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.DO_NOTHING, related_name='bookings', to=settings.AUTH_USER_MODEL),
        ),
    ]
