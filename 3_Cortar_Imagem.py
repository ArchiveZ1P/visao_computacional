import cv2 as cv
img = cv.imread('Desafios/bola.webp')
##Exibindo a imagem original
cv.imshow("Original", img)
##Realizando o Recorte
recorte = img[300:400, 200:610] #(y1:y2,x1:x2)
#Exibindo o recorte
cv.imshow("Recorte", recorte)
cv.waitKey(0)
cv.destroyAllWindows