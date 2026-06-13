"""
Aplicación de reconocimiento/detección facial con OpenCV.
Semana 16 - Machine Learning / OpenCV

Uso:
    python main.py

Controles:
    ESC o Q -> cerrar la aplicación
"""

import sys
from pathlib import Path

import cv2


WINDOW_NAME = "Reconocimiento facial - OpenCV"


def cargar_clasificador_facial() -> cv2.CascadeClassifier:
    """Carga el clasificador Haar Cascade incluido en OpenCV."""
    cascade_path = Path(cv2.data.haarcascades) / "haarcascade_frontalface_default.xml"

    if not cascade_path.exists():
        print("No se encontró el archivo Haar Cascade de OpenCV.")
        print(f"Ruta esperada: {cascade_path}")
        sys.exit(1)

    clasificador = cv2.CascadeClassifier(str(cascade_path))

    if clasificador.empty():
        print("No se pudo cargar el clasificador facial.")
        sys.exit(1)

    return clasificador


def abrir_camara(indice: int = 0) -> cv2.VideoCapture:
    """Abre la cámara web del equipo."""
    camara = cv2.VideoCapture(indice)

    if not camara.isOpened():
        print("No se pudo abrir la cámara.")
        print("Verifica que tu webcam esté conectada y que otra app no la esté usando.")
        sys.exit(1)

    return camara


def ejecutar_reconocimiento_facial() -> None:
    """Ejecuta la detección facial en tiempo real."""
    detector_rostros = cargar_clasificador_facial()
    camara = abrir_camara()

    print("Aplicación iniciada.")
    print("Presiona ESC o Q para cerrar.")

    while True:
        lectura_correcta, frame = camara.read()

        if not lectura_correcta:
            print("No se pudo leer el video de la cámara.")
            break

        gris = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

        rostros = detector_rostros.detectMultiScale(
            gris,
            scaleFactor=1.1,
            minNeighbors=5,
            minSize=(60, 60)
        )

        for (x, y, ancho, alto) in rostros:
            cv2.rectangle(
                frame,
                (x, y),
                (x + ancho, y + alto),
                (255, 0, 0),
                2
            )
            cv2.putText(
                frame,
                "Rostro detectado",
                (x, y - 10),
                cv2.FONT_HERSHEY_SIMPLEX,
                0.7,
                (255, 0, 0),
                2
            )

        cv2.putText(
            frame,
            f"Rostros: {len(rostros)}",
            (10, 30),
            cv2.FONT_HERSHEY_SIMPLEX,
            0.8,
            (0, 255, 0),
            2
        )

        cv2.imshow(WINDOW_NAME, frame)

        tecla = cv2.waitKey(1) & 0xFF
        if tecla == 27 or tecla == ord("q"):
            break

    camara.release()
    cv2.destroyAllWindows()
    print("Aplicación finalizada.")


if __name__ == "__main__":
    ejecutar_reconocimiento_facial()
