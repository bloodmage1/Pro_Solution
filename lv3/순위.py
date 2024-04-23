n= 5

results = [[4, 3], [4, 2], [3, 2], [1, 2], [2, 5]]

check = [[] for i in range(len(results))]

for i in range(len(check)):
    for j in range(n):
        check[i].append(0)

for i in range(len(results)):
    check[results[i][0]-1][results[i][1]-1] = 1
    check[results[i][1]-1][results[i][0]-1] = -1

# i 를 진 애들은 i 한테 이긴애들한테도 진 것
# i 에게 이긴 애들은 i 한테 진 애들한테 이긴 것.

print(check)