# Generated by Django 4.2.13 on 2024-06-21 09:46

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('serializer_quik', '0002_rename_create_time_user_createtime'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='updatetime',
            field=models.DateTimeField(default=django.utils.timezone.now, verbose_name='更新时间'),
        ),
    ]
