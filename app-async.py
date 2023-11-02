import asyncio, aiohttp
import sys
import argparse
from bs4 import BeautifulSoup as bs

from asyncio import ALL_COMPLETED

async def handle_update(queue, link, depth, max_depth):
    depth = int(depth)
    max_depth = int(max_depth)
    links = []
    async with aiohttp.ClientSession() as session:
        resp = await session.get(link)
        resp_data = await resp.text()
        soup = bs(resp_data, 'html.parser')
        for link in soup.find_all('a'):
            href = link.get('href')
            links.append(href)
            if depth < max_depth:
                queue.put_nowait((href, depth+1))
    return links 

async def _worker(queue, num, max_depth):
    #print(f"worker {num} start")
    urls = []
    while True:
        if queue.empty():
            break
        url, depth = await queue.get()
        urls += await handle_update(queue, url, depth, max_depth) 
        queue.task_done()
        #print(f"worker {num} next")
    #print(f"worker {num} end")
    return urls

def createParser ():
    # парсинг ключей
    parser = argparse.ArgumentParser()
    parser.add_argument ('-u', '--url', required=True)
    parser.add_argument ('-f', '--file', default=None)
    parser.add_argument ('-d', '--depth', default=2, type=int)
    parser.add_argument ('-w', '--workers', default=4, type=int)
 
    return parser

async def main(url: str, filename: str, max_depth: int, workers: int):
    queue_links = asyncio.Queue()
    result_links = []
    queue_links.put_nowait((url, 1))
    tasks = [asyncio.create_task(_worker(queue_links, 0, 1))]
    done, _ = await asyncio.wait(tasks, return_when=ALL_COMPLETED)
    for future in done:
            res = future.result()
            result_links.extend(res)
    
    if int(max_depth) > 1:
        for url in result_links:
            queue_links.put_nowait((url,2))
        tasks = [asyncio.create_task(_worker(queue_links, i, max_depth)) for i in range(workers)]
        done, _ = await asyncio.wait(tasks, return_when=ALL_COMPLETED)

        for future in done:
            res = future.result()
            result_links.extend(res)

# ответ    
    result_links = "\n".join(result_links)
    if filename == None:
        print(result_links)
    else:
        with open(filename, mode='w', encoding='utf-8') as f:
            f.write(result_links)
        print('Done')
    
if __name__ == '__main__':
    parser = createParser()
    args = parser.parse_args (sys.argv[1:])

    asyncio.run(main(args.url, args.file, args.depth, args.workers))
