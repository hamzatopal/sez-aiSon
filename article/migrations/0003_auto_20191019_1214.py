# Generated by Django 2.2.5 on 2019-10-19 09:14

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('article', '0002_auto_20191019_1205'),
    ]

    operations = [
        migrations.RenameField(
            model_name='article',
            old_name='articel_image',
            new_name='article_image',
        ),
    ]
