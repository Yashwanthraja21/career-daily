N = int(input()) # Number of rows
M = int(input()) # Number of columns
matrix, sum_, j = [], 0, 0 # Initialize matrix, sum and column index

for i in range(N):
    value = list(map(int, input().split()))
    matrix.append(value)

for i in range(N):
    if i == j:
        sum_ += matrix[i][j] # Add diagonal element to sum
        j += 1 # Move to next column
print(sum_)