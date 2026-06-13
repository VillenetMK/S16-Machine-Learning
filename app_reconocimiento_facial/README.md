# App de reconocimiento facial con OpenCV

Esta aplicación implementa una detección facial en tiempo real usando Python y OpenCV. La cámara del equipo captura video, el programa convierte cada fotograma a escala de grises y aplica un clasificador Haar Cascade para localizar rostros.

## Requisitos

- Python 3.10 o superior
- Cámara web funcional
- OpenCV

## Instalación

Abre una terminal dentro de esta carpeta y ejecuta:

```bash
pip install -r requirements.txt
```

Si `pip` no funciona, usa:

```bash
py -m pip install -r requirements.txt
```

## Ejecución

```bash
python main.py
```

También puedes ejecutar:

```bash
py main.py
```

## Funcionamiento

1. Se importa la librería `cv2`.
2. Se carga el clasificador `haarcascade_frontalface_default.xml` incluido en OpenCV.
3. Se abre la cámara del equipo.
4. Cada imagen capturada se convierte a escala de grises.
5. El clasificador detecta los rostros dentro del fotograma.
6. El programa dibuja un rectángulo sobre cada rostro detectado.
7. El resultado se muestra en una ventana en tiempo real.

## Controles

- Presiona `ESC` para cerrar.
- Presiona `Q` para cerrar.

## Nota

Este ejemplo realiza detección facial, es decir, identifica la ubicación de rostros en la cámara. No reconoce la identidad de una persona específica.
