# Generated by Django 4.2.1 on 2023-05-28 19:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tasks', '0012_community_creation_date_community_founder_user'),
    ]

    operations = [
        migrations.AddField(
            model_name='community',
            name='is_open',
            field=models.BooleanField(default=0),
        ),
    ]
