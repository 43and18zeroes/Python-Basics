import numpy as np

def fibonacci_matrix(n):
    def matrix_mult(A, B):
        return [[A[0][0] * B[0][0] + A[0][1] * B[1][0],
                 A[0][0] * B[0][1] + A[0][1] * B[1][1]],
                [A[1][0] * B[0][0] + A[1][1] * B[1][0],
                 A[1][0] * B[0][1] + A[1][1] * B[1][1]]]

    def matrix_pow(M, p):
        if p == 1:
            return M
        if p % 2 == 0:
            half_pow = matrix_pow(M, p // 2)
            return matrix_mult(half_pow, half_pow)
        else:
            return matrix_mult(M, matrix_pow(M, p - 1))

    F = [[1, 1], [1, 0]]
    return matrix_pow(F, n)[0][1]

# Example
fibonacci_matrix(10)  # Output: 55 (10th Fibonacci number)


