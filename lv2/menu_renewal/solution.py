orders1 = ["ABCFG", "AC", "CDE", "ACDE", "BCFG", "ACDEH"]
course1 = [2,3,4]

orders2 = ["ABCDE", "AB", "CD", "ADE", "XYZ", "XYZ", "ACD"]
course2 = [2,3,5]

orders3 = ["XYZ", "XWY", "WXA"]
course3 = [2,3,4]


from collections import Counter
from itertools import combinations
from math import comb


answer = []

for i in course1:
    array = []
    for j in orders1:
        order = sorted(j)
        array.extend(list(combinations(order,i)))
        
    ton = Counter(array)
    
    if max(count.)

    # for key, value in ton.items():
    #     if value >= 2:
            

print(ton)

# str_answer = ""

# for i in orders1:
#     str_answer += i
    
# a = Counter(str_answer)

# result = []

# for i in course1:
#     result1 = ""
#     for k,v in a.items():
#         if v >= i:
#             result1 += k
    
#     result.append(result1)

# print(result)
