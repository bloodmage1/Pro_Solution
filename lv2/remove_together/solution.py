# s = "baabaa"

# a = 1

# stack = []

# def solution(s):
#     stack = []
#     for i in range(len(s)):
#         if not stack:
#             stack.append(s[i])
#             # print(stack)# stack이 비어있다면 push()
#         else:
#             if s[i] == stack[-1]:       # stack 마지막 값과 s[i]가 같다면 pop()
#                 stack.pop()
                
#             else:
#                 stack.append(s[i])      # stack 마지막 값과 s[i]가 다르면 push()
#                 print(stack)
#     if stack : return 0                 # stack이 비어있지 않다면 return 0
#     else : return 1      
    
# print(solution(s))

df = {}
import pandas as pd
import numpy as np

df['normal'] = range(1,101)
df["disease"] = range(1,101)

df = pd.DataFrame(df, index=np.arange(100))

# print(df)

print(100%33)





