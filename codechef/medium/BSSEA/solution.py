# cook your dish here
n = int(input())
a = list(map(int, input().split()))

small = min(a)
large = max(a)

center = (small + large) / 2

answer = min(a, key=lambda x: (abs(x - center), x))

print(answer)