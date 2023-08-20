from django.contrib import admin
from .models import Profile
# Register your models here

class profileAdmin(admin.ModelAdmin):
    list_display = ['created_at']

admin.site.register(Profile,profileAdmin)
