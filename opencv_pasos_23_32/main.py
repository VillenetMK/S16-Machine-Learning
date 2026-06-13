import cv2
from pathlib import Path
from urllib.request import urlretrieve

CASCADE_FILE = Path("haarcascade_frontalface_default.xml")
CASCADE_URL = "https://raw.githubusercontent.com/opencv/opencv/master/data/haarcascades/haarcascade_frontalface_default.xml"

if not CASCADE_FILE.exists():
    print("No se encontró haarcascade_frontalface_default.xml en la carpeta del proyecto.")
    print("Descargando desde GitHub/OpenCV...")
    urlretrieve(CASCADE_URL, CASCADE_FILE)
    print("Descarga finalizada.")

face_cascade = cv2.CascadeClassifier(str(CASCADE_FILE))

if face_cascade.empty():
    raise RuntimeError("No se pudo cargar haarcascade_frontalface_default.xml")

cap = cv2.VideoCapture(0)

if not cap.isOpened():
    raise RuntimeError("No se pudo abrir la cámara.")

while True:
    ret, img = cap.read()

    if not ret:
        print("No se pudo leer la imagen de la cámara.")
        break

    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

    faces = face_cascade.detectMultiScale(gray, 1.1, 4)

    for (x, y, w, h) in faces:
        cv2.rectangle(img, (x, y), (x + w, y + h), (255, 0, 0), 2)

    cv2.imshow("img", img)

    if cv2.waitKey(30) & 0xFF == 27:
        break

cap.release()
cv2.destroyAllWindows()
