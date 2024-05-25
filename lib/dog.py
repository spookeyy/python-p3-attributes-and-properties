#!/usr/bin/env python3

APPROVED_BREEDS = [
    "Mastiff",
    "Chihuahua",
    "Corgi",
    "Shar Pei",
    "Beagle",
    "French Bulldog",
    "Pug",
    "Pointer"
]

class Dog:
    def __init__(self, name="", breed="Chihuahua"):
        self.name = name
        self.breed = breed
# check if it exists first
        if self.breed not in APPROVED_BREEDS:
            print("Breed must be in list of approved breeds." )
    # proceed and check if it is a string
        elif self.name == "" or self.name != type(str):
            print("Name must be string between 1 and 25 characters.")