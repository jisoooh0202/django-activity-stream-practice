# Generated by Django 4.1 on 2023-05-12 08:53

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('dashboards', '0003_myaction'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Supervisor',
        ),
        migrations.DeleteModel(
            name='Task',
        ),
    ]
