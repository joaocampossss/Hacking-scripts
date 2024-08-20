#!/usr/bin/env python3

import requests

def download(url):
    get_response = requests.get(url)
    file_name = url.split("/")[-1]
    #print(get_response.content)

    with open(file_name, "wb") as out_file:
        out_file.write(get_response.content)

download("https://buffer.com/library/content/images/size/w1200/2023/10/free-images.jpg")