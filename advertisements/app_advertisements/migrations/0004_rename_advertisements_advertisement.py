# Generated by Django 4.2.3 on 2023-07-27 17:14

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app_advertisements', '0003_alter_advertisements_table'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Advertisements',
            new_name='Advertisement',
        ),
    ]
