#Ainda vou tentar melhorar

import cv2 as cv
import numpy as np

video = cv.VideoCapture("Desafios/arena.mp4")
while video.isOpened():
    ret, frame = video.read()
    frame_hsv = cv.cvtColor(frame, cv.COLOR_BGR2HSV)
    frame_gauss = cv.GaussianBlur(frame_hsv, (5,5), 1000)
    #Cópia do frame para desenhar os contornos
    frame_contours = frame.copy()
    
    #Vermelho excluindo laterais
    limite_inferior = np.array([0, 150, 90])
    limite_superior = np.array([60, 255, 255])
    mascara = cv.inRange(frame_hsv, limite_inferior, limite_superior)
    contours, hierarchy = cv.findContours(mascara, cv.RETR_EXTERNAL, cv.CHAIN_APPROX_SIMPLE)
    cv.drawContours(frame_contours, contours, -1, (144,238,144), thickness=cv.FILLED)
    cv.drawContours(frame_contours, contours, -1, (144,238,144), 20)

    #Outras Cores
    limite_inferior1 = np.array([60, 100, 50])
    limite_superior1 = np.array([180, 255, 255])
    mascara1 = cv.inRange(frame_hsv, limite_inferior1, limite_superior1)
    contours1, hierarchy1 = cv.findContours(mascara1, cv.RETR_EXTERNAL, cv.CHAIN_APPROX_SIMPLE)
    cv.drawContours(frame_contours, contours1, -1, (144,238,144), thickness=cv.FILLED)
    cv.drawContours(frame_contours, contours1, -1, (144,238,144), 20)
    
    ##Quadrados Brancos
    #Deixa cinza
    frame_gauss = cv.GaussianBlur(frame, (5,5), 1000)
    frame_cinza = cv.cvtColor(frame_gauss, cv.COLOR_BGR2GRAY)
    # Ignora uma determinada altura(evitar a tomada)
    altura, largura = frame_cinza.shape
    metade_inferior = frame_cinza[altura//5:]
    #Identifica o contorno e preenche
    ret, thresh2 = cv.threshold(metade_inferior, 145, 255, cv.THRESH_BINARY)
    contours2, hierarchy1 = cv.findContours(thresh2, cv.RETR_TREE, cv.CHAIN_APPROX_SIMPLE)
    cv.drawContours(frame_contours[altura//5:], contours2, -1, (144,238,144), thickness=cv.FILLED)
    cv.drawContours(frame_contours[altura//5:], contours2, -1, (144,238,144), 30)

    ##Bordas Pretas
    #Ignora uma determinada altura(evitar a tomada)
    ret, thresh3 = cv.threshold(metade_inferior, 145,255, cv.THRESH_BINARY)
    contours3, hierarchy2 = cv.findContours(thresh3, cv.RETR_TREE, cv.CHAIN_APPROX_SIMPLE)
    cv.drawContours(frame_contours[altura//5:], contours3, -1,(144,238,144), 70)
    
    #Efeito de transparencia
    frame = cv.addWeighted(frame, 0.7, frame_contours, 0.5, 0)
    
    cv.imshow('arena', frame)
    if cv.waitKey(1) & 0xFF == ord('q'): break
video.release()
cv.destroyAllWindows()