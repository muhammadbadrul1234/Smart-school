# Generated by Django 3.2.20 on 2023-10-12 13:29

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Student',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=50)),
                ('last_name', models.CharField(max_length=50)),
                ('date_of_birth', models.DateField()),
                ('gender', models.CharField(choices=[('Male', 'Male'), ('Female', 'Female'), ('Other', 'Other')], max_length=10)),
                ('address', models.TextField()),
                ('phone_number', models.CharField(max_length=15)),
                ('email', models.EmailField(max_length=100)),
                ('guardian_name', models.CharField(max_length=100)),
                ('guardian_phone_number', models.CharField(max_length=15)),
                ('guardian_email', models.EmailField(max_length=100)),
                ('roll_number', models.CharField(max_length=15)),
                ('admission_date', models.DateField()),
                ('current_class', models.CharField(max_length=50)),
            ],
        ),
    ]
