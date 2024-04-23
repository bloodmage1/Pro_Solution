begin = "hit"
target = "cog"

words = ["hot", "dot", "dog", "lot", "log", "cog"]

def check(begin, target, word):
    for j in range(len(begin)):
        if begin[j] != word[j] and begin != target:
            if word[j] == target[j]:
                return True 
    return False

def comp(begin, target):
    wrong = 0
    for i in range(len(begin)):
        if begin[i] != target[i]:
            wrong += 1
    if wrong == 1:
        return True
    else:
        return False

answer = 0
while True:
    wrong = 0

    for i in words:
        if check(begin, target, i):
            begin = i
            answer += 1
        else:
            continue
    if comp(begin, target):
        answer += 1
        break

    print(answer)


