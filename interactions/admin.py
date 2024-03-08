from django.contrib import admin
from .models import ClubInteraction, UserInteraction



class ClubInteractionAdmin(admin.ModelAdmin):
    list_display = ('user', 'club_id')
    list_filter = ('user', 'club_id')
    search_fields = ('user__username', 'club_id__name')
   

admin.site.register(ClubInteraction, ClubInteractionAdmin)

class UserInteractionAdmin(admin.ModelAdmin):
    list_display = ('user', 'follow_user')
    list_filter = ('user', 'follow_user')
    search_fields = ('user__username', 'follow_user__username')
    

admin.site.register(UserInteraction, UserInteractionAdmin)