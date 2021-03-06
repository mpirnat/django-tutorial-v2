from django.contrib import admin
from characters.models import Character, Race, Class, Item


class CharacterAdmin(admin.ModelAdmin):

    list_display = ('name', 'level', 'race', 'cclass', 'player',
                    'created', 'modified')
    list_filter = ('cclass__name', 'race__name', 'created', 'modified')

    search_fields = ['name', 'background', 'race__name', 'cclass__name',
                     'player__username']

    readonly_fields = ('created', 'modified')

    fieldsets = [
        (None, {'fields': ['player', 'name', 'level', 'race', 'cclass',
                           'background']}),
        ('Hit Points', {'fields': ['max_hit_points', 'current_hit_points']}),
        ('Stats', {'fields': ['strength', 'dexterity', 'constitution',
                              'intelligence', 'wisdom', 'charisma']}),
        (None, {'fields': ['experience_points', 'inventory']}),
        ('Date Information', {'fields': ['created', 'modified']}),
    ]


admin.site.register(Character, CharacterAdmin)
admin.site.register(Race)
admin.site.register(Class)
admin.site.register(Item)
