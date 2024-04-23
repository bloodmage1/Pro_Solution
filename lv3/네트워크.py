n = 3
computers = [[1, 1, 0], [1, 1, 0], [0, 0, 1]]

# x = [[] for i in range(n+1)]

# for i in range(len(computers)):
#     for j in range(len(computers[i])):
#         if i == j:
#             continue
#         elif computers[i][j] == 1:
#             x[i+1].append(j+1)

# visited = [False for i in range(n+1)]

# def dfs(x, visited, v):
#     visited[v] = True

#     for i in x[v]:
#         if visited[i] == False:
#             dfs(x, visited, i)

# result = 0

# if i in range(1,n+1):
#     if visited[i] == False:
#         dfs(x, visited, i)
#         result += 1

# print(result)

def dfs(n, computers, com, visited):
    visited[com] = True
    for connect in range(n):
        if connect != com and computers[com][connect] == 1:
            if visited[connect] == False:
                dfs(n, computers, com, visited)

answer = 0
visited = [False for i in range(n)]
n = 3
computers = [[1, 1, 0], [1, 1, 0], [0, 0, 1]]

for com in range(n):
    if visited[com] == False:

        dfs(n, computers, com, visited)
        answer += 1

print(answer)





