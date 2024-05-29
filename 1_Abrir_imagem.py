import cv2 as cv
imagem = cv.imread("Desafios/animal.jpg")

cv.imshow('animal', imagem)
while True:
    if cv.waitKey(1) & 0xFF == 27: break ##fecha a imagem com a telca esc
    cv.imshow('animal', imagem)
cv.destroyAllWindows()