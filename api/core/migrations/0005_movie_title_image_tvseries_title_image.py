# Generated by Django 4.1.7 on 2023-03-27 23:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0004_seasontvseries_tvseries_seriestvseries_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='movie',
            name='title_image',
            field=models.ImageField(blank=True, default=None, null=True, upload_to='', verbose_name='Название изображением'),
        ),
        migrations.AddField(
            model_name='tvseries',
            name='title_image',
            field=models.ImageField(blank=True, default=None, null=True, upload_to='', verbose_name='Название изображением'),
        ),
    ]
