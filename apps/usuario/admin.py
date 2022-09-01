from django.contrib import admin
from django.contrib.admin.decorators import register
from .models import Usuario


@admin.register(Usuario)
class ProfileUsers(admin.ModelAdmin):
    list_display= ('usuario', 'resume')