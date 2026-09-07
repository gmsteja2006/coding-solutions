# cook your dish here
# Read input values
A, B, X = map(int, input().split())

# Calculate combined score
total = A + B

# Check if Astra passes
if total >= X:
    print("YES")
else:
    print("NO")
