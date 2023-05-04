ALIAS - open /sgoinfre/Perso/yzisis-p/work/Visual\ Studio\ Code.app

The script normalizer is installed in '/Users/yzisis-p/Library/Python/3.7/bin' which is not on PATH.

# 0 Parse the commands from the CLI
# argparse  

# To use the
# import requests
# python -m pip install requests
# 1 Check the URL exist

# 2 Check the URL is not empty

# 3 Get the content

# 4 Check if there are any URLs ending on .jpg .jpeg .png .bmp

# https://www.actualno.com/politics/borisov-horata-ni-kazaha-bez-gerb-ne-moje-bez-pp-db-syshto-kanim-vsichki-partii-video-news_1943109.html

# Example tests
spider -r https://www.actualno.com/politics/borisov-horata-ni-kazaha-bez-gerb-ne-moje-bez-pp-db-syshto-kanim-vsichki-partii-video-news_1943109.html
spider -r -l 2 https://www.actualno.com/politics/borisov-horata-ni-kazaha-bez-gerb-ne-moje-bez-pp-db-syshto-kanim-vsichki-partii-video-news_1943109.html
spider -path datatmp https://www.actualno.com/politics/borisov-horata-ni-kazaha-bez-gerb-ne-moje-bez-pp-db-syshto-kanim-vsichki-partii-video-news_1943109.html

Check the status of the url 

import requests

r = requests.get('https://www.actualno.com/politics/borisov-horata-ni-kazaha-bez-gerb-ne-moje-bez-pp-db-syshto-kanim-vsichki-partii-video-news_1943109.html')
r.status_code

# Save Image
import shutil # save img locally

file_name = new.txt

if res.status_code == 200:
    with open(file_name,'wb') as f:
        shutil.copyfileobj(res.raw, f)
    print('Image sucessfully Downloaded: ',file_name)
else:
    print('Image Couldn\'t be retrieved')

-

# Take out filename out of entire URL
filename = image_url.split("/")[-1]


# Adding information about user agent for use with request library !
opener=urllib.request.build_opener()
opener.addheaders=[('User-Agent','Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/36.0.1941.0 Safari/537.36')]
urllib.request.install_opener(opener)


# Urllib Module
# The standard Python library for accessing websites via your program is urllib. It is also used by the requests module.

# Through urllib, we can do a variety of things: access websites, download data, parse data, send GET and, POST requests.

# We can download our image using just a few lines of code:


# importing required modules
import urllib.request

# setting filename and image URL
filename = 'sunshine_dog.jpg'
image_url = "https://cdn.pixabay.com/photo/2020/02/06/09/39/summer-4823612_960_720.jpg"

# calling urlretrieve function to get resource
urllib.request.urlretrieve(image_url, filename)

## Importing Necessary Modules
import requests # to get image from the web
import shutil # to save it locally

## Set up the image URL and filename
image_url = "https://cdn.pixabay.com/photo/2020/02/06/09/39/summer-4823612_960_720.jpg"
filename = image_url.split("/")[-1]

# Open the url image, set stream to True, this will return the stream content.
r = requests.get(image_url, stream = True)

# Check if the image was retrieved successfully
if r.status_code == 200:
    # Set decode_content value to True, otherwise the downloaded image file's size will be zero.
    r.raw.decode_content = True
    
    # Open a local file with wb ( write binary ) permission.
    with open(filename,'wb') as f:
        shutil.copyfileobj(r.raw, f)
        
    print('Image sucessfully Downloaded: ',filename)
else:
    print('Image Couldn\'t be retreived')



