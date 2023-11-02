Домашнее задание №1 "Парсер ссылок с сайта"

В задании не указана глубина парсинга ссылок, поэтому добавлен параметр DEPTH = 2

Файл app.py

usage: app.py [-h] -u URL [-f FILE] [-d DEPTH]

options:
  -h, --help            show this help message and exit
  -u URL, --url URL
  -f FILE, --file FILE
  -d DEPTH, --depth DEPTH

Файл app-async.py
usage: app-async.py [-h] -u URL [-f FILE] [-d DEPTH] [-w WORKERS]

options:
  -h, --help            show this help message and exit
  -u URL, --url URL
  -f FILE, --file FILE
  -d DEPTH, --depth DEPTH
  -w WORKERS, --workers WORKERS