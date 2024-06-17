import yt_dlp
import ffmpeg
import os
from pathlib import Path
import requests
import webbrowser
from mutagen.easyid3 import EasyID3
from mutagen.id3 import ID3, APIC

def download_youtube_audio_with_thumbnail(url, output_path, file_name, author, custom_thumbnail_path=None):
    # Настройка параметров для yt-dlp
    ydl_opts = {
        'format': 'bestaudio/best',
        'outtmpl': '%(title)s.%(ext)s',
        'postprocessors': [{
            'key': 'FFmpegExtractAudio',
            'preferredcodec': 'mp3',
            'preferredquality': '192',
        }],
    }

    # Скачиваем аудио
    with yt_dlp.YoutubeDL(ydl_opts) as ydl:
        info = ydl.extract_info(url, download=True)
        audio_filename = ydl.prepare_filename(info).rsplit('.', 1)[0] + '.mp3'
        thumbnail_url = info.get('thumbnail', None)

    # Скачиваем превью, если пользователь не указал путь к обложке
    if not custom_thumbnail_path and thumbnail_url:
        custom_thumbnail_path = file_name + '.jpg'
        response = requests.get(thumbnail_url)
        with open(custom_thumbnail_path, 'wb') as file:
            file.write(response.content)

    # Путь к сохранению аудиофайла
    final_audio_path = Path(output_path) / (file_name + '.mp3')

    # Убедимся, что выходной путь существует
    Path(output_path).mkdir(parents=True, exist_ok=True)

    # Добавление обложки к аудиофайлу
    input_audio = ffmpeg.input(audio_filename)
    input_image = ffmpeg.input(custom_thumbnail_path)
    ffmpeg.output(input_audio, input_image, str(final_audio_path), 
                  **{'c:v': 'mjpeg', 'c:a': 'copy', 'disposition:v': 'attached_pic'}).run(overwrite_output=True)

    # Установка тегов
    audio = EasyID3(str(final_audio_path))
    audio['artist'] = author
    audio['title'] = file_name  # Добавляем название без расширения
    audio.save()

    # Добавление обложки в теги
    audio = ID3(str(final_audio_path))
    with open(custom_thumbnail_path, 'rb') as albumart:
        audio['APIC'] = APIC(
            encoding=3,
            mime='image/jpeg',
            type=3,  # 3 is for the cover (front) image
            desc='Cover',
            data=albumart.read()
        )
    audio.save()

    # Удаление временных файлов, если обложка была скачана
    os.remove(audio_filename)
    if custom_thumbnail_path == file_name + '.jpg':
        os.remove(custom_thumbnail_path)

if __name__ == "__main__":
    # Получаем данные от пользователя
    url = input("Введите URL ссылки на YouTube видео: ")
    file_name = input("Введите название аудиофайла: ")
    author = input("Введите автора аудиофайла: ")
    custom_thumbnail_path = input("Введите путь к обложке (оставьте пустым для использования превью с YouTube): ")

    # Путь к папке, где находится скрипт
    output_path = os.path.dirname(os.path.abspath(__file__))

    download_youtube_audio_with_thumbnail(url, output_path, file_name, author, custom_thumbnail_path)
    print("Аудиофайл успешно сохранен.")
