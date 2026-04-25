# objects -> maxsus proprtyga ega bolgan data type
# import array
# import math

# from math import ceil, asin
# print('============')

# print(type('hello world'))
# print(type(123))
# print(type(3.14))
# print(type(True))
# print(type(math))
# print(type(array))

# print(ceil(98.1))

# print('=====handling system')

car_dict = dict(name='tayota', year=2025, electric=True)

# speed = car_dict['speed']

# try:
#     print('first step otyabdi topilsa ishledi')
#     result = car_dict['speed']
#     print(result)
# except KeyError as err:
#     print('speed tpilmadi', err)
# else:
#     print('speed topilsa else ishledi')
# finally:
#     print('nima bosaham finally ishledi')


try:
    print('first step otyabdi topilsa ishledi')
    a = car_dict.speed
    result = car_dict['yea']
    print(result)
except Exception as err:
    print('Error:', err)
else:
    print('speed topilsa else ishledi')
finally:
    print('nima bosaham finally ishledi')
