# Generated by Django 4.1.1 on 2023-02-04 15:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mainapp', '0014_desease_user'),
    ]

    operations = [
        migrations.AddField(
            model_name='doctor',
            name='license',
            field=models.IntegerField(default=1),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='doctor',
            name='proefficiency',
            field=models.CharField(default=1, max_length=200),
            preserve_default=False,
        ),
    ]