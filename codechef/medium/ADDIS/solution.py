# cook your dish here
from collections import Counter

T = int(input())

for _ in range(T):
    N = int(input())
    A = list(map(int, input().split()))

    freq = Counter(A)
    max_freq = max(freq.values())

    answer = (max_freq + 1) // 2

    print(answer)