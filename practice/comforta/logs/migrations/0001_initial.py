# Generated by Django 3.1.3 on 2020-11-30 13:52

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('inst', '0005_auto_20201129_2224'),
    ]

    operations = [
        migrations.CreateModel(
            name='Log',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('LogContent', models.CharField(max_length=254)),
                ('LogDate', models.DateField(auto_now=True)),
                ('Facility', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='inst.installation', to_field='UIN')),
            ],
        ),
    ]