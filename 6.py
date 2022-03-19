from sched import scheduler


n, h, m, k = map(int, input().split(" "))
schedule = []
for i in range(n):
    schedule.append(input())

print(n, h, m, k)
print(schedule)

day_in_minutes = h*m
for i in range(1, h+1):
