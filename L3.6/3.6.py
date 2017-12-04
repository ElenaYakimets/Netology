# -*- coding: utf-8 -*-


class Animal():
    name = ''
    sound = ''
    food = ''


    def __init__(self, a_name, a_sound):
        self.name = a_name
        self.sound = a_sound


    def anim_sound(self):
        print(self.sound)


class Big_Cows(Animal):
    def __init__(self, litres):
        Animal.__init__(self, 'cow', 'mumu')
        self.milk_out_litres = litres


cow = Big_Cows(5)
print(cow.name)
print(cow.milk_out_litres)
cow.anim_sound()


class Big_Goats (Animal):
    def __init__(self, the_number):
        Animal.__init__(self, 'goat', 'bee-bee')
        self.horns = the_number


goat = Big_Goats(2)
print(goat.name)
print(goat.horns)
goat.anim_sound()


class Big_Sheeps (Animal):
    def __init__(self, kilo):
        Animal.__init__(self, 'sheep', 'bee-bee-bee')
        self.wool = kilo


sheep = Big_Sheeps(15)
print(sheep.name)
print(sheep.wool)
sheep.anim_sound()


class Big_Pigs (Animal):
    def __init__(self, meat_kg):
        Animal.__init__(self, 'pig', 'hru')
        self.meat = meat_kg


pig = Big_Pigs(45)
print(pig.name)
print(pig.meat)
pig.anim_sound()


class Beak_Ducks (Animal):
    def __init__(self, can_dive):
        Animal.__init__(self, 'duck', 'crya-crya')
        self.dive_meters = can_dive


duck = Beak_Ducks(0.5)
print(duck.name)
print(duck.dive_meters)
duck.anim_sound()


class Beak_Chickens(Animal):
    def __init__(self, make_eggs):
        Animal.__init__(self, 'chicken', 'ko-ko')
        self.eggs = make_eggs


chicken = Beak_Chickens(20)
print(chicken.name)
print(chicken.eggs)
chicken.anim_sound()


class Beak_Geese(Animal):
    def __init__(self, can_swim):
        Animal.__init__(self, 'goose', 'ga-ga')
        self.swim_meters = can_swim


goose = Beak_Geese(300)
print(goose.name)
print(goose.swim_meters)
goose.anim_sound()
