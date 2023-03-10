# Generated by Django 4.0.4 on 2023-01-06 14:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Management', '0014_alter_user_email'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='email',
            field=models.EmailField(max_length=254, null=True, unique=True),
        ),
        migrations.AlterField(
            model_name='user',
            name='gender',
            field=models.CharField(max_length=20, null=True),
        ),
    ]
