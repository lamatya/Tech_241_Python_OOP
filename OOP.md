
OOP- Object Oriented Programming

Classes- Creating a class is like a template or a design that can encapsulates data and methods that operate on the data. It defines a set of attributes and methods that characterises the behaviours of the objects created from the class. 

Example of a class;

class Dog:

![MicrosoftTeams-image (7).png](..%2F..%2F..%2FDownloads%2FMicrosoftTeams-image%20%287%29.png)

    animal_kind = "canine" # class variable

    def bark(self):  # class function = methods
        self.animal_kind
        # print(self.animal_kind)
        return "woof"


The four Pillars of OOP
- Encapsulation - classes are self contained.
- *Abstraction - continuation of oop. You dont always need to know how something works, to use it.
- *Inheritance - Inherit the variables and class methods from the parent class.
- Polymorphism - Methods can have the same name, but can act differently.


For the Four Pillars, what is the purpose of each? And showcase an example of each in action.
Recommendation is use Dog examples for classes, and Animal->Reptile->Snake->Python example for 4 pillars.

- The purpose of Encapsulation is one of the fundamental concepts in OOP, it helps in describing the idea of wrapping the data and the methods that work on data. It hides the data therefore, the program can focus on the overall logic.

# Showcasing Encaspulation

from reptile import Reptile

class Snake(Reptile):

    def __init__(self):
        super().__init__()
        self.forked_tongue = True
        self.cold_blooded = True
        self.venom = None # Not all snale are venomous
        self.limbs = False

    def use_tongue_to_smell(self):
        print("Do I say it smells, or tastes nice.....?")

- sidney = Snake()

- sidney.breathe() # Animal method

- sidney.seek_heat() # Reptile method

- sidney.use_ tounge_to_smell() # snake method

- Encapsulation is also really good, for protecting important variables.

Types of modifiers in python;

- Public -- anyone, anywhere can use it

- Private -- accessible only within the class

- protected --

Abstraction:

It is one of the key concepts of OOP and its to handle the complexity by hiding unnecessary details from the user which helps user to implement more complex logic.

It is used to describe things in simple terms. 

lass Animal:

    def __init__(self):

        self.alive = True
        self.spine = True
        self.eyes = True
        self.lungs = True

    def breathe(self):
        print("One breath at a time, in and out")

    def eat(self):
        print("Nom Nom Nom")

    def procreate(self):
        print("This to find a mate")

    def move(self):
        print("Onwards and upwards")
Breathe is abstracted


Inheritance:

Example of Inheritance 

from animal import Animal

class Reptile(Animal):

    def __init__(self):
        super().__init__() # initiation the parent/base class -  inherit everything from Animal.
        self.cold_blooded = True
        self.tetrapod = None # Not all reptiles have 4 legs
        self.heart_chambers = [3, 4]
        self.amniotic_eggs = None # Not true nor false

    def seek_heat(self):
        print("it's chilly outside, I need a sunbed")

    def hunt(self):
        print("Hunting prey")

    def use_venom(self):
        print("If I have it, may as well use it")

    def attract_mate_through_scent(self):
        print("Time to put on the aftershave")

- bulbasaur = Reptile()

- bulbasaur.hunt()  # Reptile Method

- bulbasaur.breathe() # Animal method

Polymorphism

from snake import Snake

class Python(Snake):

    def __init__(self):
        super().__init__()
        self.large = True
        self.two_lungs = True
        self.venom = False

    def digest_large_prey(self):
        print("ok, hand me the stretchy pants")

    def constrict(self):
        print("and...squeeeeeze")

    def climb(self):
        print("up we go")

    def shed_skin(self):
        print("I'm growing out of this now")

    def breathe(self):
        print("I am breathing but I am a Python!")

Picture showing all 4 pillars 

![MicrosoftTeams-image (10).png](..%2F..%2F..%2FDownloads%2FMicrosoftTeams-image%20%2810%29.png)