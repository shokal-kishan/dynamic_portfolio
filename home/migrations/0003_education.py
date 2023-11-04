# Generated by Django 4.2.6 on 2023-10-31 13:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0002_projects_project_desc_projects_project_is_ml_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='Education',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('degree', models.CharField(max_length=50)),
                ('start_date', models.IntegerField()),
                ('end_date', models.IntegerField()),
                ('is_cgpa', models.BooleanField()),
                ('marks', models.FloatField()),
                ('shool', models.CharField(max_length=50)),
            ],
        ),
    ]
