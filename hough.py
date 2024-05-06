import cv2
import numpy as np

def detectar_estolones_rectos(imagen):

    gray = cv2.cvtColor(imagen, cv2.COLOR_BGR2GRAY)

    # Parámetros de la función HoughLinesP
    rho = 1
    theta = np.pi/180
    threshold = int(len(imagen[0])/4)
    minLineLength = int(len(imagen[0])/2)
    maxLineGap = int(len(imagen)*0.08)

    lineas = cv2.HoughLinesP(gray, rho, theta, threshold, minLineLength, maxLineGap)

    # Dibuja las líneas detectadas sobre la imagen original
    if lineas is not None:
        for linea in lineas:
            x1, y1, x2, y2 = linea[0]
            cv2.line(imagen, (x1, y1), (x2, y2), (0, 255, 0), 2)

    # Muestra la imagen con las líneas detectadas
    cv2.imshow('HoughLinesP', imagen)
    cv2.waitKey(0)
    cv2.destroyAllWindows()

    return(int(len(lineas)/2))


"""---------------Ejemplo de uso------------------------
image = cv2.imread('dataset/imagen_ejemplo.jpg')
print(detectar_estolones_rectos(image))
-----------------------------------------------------"""