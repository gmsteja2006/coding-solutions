# cook your dish here
# Read input
N = int(input())
A = list(map(int, input().split()))
M = int(input())

# Remove M least significant bits from each element
result = [a >> M for a in A]

# Print the resulting array
print(*result)
