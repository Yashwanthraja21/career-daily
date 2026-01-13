row = int(input("Enter the number of rows: "))
col = int(input("Enter the number of columns: "))
matrix1, matrix2, result = [], [], []

for i in range(row):
    values = list(map(int, input().split()))
    matrix1.append(values)

for i in range(row):
    values = list(map(int, input().split()))
    matrix2.append(values)

for i in range(row):
    temp = []
    for j in range(col):
        temp.append(matrix1[i][j] + matrix2[i][j])
    result.append(temp)
print(result)