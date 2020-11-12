# Generated by Django 2.2.16 on 2020-11-06 19:18

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('organzation', '0002_courseorg_category'),
    ]

    operations = [
        migrations.AddField(
            model_name='courseorg',
            name='course_nums',
            field=models.IntegerField(default=0, verbose_name='课程数'),
        ),
        migrations.AddField(
            model_name='courseorg',
            name='students',
            field=models.IntegerField(default=0, verbose_name='学习人数'),
        ),
        migrations.AddField(
            model_name='teacher',
            name='image',
            field=models.ImageField(default=django.utils.timezone.now, upload_to='org/%Y/%m', verbose_name='logo'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='courseorg',
            name='image',
            field=models.ImageField(upload_to='org/%Y/%m', verbose_name='logo'),
        ),
    ]
