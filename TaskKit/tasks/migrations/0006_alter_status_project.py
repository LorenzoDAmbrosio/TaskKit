# Generated by Django 4.2.1 on 2023-05-28 13:23

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('tasks', '0005_remove_project_statuses_status_project'),
    ]

    operations = [
        migrations.AlterField(
            model_name='status',
            name='project',
            field=models.ForeignKey(default=0, on_delete=django.db.models.deletion.CASCADE, related_name='statuses', to='tasks.project'),
        ),
    ]