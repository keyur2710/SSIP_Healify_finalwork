# Generated by Django 4.1.1 on 2022-10-01 12:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mainapp', '0006_desease'),
    ]

    operations = [
        migrations.AddField(
            model_name='diseasetest',
            name='percentage',
            field=models.IntegerField(default=1),
            preserve_default=False,
        ),
    ]