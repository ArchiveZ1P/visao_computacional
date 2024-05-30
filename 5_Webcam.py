import cv2 as cv
##Abre webcam
cam = cv.VideoCapture(0)
while (True):
    ret, frame = cam.read()
    ##Desenha o retangulo
    cv.rectangle(frame,(250,200),(400,300),0,3)
    cv.imshow('webcam', frame)
    if cv.waitKey(1) & 0xFF == ord('q'): break
cam.release()
cv.destroyAllWindows()