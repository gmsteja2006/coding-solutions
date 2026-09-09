# cook your dish here
T = int(input())

for _ in range(T):
    N = int(input())
    A = input()
    B = input()

    if A.count('a') + B.count('a') == N:
        print("Yes")
    else:
        print("No")