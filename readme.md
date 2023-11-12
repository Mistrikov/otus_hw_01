Домашнее задание №1 "Парсер ссылок с сайта"

В задании не указана глубина парсинга ссылок, поэтому добавлен параметр DEPTH = 1

<h3>Файл app.py</h3>

usage: app.py [-h] -u URL [-f FILE] [-d DEPTH]

options:
  -h, --help            show this help message and exit
  -u URL, --url URL
  -f FILE, --file FILE
  -d DEPTH, --depth DEPTH

<h3>Файл app-async.py</h3>
usage: app-async.py [-h] -u URL [-f FILE] [-d DEPTH] [-w WORKERS]

options:
  -h, --help            show this help message and exit
  -u URL, --url URL
  -f FILE, --file FILE
  -d DEPTH, --depth DEPTH
  -w WORKERS, --workers WORKERS
