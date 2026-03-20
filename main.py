from bs4 import BeautifulSoup as bs
import requests as rq
import polars as pl
import pathlib as ph
import urllib.parse as urlp


dl_path = ph.Path('data/raw')
url= 'https://amazon-reviews-2023.github.io/index.html'
def data_dictionary():
    {
        'name':'',
        'link':'',
    }

def content_request(url):

    dl_path.mkdir(parents=True, exist_ok=True)

    request = rq.get(url)

    if not request.ok:
        raise RuntimeError(f"Server returned {request.status_code}")
    
    try:
        request_content = bs(request.content,'html.parser')
        return request_content
    except Exception as e :
        raise RuntimeError(f"Failed to parse HTML: {e}") from e

def get_links(request):
    links = []  
    for link in request.find_all(attrs ={'href':True,'download':True}):
        links.append(link['href'])
    return links

def get_names(links):
    names = []
    for link in links:
        names.append(ph.Path(urlp.urlparse(link).path).name)
    return names

links = get_links(content_request(url))
names = get_names(links)
print(f'{names}')