#!/usr/bin/env python3
import requests
import socket

localhost = socket.gethostbyname('localhost')
request = requests.get("http://www.google.com")

def check_localhost():
    if localhost == "127.0.0.1":
       return True

def check_connectivity():
    if request.status_code == 200:
       return True
