# Generated by Django 4.2.7 on 2023-11-21 16:35

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('guide', '0003_alter_guide_image'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='guide',
            name='content',
        ),
    ]
