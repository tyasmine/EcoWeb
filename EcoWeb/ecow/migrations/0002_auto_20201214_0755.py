# Generated by Django 3.1 on 2020-12-14 07:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ecow', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='bio',
            field=models.TextField(blank=True, max_length=1000),
        ),
        migrations.AddField(
            model_name='user',
            name='seniority',
            field=models.IntegerField(default=2020),
        ),
        migrations.AlterField(
            model_name='user',
            name='first_name',
            field=models.CharField(max_length=200),
        ),
        migrations.AlterField(
            model_name='user',
            name='last_name',
            field=models.CharField(max_length=200),
        ),
    ]
