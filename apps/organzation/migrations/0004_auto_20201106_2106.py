# Generated by Django 2.2.16 on 2020-11-06 21:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('organzation', '0003_auto_20201106_1918'),
    ]

    operations = [
        migrations.AlterField(
            model_name='teacher',
            name='image',
            field=models.ImageField(default='', upload_to='teacher/%Y/%m', verbose_name='头像'),
        ),
    ]
