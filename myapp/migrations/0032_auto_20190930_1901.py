# Generated by Django 2.2.5 on 2019-09-30 11:01

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0031_auto_20190929_1532'),
    ]

    operations = [
        migrations.AlterField(
            model_name='articles',
            name='Create_date',
            field=models.DateField(default=datetime.datetime(2019, 9, 30, 11, 1, 9, 522629, tzinfo=utc)),
        ),
    ]
