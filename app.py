import requests
import sys
import argparse
import time
from bs4 import BeautifulSoup as bs
from urllib.parse import urljoin # для формирования правильной ссылки из бозового url и относительной ссылки

def createParser ():
    # парсинг ключей
    parser = argparse.ArgumentParser()
    parser.add_argument ('-u', '--url', required=True)
    parser.add_argument ('-f', '--file', default=None)
    parser.add_argument ('-d', '--depth', default=1, type=int)
 
    return parser

def get_links_from_page(url):
    links = []
    #print(f'Парсинг страницы по ссылке {url}') # включить, чтобы было видно, что скрипт не завис :)
    try:
        r = requests.get(url)
        if r.status_code == 200:
            base_url = r.url
            soup = bs(r.text, 'html.parser')
            for link in soup.find_all('a'):
                lnk = urljoin(base_url, link.get('href')) # формируем валидную ссылку
                if lnk.startswith('tel') or lnk.startswith('mailto') or lnk.startswith('javascript') or lnk.startswith('tg'): # убрать ссылки на тел, почту, javascript
                    continue
                links.append(lnk)
    except Exception as e: 
        print(e)
    #links = set(links) # убрать одинаковые ссылки
    return links 

def main(url, filename, max_depth):
    result_links = [url]
    total_links = []

    for i in range(1, int(max_depth)+1):
        links = result_links
        result_links = []
        for link in links:
            result_links += get_links_from_page(link)
        total_links.extend(result_links)
    
    result_links = "\n".join(total_links)
    
    if filename == None:
        print(result_links)
    else:
        with open(filename, mode='w', encoding='utf-8') as f:
            f.write(result_links)
        print('Done')
    
if __name__ == '__main__':
    parser = createParser()
    args = parser.parse_args (sys.argv[1:])
    start_time = time.time()
    main(args.url, args.file, args.depth)
    print("--- %s seconds ---" % (time.time() - start_time))