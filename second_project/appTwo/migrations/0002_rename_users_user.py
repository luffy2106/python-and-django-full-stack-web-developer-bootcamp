# Generated by Django 4.1.7 on 2023-02-27 13:36

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('appTwo', '0001_initial'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Users',
            new_name='User',
        ),
    ]