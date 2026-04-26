"""
1) what is comp and type of comp 
2) dict and set comp 

"""

# built comp 
"""
1) *iterable 
2) <expression> for item in iterable
3)  <expression> for item in iterable condition 
"""

print('=======*iterable========')
numbers = [1,2,3,54,4,52,0,11]
new_num = [*numbers]                     #1

print(id(numbers), id(new_num))


print('======exp -> for i in iterable========')
people = [('amir', 23), ('fotih', 52), ('arastu', 84)]

person_name = [person[0] for person in people]                   #2
print(person_name)


print('========exp for i in iterable + cond')


cars = [
    ('mers' , 114),
    ('tayota', 103),
    ('chevrolet0', 45),
    ('bmw', 92)
]

car_filter = [car[0] for car in cars if car[1]>80]
print(car_filter)