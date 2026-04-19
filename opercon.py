#  operators :   > < >= <= == != , is,    + - *  / // % **
# conditions if else elif 
# logical operators : and or not

a=140 
b= 45 
print(a>b)

print(a<b)

c= a**2

print(c)

print(a+b)
print(c-a)

f= '#'

print(f*10)

e= dict(name='omar', age = 21)
t= dict(name='umar', age =21)
y=e                            # only values not keys
print(e==t)

print(e is t)
print(e is y)

print(id(e))
print(id(t))
print(id(y))


x= 10 

if x<63:
    print('case c ')
elif x<84:
    print('case b')
else:
    print('case a')


a= 40 
person = None
if a>50:
    person = 'Omar'
else:    
    person = 'Umar'

print(person)


age = 20 

person = 'adult' if age>18 else 'child'
print(person)


is_student = False
is_guest = False 
is_admin = False
is_guest = False

if is_student:
    print('Student room')

elif is_student and is_admin:
    print('go to admin room')
elif  is_student or is_admin:
    print('go to student room')
elif is_guest:
    print('go to guest room')
else:
    print('go to home')