row = int(input("Enter the number of rows: "))
col = int(input("Enter the number of columns: "))
matrix1, matrix2, result = [], [], []

for i in range(row):
    values = list(map(int, input().split())) # Read first matrix
    matrix1.append(values)

for i in range(row):
    values = list(map(int, input().split())) # Read second matrix
    matrix2.append(values) 

for i in range(row):
    temp = [] # Temporary list to store sum of each row
    for j in range(col):
        temp.append(matrix1[i][j] + matrix2[i][j]) # Sum corresponding elements
    result.append(temp) # Append the summed row to result
print(result) 