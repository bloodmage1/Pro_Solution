orders = ["ABCFG", "AC", "CDE", "ACDE", "BCFG", "ACDEH"]
course = [2,3,4]
# result = ["AC", "ACDE", "BCFG", "CDE"]

import string

list_upper = list(string.ascii_uppercase)
list_number = [0 for i in range(len(list_upper))]

dic = {}

for i in orders:
    for j in i:
        for k in range(len(list_upper)):
            if j == list_upper[k]:
                list_number[k] += 1
                
for i in range(len(list_upper)):
    dic[list_upper[i]] = list_number[i]
    
for k,v in dic.items():
    print(k,v)


# orders = ["ABCDE", "AB", "CD", "ADE", "XYZ", "XYZ", "ACD"]
# course = [2,3,5]
# result = ["ACD", "AD", "ADE", "CD", "XYZ"]

# orders = ["XYZ", "XWY", "WXA"]
# course = [2,3,4]	
# result = ["WX", "XY"]



