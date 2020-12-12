# Generated by Django 3.1.4 on 2020-12-12 09:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0005_auto_20201212_1231'),
    ]

    operations = [
        migrations.CreateModel(
            name='File',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50, verbose_name='Версия программы')),
                ('file_prog', models.FileField(upload_to=None, verbose_name='Установщик программы')),
            ],
            options={
                'verbose_name': 'Программа',
                'verbose_name_plural': 'Версии программы',
            },
        ),
    ]
