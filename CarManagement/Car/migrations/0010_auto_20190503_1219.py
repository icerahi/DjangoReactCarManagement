# Generated by Django 2.0.5 on 2019-05-03 12:19

from decimal import Decimal
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Car', '0009_auto_20190503_1201'),
    ]

    operations = [
        migrations.AlterField(
            model_name='car',
            name='horsepower',
            field=models.DecimalField(decimal_places=2, default=Decimal('0'), max_digits=20),
        ),
        migrations.AlterField(
            model_name='car',
            name='price',
            field=models.DecimalField(decimal_places=2, default=Decimal('0'), max_digits=20),
        ),
        migrations.AlterField(
            model_name='car',
            name='status',
            field=models.IntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='car',
            name='year',
            field=models.IntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='showroom',
            name='registrationNumber',
            field=models.IntegerField(default=0),
        ),
    ]
