# Generated by Django 5.1.2 on 2024-10-30 18:16

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0002_blogindexpage_body_blogindexpage_date_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='blogindexpage',
            name='date',
            field=models.DateField(default=datetime.datetime(2024, 10, 30, 18, 16, 26, 787584, tzinfo=datetime.timezone.utc), verbose_name='Post date'),
        ),
    ]
