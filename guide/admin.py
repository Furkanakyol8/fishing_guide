from django.contrib import admin
from .models import Guide

class GuideAdmin(admin.ModelAdmin):
    list_display = ("name", "slug")
    search_fields = ("name", "description", "image",)
    readonly_fields = ("slug",)

admin.site.register(Guide, GuideAdmin)