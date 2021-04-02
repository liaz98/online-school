# Generated by Django 3.1 on 2020-10-07 05:50

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='TogarakList',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=150, verbose_name='To`garak nomi')),
                ('content', models.TextField(verbose_name='To`garak haqida ma`lumot')),
            ],
            options={
                'verbose_name': 'To`garak',
                'verbose_name_plural': 'To`garaklar',
            },
        ),
        migrations.CreateModel(
            name='TogarakImage',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('togarak_photo', models.FileField(upload_to='togaraklar/%m/')),
                ('togarak_list', models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, to='togaraklar.togaraklist')),
            ],
        ),
    ]
