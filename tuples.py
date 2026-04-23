'''
1)tuples

'''

num = [1,2,3,4,5,6]
l = ['helllllllloouuuuuuuu']
obj_c = dict(name='umar', year=2000)

print(num)
print(l)
print(obj_c)

fruits= ['banan', 'olma', 'nok']
fruits[2]= 'behi'
fruits.append('nok')
print(fruits)

print('=======tuple=======')

fruits = ('papaya', 'mango', 'kakos')
print(fruits)

#fruits[0]='00'
#fruits.append('465') 

print(fruits)


print('====unpacking')


name = ['umar', 'ali', 'ali']
(x,y,z) = name
print(y)

num = (1,2,3,5,5,4,5)
(x,y,*args)= num
print(args)


def num(*args):
    total = 1
    for i in args:
        total*=i
    print(f"total -> {total}")
 
num(1,2,5)
num(-10,5,1)