n= 6
times = [7,10]

answer = 0

left = 1

right = max(times) * n

while right > left:

    mid = (right + left)//2
    total = 0

    for t in times:
        plus = mid // t
        total += plus
    
    if total >= n:
        right = mid

    else:
        left = mid + 1

answer = left
print(answer)