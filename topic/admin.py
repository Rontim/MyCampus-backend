from django.contrib import admin

from .models import Topic

@admin.register(Topic)
class TopicAdmin(admin.ModelAdmin):
    list_display =  ('topic_name', )
    search_fields = ('topic_name', )
