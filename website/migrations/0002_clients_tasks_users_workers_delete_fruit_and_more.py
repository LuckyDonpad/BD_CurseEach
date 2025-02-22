# Generated by Django 5.0.1 on 2024-03-05 15:01

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('website', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Clients',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=256)),
                ('surname', models.CharField(max_length=256)),
                ('patronymic', models.CharField(max_length=256)),
                ('phone', models.CharField(max_length=256)),
                ('register_date', models.DateField()),
            ],
        ),
        migrations.CreateModel(
            name='Tasks',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=256)),
                ('status', models.IntegerField()),
                ('begin_date', models.DateField()),
                ('end_date', models.DateField()),
            ],
        ),
        migrations.CreateModel(
            name='Users',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=256)),
                ('login', models.CharField(max_length=256)),
                ('password', models.CharField(max_length=256)),
                ('status', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='Workers',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=256)),
                ('surname', models.CharField(max_length=256)),
                ('patronymic', models.CharField(max_length=256)),
            ],
        ),
        migrations.DeleteModel(
            name='Fruit',
        ),
        migrations.AddField(
            model_name='users',
            name='worker_id',
            field=models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='website.workers'),
        ),
        migrations.AddField(
            model_name='tasks',
            name='worker_id',
            field=models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='website.workers'),
        ),
    ]
