# Generated by Django 3.1.3 on 2020-11-29 15:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('inst', '0002_auto_20201129_1812'),
    ]

    operations = [
        migrations.AlterField(
            model_name='installation',
            name='DateCreated',
            field=models.DateField(auto_now_add=True),
        ),
        migrations.AlterField(
            model_name='installation',
            name='DateUpdated',
            field=models.DateField(auto_now=True),
        ),
    ]