# Generated by Django 2.0.4 on 2018-06-18 06:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0013_auto_20180618_0354'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='photo',
            field=models.ImageField(blank=True, max_length=300, upload_to='blog/post'),
        ),
    ]
