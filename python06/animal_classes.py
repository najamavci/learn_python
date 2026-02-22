class Animal:
    def make_noise(self):
        print("Detta djur har vi inget ljud för.")

class Dog(Animal):
    def make_noise(self):
        print("Voff!")

class Cat(Animal):
    def make_noise(self):
        super().make_noise()
        print("Mjau!")

class Rooster(Animal):
    def make_noise(self):
        print("Kuckeliku!")

#2b.Lägg till en klass för ett annat djur, till exempel en papegoja.
class Parrot(Animal):
    def make_noise(self):
        print("Hello! I am a parrot!")
        

def sound_off(animals):
    for animal in animals:
        animal.make_noise()

c = Cat()
d = Dog()
h = Rooster()
e = Parrot()

sound_off([c, d, h,e])

#To execute this code, please run these on the terminal: 
# /absolute-path/nbi-hendelsakademin-python/python06/animal_classes.py

'''
2a Vad gör följande kod? Fixa eventuella fel.
class Animal:
    def make_noise(self):
        print("Detta djur har vi inget ljud för.")

class Dog(Animal):
    def make_noise(self):
    print("Voff!")

class Cat(Animal):
    def make_noise(shelf):
        super().make_noise()
        print("Mjau!")

def sound_off(animal):
    animal.make_noise()

c = Cat()
d = Dog()
h = Rooster()
sound_off([c, d, h])

'''