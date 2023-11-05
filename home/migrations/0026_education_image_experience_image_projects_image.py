# Generated by Django 4.2.6 on 2023-11-04 16:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0025_alter_profile_image'),
    ]

    operations = [
        migrations.AddField(
            model_name='education',
            name='image',
            field=models.ImageField(default='', upload_to='home/images/education'),
        ),
        migrations.AddField(
            model_name='experience',
            name='image',
            field=models.ImageField(default='', upload_to='home/images/experience'),
        ),
        migrations.AddField(
            model_name='projects',
            name='image',
            field=models.ImageField(default='', upload_to='home/images/project'),
        ),
    ]