# Generated by Django 5.0.1 on 2024-01-17 18:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('list', '0007_alter_task_priority'),
    ]

    operations = [
        migrations.AlterField(
            model_name='task',
            name='priority',
            field=models.IntegerField(),
        ),
    ]
