# Generated by Django 4.0.5 on 2022-09-28 11:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0005_alter_person_college_name_alter_person_degree_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='person',
            name='college_name',
            field=models.CharField(max_length=30),
        ),
        migrations.AlterField(
            model_name='person',
            name='degree',
            field=models.CharField(max_length=5),
        ),
        migrations.AlterField(
            model_name='person',
            name='gender',
            field=models.CharField(max_length=10),
        ),
    ]