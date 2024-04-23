targets = [[4,5],[4,8],[10,14],[11,13],[5,12],[3,7],[1,4]]
result = 3
answer = 0

targets.sort(key = lambda x: [x[1], x[0]])
s = e = 0
for target in targets:
    
    if target[0] >= e:
        print(f"target: {target}")
        answer += 1
        e = target[1]
        print(f"e: {e}")

print("answer: ",answer)