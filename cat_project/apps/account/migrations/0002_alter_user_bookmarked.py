# Generated by Django 4.0.6 on 2022-08-18 17:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='bookmarked',
            field=models.TextField(null=True),
        ),
    ]
