from asyncio.windows_events import NULL
from pickle import TRUE


str1 = "FRANCE"
str2 = "french"

str1 = "handshake"
str2 = "shake hands"

# str1 = "aa1+aa2"
# str2 = "AAAA12"

# str1 = "E=M*C^2"
# str2 = "e=m*c^2"

count = 0
acount = 0

str1 = str.upper(str1)
str2 = str.upper(str2)

print(str1)
print(str2)

[" ", ]

str1.strip(" ")
str2.strip(" ")

for i in str2:
    if i.isalpha is not TRUE:
        str2.strip(i)
    
for i in str1:
    if i.isalpha is not True:
        str1.strip(i)
    acount += 1
    if i in str2:
        count += 1 
        str2 = str2.strip(i)

print(str1)
print(str2)

answer = (count / (acount + len(str2))) * 65536
answer = round(answer)

print(answer)
    
    


# def solution(str1, str2):
#     answer = 0
#     return answer