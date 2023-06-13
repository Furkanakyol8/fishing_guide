from django.contrib import admin
from .models import Fishes, Category



class FishesAdmin(admin.ModelAdmin):
    list_display = ("name", "slug",)
    search_fields = ("name", "description", "image")
    readonly_fields = ("slug",)
    list_filter = ("category",)


admin.site.register(Fishes, FishesAdmin)
admin.site.register(Category)

