# Generated by Django 3.1 on 2021-04-07 14:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ecow', '0022_auto_20210406_1410'),
    ]

    operations = [
        migrations.AddField(
            model_name='image',
            name='FIELD_image',
            field=models.FileField(blank=True, upload_to=''),
        ),
    ]
