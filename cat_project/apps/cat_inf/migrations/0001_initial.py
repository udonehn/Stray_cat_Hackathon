# Generated by Django 4.0.6 on 2022-08-11 21:52

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Cat',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('date', models.DateTimeField(auto_now_add=True)),
                ('species', models.CharField(max_length=100)),
                ('sex', models.IntegerField(max_length=100)),
                ('neutral', models.IntegerField(max_length=100)),
                ('alert', models.IntegerField(max_length=100)),
                ('character', models.CharField(max_length=100)),
                ('latitude', models.DecimalField(decimal_places=13, max_digits=17)),
                ('longitude', models.DecimalField(decimal_places=13, max_digits=17)),
                ('photo', models.ImageField(blank=True, null=True, upload_to='cat_photo')),
            ],
        ),
    ]
