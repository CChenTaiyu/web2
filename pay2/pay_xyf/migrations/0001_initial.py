# Generated by Django 3.2.19 on 2023-05-11 01:18

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='consumption_record',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Time', models.DateTimeField()),
                ('Recipient', models.CharField(max_length=45)),
                ('Amount', models.IntegerField()),
                ('Money', models.FloatField()),
                ('secret_key', models.CharField(max_length=45)),
                ('UserId', models.IntegerField()),
                ('Airline_order', models.CharField(max_length=45)),
                ('State', models.BooleanField()),
            ],
        ),
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('username', models.CharField(max_length=30)),
                ('password', models.CharField(max_length=30)),
                ('balance', models.FloatField()),
                ('name', models.CharField(max_length=15)),
            ],
        ),
    ]
