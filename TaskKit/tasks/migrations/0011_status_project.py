# Generated by Django 4.2.1 on 2023-05-28 19:00

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('tasks', '0010_remove_project_statuses'),
    ]

    operations = [
        migrations.AddField(
            model_name='status',
            name='project',
            field=models.ForeignKey(default=0, on_delete=django.db.models.deletion.CASCADE, related_name='statuses', to='tasks.project'),
            preserve_default=False,
        ),
    ]
