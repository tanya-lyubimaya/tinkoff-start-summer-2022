n = int(input())
cnt=0
while n%10 == 0:
    n /= 10
    cnt += 1
print(cnt)