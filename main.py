from bs4 import BeautifulSoup as bs
import requests as rq
import polars as pl
import pathlib as ph

#'''
# 1.First check if folder exists if not create folder
# 2.Rquest data from page and get list of urls and files
# 3.Save list somewhere as txt
# 4.Download from list
# 5.save sucessfuly downloaded files to txt
# '''
dl_path = ph.Path('data/raw')
url= 'https://amazon-reviews-2023.github.io/index.html'


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
    return request.find_all('a',attrs ={'href':True,'download':True})

links = get_links(content_request(url))
 
print(links)




