# Generated by Django 2.0.4 on 2018-07-05 01:33

from django.db import migrations
import imagekit.models.fields


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0014_auto_20180618_0621'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='photo',
            field=imagekit.models.fields.ProcessedImageField(blank=True, max_length=300, upload_to='blog/post/%Y/%m/%d'),
        ),
    ]
