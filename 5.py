from itertools import permutations

n, k = map(int, input().split(" "))
lst = list(permutations("".join([str(i) for i in range(1, n+1)])))
cnt=0
for i in lst:
    beauty = 0
    for j in range(len(i)):
        beauty += int(i[j])*(j+1)
    if beauty%k == 0:
        cnt+=1
print(cnt)