# Generated by Django 4.0.5 on 2022-09-29 10:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('city', '0006_competition_maximum_user_competition_minimum_user'),
    ]

    operations = [
        migrations.AlterField(
            model_name='competition',
            name='maximum_user',
            field=models.CharField(default='10', max_length=2),
        ),
    ]