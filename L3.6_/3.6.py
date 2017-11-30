# -*- coding: utf-8 -*-

class Animal:
    name = ''
    sound = ''
    size = ''
    food = ''
    paws = 0
    wings = 0

    def animal_sound(self):
        print(self.animal_sound)

    def amimal_food(self, food):
        print('Eat', food, 'kg of', 'animal_eats.')


class Big_animal ( Quadruped ):
    sound = 'mu-mu'
    food = 'grass'
    paws = 4
    print(cow.animal_name, cow.__dict__)
    cow.animal_shouts ()
    cow.take_profit ()

# class beak (Animal) :
#     def __init__(self, name):
#         Animal.__init__(self, name, 'small', 2, 2)
#
# class big_an (Animal) :
#     def __init__(self, name):
#         Animal.__init__ ( self, name, 'big', 4, 0)
#
# chickens = beak("Кирицы")
# ducks = beak("Утки")
# geese = beak("Гуси")
#
# Cows = big_an("Коровы")
# goats = big_an("Козы")
# sheep = big_an("Овцы")
# pigs = big_an("Свиньи")