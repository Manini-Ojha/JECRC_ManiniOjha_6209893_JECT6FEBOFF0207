#heirarchial
#It is a type of inheritance in which the properties will be derived from single parent class to multiple child class

class Parent:
    gold='2kg'
    silver='10kg'
    no_of_flats=12
class smallestBrother(Parent):
    name='Rick'
class ElderBrother(Parent):
    name='Nick'
class Sister(Parent):
    name='Dawn'
print(smallestBrother.gold)
print(ElderBrother.silver)
print(Sister.no_of_flats)