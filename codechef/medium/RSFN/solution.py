# cook your dish here
MOD = 10**9 + 7

# Step 1: Precompute Fibonacci up to 100000
MAX_I = 100000
fib = [0] * (MAX_I + 2)
fib[1] = 1
for i in range(2, MAX_I + 1):
    fib[i] = (fib[i-1] + fib[i-2]) % MOD

# Step 2: Read input
N, Q = map(int, input().split())
I = list(map(int, input().split()))

# Step 3: Build fib_values array
fib_values = [fib[x] for x in I]

# Step 4: Build prefix sum
prefix = [0] * (N + 1)
for i in range(N):
    prefix[i+1] = (prefix[i] + fib_values[i]) % MOD

# Step 5: Answer queries
for _ in range(Q):
    L, R = map(int, input().split())
    ans = (prefix[R] - prefix[L-1]) % MOD
    print(ans)
