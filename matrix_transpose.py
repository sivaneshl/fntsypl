# transpose matrix using list comprehension

matrix = [
[1,2,3],
[4,5,6],
[7,8,9]
]

# conventional method
matrix_transpose = []
for i in range(len(matrix)):
    matrix_transpose_row = []
    for row in matrix:
        matrix_transpose_row.append(row[i])
    matrix_transpose.append(matrix_transpose_row)
print(matrix_transpose)

# using list comprehension for the inner loop
matrix_transpose = []
for i in range(len(matrix)):
    matrix_transpose.append([row[i] for row in matrix])
print(matrix_transpose)

#using list comprehension
matrix_transpose = [[row[i] for row in matrix] for i in range(len(matrix))]
print(matrix_transpose)

# using zip() 
print(list(zip(*matrix)))
