# Generated by Django 4.0.4 on 2023-01-06 13:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Management', '0006_rename_is_student_user_is_paitent_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='Mobile',
            field=models.CharField(blank=True, max_length=10, null=True),
        ),
    ]