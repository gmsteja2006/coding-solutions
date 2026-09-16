# cook your dish here
# Bus Seating Problem

T = int(input())  # number of test cases

for _ in range(T):
    N, K = map(int, input().split())
    # People sitting next to someone = extra beyond N
    result = max(0, K - N)
    print(result)
