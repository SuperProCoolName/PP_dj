from django.contrib import admin
from .models import Ad

# Register your models here.


class AdAdmin(admin.ModelAdmin):
    list_display = ('title', 'price')
    readonly_fields = ('created_at',)
    search_fields = ('title', 'description')


admin.site.register(Ad, AdAdmin)
