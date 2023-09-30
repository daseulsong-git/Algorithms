# https://www.acmicpc.net/problem/25304

tot = int(input())
tot2 = 0
cnt = int(input())
lst = []

for i in range(0, cnt):
    lst.append(list(map(int, input().split())))

for j in lst :
    tot2 += j[0]*j[1]

if tot2 == tot :
    print("Yes")
else :
    print("No")