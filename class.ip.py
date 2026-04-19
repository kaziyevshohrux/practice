#  inheritance  and  polymorphism 

class Animal:
    def __init__(self, voice):
        self.voice = voice

    
    def make_voice(self):
        print(f"this animal make voice")


class Dog(Animal):
    def __init__(self, voice, name , sound):
        self.name = name
        self.sound = sound
        super().__init__(voice)

    def introduce(self):
        print(f"{self.name} says : {self.sound}")

    def protected():
        print('i can protect you')

    def make_voice(self):
        print(f"{self.name} can make sound like this -> {self.sound} ")

 

class Cat(Animal):
    def __init__(self, voice, name , sound):
        self.name = name
        self.sound = sound
        super().__init__(voice)

    def introduce(self):
        print(f"{self.name} says : {self.sound}")

    def play():
        print('i can play with you')



class Fish(Animal):
    def __init__(self, voice, name , sound):
        self.name = name
        self.sound = sound
        super().__init__(voice)

    def introduce(self):
        print(f"{self.name} says : {self.sound}")

    def Swim():
        print('i can swim')



dog = Dog(True , 'Bayrin' , 'vov-vov')
cat = Cat(True , 'Luci', 'miyaau')
fish = Fish(False , 'Nemo', 'zzzz-zzzzzz')


dog.introduce()
fish.make_voice()

dog.make_voice()

print('=============')

# fish ->  Fish  -> Animal  -> Objects   

a = isinstance(fish, Fish)
b= isinstance(Animal, object)

c= a and b
print(c)
print('=================')

data1 = issubclass(Fish , object)
data2 = issubclass(Fish, Animal)


print(data1 , data2)