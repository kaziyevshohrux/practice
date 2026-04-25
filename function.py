'''
1) define , call 
2) parametr , argument 
3) keyword , default 
4) scope

'''

# function ; block of code that performs a specific task

# java {}   , python : indentaion

# define





def greet(name):
    # pass  # for empty function
    print(f"Hello, {name}!")
def greeting(b):
    print('greeting is executed')
    return f"Hio, {b}!"

# call
result = greet('OMAR')

print(result)

result2 = greeting('shokhrux')
print(result2)


# parametr   , argument

# parametr = define qilganda beriladigan nom
# argument = call qilganda beriladigan qiymat


print('======================')


def give_gret(name, age=22):
    print('give_gret is executed')
    return f"Hello, {name}! i am {age} years old."

result3 = give_gret(name='Omar')
print(result3)

#keyword = call qilganda parametr nomi bilan beriladigan argument
# default = parametrga default qiymat berish