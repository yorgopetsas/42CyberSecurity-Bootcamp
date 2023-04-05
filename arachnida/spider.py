import argparse
import requests
import os

from bs4 import BeautifulSoup as bs
from urllib.parse import urlparse

urls_found = set()
links_found = set()    

def check_path(path):
    out = path
    check_folder = os.path.isdir(out)
    if not check_folder:
        os.makedirs(out)

def get_img_lst(url):
    rq = requests.get(url)
    soup = bs(rq.content, "html.parser")
    images = soup.select('img')
    return(images)

# def get_url_lst(url):
#     rq = requests.get(url)
#     soup = bs(rq.content)
#     for a in soup.find_all('a', href=True):
#        print("Found the URL:", a['href'])
    # urls = soup.select('a', href=True)
    # return(urls)

def image_list(path, url):
  check_path(path)
  images = get_img_lst(url)
  for i, image in enumerate(images):
    images_url = images[i]['src']
    # Remove parameters after filename
    images_url = images_url.split("?")[0]
    # Check file extention
    if images_url[-3:] in extentions or images_url[-4:] in extentions:
      # Add images to image_list
      # Retrive file name from URL
      image_name = images_url.split("/")[-1]
      # Retrive file content/data
      img_data = requests.get(images_url).content
      # Save file to selected folder (default: 'data') using binary to avoid 
      # encoding and other common problems
      with open(os.path.join(path, image_name), 'wb') as handler:
        handler.write(img_data)

def url_list(website, lv):
    try:
        rq = requests.get(url)
        soup = bs(rq.content, "html.parser")
        for a in soup.find_all('a', href=True):
            if a not in urls_found:
                urls_found.add(a['href'])
        print(urls_found)
        # Recursividad: extraer los otros sitios web
        # si aún no se alcanzó la profundidad indicada
        if lv < level:
            url_list(link[i + 1], lv + 1)

    except Exception as excepcion:
        print('Error')

def cli_scan():
    # Scan the arguments in the CLI
    scan = argparse.ArgumentParser()

    scan.add_argument("URL", help="", type=str)
    scan.add_argument("-r", help="", type=str)
    scan.add_argument("-l", help="", type=int, default=5)
    scan.add_argument("-s", help="", type=str)
    scan.add_argument("-p", help="", type=str)

    return scan.parse_args()

if __name__ == "__main__":
    global url, recur, level, sorted, path, extentions

    extentions = ["jpg", "jpeg", "gif", "bmp", "png"]
    args = cli_scan()
    url = args.URL
    recur = args.r
    level = args.l
    sorted = args.s
    path = 'data'
    if args.p:
        path = args.p
    # url_list(url, 0)
    if recur:
        url_list(url, 0)
    else:
        image_list(path, url)

