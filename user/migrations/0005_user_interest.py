# Generated by Django 5.0.2 on 2024-02-28 08:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('club', '0001_initial'),
        ('user', '0004_alter_user_is_active'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='interest',
            field=models.ManyToManyField(to='club.club'),
        ),
    ]
