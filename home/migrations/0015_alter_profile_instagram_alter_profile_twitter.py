# Generated by Django 4.2.6 on 2023-11-01 14:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0014_rename_project_is_ml_projects_is_ml_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='instagram',
            field=models.URLField(default=None, null=True),
        ),
        migrations.AlterField(
            model_name='profile',
            name='twitter',
            field=models.URLField(default=None, null=True),
        ),
    ]
