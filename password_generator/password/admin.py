from django.contrib import admin
from .models import Generator

class GeneratorAdmin(admin.ModelAdmin):
    list_display = (
            "username", 
            "site", 
            "password", 
            "date", )
admin.site.register(Generator, GeneratorAdmin)

