import cv2 as cv
import numpy as np

#Carregar a imagem
img = cv.imread('Desafios/balao.jpg')
#Converter a imagem para o espaço de cores HSV
imagem_hsv = cv.cvtColor(img, cv.COLOR_BGR2HSV)

#Verde
#Define os limites
limite_inferior = np.array([90, 90, 10])
limite_superior = np.array([135, 255, 255])
#Criar uma máscara com os limites de cor verde
mascara = cv.inRange(imagem_hsv, limite_inferior, limite_superior)
#Encontrar os contornos na máscara
contours, hierarchy = cv.findContours(mascara, cv.RETR_EXTERNAL, cv.CHAIN_APPROX_SIMPLE)

altura, largura, canais = img.shape

# Crie uma nova imagem preta com as mesmas dimensões
imagem_preta = np.zeros([altura, largura, canais])

#Desenhar os contornos na img original
cv.drawContours(imagem_preta, contours, -1, (255,255,255), thickness=cv.FILLED)

#Exibe a imagem final com contorno
cv.imshow('balao_contornos', imagem_preta)
cv.waitKey(0)
cv.destroyAllWindows()