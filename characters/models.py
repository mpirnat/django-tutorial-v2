from django.db import models


class Character(models.Model):

    name = models.CharField(max_length=200)
    background = models.TextField()

    level = models.IntegerField()
    experience_points = models.IntegerField()

    max_hit_points = models.IntegerField()
    current_hit_points = models.IntegerField()

    strength = models.IntegerField()
    dexterity = models.IntegerField()
    constitution = models.IntegerField()
    intelligence = models.IntegerField()
    wisdom = models.IntegerField()
    charisma = models.IntegerField()

    created = models.DateTimeField(auto_now_add=True)
    modified = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name
