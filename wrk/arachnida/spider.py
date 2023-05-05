from bs4 import BeautifulSoup as bs
from urllib.parse import urlparse
import argparse
import requests
import os


urls_found = []
img_found = []
imgs_downloaded = []

MAIN_DOMAIN = ""

def check_path(path):
    out = path
    check_folder = os.path.isdir(out)
    if not check_folder:
        os.makedirs(out)

# Busco img
def get_img_url_lst(url):
    rq = requests.get(url)
    soup = bs(rq.content, "html.parser")
    images = soup.select('img')
    return(images)


def image_list(path, url):
    check_path(path)
    images = get_img_url_lst(url)
    for i, image in enumerate(images):
        image_url = images[i]['src']
        # Remove parameters after filename
        image_url = image_url.split("?")[0]
        image_name = image_url.split("/")[-1]
        print(f"Image Found: {image_name}")
        if image_name not in img_found:
            print(f"Image Added: {image_name}")
            img_found.append(image_name)

        if image_name in img_found and image_name in imgs_downloaded:
            print("Image Already Downloaded")
            continue
    #     # Check file extention
        elif image_name[-3:] in extentions or image_name[-4:] in extentions:
            # Add images to image_list / Retrive file name from URL
            # Retrive file content/data
            if image_name not in imgs_downloaded:
                img_data = requests.get(image_url).content
                # Save file to selected folder (default: 'data') using binary to avoid 
                # encoding and other common problems
                with open(os.path.join(path, image_name), 'wb') as handler:
                    handler.write(img_data)
                    imgs_downloaded.append(image_name)
                
                print(f"Image downloadedb {image_name}")
    print(imgs_downloaded)
    
    # else: Delete image_url


def find_domain(url):
    tmp_domain = ''
    if url.startswith("www."):
        for c in url:
            if c != "/":
                tmp_domain += c
            else:
                break
    else:
        for c in url:
            if c != "/":
                tmp_domain += c
            else:
                break
    return(tmp_domain)


def strip_url(url):
    striped_url = ''
    if url.startswith("http://www."):
        url_prefix = "http://www."
        striped_url = url[11:]
    elif url.startswith("https://www."):
        url_prefix = "https://www."
        striped_url = url[12:]
    elif url.startswith("https://"):
        url_prefix = "https://"
        striped_url = url[8:]
    elif url.startswith("http://"):
        url_prefix = "http://"
        striped_url = url[7:]
    return (striped_url)


# BUSCO a ! Working
def get_url_lst(url):
    rq = requests.get(url)
    soup = bs(rq.content, "html.parser")
    for i, a in enumerate(soup.find_all('a', href=True)):
        current_url = a['href']
        striped_url = strip_url(current_url)
        domain_tmp = find_domain(striped_url)
        # print(f"Main Domain: {MAIN_DOMAIN}")
        # print(domain_tmp)
        if domain_tmp != MAIN_DOMAIN:
            # print("Different Domain")
            continue
        if a['href'] not in urls_found or a['href'] + "/" not in urls_found:
            urls_found.append(a['href'])


def check_url(url):
    str_url = strip_url(url)
    tmp_domain = find_domain(str_url)
    response = requests.head(url)
    if response.status_code == 200:
        return 1
    elif response.status_code == 301:
        mmeta = response.headers['Location']
        str_url2 = strip_url(mmeta)
        tmp_domain2 = find_domain(str_url2)
        if tmp_domain == tmp_domain2:
            print("Redirect Domain OK")
            return 1
        else:
            print("Redirect to external URL. Exiting ...")
            exit()
            return 0
    else:
        return 0


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
    if args.p:
        path = str(args.p) 
    else:
        path = 'data'
    if args.p:
        path = args.p
    print(path)
    status = 0
    status = check_url(url)
    if status == 0:
        print("URL not found, please provide valid URL.")
        exit()
    striped_url = strip_url(url)
    MAIN_DOMAIN = find_domain(striped_url)
    print(MAIN_DOMAIN)

    get_url_lst(url)

    print(urls_found)
    for i in urls_found:
        print(f"\n\nDownloading from: {i}\n\n")
        image_list(path, i)









    # if recur:
    #     url_list(url, 0)
    # else:
    #     image_list(path, url)

    # url_list(url, 0)

    # print(urls_lizt)
    # get_img_url_lst(url)
    # print(url_lizt)
    # print(domain)
    # print(url)
    # print(urls_found)
    # print(links_found)