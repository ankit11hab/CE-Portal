# Generated by Django 3.2.12 on 2022-09-18 12:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('city', '0002_auto_20220918_1226'),
    ]

    operations = [
        migrations.AlterField(
            model_name='city',
            name='cityComp',
            field=models.ManyToManyField(blank=True, to='city.CityComp'),
        ),
    ]
