from bs4 import BeautifulSoup as bs
from urllib.parse import urlparse
import argparse
import requests
import os
from os.path import exists

urls_to_visit = []
urls_to_visit_l = []
url_visited = []
img_found = []
imgs_downloaded = []

MAIN_DOMAIN = ""


# Check if provided (or default) path exists and create it
def check_path(path):
    out = path
    check_folder = os.path.isdir(out)
    if not check_folder:
        os.makedirs(out)


# Search for am img tag
def get_img_url_lst(url):
    rq = requests.get(url)
    soup = bs(rq.content, "html.parser")
    images = soup.select('img')
    return(images)


# Make a list of the images in the current url
def image_list(path, url):
    check_path(path)
    images = get_img_url_lst(url)

    for i, image in enumerate(images):
        image_url = images[i]['src']
        # Remove parameters after filename
        image_url = image_url.split("?")[0]
        image_name = image_url.split("/")[-1]
        print(f"Image Found: {image_name}")
        if image_url in imgs_downloaded:
            print("x Image Already Downloaded")
            continue
        elif image_url in img_found:
            print("x Image Already Added")
            continue
        elif image_url not in img_found:
            print(f"Image Added: {image_name}")
            img_found.append(image_url)


# Local: Download images from the "img_found" list to the provided path
def dwn_img_local(img_found, location, path):
    for i, image in enumerate(img_found):
        image_name = image.split("/")[-1]
        # Check file extention
        if image[-3:] in extentions or image[-4:] in extentions:
            rut = os.path.dirname(location)
            final_path = rut + '/' + image
            dst = path + '/' + image_name
            if final_path in imgs_downloaded:
                print("x Image Already Downloaded")
                continue
            try: 
                os.popen(f'cp {final_path} {dst}')
                imgs_downloaded.append(final_path)
                print(f"Local Image downloaded: {image_name}")
            except:
                print('error')


# Download images from the "img_found" list to the provided path
def dwn_img(img_found, path):
    for i, image in enumerate(img_found):
        image_name = image.split("/")[-1]
        if image in img_found and image in imgs_downloaded:
            print("x Image Already Downloaded")
            continue
        # Check file extention
        elif image[-3:] in extentions or image[-4:] in extentions:
            # Add images to image_list / Retrive file name from URL
            if image not in imgs_downloaded:
                img_data = requests.get(image).content
                # Save file to selected folder (default: 'data') using binary to avoid encoding and other common problems
                with open(os.path.join(path, image_name), 'wb') as handler:
                    # Retrive file content/data
                    handler.write(img_data)
                    imgs_downloaded.append(image)
                print(f"Image downloaded: {image_name}")


# Extract the domain from the stripped URL
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


# Local: Make a list of the images from local file
def image_list_local(path, s):
    check_path(path)
    images = s.select('img')
    for i, image in enumerate(images):
        image_url = images[i]['src']
        # Remove parameters after filename
        image_url = image_url.split("?")[0]
        image_name = image_url.split("/")[-1]
        print(f"Image Found: {image_name}")
        if image_url in imgs_downloaded:
            print("x Image Already Downloaded")
            continue
        elif image_url in img_found:
            print("x Image Already Added")
            continue
        elif image_url not in img_found:
            print(f"Image Added: {image_name}")
            img_found.append(image_url)


# Local File Function
def get_url_local(location):
    pathz = "data"
    file_name, file_extension = os.path.splitext(location)
    # if file_extension != '.html':
    #     print('Wrong file format. The program only accepts .html files.')
    #     exit()
    if file_extension == '.html':
        HTMLFile = open(location, "r")
        index = HTMLFile.read()
        s = bs(index, "html.parser")
        image_list_local(pathz, s)


# Local: Search for an a tag and append to 'urls_to_visit' list
def get_url_lst_local(location):
    HTMLFile = open(location, "r")
    index = HTMLFile.read()
    s = bs(index, "html.parser")
    for i, a in enumerate(s.find_all('a', href=True)):
        current_url = a['href']
        rut = os.path.dirname(location)
        final_url = rut + '/' + a['href']
        if final_url not in urls_to_visit and final_url + "/" not in urls_to_visit:
            urls_to_visit.append(final_url) 
        


