# Generated by Django 3.0.5 on 2020-05-25 18:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('scrapdata', '0003_auto_20200525_2328'),
    ]

    operations = [
        migrations.AlterField(
            model_name='scrapcode',
            name='prof_Name',
            field=models.CharField(max_length=30, null=True),
        ),
    ]