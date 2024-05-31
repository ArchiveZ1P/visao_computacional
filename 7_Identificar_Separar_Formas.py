import cv2 as cv

img = cv.imread("Desafios/geometricas.webp")
imgGauss = cv.GaussianBlur(img, (5,5), 0)
cinza = cv.cvtColor(imgGauss, cv.COLOR_BGR2GRAY)
ret, thresh1 = cv.threshold(cinza, 195,255, cv.THRESH_BINARY)
#Evita que a figura externa seja incluida
thresh1 = cv.bitwise_not(thresh1)
contours1, hierarchy1 = cv.findContours(thresh1, cv.RETR_TREE, cv.CHAIN_APPROX_SIMPLE)

mais_de_quatro_faces = []
quatro_faces_ou_menos = []

for contorno in contours1:
    #Contorno
    epsilon = 0.04*cv.arcLength(contorno, True)
    vertices = cv.approxPolyDP(contorno, epsilon, True)

    #Vertices
    num_vertices = len(vertices)
    if num_vertices > 4:
        mais_de_quatro_faces.append(contorno)
    else:
        quatro_faces_ou_menos.append(contorno)

#Desenha contorno e exibe
img1 = img.copy()
cv.imshow('Mais de 4 faces', cv.drawContours(img, mais_de_quatro_faces, -1,(0,0,0), 2))
cv.imshow('4 faces ou menos', cv.drawContours(img1, quatro_faces_ou_menos, -1,(0,0,0), 2))
cv.waitKey(0)
cv.destroyAllWindows()
