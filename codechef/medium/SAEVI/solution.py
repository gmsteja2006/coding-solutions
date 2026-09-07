# cook your dish here
# Read input values
N, K = map(int, input().split())
A = list(map(int, input().split()))

# Threshold value
threshold = 2 * K

# Sum elements at even indices greater than threshold
result = sum(A[i] for i in range(0, N, 2) if A[i] > threshold)

# Print result
print(result)
