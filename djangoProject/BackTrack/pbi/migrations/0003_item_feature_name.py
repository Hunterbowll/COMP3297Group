# Generated by Django 2.2.6 on 2019-10-22 15:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pbi', '0002_auto_20191022_1312'),
    ]

    operations = [
        migrations.AddField(
            model_name='item',
            name='Feature_Name',
            field=models.CharField(default=1, max_length=200),
            preserve_default=False,
        ),
    ]
