# Generated by Django 2.1.5 on 2019-04-10 02:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mastrooms', '0004_auto_20190410_0149'),
    ]

    operations = [
        migrations.AlterField(
            model_name='room',
            name='phone_number',
            field=models.CharField(max_length=10),
        ),
    ]