# Generated by Django 3.2.4 on 2021-11-08 19:47

from django.db import migrations, models
import embed_video.fields


class Migration(migrations.Migration):

    dependencies = [
        ('employee', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='tutorial',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=200)),
                ('body', models.TextField()),
                ('video', embed_video.fields.EmbedVideoField()),
            ],
        ),
        migrations.DeleteModel(
            name='Item',
        ),
    ]