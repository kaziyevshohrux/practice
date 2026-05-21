











# O-TASK (PYTHON)

# Shunday function yozing, u har xil valuelardan iborat array qabul qilsin va List ichidagi sonlar yigindisini hisoblab chiqqan javobni qaytarsin.
# MASALAN: calculate_summary([10, "10", {son: 10}, true, 35]) return 45

# def calculate_summary(arr):
#     last = []
#     for i in arr:
#         if type(i) == int:
#             last.append(i)

#     print(sum(last))  




# calculate_summary([10, "10",45, {'son': 10}, True, 35])









# M-TASK (PYTHON)

# Shunday function yozing, u string qabul qilsin va string palindrom yani togri oqilganda ham, orqasidan oqilganda ham bir hil oqiladigan soz ekanligini aniqlab boolean qiymat qaytarsin.
# MASALAN: palindrom_check("dad") return True;  palindrom_check("son") return False;


# def palindrom(gap):
#     for i in gap[-1::-1]:
#         break
#     for j in gap:
#         break

#     if i==j:
#         print(True)
#     else:
#         print(False)
# palindrom('adada')














# # K-TASK (PYTHON)

# # Shunday function yozing, u string qabul qilsin va string ichidagi eng uzun sozni qaytarsin.
# # MASALAN: find_longest("I come from Uzbekistan") return "Uzbekistan
# import math 
# def find_longest(gap):
#     a=gap.split()
#     last=[]
#     for i in a:
#         last.append(len(i))
#     s = max(last)
#     d=last.index(s)
#     print(a[d])

# find_longest("I comeeeeeeeeeeeee from Uzbekistanuzbekistan salom")








# I-TASK (PYTHON)

# Shunday function tuzing, unga string argument pass bolsin. Function ushbu agrumentdagi digitlarni yangi stringda return qilsin
# MASALAN: get_digits("m14i1t") return qiladi "141"
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