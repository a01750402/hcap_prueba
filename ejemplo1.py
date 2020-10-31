import numpy as np
import cv2
imagen = cv2.imread('imagen.jpg')
imagen = cv2.cvtColor(imagen, cv2.COLOR_BGR2RGB)
print("ojo",imagen.shape)
print("aquí",imagen[0][1][0]+10)
print(imagen)
imagen = cv2.resize(imagen,(256,256))

cv2.imwrite('reziseimage.jpg',imagen)

imagen = cv2.imread('imagen.jpg')
imagen = cv2.cvtColor(imagen,cv2.COLOR_BGR2GRAY)
print(imagen.shape)
print(imagen[0][0])
print("ojo aquí",imagen[0][1])

imagen[0][0] = 0 
imagen [0][1] = 0
imagen[0][2] = 0


cv2.imwrite('grayimagen.jpg',imagen)

matriz = np.zeros((256,256),np.float32)
print(matriz.shape)
cv2.imwrite('matrizimagen.jpg',matriz)
imagen = cv2.cvtColor(matriz,cv2.COLOR_GRAY2BGR)
print(imagen.shape)
cv2.imwrite('matrizcolorimagen.jpg',imagen)
#cv2.imshow('image',imagen)
#cv2.waitKey(0)

