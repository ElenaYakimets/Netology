# -*- coding: utf-8 -*-

class Animal ( object ):
    """docstring"""
    def __init__(self, name, size, paws, wings):
        """Constructor"""
        self.name = name
        self.size = size
        self.paws = paws
        self.wings = wings

class beak (Animal) :
    def __init__(self, name):
        Animal.__init__(self, name, 'small', 2, 2)

class big_an (Animal) :
    def __init__(self, name):
        Animal.__init__ ( self, name, 'big', 4, 0)

chickens = beak("Кирицы")
ducks = beak("Утки")
geese = beak("Гуси")

Cows = big_an("Коровы")
goats = big_an("Козы")
sheep = big_an("Овцы")
pigs = big_an("Свиньи")