from re import T
import httpx
import json
import string
import os
import ctypes
import json
import datetime
from itertools import cycle
import time 
import threading
import json
import re
from bs4 import BeautifulSoup
import requests
import httpx
from hcapbypass import bypass
import random

list_success = 0
list_error = 0
ThreadBB = 0
ThreadAA = int(input("Thread (Ex. 100): "))

os.system('')
clear = lambda: os.system('cls')
ctypes.windll.kernel32.SetConsoleTitleW(f"DISCORD ACCOUNT REGISTER [SUCCESS: {list_success} ERROR: {list_error}]")
clear()

class bcolors:
    BLACK = '\033[30m'
    RED = '\033[31m'
    GREEN = '\033[32m'
    YELLOW = '\033[33m'
    BLUE = '\033[34m'
    MAGENTA = '\033[35m'
    CYAN = '\033[36m'
    WHITE = '\033[37m'
    UNDERLINE = '\033[4m'
    RESET = '\033[0m'

usernames = []

with open('usernames.txt','r+', encoding='utf-8') as usernamefile:
	logins = usernamefile.read().splitlines()

with open('proxies.txt','r+', encoding='utf-8') as proxyfile:
    ProxyPool = cycle(proxyfile.read().splitlines())

for user in logins:
    usernames.append(user)

def random_char(y):
    return ''.join(random.choice(string.ascii_letters) for x in range(y))

def register(invite_linka):
    global ThreadBB
    global list_success
    global list_error
    ThreadBB +=1
    try:
        while True:
            currentproxy = next(ProxyPool)
            captchakey = bypass("f5561ba9-8f1e-40ca-9b5b-a0b3f719ef34", "discord.com", proxy=currentproxy)
            if captchakey == False:
                continue
            else:
                break

        print(f"{bcolors.CYAN}[!] Bypassed captcha! ({captchakey[:30]}...){bcolors.RESET}")

        header3 = {

            "Host": "discord.com",
            "Connection": "keep-alive",
            "sec-ch-ua": '"Chromium";v="92", " Not A;Brand";v="99", "Google Chrome";v="92"',
            "X-Super-Properties": "eyJvcyI6Ik1hYyBPUyBYIiwiYnJvd3NlciI6IkNocm9tZSIsImRldmljZSI6IiIsInN5c3RlbV9sb2NhbGUiOiJlbi1VUyIsImJyb3dzZXJfdXNlcl9hZ2VudCI6Ik1vemlsbGEvNS4wIChNYWNpbnRvc2g7IEludGVsIE1hYyBPUyBYIDEwXzE1XzcpIEFwcGxlV2ViS2l0LzUzNy4zNiAoS0hUTUwsIGxpa2UgR2Vja28pIENocm9tZS85Mi4wLjQ1MTUuMTMxIFNhZmFyaS81MzcuMzYiLCJicm93c2VyX3ZlcnNpb24iOiI5Mi4wLjQ1MTUuMTMxIiwib3NfdmVyc2lvbiI6IjEwLjE1LjciLCJyZWZlcnJlciI6IiIsInJlZmVycmluZ19kb21haW4iOiIiLCJyZWZlcnJlcl9jdXJyZW50IjoiIiwicmVmZXJyaW5nX2RvbWFpbl9jdXJyZW50IjoiIiwicmVsZWFzZV9jaGFubmVsIjoic3RhYmxlIiwiY2xpZW50X2J1aWxkX251bWJlciI6OTI3OTIsImNsaWVudF9ldmVudF9zb3VyY2UiOm51bGx9",
            "X-Fingerprint": "",
            "Accept-Language": "en-US",
            "sec-ch-ua-mobile": "?0",
            "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/92.0.4515.131 Safari/537.36",
            "Content-Type": "application/json",
            "Authorization": "undefined",
            "Accept": "*/*",
            "Origin": "https://discord.com",
            "Sec-Fetch-Site": "same-origin",
            "Sec-Fetch-Mode": "cors",
            "Sec-Fetch-Dest": "empty",
            "Referer": "https://discord.com/register",
            "X-Debug-Options": "bugReporterEnabled",
            "Accept-Encoding": "gzip, deflate, br",
            "Cookie": "OptanonConsent=version=6.17.0; locale=th"

        }


        email = random_char(10) + "@" + random_char(10) + ".com"
        username = random.choice(usernames)
        password =  random_char(10)
        payload = {"fingerprint": "",
                    "username": username,
                    "invite": str(invite_linka),
                    "consent": "true",
                    "gift_code_sku_id": "",
                    "captcha_key": captchakey,
                    }
    except Exception as e:
        list_error +=1

    while True:
        try:
            registerreq = httpx.post("https://discord.com/api/v9/auth/register", proxies={"https://" : "http://"+ str(next(ProxyPool))}, headers=header3, json=payload, timeout=15)
            if registerreq.status_code == 201:
                token = json.loads(registerreq.text)
                token2 = token['token']
                f1 = open("./output/token.txt", "a+")
                f1.write(f"{token2}\n")
                f1.close()
                time = datetime.datetime.now().strftime("%H:%M:%S")
                print(f"{bcolors.GREEN}[{str(time)}] TOKEN : {token2}{bcolors.RESET}")
                list_success +=1
                break
            elif registerreq.status_code == 400:
                break
            else:
                list_error +=1
                continue
        except Exception as e:
            list_error +=1
            continue

    ctypes.windll.kernel32.SetConsoleTitleW(f"DISCORD ACCOUNT REGISTER [SUCCESS: {list_success} ERROR: {list_error}]") 
    ThreadBB -= 1


if __name__ == '__main__':
    invite_linka = input("Invite Code (Example: DuSPb6fa): ")
    while True:
        if ThreadBB < ThreadAA:
            t = threading.Thread(target=register, args=[invite_linka])
            t.start()
            time.sleep(0.001)
