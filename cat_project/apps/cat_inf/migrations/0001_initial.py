# Generated by Django 4.0.6 on 2022-08-01 07:28

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Blog',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('date', models.DateTimeField(auto_now_add=True)),
                ('info2', models.CharField(max_length=100)),
                ('info3', models.CharField(max_length=100)),
                ('info4', models.CharField(max_length=100)),
            ],
        ),
    ]
