# Generated by Django 2.0.6 on 2018-06-30 16:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0002_vehicle_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='vehicle',
            name='image',
            field=models.ImageField(blank=True, default='media/vehicle_default.png', null=True, upload_to='vehicles/'),
        ),
    ]
