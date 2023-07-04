# Generated by Django 4.0.6 on 2022-08-18 14:56

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Cat',
            fields=[
                ('name', models.CharField(max_length=100)),
                ('date', models.DateTimeField(auto_now_add=True)),
                ('species', models.CharField(max_length=100)),
                ('sex', models.IntegerField()),
                ('neutral', models.IntegerField()),
                ('alert', models.IntegerField()),
                ('character', models.CharField(max_length=100)),
                ('latitude', models.DecimalField(decimal_places=13, max_digits=17)),
                ('longitude', models.DecimalField(decimal_places=13, max_digits=17)),
                ('photo', models.ImageField(blank=True, null=True, upload_to='cat_photo')),
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('author', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]