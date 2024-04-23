## case1 ##

name = ["may", "kein", "kain", "radi"]
yearning = [5, 10, 1, 3]
photo = [["may", "kein", "kain", "radi"],["may", "kein", "brin", "deny"], ["kon", "kain", "may", "coni"]]

points = {name[i]: yearning[i] for i in range(len(name))}
print(points)
answer = []
for i in range(len(photo)):
    point = 0
    for j in range(len(photo[i])):
        if photo[i][j] in points:
            point += points[photo[i][j]]
    answer.append(point)
    
print(answer)


result = [19, 15, 6]

## case 2 ##

name = ["kali", "mari", "don"]
yearning = [11, 1, 55]
photo = [["kali", "mari", "don"], ["pony", "tom", "teddy"], ["con", "mona", "don"]]



result = [67, 0, 55]

## case 3 ##

name = ["kali", "mari", "don"]
yearning = [11, 1, 55]
photo = [["kali", "mari", "don"], ["pony", "tom", "teddy"], ["con", "mona", "don"]]



result = [67, 0, 55]
