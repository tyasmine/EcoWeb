# Generated by Django 3.1 on 2021-02-25 17:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ecow', '0010_auto_20210224_1158'),
    ]

    operations = [
        migrations.AlterField(
            model_name='idea',
            name='URL_video',
            field=models.URLField(blank=True, default='https://www.westernheights.k12.ok.us/wp-content/uploads/2020/01/No-Photo-Available.jpg'),
        ),
        migrations.AlterField(
            model_name='project',
            name='URL_video',
            field=models.URLField(blank=True, default='https://www.westernheights.k12.ok.us/wp-content/uploads/2020/01/No-Photo-Available.jpg'),
        ),
    ]
