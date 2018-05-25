# Generated by Django 2.0.4 on 2018-05-25 07:29

import blog.models
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0002_auto_20180525_0719'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='lnglat',
            field=models.CharField(blank=True, help_text='경도/위도 포멧으로 입력', max_length=50, validators=[blog.models.lnglat_validator]),
        ),
    ]
