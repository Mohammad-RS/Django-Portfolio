# Generated by Django 2.2.16 on 2020-09-16 09:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('info', '0010_information_mini_about'),
    ]

    operations = [
        migrations.AddField(
            model_name='information',
            name='cv',
            field=models.FileField(blank=True, null=True, upload_to='cv'),
        ),
    ]
