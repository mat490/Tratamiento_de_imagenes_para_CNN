# Proyecto de Preparación de Imágenes para Entrenamiento de Redes Neuronales Convolucionales Alpha 0.0001

Este es un proyecto personal que tiene como objetivo crear un programa capaz de preparar imágenes para el entrenamiento de un modelo de red neuronal convolucional.

## Descripción

El propósito de este proyecto es facilitar la preparación de imágenes para su uso en el entrenamiento de modelos de redes neuronales convolucionales (CNN). El programa proporciona funcionalidades para renombrar imágenes y redimensionarlas a las dimensiones deseadas, lo cual es comúnmente necesario para el entrenamiento eficiente de modelos CNN.

## Funcionalidades

1. **Renombrar Imágenes:**
   - El programa permite renombrar imágenes en una carpeta dada, siguiendo un patrón predefinido.

2. **Redimensionar Imágenes:**
   - Las imágenes en la carpeta especificada se redimensionan a las dimensiones deseadas (28x28 en este caso).

3. **Converir las imagenes a escala de grises:**
   - Las imágenes se convierten a escalas de grises, con la finalidad de facilitar el entrenamiento de la red neuronal.

4. **Guardar Imágenes Tratadas:**
   - Las imágenes tratadas se guardan en una nueva carpeta, facilitando la organización y gestión de los datos de entrenamiento.

## Uso

1. Clona este repositorio en tu máquina local.

2. Ejecuta el script `preparar_imagenes.py`.

3. Sigue las instrucciones proporcionadas en la consola para ingresar el nombre de las imágenes y la ruta de la carpeta.

***Se incluye una muestra de imagenes de linfocitos***

## Requisitos

- Python 3.x
- Bibliotecas Python: OpenCV, NumPy, TensorFlow

## Contribuciones

¡Las contribuciones son bienvenidas! Si encuentras mejoras o tienes sugerencias, no dudes en crear un problema o enviar una solicitud de extracción.

## Licencia

Este proyecto está bajo la Licencia [MIT](LICENSE).
