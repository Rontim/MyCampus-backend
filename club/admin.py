from django.contrib import admin

from club.models import Club

@admin.register(Club)
class ClubAdmin(admin.ModelAdmin):
    list_display = ('club_name',)
    search_fields = ('club_name',)
