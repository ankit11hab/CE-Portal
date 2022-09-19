# Generated by Django 4.0.4 on 2022-09-16 13:58

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('city', '0001_initial'),
        ('users', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='team',
            name='competition',
            field=models.ForeignKey(blank=True, default='', null=True, on_delete=django.db.models.deletion.SET_NULL, to='city.competition'),
        ),
        migrations.RemoveField(
            model_name='person',
            name='competition',
        ),
        migrations.AddField(
            model_name='person',
            name='competition',
            field=models.ManyToManyField(blank=True, default=None, to='city.competition'),
        ),
    ]
