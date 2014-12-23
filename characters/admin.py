from django.contrib import admin
from characters.models import Character, Race, Class, Item

admin.site.register(Character)
admin.site.register(Race)
admin.site.register(Class)
admin.site.register(Item)
