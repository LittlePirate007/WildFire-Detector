# Generated by Django 2.2.5 on 2019-09-20 17:35

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='UserUploads',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('location_name', models.CharField(max_length=225)),
                ('image', models.ImageField(upload_to='images/')),
                ('location_long_lat', models.CharField(max_length=225)),
                ('summary_info', models.CharField(max_length=225)),
            ],
        ),
    ]
