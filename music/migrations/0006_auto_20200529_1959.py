# Generated by Django 2.1.7 on 2020-05-29 18:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('music', '0005_auto_20200528_2258'),
    ]

    operations = [
        migrations.AddField(
            model_name='base',
            name='write_up',
            field=models.CharField(blank=True, max_length=200, null=True),
        ),
        migrations.AddField(
            model_name='contact',
            name='mymap',
            field=models.ImageField(blank=True, null=True, upload_to=''),
        ),
        migrations.AddField(
            model_name='portfolio',
            name='image_banner_alt',
            field=models.CharField(blank=True, max_length=30, null=True),
        ),
    ]