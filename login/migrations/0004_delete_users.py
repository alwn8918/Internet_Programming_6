# Generated by Django 4.2.7 on 2023-11-28 02:27

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('login', '0003_users_registered_dttm_alter_users_username'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Users',
        ),
    ]
