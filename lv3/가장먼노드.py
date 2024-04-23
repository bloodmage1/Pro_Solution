vertex = [[3, 6], [4, 3], [3, 2], [1, 3], [1, 2], [2, 4], [5, 2]]
n = 6


answer = 0

# x= [[] for n in range(n+1)]

# for i in range(len(vertex)):
#     x[vertex[i][0]].append(vertex[i][1])
#     x[vertex[i][1]].append(vertex[i][0])

# from collections import deque

# cnt = 0
# visited = [-1 for i in range(n+1)]

# q = deque([[1, cnt]])

# while q:
#     value = q.popleft()
#     v = value[0]
#     cnt = value[1]

#     if visited[v] == -1:
#         visited[v] = cnt
#         cnt += 1
#         for i in x[v]:
#             q.append([i, cnt])

# print(visited.count(max(visited)))





























vertex = [[3, 6], [4, 3], [3, 2], [1, 3], [1, 2], [2, 4], [5, 2]]
n = 6


answer = 0

x = [[] for i in range(n+1)]

for i in range(len(vertex)):
    x[vertex[i][0]].append(vertex[i][1])
    x[vertex[i][1]].append(vertex[i][0])

from collections import deque

visited = [-1 for i in range(n+1)]

cnt = 0

q = deque([[1, cnt]])

while q:

    value = q.popleft()
    v = value[0]
    cnt = value[1]

    
    if visited[v] == -1:
        visited[v] = cnt

        cnt += 1
        for i in x[v]:
            q.append([i,cnt])

print(visited)

