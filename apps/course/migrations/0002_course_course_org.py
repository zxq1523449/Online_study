# Generated by Django 2.2.16 on 2020-11-06 20:27

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('organzation', '0003_auto_20201106_1918'),
        ('course', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='course',
            name='course_org',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='organzation.CourseOrg', verbose_name='所属机构'),
        ),
    ]
