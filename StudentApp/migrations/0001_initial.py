# Generated by Django 4.2.2 on 2023-06-26 05:34

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='City',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('city_name', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='Course',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('course_name', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='Student2',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Stud_name', models.CharField(max_length=50)),
                ('Stud_phno', models.BigIntegerField()),
                ('Stud_email', models.CharField(max_length=100)),
                ('Stud_fees', models.IntegerField()),
                ('Stud_city', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='StudentApp.city')),
                ('Stud_course', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='StudentApp.course')),
            ],
        ),
    ]
