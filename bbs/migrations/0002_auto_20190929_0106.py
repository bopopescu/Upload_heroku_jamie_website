# Generated by Django 2.2.5 on 2019-09-28 17:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('bbs', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='bbs',
            name='postman',
            field=models.CharField(max_length=50, null='遊客'),
        ),
        migrations.AlterModelTable(
            name='bbs',
            table='bbs',
        ),
    ]
