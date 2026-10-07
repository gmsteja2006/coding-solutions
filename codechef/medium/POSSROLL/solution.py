# cook your dish here
# Read input values
X, K, Y = map(int, input().split())

# Check if Y is a valid face of the die
if Y % K == 0 and 1 <= Y // K <= X:
    print("YES")
else:
    print("NO")
