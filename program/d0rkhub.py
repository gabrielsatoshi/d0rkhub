import requests
import time
from termcolor import colored

print('')
print('_________________________________________________________________________')
print(colored('       /$$  /$$$$$$            /$$       /$$   /$$           /$$      ','green'))
print(colored('      | $$ /$$$_  $$          | $$      | $$  | $$          | $$      ','green'))
print(colored('  /$$$$$$$| $$$$\ $$  /$$$$$$ | $$   /$$| $$  | $$ /$$   /$$| $$$$$$$ ','green'))
print(colored(' /$$__  $$| $$ $$ $$ /$$__  $$| $$  /$$/| $$$$$$$$| $$  | $$| $$__  $$','green'))
print(colored('| $$  | $$| $$\ $$$$| $$  \__/| $$$$$$/ | $$__  $$| $$  | $$| $$  \ $$','green'))
print(colored('| $$  | $$| $$ \ $$$| $$      | $$_  $$ | $$  | $$| $$  | $$| $$  | $$','green'))
print(colored('|  $$$$$$$|  $$$$$$/| $$      | $$ \  $$| $$  | $$|  $$$$$$/| $$$$$$$/','green'))
print(colored(' \_______/ \______/ |__/      |__/  \__/|__/  |__/ \______/ |_______/ ','green'))
print('_________________________________________________________________________')
print('')
print(colored('                           by l1nus & artico                    ','red'))
print('')

def check_response(domain):
    url = "https://" + domain
    try:
        response = requests.get(url)
        if response.status_code == 200:
            print(colored(f"Success!! :) {response}", "green"))
            time.sleep(2)
            print(colored(f'Results for "{domain}" : ', "yellow"))
        else:
            print(colored(f"Fail!! :( {response})", "red"))
    except requests.exceptions.RequestException as e:
        print(colored("domain failure!", "red"))

domain = input(colored("[+]Digite o domínio: ",'red','on_red'))
check_response(domain)

def dork_scraping():
    dork_file = "dork.txt"
    with open(dork_file, "r") as arquivo:
        content = arquivo.read()
    

dork_scraping()
