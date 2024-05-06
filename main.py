import preprocesamiento as pp
import hough


imagen_preprocesada=pp.preprocesar("dataset/images/phase2/good/20240504_131902.jpg")
print(f"La cantidad de estolones aproximada es de {hough.detectar_estolones_rectos(imagen_preprocesada)}")