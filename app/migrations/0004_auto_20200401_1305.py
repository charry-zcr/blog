# Generated by Django 2.1.5 on 2020-04-01 05:05

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0003_auto_20200329_1429'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='friendlink',
            options={'ordering': ['position'], 'verbose_name': '链接', 'verbose_name_plural': '链接'},
        ),
    ]
