# a= 'hello , world'
# c= 10000
# b= '500'
# print(len(a))
# print(a)
# print(a[0])
# print(a[-1])
# print(a[0:5])
# print(a[7:12])
# print(str(b))
# print(list(a) , list(b) )

# print((1+2j) * (2+3j))

# print('p' in 'anaaaaa')
# j=0

# for i in range(1,6):
#     print(i**0,i, i**2, i**3)


# Enter number of years you have lived: 100
# You have lived for 3153600000 seconds.

# num = int(input('enter number of years:'))
# seconds = num * 365 * 24 * 60 * 60
# print(f'You have lived for {seconds} seconds.')

#abs = 'nizomidingulomjonov0'
# print(abs[:-5])
# print(abs[::-1])
# print(abs[1::3])

# countr = '   Coding For All      '

# challenge = 'salom dunto molas'
# print(countr.strip(' '))

# result = '+'.join(countr)
# print(result)
# print(countr.upper())
# print(countr.count('a', 2,15))

# print(countr.endswith(' a 30'))

# print(countr.rfind('y'))

# print(countr.isalnum())
# print(abs.isalnum())

# print(abs.isalpha())


# a= 'Coding', 'For' , 'All'
# b=" ".join(a)
# print(len(b))

# print(b.upper())
# print(b.lower())

# print(b[0:6])

# print(b.replace('Coding', 'Python'))


# list = list()
# list2 = []
# print(type(list))
# companies = ['Google', 'Apple', 'Microsoft', 'Amazon', 'Facebook']
# fruits = ['banana', 'orange','lemon','lime','apple']
# companies.insert(2,'IT company')
# companies.remove('Apple')
# companies[1] = 'BML'
# result = " #; ".join(companies)
# companies.sort(reverse=True)


# print(companies[ 2:7])
# print(result)
# print(companies)
# #print(companies[0:5:2])
# mixed_data = ['umar', 21, 190.5 , True, [324, 'kimhe']]
# print(type(mixed_data))
# print(len(fruits))
# print(fruits[0:6:2])
# firs, secon , thi ,*rest = fruits 
# print(rest)

# a='papaya'

# fruits.append(a)
# print(fruits)

# fruits.insert(2, a)
# print(fruits)

# fruits.remove(a)
# print(fruits)

# front_end = ['HTML', 'CSS', 'JS', 'React', 'Redux']
# back_end = ['Node','Express', 'MongoDB']

# fullstack = front_end + back_end
# print(fullstack)

# ages = [19, 22, 19, 24, 20, 25, 26, 24, 25, 24]

# ages.sort()
# print(ages)
# min = ages[0]
# max = ages[-1]
# print('min age:', min)
# print('max age:', max)
# ages.append(min)
# ages.append(max)
# print(ages)

# total = sum(ages)
# avarge = total / len(ages)
# print('total age:', total)
# print('avarge age:', avarge)

# a= abs(min)
# print(a)

# front_end = ['HTML', 'CSS', 'JS', 'React', 'Redux']

# middle = len(front_end) //2 
# print(front_end[middle])

# con = ['China', 'Russia', 'USA', 'Finland', 'Sweden', 'Norway', 'Denmark']
# fir, sec,th,fou, *res = con
# print(res)


# empty_tuple = tuple()                                          tuple  -> ozgarmaydigon royhat   []
                                                                 # list -> ozgaradigon royhat       ()
# print(type(empty_tuple))

# fruits = ('banana', 'orange', 'mango', 'lemon')

# tple = fruits[1:4:2]
# print(tple)

fruits = {'banana', 'orange', 'mango', 'lemon'}
vegetables = ('tomato', 'potato', 'cabbage','onion', 'carrot')
fruits.update(vegetables)
print(fruits)