# Generated by Django 2.2.5 on 2019-09-30 15:32

import datetime
from django.db import migrations, models
import django.db.models.deletion
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('bbs', '0012_auto_20190930_1957'),
    ]

    operations = [
        migrations.AlterField(
            model_name='bbs',
            name='post_date',
            field=models.DateTimeField(default=datetime.datetime(2019, 9, 30, 15, 32, 14, 770275, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='bbs_comment',
            name='comment_date',
            field=models.DateTimeField(default=datetime.datetime(2019, 9, 30, 15, 32, 14, 771307, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='bbs_comment',
            name='comment_post',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='bbs.bbs'),
        ),
    ]
