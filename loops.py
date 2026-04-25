'''
loops ... 
'''

a = 'mit'
num = (1,2,3,6,5,4)
obj = dict(name='umar', year=2000)

for i in a:
    print(i)

for i in num:
    print(i)

for key in obj:
    print(key , obj.get(key))


for i in range(0, 20,2):
    print(i)


for i in range(0,30,4):
    if i > 22:
        print('you reached highest')
        break
else:


    print('try again')


count = 0

while True:
    count+=1
    a = int(input('Find number : '))
     
    if a ==41:
        print(f"You find number in {count} steps")
        break
    else:
        print('Try again')