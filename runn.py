# Dunder __builtins__ , __init__

# a = 100 
# print(a)

# print('hello')

''''
 
in python , is theree= are bultin tools:

1) FUNCTION:  print()  # for printing the output ,  input()  # for taking input from user  len () , type()
2) Type : int , str , list , dict , set , tuple  # for defining the type of data
3) CONSTANT : True , False , Nne  # for defining the constant values
'''

#print(dir(__builtins__))  # for printing the list of built-in functions and types


target = 18
def like(nums):
    for i in nums:
        cur = target - i
        if cur in nums:
            result=(i , cur)
    return tuple(sorted(result))
print(like([3,2,7,15,14]))


# syntax
dct = {'key1':'value1', 'key2':'value2', 'key3':'value3', 'key4':'value4'}
dct['key5'] = 'value5'
print(dct)

# syntax
dct = {'key1':'value1', 'key2':'value2', 'key3':'value3', 'key4':'value4'}
print(dct.items()) # dict_items([('key1', 'value1'), ('key2', 'value2'), ('key3', 'value3'), ('key4', 'value4')])