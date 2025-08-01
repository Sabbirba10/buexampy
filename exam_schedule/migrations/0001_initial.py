# Generated by Django 4.2.6 on 2024-09-24 15:50

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='ExamSchedule',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('sl', models.CharField(max_length=3)),
                ('course', models.CharField(max_length=8)),
                ('section', models.CharField(max_length=4)),
                ('mid_date', models.DateField()),
                ('start_time', models.TimeField()),
                ('end_time', models.TimeField()),
                ('room', models.CharField(max_length=10)),
            ],
        ),
    ]
