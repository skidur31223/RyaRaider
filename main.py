from datetime import datetime
import os
import fade
from colorama import init, Back, Fore, Style
import shutil
import requests
import datetime
import ctypes
import Options
init(autoreset=True)
w = Fore.WHITE
bk = Fore.BLACK
g = Fore.LIGHTGREEN_EX
y = Fore.LIGHTYELLOW_EX
c = Fore.CYAN
r = Fore.LIGHTRED_EX
b = Fore.BLUE
lb = Fore.LIGHTBLUE_EX
def print_centre(s):
    print(s.center(shutil.get_terminal_size().columns))   
class Rya:
    g = Fore.LIGHTWHITE_EX
    r = Fore.LIGHTRED_EX
    green = Fore.LIGHTGREEN_EX
    cyan = Fore.LIGHTCYAN_EX
    def save_tokens(file_path):
        valid_tokens = 0
        tokens_valid = []
        tokens=open(file_path,"r").read().splitlines()
        for token in tokens:
            if Rya.check_token(token):
                valid_tokens += 1
                tokens_valid.append(token)
        with open(file_path, 'w+') as f: f.truncate(0)
        with open(file_path, 'a+') as f:
            for token in tokens_valid:
                f.write(token + "\n")
    def check_token(touken):
        headers = {"authorization": touken}
        try:
           
            response = requests.get("https://discord.com/api/v9/users/@me/library", headers=headers)
            dn = touken.split("."); nn = dn[0]
            if response.status_code == 200:
                print(f"  {Rya.g}[{datetime.datetime.now().strftime(f'{Rya.cyan}%H:%M:%S{Rya.g}')}] {Rya.g}[{Rya.green}Success{Rya.g}] {nn}**")
                return True
            elif response.status_code == 403:
                print(f"  {Rya.g}[{datetime.datetime.now().strftime(f'{Rya.cyan}%H:%M:%S{Rya.g}')}] {Rya.g}[{Fore.LIGHTYELLOW_EX}Locked{Rya.g}] {nn}**")
                return False
            else:
                print(f"  {Rya.g}[{datetime.datetime.now().strftime(f'{Rya.cyan}%H:%M:%S{Rya.g}')}] {Rya.g}[{Rya.r}Invalid{Rya.g}] {nn}**")
                return False
        except:
            pass
tokens=open("input/tokens.txt","r").read().splitlines()
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
                                                     ░ ░               """
def set_title(title):
    ctypes.windll.kernel32.SetConsoleTitleW(title)
def MainMenu():
    os.system("cls")
    set_title(">                                                                                                RYA v1.1 | https://ryaontop.store/ | made by skidur31223")
    print(fade.greenblue(ascii))
    print(f"                {w}[{Fore.LIGHTRED_EX}»{w}] Tokens: {Fore.LIGHTRED_EX}{len(tokens)}")
    print("")
    print(f"                {w}[{r}01{w}] Joiner")
    print(f"                {w}[{r}02{w}] Leaver                                                   ┏━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┓")
    print(f"                {w}[{r}03{w}] Spammer                                                  ┃ {y}Rya is the best discord raider {w}┃")
    print(f"                {w}[{r}04{w}] Emoji Spammer                                            ┃      {y}with 13 {g}BEST {y}options {w}     ┃")
    print(f"                {w}[{r}05{w}] Fake Typing                                              ┗━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┛")
    print(f"                {w}[{r}06{w}] VC Spammer                                       ┏━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┓")                                     
    print(f"                {w}[{r}07{w}] Friend Spammer                                   ┃ {y}Name: {g}Rya{y} {w}{y}Version: {g}1.1{y}{w} {y}Author: {g}skidur31223{w} ┃")
    print(f"                {w}[{r}08{w}] Click Button                                     ┃ {y}Discord: {g}https://discord.gg/hackingraid{w} ┃")
    print(f"                {w}[{r}09{w}] Rules Accepter                                   ┗━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┛")
    print(f"                {w}[{r}10{w}] Bio Text Changer                                 ")
    print(f"                {w}[{r}11{w}] Token Checker")
    print(f"                {w}[{r}12{w}] Thread Spammer")
    print(f"                {w}[{r}13{w}] Nick Changer")
    print(f"                {w}[{r}14{w}] Exit")
    option = input(f"  {w}[{r}>{w}] {w}Choice: {g}")
    print(f"{w}")
    if option == "01" or option == "1":
        # Joiner
        Options.Joiner()
        input(f"")
        MainMenu()
    if option == "02" or option == "2":
        # Leaver
        Options.Leaver()
        input(f"")
        MainMenu()
    if option == "03" or option == "3":
        # Spammer
        Options.Spammer()
        input(f"")
        MainMenu()
    if option == "04" or option == "4":
        # Emoji Spammer
        Options.EmojiReaction()
        input(f"")
        MainMenu()
    if option == "05" or option == "5":
        # Fake Typing
        Options.FakeTyping()
        input(f"")
        MainMenu()
    if option == "06" or option == "6":
        # VC Spammer
        Options.VCSpammer()
        input(f"")
        MainMenu()
    if option == "07" or option == "7":
        # Friend Spammer
        Options.FriendSpammer()
        input(f"")
        MainMenu()
    if option == "08" or option == "8":
        # Click Button
        Options.button_clicker()
        input(f"")
        MainMenu()
    if option == "09" or option == "9":
        # Rules Accepter
        Options.accept_rules()
        input(f"")
        MainMenu()
    if option == "10":
        # Bio Text Changer
        Options.bio_changer()
        input(f"")
        MainMenu()
    if option == "11":
        # Token Checker
        Rya.save_tokens("input/tokens.txt")
        input(f"")
        MainMenu()
    if option == "12":
        # Thread Spammer
        Options.thread_spammer()
        input(f"")
        MainMenu()
    if option == "13":
        # Nick Changer
        Options.nickchanger()
        input(f"")
        MainMenu()
    if option == "14":
        exit()
MainMenu()