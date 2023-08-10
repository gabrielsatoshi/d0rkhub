################-IMPORTS-###################
import sqlite3
import requests
from bs4 import BeautifulSoup
from termcolor import colored
import time

###############DATA-CONECTION###############
db_name = 'save_payloads'
con = sqlite3.connect(db_name)
###############CREATING TABLE###############

con.execute('''CREATE TABLE IF NOT EXISTS urls
               (id INTEGER PRIMARY KEY NOT NULL,
                domain VARCHAR NOT NULL,
                results VARCHAR NOT NULL);''')

#################INTERFACE##################


ascii_d0rkhub = '''                                                        
       /$$  /$$$$$$            /$$       /$$                 /$$        
      | $$ /$$$_  $$          | $$      | $$                | $$         .--.
  /$$$$$$$| $$$$\ $$  /$$$$$$ | $$   /$$| $$$$$$$  /$$   /$$| $$$$$$$   / /  ` 
 /$$__  $$| $$ $$ $$ /$$__  $$| $$  /$$/| $$__  $$| $$  | $$| $$__  $$ | |
| $$  | $$| $$\ $$$$| $$  \__/| $$$$$$/ | $$  \ $$| $$  | $$| $$  \ $$  \ \__,
| $$  | $$| $$ \ $$$| $$      | $$_  $$ | $$  | $$| $$  | $$| $$  | $$   '--' 
|  $$$$$$$|  $$$$$$/| $$      | $$ \  $$| $$  | $$|  $$$$$$/| $$$$$$$/             
 \_______/ \______/ |__/      |__/  \__/|__/  |__/ \______/ |_______/  
'''
print('')
print(colored('_________________________________________________________________________','blue'))
print(colored(ascii_d0rkhub,'green'))
print(colored('                       created by l1nu$ & artico','yellow'))
print(colored('_________________________________________________________________________','blue'))
print('')
#################INFORMATION################
warning = (colored('[!]','red','on_red'))
information = (colored('d0rkhub is a tool that should be used for academic purposes only\nit was not created to hurt or attack any government or institution.','black','on_dark_grey'))
print(colored(warning+information))
print(colored('https://github.com/gabrielsatoshi/d0rkhub','black'))
#################VIEW PAYLOADS##############
see_dorks = str(input(colored('~ View payloads? ~ [y/n] ','red')))
def view_payloads():
    if(see_dorks == 'y'):
        with open('dorks.txt', 'r') as d:
            dork_file = d.read()
            see_payloads = (colored(dork_file,'yellow'))
            print('')
            print('Payloads:'+see_payloads)
    else:
        ('ok..')
view_payloads()

###############CAPTURING DOMAIN#############

print('')
print(colored('~ Give me a target domain ~','magenta'))
domain = input(colored('+ ','magenta'))

##############COFIGURING URL################

def google_search_urls(query):
    search_query = "https://www.google.com/search?q=" + query.replace(' ', '+')


    response = requests.get(search_query)


    soup = BeautifulSoup(response.content, 'html.parser')


    search_results = soup.find_all('a')
    urls = [link['href'] for link in search_results if link['href'].startswith('/url?q=')]


    clean_urls = [url.split('/url?q=')[1].split('&')[0] for url in urls]


    return clean_urls

##############GETTING THE PAYLOADS##########

with open('dorks.txt', 'r') as d:
    dork_file = d.read()

#########JOINING PAYLOADS TO DOMAIN#########

query = domain
search_urls = google_search_urls(dork_file + f' site: {domain}')
print('')
print(colored(f'~ Results for : "{domain}" ~','magenta'))

#########PRINTING QUERY RESULTS#############

for line in search_urls:
    print(colored(line,'yellow'))
print('')

##########QUESTION SAVE RESULTS#############

save_results = input(colored('~ Save results? ~','magenta'))
print('')
while save_results != 'y' and save_results != 'n':
    save_results = input(colored('Try [y/n] :','red'))

##########QUESTION CONDITIONAL##############

if(save_results == 'y'):
    #######SAVING THE RESULTS ON DATABANK#######
    con.execute(f'INSERT INTO urls (domain, results) VALUES ("{domain}", "{search_urls}")')
    con.commit()
    ########PRINTING DATABANK RESULTS###########
    print(colored(f'saved data in {db_name}.','green'))
    for row in con.execute('SELECT * FROM urls '):
        print(colored(row,'blue'))
    ##############CLOSING CONECTION#############
    con.close()
else:
    print('Bye..')


