# Generated by Django 2.1.5 on 2019-04-10 00:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mastrooms', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='room',
            name='bed',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='room',
            name='bucket_mug',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='room',
            name='cctv',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='room',
            name='cooler',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='room',
            name='elevator',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='room',
            name='fan',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='room',
            name='geyser',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='room',
            name='mattress',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='room',
            name='power_backup',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='room',
            name='ro_water',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='room',
            name='table_chair',
            field=models.BooleanField(default=False),
        ),
        migrations.AlterField(
            model_name='room',
            name='image1',
            field=models.ImageField(blank=True, null=True, upload_to='static/media'),
        ),
        migrations.AlterField(
            model_name='room',
            name='image2',
            field=models.ImageField(blank=True, null=True, upload_to='static/media'),
        ),
        migrations.AlterField(
            model_name='room',
            name='image3',
            field=models.ImageField(blank=True, null=True, upload_to='static/media'),
        ),
        migrations.AlterField(
            model_name='room',
            name='image4',
            field=models.ImageField(blank=True, null=True, upload_to='static/media'),
        ),
    ]
