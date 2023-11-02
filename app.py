import asyncio, requests
import sys
import argparse
from bs4 import BeautifulSoup as bs

def createParser ():
    # парсинг ключей
    parser = argparse.ArgumentParser()
    parser.add_argument ('-u', '--url', required=True)
    parser.add_argument ('-f', '--file', default=None)
    parser.add_argument ('-d', '--depth', default=2, type=int)
 
    return parser

def get_links_from_page(url):
    links = []
    r = requests.get(url)
    if r.status_code == 200:
        soup = bs(r.text, 'html.parser')
        for link in soup.find_all('a'):
            links.append(link.get('href'))
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
        #pass
    else:
        with open(filename, mode='w', encoding='utf-8') as f:
            f.write(result_links)
        print('Done')
    
if __name__ == '__main__':
    parser = createParser()
    args = parser.parse_args (sys.argv[1:])

    main(args.url, args.file, args.depth)
    #print(args.url, args.file, args.depth)