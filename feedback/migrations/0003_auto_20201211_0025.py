# Generated by Django 3.1.4 on 2020-12-10 21:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('feedback', '0002_auto_20201211_0025'),
    ]

    operations = [
        migrations.AlterField(
            model_name='error',
            name='email',
            field=models.EmailField(max_length=254, verbose_name='Почта'),
        ),
        migrations.AlterField(
            model_name='idea',
            name='email',
            field=models.EmailField(max_length=254, verbose_name='Почта'),
        ),
        migrations.AlterField(
            model_name='question',
            name='email',
            field=models.EmailField(max_length=254, verbose_name='Почта'),
        ),
    ]