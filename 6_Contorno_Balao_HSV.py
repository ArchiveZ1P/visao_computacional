import cv2 as cv
import numpy as np

#Carregar a imagem
img = cv.imread('Desafios/balao.jpg')
#Converter a imagem para o espaço de cores HSV
imagem_hsv = cv.cvtColor(img, cv.COLOR_BGR2HSV)

#Verde
#Define os limites
limite_inferior = np.array([60, 150, 0])
limite_superior = np.array([75, 255, 255])
#Criar uma máscara com os limites de cor verde
mascara = cv.inRange(imagem_hsv, limite_inferior, limite_superior)
#Encontrar os contornos na máscara
contours, hierarchy = cv.findContours(mascara, cv.RETR_EXTERNAL, cv.CHAIN_APPROX_SIMPLE)
#Desenhar os contornos na img original
cv.drawContours(img, contours, -1, (0,0,0), 1)

#Azul
limite_inferior1 = np.array([80, 150, 0])
limite_superior1 = np.array([150, 255, 255])
mascara1 = cv.inRange(imagem_hsv, limite_inferior1, limite_superior1)
contours1, hierarchy1 = cv.findContours(mascara1, cv.RETR_EXTERNAL, cv.CHAIN_APPROX_SIMPLE)
cv.drawContours(img, contours1, -1, (0,0,0), 1)

#Vermelho
limite_inferior2 = np.array([0, 80, 0])
limite_superior2 = np.array([50, 255, 255])
mascara2 = cv.inRange(imagem_hsv, limite_inferior2, limite_superior2)
contours2, hierarchy1 = cv.findContours(mascara2, cv.RETR_EXTERNAL, cv.CHAIN_APPROX_SIMPLE)
cv.drawContours(img, contours2, -1, (0,0,0), 1)

#Rosa
limite_inferior3 = np.array([155, 80, 0])
limite_superior3 = np.array([165, 255, 255])
mascara3 = cv.inRange(imagem_hsv, limite_inferior3, limite_superior3)
contours3, hierarchy1 = cv.findContours(mascara3, cv.RETR_EXTERNAL, cv.CHAIN_APPROX_SIMPLE)
cv.drawContours(img, contours3, -1, (0,0,0), 1)

#Exibe a imagem final com contorno
cv.imshow('balao_contornos', img)
cv.waitKey(0)
cv.destroyAllWindows()