# Strip URL
def strip_url(url):
    striped_url = ''
    # print(f"\n CU {url}\n")
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
    elif url == '':
        print()
    else:
        # print('\n\n NEEWWW')
        file_exists = exists(url)
        # print(file_exists)
        # print('\n\n NNNNEEEWWWW')
        if file_exists == True:
            local = True
            get_url_local(url)
            dwn_img_local(img_found, url, path)
            get_url_lst_local(url)
            l = level
            if recur == True and l > 1:
                while l > 1:
                    for v in range(len(urls_to_visit)):
                        # print(v)
                        get_url_local(urls_to_visit[v])
                        dwn_img_local(img_found, url, path)
                        get_url_lst_local(urls_to_visit[v])
                        l -= 1
            ## Final Results
            print()
            print("\n-- Images Downlaoded:")
            for img in imgs_downloaded:
                print(img)
            print("\n-- Pending to vist next depth:")
            for u in urls_to_visit:
                print(u)
            exit()            

    return (striped_url)


# Search for an a tag and append to 'urls_to_visit' list
def get_url_lst(url):
    rq = requests.get(url)
    soup = bs(rq.content, "html.parser")
    for i, a in enumerate(soup.find_all('a', href=True)):
        current_url = a['href']
        striped_url = strip_url(current_url)
        domain_tmp = find_domain(striped_url)
        if domain_tmp != MAIN_DOMAIN:
            print("Different Domain")
            continue
        if a['href'] not in urls_to_visit and a['href'] + "/" not in urls_to_visit:
            urls_to_visit.append(a['href'])


# Same as above but represents the list of news URLs to visit if there is another level pending
def get_url_lst_next(url):
    rq = requests.get(url)
    soup = bs(rq.content, "html.parser")
    for i, a in enumerate(soup.find_all('a', href=True)):
        current_url = a['href']
        striped_url = strip_url(current_url)
        domain_tmp = find_domain(striped_url)
        if domain_tmp != MAIN_DOMAIN:
            continue
        if a['href'] not in urls_to_visit_l and \
            a['href'] + "/" not in urls_to_visit_l and \
            a['href'] not in urls_to_visit and \
            a['href'] + "/" not in urls_to_visit and \
            a['href'] not in url_visited and \
            a['href'] + "/" not in url_visited:
            urls_to_visit_l.append(a['href'])


# Basic URL test
def check_url(url):
    str_url = strip_url(url)
    tmp_domain = find_domain(str_url)
    try:
        response = requests.head(url)
    except ValueError as ve:
        print("Oops! The link is not working.  Try again...", ve)
        exit()
    if response.status_code == 200:
        return 1
    elif response.status_code == 301:
        mmeta = response.headers['Location']
        str_url2 = strip_url(mmeta)
        tmp_domain2 = find_domain(str_url2)
        if tmp_domain == tmp_domain2:
            print("Domain OK")
            return 1
        else:
            print("Redirect to external URL. Exiting ...")
            exit()
            return 0
    else:
        return 0


# Parse CLI arguments
def cli_scan():
    # Scan the arguments in the CLI
    scan = argparse.ArgumentParser()
    scan.add_argument("URL", help="", type=str)
    scan.add_argument("-r", help="", action="store_true")
    scan.add_argument("-l", help="", type=int, nargs="?", default=5)
    scan.add_argument("-p", help="", type=str)
    return scan.parse_args()


# Main Function
if __name__ == "__main__":
    global url, recur, path, level, extentions, local

    local = False
    extentions = ["jpg", "jpeg", "gif", "bmp", "png"]
    args = cli_scan()
    url = args.URL
    if args.r == None:
        recur = False
    else: 
        recur = args.r
    level = args.l
    if args.p:
        path = str(args.p) 
    else:
        path = 'data'
    if args.p:
        path = args.p
    status = 0
    status = check_url(url)
    if status == 0:
        print("URL not found, please provide valid URL.")
        exit()
    striped_url = strip_url(url)
    
    MAIN_DOMAIN = find_domain(striped_url)
    print(MAIN_DOMAIN)


    if recur == False or level == 1:
        image_list(path, url)
        dwn_img(img_found, path)
        print(f"\nIMGs found: {img_found}\n")
        print("\nImages Downlaoded:")
        for img in imgs_downloaded:
            print(img)


    elif recur == True and level > 1:
        get_url_lst(url)
        print(f'\nRecurir {level} times')
        while level > 1:
            for u in urls_to_visit:
                print(f"-->Current URL {u}")
                if u not in url_visited:
                    get_url_lst_next(u)
                    image_list(path, u)
                    url_visited.append(u)
                elif u in url_visited:
                    print("\nx Already Vsited\n")
            dwn_img(img_found, path)
            urls_to_visit.extend(urls_to_visit_l)
            level -= 1
        ## Final Results
        print(f"\nUrl to visit: {urls_to_visit}\n")
        print(f"\nUrl from Next level of depth: {urls_to_visit_l}")
        print(f"\nUrls visited: {url_visited}")
        print("\nImages Downlaoded:")
        for img in imgs_downloaded:
            print(img)
