from django.contrib import admin

# Register your models here.
from core.models import Entry, Language

admin.site.register(Entry)
admin.site.register(Language)
