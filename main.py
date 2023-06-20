import requests
from bs4 import BeautifulSoup

url = 'https://www.amazon.com.br/s?k=samsung+a54&i=electronics&crid=LY498X1MWR1I&qid=1687271854&sprefix=samsung%2Celectronics%2C391&ref=sr_pg_1'

headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/114.0.0.0 Safari/537.36'}

def proxima_pagina(soup):
    #procurar botao proxima pagina
    paginas = soup.find('a', {'class': 's-pagination-item s-pagination-next s-pagination-button s-pagination-separator'})

    # se o botão não estiver desabilitado(ultima pagina)
    if not paginas.find('span', {'class': 's-pagination-item s-pagination-next s-pagination-disabled'}):
        base_url = 'https://www.amazon.com.br'
        prox = soup.find('a', {'class': 's-pagination-item s-pagination-next s-pagination-button s-pagination-separator'}).get('href')
        final_url = base_url + prox
        return final_url
    else:
        return


while True:
    site = requests.get(url, headers=headers)
    print(site)
    soup = BeautifulSoup(site.content, 'html.parser')
    url = proxima_pagina(soup)
    if not url:
        break
    print(url)
