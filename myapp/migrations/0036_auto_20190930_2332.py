# Generated by Django 2.2.5 on 2019-09-30 15:32

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0035_auto_20190930_1957'),
    ]

    operations = [
        migrations.AlterField(
            model_name='articles',
            name='Create_date',
            field=models.DateField(default=datetime.datetime(2019, 9, 30, 15, 32, 14, 734371, tzinfo=utc)),
        ),
    ]