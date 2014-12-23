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


class Alignment:
    LAWFUL_GOOD = 'LG'
    LAWFUL_NEUTRAL = 'LN'
    LAWFUL_EVIL = 'LE'
    NEUTRAL_GOOD = 'NG'
    NEUTRAL = 'NN'
    NEUTRAL_EVIL = 'NE'
    CHAOTIC_GOOD = 'CG'
    CHAOTIC_NEUTRAL = 'CN'
    CHAOTIC_EVIL = 'CE'

    CHOICES = (
        (LAWFUL_GOOD, 'Lawful Good'),
        (LAWFUL_NEUTRAL, 'Lawful Neutral'),
        (LAWFUL_EVIL, 'Lawful Evil'),
        (NEUTRAL_GOOD, 'Neutral Good'),
        (NEUTRAL, 'Netural'),
        (NEUTRAL_EVIL, 'Neutral Evil'),
        (CHAOTIC_GOOD, 'Chaotic Good'),
        (CHAOTIC_NEUTRAL, 'Chaotic Neutral'),
        (CHAOTIC_EVIL, 'Chaotic Evil'),
    )


class Race(models.Model):

    name = models.CharField(max_length=200)
    description = models.TextField()

    def __str__(self):
        return self.name


class Class(models.Model):

    name = models.CharField(max_length=200)
    description = models.TextField()

    def __str__(self):
        return self.name

    class Meta:
        verbose_name_plural = "Classes"


class Item(models.Model):

    name = models.CharField(max_length=200)
    description = models.TextField()

    value = models.IntegerField(default=0)
    weight = models.IntegerField(default=1)

    def __str__(self):
        return self.name


class Character(models.Model):

    name = models.CharField(max_length=200)
    background = models.TextField()

    race = models.ForeignKey(Race)
    # This name isn't ideal, but 'class' is a Python builtin, so here we are...
    # I went with 'cclass' as short for 'character class'.
    cclass = models.ForeignKey(Class, verbose_name="class")

    alignment = models.CharField(max_length=2, choices=Alignment.CHOICES,
            default=Alignment.NEUTRAL)

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

    inventory = models.ManyToManyField(Item)

    created = models.DateTimeField(auto_now_add=True)
    modified = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name
