# Generated by Django 4.0.6 on 2022-09-10 04:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('city', '0003_remove_applicant_group_team_members'),
    ]

    operations = [
        migrations.AlterField(
            model_name='applicant',
            name='name',
            field=models.CharField(max_length=50),
        ),
    ]