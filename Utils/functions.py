"""Funciones generales del programa"""
import cv2
import face_recognition


def face_encoding(path_image: str):
    """Detecta los rostros disponibles en una imagen

    Args:
        path_image (str): Ruta de la imagen original

    Returns:
        img_encoging: Imagen codificada
    """

    # Cargamos la imagen
    img_original = cv2.imread(path_image)

    # Convertimos la imagen en formato RGB
    img_rgb = cv2.cvtColor(img_original, cv2.COLOR_BGR2RGB)

    # Buscamos los rostros disponibles en la imagen
    img_encoding = face_recognition.face_encodings(img_rgb)

    return img_encoding


def face_compare(image_1, image_2):
    """Realiza la comparación entre dos rostros

    Args:
        image_1 (_type_): Imagen de referencia
        image_2 (_type_): Imagen a evaluar
    """

    # Realizamos la comparación entre los rostros
    result = face_recognition.compare_faces([image_1], image_2)
    return result[0]
