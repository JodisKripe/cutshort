# Generated by Django 3.0.7 on 2020-07-10 17:07

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('shortner', '0001_initial'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Links',
            new_name='Link',
        ),
    ]
