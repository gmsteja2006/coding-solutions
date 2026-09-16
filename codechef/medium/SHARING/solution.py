# cook your dish here
# Sharing Cookies Problem

# Read input values
A, B = map(int, input().split())

# Check if total cookies can be divided equally
if (A + B) % 2 != 0:
    print(-1)
else:
    # Each should get half of total
    target = (A + B) // 2
    # Alice needs to give this many cookies to Bob
    print(A - target)
