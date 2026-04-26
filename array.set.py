'''
1) Array
2)set
3)set operators
'''

from array import array 
print('========Array=========') 
numbers = array('i' , [1,5,6,5,4,45,6,100])
# f i
num = array('f', [1,6,4.3])

print(numbers)

numbers.append(101)
numbers.insert(0,0)

print(numbers)

numbers.remove(5)
numbers.pop()

print(numbers)

del numbers[2:7:2]
print(numbers)


print('=======set======')


num= array('i', [1,2,3,4,5,67,8,9,9,5,1,2])
# {}
new_num = set(num)
print(new_num)


new_num.add(100)
new_num.add(67)

print(new_num)


print('=========set operators   |   ,   &   ,   -    ,   ^ ')

#   |    union hammasini oberadi set qilin

num1={50,20,30,90,10}
num2={20,10}

result1=num1|num2
print(result1)


#  &    ikkalosida ham borini oberadi 

result2= num1 & num2
print(result2)


# -  birnchsidan iknchsini ayridi bor bosa chiqarib yogini qoldiradi 

result3 = num2 - num1
print(result3)

# ^    ikkalasida borini tashedi yani set boladigonni tashedi 

result4 = num1 ^ num2
print(result4)

print(result1,result2)




numbers = [0,1,2,2,3,3,3,4,4,4,4]



nums = [7, 11, 15,1,5,4,6]
target = 9 

filtered = filter(lambda ele : ele < target , nums)
resul = list(filtered)

for i in resul:
    target-=i
    if()