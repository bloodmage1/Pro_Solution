# lines = [
# "2016-09-15 01:00:04.001 2.0s",
# "2016-09-15 01:00:07.000 2s"
# ]

# lines = [
# "2016-09-15 01:00:04.002 2.0s",
# "2016-09-15 01:00:07.000 2s"
# ]

lines =  [
"2016-09-15 20:59:57.421 0.351s",
"2016-09-15 20:59:58.233 1.181s",
"2016-09-15 20:59:58.299 0.8s",
"2016-09-15 20:59:58.688 1.041s",
"2016-09-15 20:59:59.591 1.412s",
"2016-09-15 21:00:00.464 1.466s",
"2016-09-15 21:00:00.741 1.581s",
"2016-09-15 21:00:00.748 2.31s",
"2016-09-15 21:00:00.966 0.381s",
"2016-09-15 21:00:02.066 2.62s"
]

lines = ["2016-09-15 01:00:04.001 2.0s", "2016-09-15 01:00:07.000 2s"]
all_work = []
for i in range(len(lines)):



    a,b, c = lines[i].split(" ")

    d,e,f = b.split(":")

    hour = int(d) * 3600
    minute = int(e) * 60
    second = float(f)
    end_time = hour + minute + second

    duration_time = float(c.strip("s"))
    start_time = end_time - duration_time + 0.001

    work = []
    work.append(start_time)
    work.append(end_time)
    all_work.append(work)

answer = 0
print(all_work)
for i in range(len(all_work)):
    cnt = 0

    for j in range(i, len(all_work)):
        if all_work[i][1] >= all_work[j][0] - 1:
            cnt += 1
    answer = max(cnt, answer)

print(answer)






