# Generated by Django 3.2.7 on 2022-05-29 14:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('hotel_app', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='room',
            name='room_type',
            field=models.IntegerField(choices=[(1, 'Одноместный'), (2, 'Двуместный'), (3, 'Трёхместный')], max_length=30),
        ),
    ]
