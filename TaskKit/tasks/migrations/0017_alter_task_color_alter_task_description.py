# Generated by Django 4.2.1 on 2023-05-31 14:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tasks', '0016_alter_task_color'),
    ]

    operations = [
        migrations.AlterField(
            model_name='task',
            name='color',
            field=models.CharField(blank=True, default='000000FF', max_length=8),
        ),
        migrations.AlterField(
            model_name='task',
            name='description',
            field=models.TextField(blank=True),
        ),
    ]
