# Generated by Django 3.1.3 on 2020-11-15 05:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('_employee', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='employeedb',
            name='image',
            field=models.ImageField(upload_to='ABC/uploads/'),
        ),
    ]
