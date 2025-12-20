# sum of a matrix
def matrix_sum(matrix):
    total = 0
    r=len(matrix)
    c=len(matrix[0])
    for i in range(r):
        for j in range(c):
            total+=matrix[i][j]
    return total 
print(matrix_sum([[1, 2, 3], [4, 5, 6], [7, 8, 9]]))  # Output: 45