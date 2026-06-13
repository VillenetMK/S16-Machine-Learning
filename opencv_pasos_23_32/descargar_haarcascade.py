from pathlib import Path
from urllib.request import urlretrieve

URL = "https://raw.githubusercontent.com/opencv/opencv/master/data/haarcascades/haarcascade_frontalface_default.xml"
DESTINO = Path("haarcascade_frontalface_default.xml")

print("Descargando haarcascade_frontalface_default.xml...")
urlretrieve(URL, DESTINO)
print(f"Archivo guardado en: {DESTINO.resolve()}")
