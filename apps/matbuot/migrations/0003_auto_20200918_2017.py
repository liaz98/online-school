# Generated by Django 3.1 on 2020-09-18 15:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('matbuot', '0002_galereya'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='galereya',
            options={'ordering': ['sorting'], 'verbose_name': 'Galereya', 'verbose_name_plural': 'Galereya'},
        ),
        migrations.AddField(
            model_name='galereya',
            name='sorting',
            field=models.PositiveIntegerField(default=0),
        ),
    ]