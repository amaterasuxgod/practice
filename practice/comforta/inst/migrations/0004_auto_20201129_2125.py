# Generated by Django 3.1.3 on 2020-11-29 18:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('inst', '0003_auto_20201129_1815'),
    ]

    operations = [
        migrations.AlterField(
            model_name='installation',
            name='NetworkMode',
            field=models.CharField(choices=[('home', 'Home'), ('OneDevice', 'OneDevice')], default='Home', max_length=254),
        ),
        migrations.AlterField(
            model_name='installation',
            name='UIN',
            field=models.CharField(max_length=17, null=True, unique=True),
        ),
    ]