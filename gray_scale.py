import cv2
import numpy as np

def grb_2_gray(image):
    gray_im = np.zeros((len(image),len(image[0])))
    
    for i in range(len(image)):
        for j in range(len(image[0])):
            sum = 0
            for iaux in range(3):
                sum += image[i][j][iaux]
        sum = (sum)/3
        gray_im[i][j] = sum
    return gray_im
imagen = cv2.imread('imagen.jpg')
#print(grb_2_gray(imagen))
cv2.imwrite('prueba_grb_2_gray.jpg',grb_2_gray(imagen))



