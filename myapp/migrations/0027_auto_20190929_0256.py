# Generated by Django 2.2.5 on 2019-09-28 18:56

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0026_auto_20190929_0246'),
    ]

    operations = [
        migrations.AlterField(
            model_name='articles',
            name='Create_date',
            field=models.DateField(default=datetime.datetime(2019, 9, 28, 18, 56, 0, 381788, tzinfo=utc)),
        ),
    ]
