n = int(input())
x = list(map(int, input().split()))

ans = 10 * 10 ** 6
for i in range(101):
    t = 0
    for j in x:
        t += (j - i) ** 2
    
    ans = min(ans, t)

print(ans)
