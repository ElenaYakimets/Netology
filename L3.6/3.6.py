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


class Mammals(Animal):
    gives_milk = False
    gives_meat = False

    def we_have(self):
        if self.gives_milk:
            print('Дает молоко.')
        elif self.gives_meat:
            print('Дает мясо.')


class Birds(Animal):
    gives_eggs = False

    def we_have(self):
        if self.gives_eggs:
            print('Несет яйца.')


class Big_Cows(Mammals):
    def __init__(self, litres):
        Animal.__init__(self, 'cow', 'mumu')
        self.milk_out_litres = litres
        self.gives_milk = True


cow = Big_Cows(5)
print(cow.name)
print(cow.milk_out_litres)
cow.we_have()


class Big_Goats (Mammals):
    def __init__(self, the_number):
        Animal.__init__(self, 'goat', 'bee-bee')
        self.horns = the_number
        self.gives_milk = True


goat = Big_Goats(2)
print(goat.name)
print(goat.horns)
goat.anim_sound()
goat.we_have()


class Big_Sheeps (Mammals):
    def __init__(self, kilo):
        Animal.__init__(self, 'sheep', 'bee-bee-bee')
        self.wool = kilo
        self.gives_milk = True


sheep = Big_Sheeps(15)
print(sheep.name)
print(sheep.wool)
sheep.anim_sound()
sheep.we_have()


class Big_Pigs (Mammals):
    def __init__(self, meat_kg):
        Animal.__init__(self, 'pig', 'hru')
        self.meat = meat_kg
        self.gives_meat = True


pig = Big_Pigs(45)
print(pig.name)
print(pig.meat)
pig.anim_sound()
pig.we_have()


class Beak_Ducks (Birds):
    def __init__(self, can_dive):
        Animal.__init__(self, 'duck', 'crya-crya')
        self.dive_meters = can_dive
        self.gives_eggs = True


duck = Beak_Ducks(0.5)
print(duck.name)
print(duck.dive_meters)
duck.anim_sound()
duck.we_have()


class Beak_Chickens(Birds):
    def __init__(self, make_eggs):
        Animal.__init__(self, 'chicken', 'ko-ko')
        self.eggs = make_eggs
        self.gives_eggs = True


chicken = Beak_Chickens(20)
print(chicken.name)
print(chicken.eggs)
chicken.anim_sound()
chicken.we_have()


class Beak_Geese(Birds):
    def __init__(self, can_swim):
        Animal.__init__(self, 'goose', 'ga-ga')
        self.swim_meters = can_swim
        self.gives_eggs = True


goose = Beak_Geese(300)
print(goose.name)
print(goose.swim_meters)
goose.anim_sound()
goose.we_have()
