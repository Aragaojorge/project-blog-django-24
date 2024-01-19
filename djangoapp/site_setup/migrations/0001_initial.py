# Generated by Django 4.2.9 on 2024-01-18 01:41

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='MenuLink',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('text', models.CharField(max_length=50)),
                ('url_or_path', models.CharField()),
                ('new_tab', models.BooleanField(default=False)),
            ],
            options={
                'verbose_name': 'Menu Link',
                'verbose_name_plural': 'Menu Links',
            },
        ),
    ]