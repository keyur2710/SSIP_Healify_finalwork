# Generated by Django 4.1.1 on 2022-10-01 08:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mainapp', '0005_diseasetest'),
    ]

    operations = [
        migrations.CreateModel(
            name='Desease',
            fields=[
                ('id', models.IntegerField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=250)),
                ('description', models.CharField(max_length=500)),
            ],
        ),
    ]