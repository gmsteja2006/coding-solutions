# Bus Seating Problem

T = int(input())  # number of test cases

for _ in range(T):
    N, K = map(int, input().split())
    if K <= N:
        print(0)
    else:
        print(2 * (K - N))
