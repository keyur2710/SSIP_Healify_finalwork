# Generated by Django 4.1.1 on 2022-10-05 16:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mainapp', '0008_doctor_image'),
    ]

    operations = [
        migrations.AddField(
            model_name='doctor',
            name='description',
            field=models.TextField(blank=True),
        ),
    ]
