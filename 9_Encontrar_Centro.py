import cv2 as cv

img = cv.imread('Desafios/bola.webp')
blur = cv.GaussianBlur(img, (5, 5), 0)
cinza = cv.cvtColor(blur, cv.COLOR_BGR2GRAY)
ret, thresh = cv.threshold(cinza, 240, 255, cv.THRESH_BINARY)

#Evita que a figura externa seja incluida
thresh = cv.bitwise_not(thresh)

contours, hierarchy = cv.findContours(thresh, cv.RETR_EXTERNAL, cv.CHAIN_APPROX_SIMPLE)

for contour in contours:
    moments = cv.moments(contour)
    cx = int(moments["m10"]/moments["m00"])
    cy = int(moments["m01"]/moments["m00"])
    cv.circle(img, (cx, cy), 0, 0, 10)

cv.imshow('bola', img)
cv.waitKey(0)
cv.destroyAllWindows()