# OpenCV: detección facial - pasos 23 al 32

Este proyecto sigue el paso a paso indicado en las páginas 23 a 32 del material de la Semana 16.

## Paso 23: Entrar al repositorio de Haar Cascades

Abrir la URL indicada en el material:

```text
https://github.com/opencv/opencv/tree/master/data/haarcascades
```

## Paso 24: Seleccionar el archivo correcto

Buscar y seleccionar el archivo:

```text
haarcascade_frontalface_default.xml
```

Este archivo contiene el clasificador Haar Cascade para detectar rostros frontales.

## Paso 25: Ver el archivo en formato Raw

Dentro de GitHub, presionar el botón **Raw** para ver el contenido del XML sin formato.

## Paso 26: Descargar el archivo al proyecto

Guardar el archivo dentro de la carpeta del proyecto.

En este repo se agregó un script para hacer esa descarga automáticamente:

```bash
python descargar_haarcascade.py
```

También el archivo `main.py` descarga el XML automáticamente si no existe.

## Paso 27: Abrir la carpeta en VS Code

Abrir la carpeta:

```text
opencv_pasos_23_32
```

en Visual Studio Code.

## Paso 28: Crear el archivo main.py

El archivo creado es:

```text
main.py
```

## Paso 29: Iniciar el código importando OpenCV

El código inicia con:

```python
import cv2
```

## Paso 30: Instalar OpenCV si hay error de importación

Desde la terminal de VS Code ejecutar:

```bash
pip install opencv-python
```

Si no funciona:

```bash
py -m pip install opencv-python
```

## Paso 31: Escribir el código de detección facial

El código utiliza:

```python
face_cascade = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')
cap = cv2.VideoCapture(0)
```

Luego convierte la imagen a escala de grises, detecta rostros con `detectMultiScale()` y dibuja un rectángulo sobre el rostro detectado.

## Paso 32: Ejecutar la aplicación

Desde la carpeta del proyecto:

```bash
python main.py
```

También puede ejecutarse con:

```bash
py main.py
```

La cámara se abre y, cuando detecta un rostro, aparece un rectángulo azul. Para cerrar la aplicación se presiona **ESC**.

## Archivos incluidos

```text
opencv_pasos_23_32/
├── main.py
├── requirements.txt
├── descargar_haarcascade.py
└── PASOS_23_AL_32.md
```
