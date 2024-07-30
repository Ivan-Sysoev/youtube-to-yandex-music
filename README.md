# Скачивание MP3 с YouTube с использованием пользовательской обложки

* [Описание](#Описание)
* [Установка](#Установка)
* [Использование](#Использование)
* [Загрузка на Яндекс музыку](#Загрузка-на-Яндекс-музыку)
* [Пример](#Пример)
* [Особенности](#Особенности)
* [Благодарности](#Благодарности)

## Описание
За последнее время Яндекс Музыка утеряла права на большое количество зарубежной музыки, но сервис предоставляет возможность загружать пользовательские треки. Для того, чтобы сервис корректно отображал данные аудиофайла (Название, автор, обложка) нужно произвести несколько операций, которые как раз и делает этот Python скрипт за вас!

Этот скрипт на Python скачивает аудио с видео на YouTube и сохраняет его в формате MP3 с пользовательской или стандартной обложкой. Пользователь может указать название аудиофайла, автора и при необходимости предоставить свою обложку. Если пользователь не предоставляет обложку, используется стандартная обложка с YouTube.

## Установка
* Установите Python 3.x, если он еще не установлен.
* Установите необходимые Python пакеты:
```
pip install ffmpeg-python mutagen requests yt-dlp
```
* Убедитесь, что ffmpeg установлен и доступен в PATH вашей системы. Вы можете скачать его с [официального сайта FFmpeg](https://ffmpeg.org/download.html).

## Использование
* Клонируйте этот репозиторий или скачайте скрипт.
* Запустите скрипт и следуйте инструкциям для ввода необходимых данных:
```
python yandex-music.py
```
* Скрипт запросит:
    * URL видео с YouTube.
    * Желаемое название аудиофайла.
    * Имя автора.
    * Необязательный путь к изображению обложки.

## Загрузка на Яндекс музыку
* Откройте [официальный сайт Яндекс музыки](https://music.yandex.ru)
* В правом верхнем углу страницы нажмите кнопку `Коллекция`.
* Перейдите на вкладку `Плейлисты`.
* Создайте новый плейлист или откройте существующий.
* Под описанием плейлиста нажмите кнопку `Загрузить трек` и выберите файлы на компьютере.

## Пример
```
$ python yandex-music.py
Введите URL ссылки на YouTube видео: https://www.youtube.com/watch?v=dQw4w9WgXcQ
Введите название аудиофайла: MyFavoriteSong
Введите автора аудиофайла: Rick Astley
Введите путь к обложке (оставьте пустым для использования превью с YouTube): 
```
Скрипт скачает аудио, применит указанные метаданные и обложку, и сохранит MP3 файл в папке, где находится сам скрипт.

## Особенности
* Скачивает аудио с видео на YouTube в наилучшем доступном качестве.
* Позволяет пользователю указать название аудиофайла и автора.
* Поддерживает пользовательские обложки или использует стандартную обложку видео с YouTube.
* Добавляет указанные автор и название в метаданные MP3 файла.
* Включает обложку как изображение альбома в метаданных MP3 файла.
* Автоматически удаляет временные файлы после обработки.

## Благодарности
Этот проект был создан с помощью ChatGPT.
