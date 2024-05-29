import cv2 as cv
img = cv.imread('Desafios/animal.jpg')
##Deixando a imagem cinza
cinza = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
##Exibindo a imagem cinza
cv.imshow('cinza', cinza)
cv.waitKey(0)
cv.destroyAllWindows()