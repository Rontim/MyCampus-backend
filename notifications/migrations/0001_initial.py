# Generated by Django 5.0.2 on 2024-02-27 11:20

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('club', '0001_initial'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='SystemNotifications',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('content', models.TextField()),
                ('create_at', models.DateField(auto_now_add=True)),
                ('system', models.BooleanField(default=True)),
            ],
            options={
                'db_table': 'System Notifications',
            },
        ),
        migrations.CreateModel(
            name='ClubNotifications',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('content', models.TextField()),
                ('create_at', models.DateField(auto_now_add=True)),
                ('club', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='club.club')),
            ],
            options={
                'db_table': 'Club Notifications',
            },
        ),
        migrations.CreateModel(
            name='UserNotifications',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('content', models.TextField()),
                ('create_at', models.DateField(auto_now_add=True)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'db_table': 'User Notifications',
            },
        ),
    ]
