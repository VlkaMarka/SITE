# Generated by Django 3.1.4 on 2020-12-10 21:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('feedback', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='error',
            name='email',
            field=models.EmailField(default='example@gmail,com', max_length=254, verbose_name='Почта'),
        ),
        migrations.AddField(
            model_name='idea',
            name='email',
            field=models.EmailField(default='example@gmail,com', max_length=254, verbose_name='Почта'),
        ),
        migrations.AddField(
            model_name='question',
            name='email',
            field=models.EmailField(default='example@gmail,com', max_length=254, verbose_name='Почта'),
        ),
    ]
