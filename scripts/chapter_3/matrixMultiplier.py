# script to multiply basic matrix

a = [[0, 64, 128], [48, 192, 144], [142, 226, 168]]
b = [[-1, 0, -2], [0.5, 4.5, -1.5], [1.5, 2, -3]]

def matrixMultiplier(matrix1, matrix2):
    result = 0
    for arr1 in matrix1:
        for num1 in arr1:
            numIndex = arr1.index(num1)
            result += num1 * matrix2[matrix1.index(arr1)][numIndex]
    return result

result = print(matrixMultiplier(a, b))
