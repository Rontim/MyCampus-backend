from django.contrib import admin
from .models import ClubInteraction, UserInteraction


admin.site.register(ClubInteraction)
admin.site.register(UserInteraction)
