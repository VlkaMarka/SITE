# Generated by Django 3.1.4 on 2020-12-12 15:53

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0008_file_date_joined'),
    ]

    operations = [
        migrations.RenameField(
            model_name='file',
            old_name='date_joined',
            new_name='date',
        ),
    ]
