import cv2

def preprocesar(rutaimg):
    img = cv2.imread(rutaimg)

    # Especifica el nuevo ancho deseado
    nueva_anchura = 300

    # Calcula la altura correspondiente para mantener la relación de aspecto
    alto_original, ancho_original = img.shape[:2]
    factor_escala = nueva_anchura / ancho_original
    nueva_altura = int(alto_original * factor_escala)

    # Redimensiona la imagen utilizando cv2.resize()
    imagen_redimensionada = cv2.resize(img, (nueva_anchura, nueva_altura))

    # Suavizar
    imagen_suavizada = cv2.GaussianBlur(imagen_redimensionada, (5, 5), 0)

    # Convertir la imagen a escala de grises
    gray_img = cv2.cvtColor(imagen_suavizada, cv2.COLOR_BGR2GRAY)

    # Aplica el método de Otsu para binarizar la imagen
    _, otsu_threshold = cv2.threshold(gray_img, 0, 255, cv2.THRESH_BINARY + cv2.THRESH_OTSU)

    # Aplicar el detector de bordes Canny
    canny_edges = cv2.Canny(otsu_threshold, threshold1=50, threshold2=150)

    cv2.imshow('Imagen Preprocesada', canny_edges)
    cv2.waitKey(0)
    cv2.destroyAllWindows()

    return canny_edges