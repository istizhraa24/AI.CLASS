# PROGRAM DENGAN LIBRARY NUMPY

import numpy as np

A = np.array([[3, 0], [-1, 2], [1, 1]])
B = np.array([[4, -1], [0, 2]])
C = np.array([[1, 4, 2], [3, 1, 5]])
D = np.array([[1, 5, 2], [-1, 0, 1], [3, 2, 4]])
E = np.array([[6, 1, 3], [-1, 1, 2], [4, 1, 3]])

A_kali_C = np.dot(A, C)
A_kali_B = np.dot(A, B)
D_tambah_E = D + E
D_kurang_E = D - E

# percobaan yang akan menghasilkan error
try:
    A_kali_D = np.dot(A, D)
    print("Hasil dari A x D : ")
    print(A_kali_D)
except ValueError as e:
    print("Error pada A x D:", e)

print("Hasil dari A x C : ")
print(A_kali_C)
print("Hasil dari A x B : ")
print(A_kali_B)
print("Hasil dari D + E : ")
print(D_tambah_E)
print("Hasil dari D - E : ")
print(D_kurang_E)

# PROGRAM TIDAK PAKAI LIBRARY NUMPY

A = [[3, 0], [-1, 2], [1, 1]]
B = [[4, -1], [0, 2]]
C = [[1, 4, 2], [3, 1, 5]]
D = [[1, 5, 2], [-1, 0, 1], [3, 2, 4]]
E = [[6, 1, 3], [-1, 1, 2], [4, 1, 3]]

def multiply(X, Y):
    if len(X[0]) != len(Y):  
        raise ValueError("Ukuran matriks tidak sesuai untuk perkalian.")
    return [[sum(X[i][k] * Y[k][j] for k in range(len(Y))) for j in range(len(Y[0]))] for i in range(len(X))]

def add(X, Y):
    return [[X[i][j] + Y[i][j] for j in range(len(X[0]))] for i in range(len(X))]

def subtract(X, Y):
    return [[X[i][j] - Y[i][j] for j in range(len(X[0]))] for i in range(len(X))]

A_kali_C = multiply(A, C)
A_kali_B = multiply(A, B)
D_tambah_E = add(D, E)
D_kurang_E = subtract(D, E)

# operasi A x D yang akan menghasilkan error
try:
    A_kali_D = multiply(A, D)
    print("Hasil dari A x D : ", A_kali_D)
except ValueError as e:
    print("Error pada A x D:", e)

print("Hasil dari A x C : ", A_kali_C)
print("Hasil dari A x B : ", A_kali_B)
print("Hasil dari D + E : ", D_tambah_E)
print("Hasil dari D - E : ", D_kurang_E)