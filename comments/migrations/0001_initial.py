# Generated by Django 5.0.2 on 2024-03-07 15:22

import comments.models
import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('blog', '0001_initial'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='BlogComment',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('unique_id', models.CharField(default=comments.models.generate_uuid, max_length=200, unique=True)),
                ('comment', models.TextField()),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('blog', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='blog.blog', to_field='slug')),
                ('commentor', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, to_field='username')),
                ('mentions', models.ManyToManyField(blank=True, related_name='mentions', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name': 'Blog Comment',
                'verbose_name_plural': 'Blog Comments',
                'db_table': 'Blog_comments',
            },
        ),
        migrations.CreateModel(
            name='ReplyComment',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('unique_id', models.CharField(default=comments.models.generate_uuid, max_length=200, unique=True)),
                ('reply', models.TextField()),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('comment', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='replies', to='comments.blogcomment', to_field='unique_id')),
                ('mentions', models.ManyToManyField(blank=True, related_name='mentioned_in_replies', to=settings.AUTH_USER_MODEL)),
                ('replier', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, to_field='username')),
            ],
            options={
                'verbose_name': 'Reply Comment',
                'verbose_name_plural': 'Reply Comments',
                'db_table': 'Reply_comments',
            },
        ),
    ]