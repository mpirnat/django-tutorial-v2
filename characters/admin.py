from django.contrib import admin
from characters.models import Character, Race, Class, Item


class CharacterAdmin(admin.ModelAdmin):
    fieldsets = [
        (None, {'fields': ['name', 'level', 'race', 'cclass', 'background']}),
        ('Hit Points', {'fields': ['max_hit_points', 'current_hit_points']}),
        ('Stats', {'fields': ['strength', 'dexterity', 'constitution',
                              'intelligence', 'wisdom', 'charisma']}),
        (None, {'fields': ['experience_points', 'inventory']}),
    ]

admin.site.register(Character, CharacterAdmin)
admin.site.register(Race)
admin.site.register(Class)
admin.site.register(Item)
