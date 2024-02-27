from django.contrib import admin

from .models import Topic

@admin.register(Topic)
class TopicAdmin(admin.ModelAdmin):
    list_display = '__all__'
    search_fields = ('topic_name')
