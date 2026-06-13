# Paso a paso para la creación de la app de reconocimiento facial

Este documento describe cómo se creó la aplicación de detección facial con Python y OpenCV, siguiendo el flujo mostrado en la Semana 16: instalación de OpenCV, creación del archivo `main.py`, captura de cámara, procesamiento de imagen, detección del rostro y salida en pantalla.

## 1. Crear la carpeta del proyecto

Primero se crea una carpeta para separar la aplicación del resto de archivos del repositorio.

```bash
mkdir app_reconocimiento_facial
cd app_reconocimiento_facial
```

## 2. Crear el archivo de dependencias

Se crea el archivo `requirements.txt` para indicar qué librería necesita la aplicación.

```txt
opencv-python==4.10.0.84
```

## 3. Instalar OpenCV

Desde la terminal se instala la dependencia del proyecto.

```bash
pip install -r requirements.txt
```

Si el comando anterior no funciona, se puede usar:

```bash
py -m pip install -r requirements.txt
```

## 4. Crear el archivo principal

Se crea el archivo `main.py`, que contendrá el código de la aplicación.

```bash
type nul > main.py
```

En VS Code también se puede crear manualmente haciendo clic derecho en la carpeta y seleccionando **New File**.

## 5. Importar las librerías necesarias

Dentro de `main.py` se importa OpenCV y algunas librerías auxiliares.

```python
import sys
from pathlib import Path
import cv2
```

- `cv2`: permite usar OpenCV.
- `Path`: ayuda a ubicar el archivo clasificador facial.
- `sys`: permite cerrar el programa si ocurre un error.

## 6. Cargar el clasificador facial

OpenCV incluye el archivo `haarcascade_frontalface_default.xml`, que sirve para detectar rostros frontales.

```python
def cargar_clasificador_facial() -> cv2.CascadeClassifier:
    cascade_path = Path(cv2.data.haarcascades) / "haarcascade_frontalface_default.xml"

    if not cascade_path.exists():
        print("No se encontró el archivo Haar Cascade de OpenCV.")
        sys.exit(1)

    clasificador = cv2.CascadeClassifier(str(cascade_path))

    if clasificador.empty():
        print("No se pudo cargar el clasificador facial.")
        sys.exit(1)

    return clasificador
```

Este paso equivale a descargar y usar el archivo `haarcascade_frontalface_default.xml`, pero se aprovecha el archivo que ya viene incluido con OpenCV.

## 7. Abrir la cámara del equipo

La aplicación usa la cámara principal del equipo con `cv2.VideoCapture(0)`.

```python
def abrir_camara(indice: int = 0) -> cv2.VideoCapture:
    camara = cv2.VideoCapture(indice)

    if not camara.isOpened():
        print("No se pudo abrir la cámara.")
        sys.exit(1)

    return camara
```

El índice `0` representa la cámara predeterminada del equipo.

## 8. Leer la imagen de la cámara

Dentro de un ciclo `while`, la aplicación lee los fotogramas capturados por la cámara.

```python
lectura_correcta, frame = camara.read()
```

- `lectura_correcta`: indica si la cámara entregó una imagen válida.
- `frame`: contiene la imagen capturada.

## 9. Convertir la imagen a escala de grises

El detector Haar Cascade trabaja mejor con imágenes en escala de grises.

```python
gris = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
```

Esto reduce la información de color y facilita la detección del rostro.

## 10. Detectar los rostros

Se usa `detectMultiScale()` para buscar rostros dentro de la imagen.

```python
rostros = detector_rostros.detectMultiScale(
    gris,
    scaleFactor=1.1,
    minNeighbors=5,
    minSize=(60, 60)
)
```

Parámetros usados:

- `scaleFactor=1.1`: ajusta la búsqueda en diferentes tamaños.
- `minNeighbors=5`: reduce falsas detecciones.
- `minSize=(60, 60)`: ignora detecciones demasiado pequeñas.

## 11. Dibujar el rectángulo sobre el rostro

Por cada rostro encontrado, se dibuja un rectángulo azul sobre la imagen.

```python
for (x, y, ancho, alto) in rostros:
    cv2.rectangle(
        frame,
        (x, y),
        (x + ancho, y + alto),
        (255, 0, 0),
        2
    )
```

Las variables `x`, `y`, `ancho` y `alto` representan la posición y tamaño del rostro detectado.

## 12. Mostrar texto informativo

Se muestra un texto encima del rostro detectado y también la cantidad de rostros encontrados.

```python
cv2.putText(
    frame,
    "Rostro detectado",
    (x, y - 10),
    cv2.FONT_HERSHEY_SIMPLEX,
    0.7,
    (255, 0, 0),
    2
)
```

```python
cv2.putText(
    frame,
    f"Rostros: {len(rostros)}",
    (10, 30),
    cv2.FONT_HERSHEY_SIMPLEX,
    0.8,
    (0, 255, 0),
    2
)
```

## 13. Mostrar la ventana de resultado

La imagen procesada se muestra en una ventana de OpenCV.

```python
cv2.imshow("Reconocimiento facial - OpenCV", frame)
```

En esta ventana se ve la cámara en tiempo real con los rostros marcados.

## 14. Cerrar la aplicación con ESC o Q

Se captura la tecla presionada por el usuario.

```python
tecla = cv2.waitKey(1) & 0xFF
if tecla == 27 or tecla == ord("q"):
    break
```

- `27`: corresponde a la tecla ESC.
- `q`: permite cerrar la ventana usando la letra Q.

## 15. Liberar recursos

Al finalizar, se libera la cámara y se cierran las ventanas abiertas.

```python
camara.release()
cv2.destroyAllWindows()
```

Esto evita que la cámara quede ocupada por el programa.

## 16. Ejecutar la aplicación

Desde la terminal, estando dentro de la carpeta `app_reconocimiento_facial`, se ejecuta:

```bash
python main.py
```

También se puede usar:

```bash
py main.py
```

## 17. Resultado esperado

Al ejecutar la aplicación:

1. Se abre la cámara del equipo.
2. La imagen se procesa en tiempo real.
3. Si aparece un rostro, se dibuja un rectángulo sobre él.
4. Se muestra la cantidad de rostros detectados.
5. La aplicación se cierra con ESC o Q.

## 18. Estructura final del proyecto

```txt
app_reconocimiento_facial/
│
├── main.py
├── requirements.txt
├── README.md
├── PASO_A_PASO_CREACION.md
└── .gitignore
```

## 19. Conclusión

La aplicación cumple el flujo de trabajo de OpenCV: entrada, procesamiento e inferencia, y salida. La entrada es la cámara, el procesamiento consiste en convertir la imagen a escala de grises y aplicar el clasificador Haar Cascade, y la salida es la ventana donde se muestra el rostro detectado.
