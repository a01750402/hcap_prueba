import numpy as np


#funcion que calcula la matriz resultante C después de aplicar la operacion de convolucion de A*B
def convolution(A,B):
    C = np.zeros((A.shape[0] - 2,A.shape[1] - 2))
    contador = 0
    sum = 0
    for i in range C.shape[0]:
        for j in range C.shape[1]:
            while True: 
                sum += 
    
    return C #convolution matrix

Matrix1 = [[6,0,0,3],[8,4,9,1],[4,1,3,12],[3,2,1,100]]
Filtro = [[1,0,2],[5,0,9],[6,2,1]]
A = np.array(Matrix1)
B = np.array(Filtro)
C = np.zeros((2,2))


#print(Matrix1)
print(A)
print(A[1][0]) 
print(C) 
