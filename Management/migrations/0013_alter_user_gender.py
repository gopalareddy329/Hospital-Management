# Generated by Django 4.0.4 on 2023-01-06 13:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Management', '0012_user_address_user_bloogroup'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='gender',
            field=models.CharField(blank=True, max_length=7, null=True),
        ),
    ]
