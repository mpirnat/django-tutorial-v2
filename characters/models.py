import random
from django.db import models


def generate_stat():
    """Roll 3D6 to make a stat!"""
    return (random.randint(1, 6) + random.randint(1, 6) +
            random.randint(1, 6))


class Character(models.Model):

    name = models.CharField(max_length=200)
    background = models.TextField()

    level = models.IntegerField(default=1)
    experience_points = models.IntegerField(default=0)

    max_hit_points = models.IntegerField(default=10)
    current_hit_points = models.IntegerField(default=10)

    strength = models.IntegerField(default=generate_stat)
    dexterity = models.IntegerField(default=generate_stat)
    constitution = models.IntegerField(default=generate_stat)
    intelligence = models.IntegerField(default=generate_stat)
    wisdom = models.IntegerField(default=generate_stat)
    charisma = models.IntegerField(default=generate_stat)

    created = models.DateTimeField(auto_now_add=True)
    modified = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name
