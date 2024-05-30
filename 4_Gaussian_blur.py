import cv2 as cv
img = cv.imread("Desafios/animal.jpg")
imgGauss = cv.GaussianBlur(img, (5,5), 10)
cv.imshow("Original", img)
cv.imshow("Desfocada", imgGauss)
cv.waitKey(0)
cv.destroyAllWindows