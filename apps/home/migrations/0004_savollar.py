# Generated by Django 3.1 on 2020-10-13 12:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0003_auto_20200919_1708'),
    ]

    operations = [
        migrations.CreateModel(
            name='Savollar',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('savol', models.TextField(verbose_name='Savol matni')),
                ('javob', models.TextField(verbose_name='Javob matni')),
            ],
            options={
                'verbose_name': 'Savol va Javob',
                'verbose_name_plural': 'Savollar va Javoblar',
            },
        ),
    ]