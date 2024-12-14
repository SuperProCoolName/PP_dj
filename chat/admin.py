from django.contrib import admin
from .models import Message


class MessageAdmin(admin.ModelAdmin):
    date_hierarchy = 'timestamp'
    readonly_fields = ('sender', 'receiver', 'content', 'is_read', 'timestamp')
    search_fields = ('content', 'timestamp')


admin.site.register(Message, MessageAdmin)
