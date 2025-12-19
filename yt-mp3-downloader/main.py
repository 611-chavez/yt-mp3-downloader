from downloader.mp3 import descargar_mp3

FFMPEG_PATH = r"C:\ruta\a\ffmpeg\bin"

def main():
    with open("playlist.txt", "r", encoding="utf-8") as f:
        urls = [line.strip() for line in f if line.strip()]

    for url in urls:
        print(f"Descargando: {url}")
        descargar_mp3(url, ruta_ffmpeg=FFMPEG_PATH)


if __name__ == "__main__":
    main()


"""
AVISO LEGAL

Este proyecto ha sido desarrollado exclusivamente con fines educativos.
El usuario es responsable del uso que haga del software.
"""