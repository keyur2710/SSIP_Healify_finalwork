# Generated by Django 4.1.1 on 2023-02-06 04:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mainapp', '0017_patientdoctorconnect'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userprofile',
            name='date_of_birth',
            field=models.CharField(max_length=100),
        ),
    ]