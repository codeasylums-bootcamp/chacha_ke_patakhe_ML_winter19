# Generated by Django 3.0 on 2019-12-15 19:19

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('ScrapApp', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='browseitems',
            old_name='link',
            new_name='image_link',
        ),
    ]
