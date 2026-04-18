class Person:
    massage = 'class state property'

    def __init__(self , name , age):
        self.name = name
        self.age = age

    
    def introduce(self):
        print(f"hello, my name is {self.name} and i am {self.age}")


    @classmethod
    def explain(cls):
        print('class method is executed')

person1 = Person('omar' , 21)
person2 = Person('aziz' , 65)
persom3 = Person('ulube', 54)

person1.introduce()
print(person2.name)


# class state -> statick 

new_massage = Person.massage
print(new_massage)

Person.explain()
