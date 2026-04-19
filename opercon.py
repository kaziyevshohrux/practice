#  operators :   > < >= <= == != , is,    + - *  / // % **


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