# Generated by Django 3.1.3 on 2020-11-29 15:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('inst', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='installation',
            name='UIN',
            field=models.CharField(max_length=17, unique=True),
        ),
    ]
