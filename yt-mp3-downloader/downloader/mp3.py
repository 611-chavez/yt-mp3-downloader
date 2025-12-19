import os
from yt_dlp import YoutubeDL


def descargar_mp3(url, carpeta_destino="descargas", ruta_ffmpeg=None):
    os.makedirs(carpeta_destino, exist_ok=True)

    opciones = {
        'format': 'bestaudio/best',
        'outtmpl': os.path.join(carpeta_destino, '%(title)s.%(ext)s'),
        'noplaylist': True,
        'postprocessors': [{
            'key': 'FFmpegExtractAudio',
            'preferredcodec': 'mp3',
            'preferredquality': '192',
        }],
    }

    if ruta_ffmpeg:
        opciones['ffmpeg_location'] = ruta_ffmpeg

    with YoutubeDL(opciones) as ydl:
        ydl.download([url])
