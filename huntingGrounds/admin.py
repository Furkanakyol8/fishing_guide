from django.contrib import admin
from .models import Grounds

class GroundsAdmin(admin.ModelAdmin):
    list_display = ('name', 'description', 'image')  # Listede görüntülemek istediğiniz alanları belirtin

admin.site.register(Grounds, GroundsAdmin)
