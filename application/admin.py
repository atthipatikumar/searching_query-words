from django.contrib import admin

from .models import Details

class DetailsAdmin(admin.ModelAdmin):
    list_display = ("name", "state_id",)

admin.site.register(Details, DetailsAdmin)