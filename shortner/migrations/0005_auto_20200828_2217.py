# Generated by Django 3.0.7 on 2020-08-28 16:47

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('shortner', '0004_auto_20200711_0013'),
    ]

    operations = [
        migrations.RenameField(
            model_name='link',
            old_name='longLink',
            new_name='longlink',
        ),
        migrations.RenameField(
            model_name='link',
            old_name='shortLink',
            new_name='shortlink',
        ),
    ]
