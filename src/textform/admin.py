from django.contrib import admin

from .models import Message

class MessageAdmin(admin.ModelAdmin):
    fields = ['pub_date', 'text']

admin.site.register(Message)
