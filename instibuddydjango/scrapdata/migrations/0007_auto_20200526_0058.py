# Generated by Django 3.0.5 on 2020-05-25 19:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('scrapdata', '0006_auto_20200526_0055'),
    ]

    operations = [
        migrations.AlterField(
            model_name='scrapcode',
            name='phone_number',
            field=models.CharField(max_length=40, null=True),
        ),
    ]
