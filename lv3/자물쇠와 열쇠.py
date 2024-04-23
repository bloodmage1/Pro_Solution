key = [[0, 0, 0], [1, 0, 0], [0, 1, 1]]
lock = [[1, 1, 1], [1, 1, 0], [1, 0, 1]]

rotation1 = [[] for i in range(len(key))]
rotation2 = [[] for i in range(len(key))]
rotation3 = [[] for i in range(len(key))]

k = len(key)
l = len(lock)
li = len(lock[0])

for i in range(len(key)):
    for j in range(len(key[i])):
        rotation1[i].append(key[j][k-i-1])
for i in range(len(key)):
    for j in range(len(key[i])):
        rotation2[i].append(rotation1[j][k-i-1])
for i in range(len(key)):
    for j in range(len(key[i])):
        rotation3[i].append(rotation2[j][k-i-1])

rotations = [key, rotation1, rotation2, rotation3]

new_lock = [[] for i in range(l+2*k-2)]

for i in range(len(new_lock)):
    for j in range(l+2*k-2):
        new_lock[i].append(0)

for i in range(k-1, k-1+l):
    for j in range(k-1, k-1+li): 
        new_lock[i][j] = lock[i-(k-1)][j-(k-1)]

def check(new_lock):
    answer = 0
    for i in range(k-1, k-1+l):
        for j in range(k-1, k-1+li): 
            if new_lock[i][j] ==1:
                answer += 1
    if answer == l*li:
        return True
    else:
        return False

for p in range(l+k-1):
    for q in range(l+k-1):
        for d in rotations:
            r_key = d
            for i in range(k):
                for j in range(k):
                    new_lock[p+i][q+j] += r_key[i][j]
            if check(new_lock):
                print(True)

            for i in range(len(key)):
                for j in range(len(key[i])):
                    new_lock[p+i][q+j] -= r_key[i][j]

print(False)

