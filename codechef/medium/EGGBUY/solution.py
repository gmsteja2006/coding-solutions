# cook your dish here
X, Y, F = map(int, input().split())

cost1 = 12 * X
cost2 = 12 * Y + F

print(min(cost1, cost2))