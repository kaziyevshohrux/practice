'''
list()
methods()
lumbda function()
enamurate , map , filter

'''

person = dict(name='umar', age = 22)    #dictionary
mix = (10 , 'salom' , False)            #tuple
grups = ['mit41', 'mit43', 'mit39']

for i in grups:
    print('grups name' , i)


fruits = ['apple', 'abrikos', 'mango', 'hurmo']

a= fruits[2]
b= fruits[0:2]
c= fruits[2:3]
d=fruits[1:3:1]
f=fruits[0::3]
j=fruits[::-1]


print(a)
print(b)
print(c)
print(d)
print(f)
print(j)

print('=========================methods=============================')
# list methods  ->   append(), insert(), pop(), remove(), clear(), sort(), sorted(), index(), 


animal = ['dog', 'fish', 'cat', 'lion', 'tiger']
print(animal)

animal.append('mice')
print(animal)

animal.insert(0,'chubakabra')
print(animal)

size = len(animal)-1
animal.pop(size)
print(animal)

animal.pop(0)
print(animal)

animal.remove('fish')
print(animal)

a=animal.index('lion')
print(a)

animal.clear()
print(animal)


numbers = [2,5,6,22,2,45,2,23,12,5,0,202]

numbers.sort()

print(numbers)

sortednum = sorted(numbers)

print(sortednum)



print('========lamda========')

def xyz(x,y): return x*y
print(xyz(5,5))



people = [
    ('omar', 21, 'a'),
    ('ulugbek' ,45, 'l'),
    ('joratbe', 65, 'c'),
    ('furqat', 18, 's')
]

people.sort()
print(people)

print('====yosh====')


people.sort(key=lambda person:person[2])
print(people)