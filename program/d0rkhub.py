import requests
import time
from termcolor import colored
ascii_d0rkhub = '''
       /$$  /$$$$$$            /$$       /$$                 /$$      
      | $$ /$$$_  $$          | $$      | $$                | $$      
  /$$$$$$$| $$$$\ $$  /$$$$$$ | $$   /$$| $$$$$$$  /$$   /$$| $$$$$$$ 
 /$$__  $$| $$ $$ $$ /$$__  $$| $$  /$$/| $$__  $$| $$  | $$| $$__  $$
| $$  | $$| $$\ $$$$| $$  \__/| $$$$$$/ | $$  \ $$| $$  | $$| $$  \ $$
| $$  | $$| $$ \ $$$| $$      | $$_  $$ | $$  | $$| $$  | $$| $$  | $$
|  $$$$$$$|  $$$$$$/| $$      | $$ \  $$| $$  | $$|  $$$$$$/| $$$$$$$/
 \_______/ \______/ |__/      |__/  \__/|__/  |__/ \______/ |_______/ 
'''
print('')
print('_________________________________________________________________________')
print(ascii_d0rkhub)
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
