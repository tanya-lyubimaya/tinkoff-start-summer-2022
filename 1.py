from math import ceil

a, b, n = int(input()), int(input()), int(input())
if a > ceil(b / n):
    print("Yes")
else:
    print("No")