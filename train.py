# K-TASK (PYTHON)

# Shunday function yozing, u string qabul qilsin va string ichidagi eng uzun sozni qaytarsin.
# MASALAN: find_longest("I come from Uzbekistan") return "Uzbekistan
import math 
def find_longest(gap):
    a=gap.split()
    last=[]
    for i in a:
        last.append(len(i))
    s = max(last)
    d=last.index(s)
    print(a[d])

find_longest("I comeeeeeeeeeeeee from Uzbekistanuzbekistan salom")








# I-TASK (PYTHON)

# Shunday function tuzing, unga string argument pass bolsin. Function ushbu agrumentdagi digitlarni yangi stringda return qilsin
# MASALAN: get_digits("m14i1t") return qiladi "141"
# nums = [1,2,3,4,5,6,7,8,9,0]
# def get_digits(blabla):
#     res=[]
#     for i in blabla:
#         if i.isdigit():
#             res.append(i)
#     return "".join(res)
# print(get_digits('141bla141'))



# G-TASK (PYTHON)

# Shunday function tuzingki unga integerlardan iborat array pass bolsin va function bizga osha arrayning eng katta qiymatiga tegishli birinchi indexni qaytarsin.
# MASALAN: get_highest_index([5, 21, 12, 21, 8]) return qiladi 1 sonini.
# import math
# def get_h(arr):
#     a = max(arr)
#     print(arr.index(a))
    

# get_h([5,12,21,8])