# Generated by Django 2.0.5 on 2019-05-03 06:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Car', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='ShowRoom',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=30)),
                ('registrationNumber', models.CharField(max_length=30)),
            ],
        ),
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('email', models.CharField(max_length=30)),
                ('username', models.CharField(max_length=30)),
                ('password', models.CharField(max_length=30)),
            ],
        ),
    ]
