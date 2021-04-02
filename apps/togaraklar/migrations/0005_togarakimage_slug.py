# Generated by Django 3.1 on 2020-10-07 10:42

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('togaraklar', '0004_togaraklist_slug'),
    ]

    operations = [
        migrations.AddField(
            model_name='togarakimage',
            name='slug',
            field=models.SlugField(default=django.utils.timezone.now, max_length=150),
            preserve_default=False,
        ),
    ]
