# Generated by Django 3.2.5 on 2021-07-31 19:36

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('main_app', '0007_auto_20210731_1934'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Medications',
            new_name='Medication',
        ),
    ]
