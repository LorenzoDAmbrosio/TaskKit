# Generated by Django 4.2.1 on 2023-05-28 19:32

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('tasks', '0011_status_project'),
    ]

    operations = [
        migrations.AddField(
            model_name='community',
            name='creation_date',
            field=models.DateTimeField(auto_now_add=True, default=django.utils.timezone.now),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='community',
            name='founder_user',
            field=models.ForeignKey(default=2, on_delete=django.db.models.deletion.CASCADE, related_name='founded_communities', to=settings.AUTH_USER_MODEL),
            preserve_default=False,
        ),
    ]
