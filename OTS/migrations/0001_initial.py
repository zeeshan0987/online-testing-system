# Generated by Django 4.0.4 on 2022-11-29 18:15

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Question',
            fields=[
                ('qno', models.IntegerField(auto_created=True, primary_key=True, serialize=False)),
                ('que', models.CharField(max_length=200)),
                ('optiona', models.CharField(max_length=100)),
                ('optionb', models.CharField(max_length=100)),
                ('optionc', models.CharField(max_length=100)),
                ('optiond', models.CharField(max_length=100)),
                ('answer', models.CharField(max_length=1)),
            ],
        ),
    ]
