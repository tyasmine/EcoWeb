# Generated by Django 3.1 on 2020-12-14 13:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ecow', '0003_auto_20201214_0759'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='public',
            field=models.BooleanField(default=False),
        ),
    ]
