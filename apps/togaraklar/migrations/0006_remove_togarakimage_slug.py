# Generated by Django 3.1 on 2020-10-07 10:46

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('togaraklar', '0005_togarakimage_slug'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='togarakimage',
            name='slug',
        ),
    ]
