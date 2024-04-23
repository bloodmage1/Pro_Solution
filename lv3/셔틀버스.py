# n, t, m = 1,1,5
# timetable = ["08:00", "08:01", "08:02", "08:03"]
n, t, m = 2,10,2
timetable = ["09:10", "09:09", "08:00"]
# n, t, m = 2,1,2
# timetable = ["09:00", "09:00", "09:00", "09:00"]
# n, t, m = 1,1,5
# timetable = ["00:01", "00:01", "00:01", "00:01", "00:01"]
# n, t, m = 1,1,1
# timetable = ["23:59"]
# n, t, m = 10,60,45
# timetable = ["23:59","23:59", "23:59", "23:59", "23:59", "23:59", "23:59", "23:59", "23:59", "23:59", "23:59", "23:59", "23:59", "23:59", "23:59", "23:59"]

real_tt = []

for i in range(len(timetable)):
    a,b = timetable[i].split(":")
    real_time = int(a)*60 + int(b)

    real_tt.append(real_time)

real_tt.sort(reverse=True)
start_time = 540

while n > 0 :

    for i in range(m):
        if real_tt[-1] <= start_time:
            a = real_tt.pop()
            if len(real_tt) == 0 :
                answer = start_time
                break

        else:
            break
        
    n -= 1
    start_time += t

if len(real_tt)>=1:
    answer = a


print(answer)












