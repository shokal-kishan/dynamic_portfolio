# Generated by Django 4.2.6 on 2023-11-03 12:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0023_contact'),
    ]

    operations = [
        migrations.CreateModel(
            name='Coding_profile',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=30)),
                ('link', models.URLField()),
                ('problems', models.IntegerField()),
            ],
        ),
    ]
