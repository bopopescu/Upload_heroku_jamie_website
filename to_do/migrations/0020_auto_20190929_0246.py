# Generated by Django 2.2.5 on 2019-09-28 18:46

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('to_do', '0019_auto_20190929_0106'),
    ]

    operations = [
        migrations.AlterField(
            model_name='do_list',
            name='event_date',
            field=models.DateField(default=datetime.datetime(2019, 9, 28, 18, 46, 57, 126036, tzinfo=utc)),
        ),
    ]