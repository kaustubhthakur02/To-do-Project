# Generated by Django 5.0.1 on 2024-01-17 13:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('list', '0002_alter_task_priority'),
    ]

    operations = [
        migrations.AlterField(
            model_name='task',
            name='priority',
            field=models.CharField(max_length=10),
        ),
    ]
