import requests
from bs4 import BeautifulSoup
from termcolor import colored
import time

#       enjoy :)

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
print(colored('_________________________________________________________________________','blue'))
print(colored(ascii_d0rkhub,'green'))
print(colored('                       created by l1nu$ & artico','yellow'))
print(colored('_________________________________________________________________________','blue'))
print('')

see_dorks = str(input(colored('~ View payloads? ~ [y/n] ','red')))
if(see_dorks == 'y'):
    with open('dorks.txt', 'r') as d:
        dork_file = d.read()
        see_payloads = (colored(dork_file,'yellow'))
        print('')
        print('Payloads:'+see_payloads)
else:
    ('ok..')
print('')
print(colored('~ Give me a target domain ~','magenta'))
domain = input(colored('+ ','magenta'))


def google_search_urls(query):
    search_query = "https://www.google.com/search?q=" + query.replace(' ', '+')


    response = requests.get(search_query)


    soup = BeautifulSoup(response.content, 'html.parser')


    search_results = soup.find_all('a')
    urls = [link['href'] for link in search_results if link['href'].startswith('/url?q=')]


    clean_urls = [url.split('/url?q=')[1].split('&')[0] for url in urls]


    return clean_urls

with open('dorks.txt', 'r') as d:
    dork_file = d.read()

query = domain

search_urls = google_search_urls(dork_file + f' site: {domain}')
print('')
print(colored(f'Results for : "{domain}"','magenta'))

for line in search_urls:
    print(colored(line,'yellow'))

print('')

