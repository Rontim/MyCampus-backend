# Generated by Django 5.0.2 on 2024-03-06 09:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('topic', '0002_alter_topic_table'),
        ('user', '0006_alter_user_options_alter_user_table'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='interest',
            field=models.ManyToManyField(related_name='interests', to='topic.topic'),
        ),
    ]
