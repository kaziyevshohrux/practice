# I-TASK (PYTHON)

# Shunday function tuzing, unga string argument pass bolsin. Function ushbu agrumentdagi digitlarni yangi stringda return qilsin
# MASALAN: get_digits("m14i1t") return qiladi "141"
nums = [1,2,3,4,5,6,7,8,9,0]
def get_digits(blabla):
    res=[]
    for i in blabla:
        if i.isdigit():
            res.append(i)
    return "".join(res)
print(get_digits('141bla141'))



# G-TASK (PYTHON)

# Shunday function tuzingki unga integerlardan iborat array pass bolsin va function bizga osha arrayning eng katta qiymatiga tegishli birinchi indexni qaytarsin.
# MASALAN: get_highest_index([5, 21, 12, 21, 8]) return qiladi 1 sonini.
# import math
# def get_h(arr):
#     a = max(arr)
#     print(arr.index(a))
    

# get_h([5,12,21,8])