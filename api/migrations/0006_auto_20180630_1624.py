# Generated by Django 2.0.6 on 2018-06-30 16:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0005_vehicle_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='vehicle',
            name='image',
            field=models.ImageField(default='vehicle_default.png', upload_to='vehicles/'),
        ),
    ]