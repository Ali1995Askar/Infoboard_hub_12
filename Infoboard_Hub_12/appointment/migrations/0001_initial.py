# Generated by Django 3.2.6 on 2021-09-03 12:12

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Advertising',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(default='Hallo Zusammen', max_length=250)),
                ('body', models.TextField(default='Herzlich willkommen')),
                ('image', models.ImageField(default='advertising-images/logo.jpg', null=True, upload_to='advertising-images/')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Group',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(default='unKnown group', max_length=250)),
            ],
        ),
        migrations.CreateModel(
            name='Appointment',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('party_type', models.CharField(max_length=250)),
                ('party_organizer', models.CharField(max_length=250)),
                ('location', models.CharField(max_length=250)),
                ('room', models.CharField(max_length=250)),
                ('party_date', models.DateTimeField()),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('group', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='appointment.group')),
            ],
        ),
    ]
