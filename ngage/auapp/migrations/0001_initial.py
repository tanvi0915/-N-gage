# Generated by Django 3.2.4 on 2021-11-09 08:27

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='DeleteModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('deleted_Employee', models.CharField(max_length=50)),
                ('deleting_HR', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='EventsModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('ename', models.CharField(max_length=50)),
                ('image_url', models.CharField(max_length=400)),
                ('description', models.CharField(max_length=250)),
                ('date_of_event', models.DateField()),
            ],
        ),
    ]