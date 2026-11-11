# cook your dish here
def solve():
    N, D = map(int, input().split())
    A = list(map(int, input().split()))
    B = list(map(int, input().split()))

    # Scenario 1: Buy all from Shop 1
    cost1 = D + sum(A)

    # Scenario 2: Buy all from Shop 2
    cost2 = D + sum(B)

    # Scenario 3: Buy from both shops
    cost3 = 2 * D
    for i in range(N):
        cost3 += min(A[i], B[i])

    print(min(cost1, cost2, cost3))

T = int(input())
for _ in range(T):
    solve()