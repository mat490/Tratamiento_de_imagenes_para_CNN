import os
import shutil

nombre_imagen = input("<ingrese el nombre de las imagenes sin su extension>")
# Ruta de la carpeta que contiene las imágenes
ruta_carpeta = input(f"<Ingrese la direccion de la carpeta de imagenes>")

imagenes = []

def contar_imagenes_en_carpeta(ruta_carpeta):
    # Obtener la lista de archivos en la carpeta
    archivos = os.listdir(ruta_carpeta)

    # Filtrar solo los archivos que tienen extensiones de imagen (puedes agregar más extensiones según tus necesidades)
    imagenes = [archivo for archivo in archivos if archivo.lower().endswith(('.png', '.jpg', '.jpeg', '.gif', '.bmp'))]

    # Contar y devolver el número de imágenes
    return len(imagenes)

# Contar el número de imágenes en la carpeta
numero_de_imagenes = contar_imagenes_en_carpeta(ruta_carpeta)
print(f"Número total de imágenes en la carpeta: {numero_de_imagenes}")

# Crear una lista de nombres para las imágenes
lista_nombres = []
for i in range(numero_de_imagenes):
    extension = ".jpg"
    nombre = f"{nombre_imagen}_{i}{extension}"
    lista_nombres.append(nombre)

# Renombrar las imágenes en la carpeta
for i, nombre in enumerate(os.listdir(ruta_carpeta)):
    ruta_antigua = os.path.join(ruta_carpeta, nombre)
    ruta_nueva = os.path.join(ruta_carpeta, lista_nombres[i])
    os.rename(ruta_antigua, ruta_nueva)
    print(f"Imagen renombrada: {nombre} -> {lista_nombres[i]}")

import cv2
import numpy as np


imags_tratadas = []
print("|ATENCIÓN|Están por ser tratadas las imagenes se creara una copia y una nueva carpeta para guardarlas|ATENCIÓN|")
nombre_carpeta_imgs_tratadas = input("<Ingrese el nombre que llevara la carpeta>")
# Nueva carpeta para las imágenes redimensionadas
carpeta_imagenes_tratadas = os.path.join("./imagenes", nombre_carpeta_imgs_tratadas)
# Crear la carpeta si no existe
if not os.path.exists(carpeta_imagenes_tratadas):
    os.makedirs(carpeta_imagenes_tratadas)

for i in range(numero_de_imagenes):
    ruta_img = ruta_carpeta + "/" + lista_nombres[i]
    print(ruta_img)
    # Cargar la imagen en escala de grises directamente
    img = cv2.imread(ruta_img, cv2.IMREAD_GRAYSCALE)
    # Redimensionar la imagen a las dimensiones deseadas (28x28)
    img_tratada = cv2.resize(img, (28, 28))
    # Añadir una dimensión para que coincida con el formato de entrada del modelo (28, 28, 1)
    img_final = np.expand_dims(img_tratada, axis=-1)
    
    # Crear el nombre del archivo para la imagen tratada
    nombre_tratado = f"{nombre_imagen}_{i}_tratada.jpg"
    # Combinar la carpeta de imágenes tratadas con el nombre del archivo
    ruta_imagen_tratada = os.path.join(carpeta_imagenes_tratadas, nombre_tratado)
    cv2.imwrite(ruta_imagen_tratada, img_final)
    imags_tratadas.append(img_final)

