# Generated by Django 4.0.5 on 2022-09-28 11:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0003_team_city'),
    ]

    operations = [
        migrations.AddField(
            model_name='person',
            name='college_name',
            field=models.CharField(default=None, max_length=30),
        ),
        migrations.AddField(
            model_name='person',
            name='degree',
            field=models.CharField(default=None, max_length=5),
        ),
        migrations.AddField(
            model_name='person',
            name='gender',
            field=models.CharField(default=None, max_length=10),
        ),
    ]
