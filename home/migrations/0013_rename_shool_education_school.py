# Generated by Django 4.2.6 on 2023-10-31 20:01

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0012_alter_experience_company_alter_experience_end_date_and_more'),
    ]

    operations = [
        migrations.RenameField(
            model_name='education',
            old_name='shool',
            new_name='school',
        ),
    ]
