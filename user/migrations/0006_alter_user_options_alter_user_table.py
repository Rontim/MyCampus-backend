# Generated by Django 5.0.2 on 2024-03-03 10:11

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0005_user_interest'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='user',
            options={'verbose_name_plural': 'Users'},
        ),
        migrations.AlterModelTable(
            name='user',
            table='User',
        ),
    ]