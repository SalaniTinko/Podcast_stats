# Generated by Django 2.2.5 on 2020-12-09 21:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('podcast_app', '0004_auto_20201209_2103'),
    ]

    operations = [
        migrations.AlterField(
            model_name='totalpodcaststate',
            name='new_plays',
            field=models.CharField(blank=True, default='0', max_length=120),
        ),
        migrations.AlterField(
            model_name='totalpodcaststate',
            name='new_subscribes',
            field=models.CharField(blank=True, default='0', max_length=120),
        ),
    ]
