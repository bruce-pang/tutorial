# Generated by Django 4.2.13 on 2024-06-22 10:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('quikstart', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userinfo',
            name='token',
            field=models.CharField(blank=True, max_length=64, null=True, verbose_name='token'),
        ),
    ]