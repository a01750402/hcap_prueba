import numpy as np


#funcion que calcula la matriz resultante C después de aplicar la operacion de convolucion de A*B
def convolution(A,B):
    C = np.zeros((len(A) - 2, len(A[0]) - 2))
    suma = 0 
    for i in range(len(C)):
        for j in range(len(C[0])):
            for iaux in range(len(B)):
                for jaux in range(len(B[0])):
                    suma += A[i + iaux][j + jaux]*B[iaux][jaux]
            C[i][j] = suma
    
    return C #convolution matrix

Matrix1 = [[6,0,0,3],[8,4,9,1],[4,1,3,12],[3,2,1,100]]
Filtro = [[1,0,2],[5,0,9],[6,2,1]]
A = np.array(Matrix1)
B = np.array(Filtro)
#C = np.zeros((2,2))
convolution(A,B)

#print(Matrix1)
print(A)
print(A[1][0]) 
print(convolution(A,B))
