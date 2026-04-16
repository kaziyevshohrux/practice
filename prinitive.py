print('======================')
# java : malumot manzili nomlanishi
# python : referns nomlanishi

count = 100
count_type = type(count)
print("the type of count: ", count_type, "value of count: ", count)

result1 = count.bit_count()
result2 = count.denominator
print(result1, result2)

print('=====str==========')

course = 'AI, python, java'
resultt = type(course)
print(f"result(1): {resultt}")

resultt = course.upper()
print(f"result(2): {resultt}")

resultt = course.title()
print(f"result(3): {resultt}")


resultt = course.replace('AI', 'ENGENEER')
print(f"result(4): {resultt}")


print('====boolean=====')

# functions   str , int , input , bool ()

a = input('give value : ')
print('a:',a)

res = a.isnumeric()
print('a:',res)


# truthy and falthy 

# truth  > true , 100 , -100 , 'dsff'
# falsy  > false  , 0  , '' , none 

test_falsy = '' or False or None or 10
print(bool(test_falsy))

test_truth= 'dasas' or 100  or -10
print(bool(test_truth))


print('===========scopes===========')
b=100
def calculate(a):
    c= a*b
    return c
result = calculate(10)
print(result)