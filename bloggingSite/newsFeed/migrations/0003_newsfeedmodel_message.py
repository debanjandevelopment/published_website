# Generated by Django 4.1.3 on 2022-11-25 19:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('newsFeed', '0002_remove_newsfeedmodel_message'),
    ]

    operations = [
        migrations.AddField(
            model_name='newsfeedmodel',
            name='message',
            field=models.TextField(blank=True),
        ),
    ]
