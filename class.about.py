# class Person:
#     massage = 'class state property'

#     def __init__(self , name , age):
#         self.name = name
#         self.age = age

    
#     def introduce(self):
#         print(f"hello, my name is {self.name} and i am {self.age}")


#     @classmethod
#     def explain(cls):
#         print('class method is executed')

# person1 = Person('omar' , 21)
# person2 = Person('aziz' , 65)
# persom3 = Person('ulube', 54)

# person1.introduce()
# print(person2.name)


# class state -> statick 

# new_massage = Person.massage
# print(new_massage)

# Person.explain()


# print('==========special methods=============')

# special methods -> __init__, ....


class Car():
    firstMassage = "this is a car class"

    def __init__(self , name , year):

        self.name = name
        self.year = year

    def startengine(self):
        print(f"{self.name} is start engine")

    def stopengine(self): 
        print(f"{self.name} is stop engine")

    def __str__(self):                     # yasalgan objectni  'print' qilse 
        return f"{self.name} was produced in {self.year} "
    def __call__(self):                    # yasalgan objecti function oxsajb call qilse 
        print('call look like function ')
    

car = Car('bmw', 2020)
print(car.firstMassage)
car.startengine()
car.stopengine()
print(car)
car()

