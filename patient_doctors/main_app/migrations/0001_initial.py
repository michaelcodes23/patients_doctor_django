# Generated by Django 3.2.5 on 2021-07-29 01:09

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Doctor',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=150)),
                ('age', models.IntegerField()),
                ('gender', models.CharField(max_length=50)),
                ('office_location', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='Patient',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=150)),
                ('age', models.IntegerField()),
                ('symptoms', models.TextField()),
                ('insurance', models.CharField(max_length=250)),
                ('gender', models.CharField(max_length=50)),
                ('address', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='PatientstoDoctors',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('doctor', models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, related_name='doctors', to='main_app.doctor')),
                ('patient', models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, related_name='patients', to='main_app.patient')),
            ],
        ),
    ]
