# Generated by Django 4.1.6 on 2023-02-05 06:59

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='ParentInfo',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('id_number', models.CharField(max_length=15)),
                ('full_name', models.CharField(max_length=255)),
                ('birth_of_date', models.CharField(max_length=20)),
                ('contact_number', models.CharField(max_length=12)),
            ],
        ),
        migrations.CreateModel(
            name='Student',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('index_number', models.CharField(max_length=20)),
                ('full_name', models.CharField(max_length=255)),
                ('birth_of_date', models.DateField()),
                ('image_id', models.CharField(max_length=20)),
                ('sex', models.CharField(max_length=2)),
                ('nfc_identifier', models.CharField(max_length=255)),
                ('address', models.TextField(max_length=1000)),
                ('parent_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='student.parentinfo')),
            ],
        ),
    ]
