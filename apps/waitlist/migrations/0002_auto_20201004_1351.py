# Generated by Django 3.1 on 2020-10-04 08:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('waitlist', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='waitlist',
            name='email',
            field=models.EmailField(max_length=254, unique=True, verbose_name='email address'),
        ),
    ]