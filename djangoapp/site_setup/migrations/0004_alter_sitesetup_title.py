# Generated by Django 4.2.9 on 2024-01-18 02:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('site_setup', '0003_alter_sitesetup_options'),
    ]

    operations = [
        migrations.AlterField(
            model_name='sitesetup',
            name='title',
            field=models.CharField(max_length=50),
        ),
    ]