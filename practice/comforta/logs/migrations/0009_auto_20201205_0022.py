# Generated by Django 3.1.3 on 2020-12-04 21:22

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('logs', '0008_auto_20201202_0231'),
    ]

    operations = [
        migrations.RenameField(
            model_name='log',
            old_name='Facility',
            new_name='Installation',
        ),
    ]
