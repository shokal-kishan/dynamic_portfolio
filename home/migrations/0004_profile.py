# Generated by Django 4.2.6 on 2023-10-31 14:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0003_education'),
    ]

    operations = [
        migrations.CreateModel(
            name='Profile',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=20)),
                ('email', models.EmailField(max_length=254)),
                ('phone', models.BigIntegerField()),
                ('dob', models.DateField()),
                ('address', models.CharField(max_length=50)),
                ('summary', models.TextField()),
                ('bio', models.CharField(max_length=30)),
                ('image', models.ImageField(default='', upload_to='')),
            ],
        ),
    ]