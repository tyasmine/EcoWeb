# Generated by Django 3.1 on 2021-04-06 09:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ecow', '0016_auto_20210406_0826'),
    ]

    operations = [
        migrations.AlterField(
            model_name='article',
            name='URL_image',
            field=models.URLField(default='https://upload.wikimedia.org/wikipedia/commons/thumb/a/ac/No_image_available.svg/1024px-No_image_available.svg.png'),
        ),
    ]
