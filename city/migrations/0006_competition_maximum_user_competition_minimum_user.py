# Generated by Django 4.0.5 on 2022-09-29 10:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('city', '0005_merge_20220927_2336'),
    ]

    operations = [
        migrations.AddField(
            model_name='competition',
            name='maximum_user',
            field=models.CharField(default='10', max_length=5),
        ),
        migrations.AddField(
            model_name='competition',
            name='minimum_user',
            field=models.CharField(default='1', max_length=1),
        ),
    ]
