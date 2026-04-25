# itarable objects

# string , list , uple , range , set , dict .... - - bu data type lar iterable objects hisoblanadi

a = 'mit'
for letter in a:
    print(letter)


for i in range(3):
    print(i)


print('==============')


person = {'name': 'omar', 'age': '20', 'nation': 'uzbek'}
person2 = dict(name='umar', age=33, nation='korean')


name = person['name']
print(person)
print(person2)
print(name)
print('=============')

hobby = person.get('hobby', 'scrolling')
balance = person.get('balance', 20)

age = person2.get('age')

print(hobby, balance, age)

print('==============')

del person['nation']

for value in person:
    print(value , person[value])
