# Generated by Django 3.1.3 on 2020-11-29 19:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('inst', '0004_auto_20201129_2125'),
    ]

    operations = [
        migrations.AlterField(
            model_name='installation',
            name='DeviceMode',
            field=models.CharField(choices=[('off', 'Off'), ('one', 'One'), ('two', 'Two'), ('three', 'Three'), ('four', 'Four')], default='off', max_length=254),
        ),
        migrations.AlterField(
            model_name='installation',
            name='NetworkMode',
            field=models.CharField(choices=[('home', 'Home'), ('OneDevice', 'OneDevice')], default='home', max_length=254),
        ),
    ]
