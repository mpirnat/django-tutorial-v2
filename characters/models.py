import random
from django.db import models


def generate_stat():
    """Roll 3D6 to make a stat!"""
    return roll_dice(3, 6)


def roll_dice(times, sides, modifier=0):
    """
    Simulate a dice roll of XdY + Z.

    "Rolls" a die of Y sides X times, gets the sum, and adjusts it by an
    optional modifier.

    Example usage:

       # Stats: 3d6
       >>> roll_dice(3, 6)

       # Saving throw: 1d20
       >>> roll_dice(1, 20)

       # Damage (longsword +1): 1d8 + 1
       >>> roll_dice(1, 8, plus=1)

       # Damage (cursed longsword - 2): 1d8 - 2
       >>> roll_dice(1, 8, plus=-2)
    """
    randint = random.randint
    return sum(map(lambda x: randint(1, sides), range(times))) + modifier


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
