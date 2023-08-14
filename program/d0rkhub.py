import sqlite3
import requests
from bs4 import BeautifulSoup
from termcolor import colored
import time

db_name = 'save_payloads'
con = sqlite3.connect(db_name)
con.execute('''CREATE TABLE IF NOT EXISTS urls
               (id INTEGER PRIMARY KEY NOT NULL,
                domain VARCHAR NOT NULL,
                results VARCHAR NOT NULL);''')

def delete_message():
    symbol = colored('[!]','black','on_red')
    message = colored('You will erase all data!.','black','on_yellow')
    print(symbol+message)
def success_message():
    symbol = colored('[+]','black','on_light_grey')
    message = colored('Success!','black','on_green')
    print(symbol+message)

error = '[?]'
success = '[+]'

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
voidstring2 = '|'
information = (colored('d0rkhub is a tool that should be used for academic purposes only\nit was not created to hurt or attack any government or institution.','black','on_dark_grey'))
print(colored(warning+information))
print(colored('https://github.com/gabrielsatoshi/d0rkhub','black'))
#################VIEW PAYLOADS##############
number1_menu = colored('[1]DorkHub','black','on_yellow')
number2_menu = colored('[2]View data','black','on_cyan')
number3_menu = colored('[3]Delete data','black','on_red')
number4_menu = colored('[4]View payloads','black','on_blue')
number5_menu = colored('[5]Exit ','black','on_dark_grey')
voidstring = '|'

print(number1_menu+number2_menu+number3_menu+number4_menu+number5_menu+voidstring)
def main():
    menu_q = int(input(colored('~ Chose a number ~ :','magenta')))


    def google_search_urls(query):
        search_query = "https://www.google.com/search?q=" + query.replace(' ', '+')


        response = requests.get(search_query)


        soup = BeautifulSoup(response.content, 'html.parser')


        search_results = soup.find_all('a')
        urls = [link['href'] for link in search_results if link['href'].startswith('/url?q=')]


        clean_urls = [url.split('/url?q=')[1].split('&')[0] for url in urls]


        return clean_urls

    with open('program/payloads.txt', 'r') as d:
        dork_file = d.read()


    match  menu_q:
        case 1:
            print('')
            time.sleep(1)
            print(colored('~ Give me a target domain ~','magenta'))
            domain = input(colored('+ ','magenta'))   
            query = domain
            with open('program/payloads.txt', 'r') as d:
                dork_file = d.read()
            search_urls = google_search_urls(dork_file + f' site: {domain}')
            print('')
            print(colored(f'~ Results for : "{domain}" ~','magenta'))
            for line in search_urls:
                print(colored(line,'yellow'))
            print('')
            save_results = input(colored('~ Save results? [y/n] ~','magenta'))
            print('')
            while save_results != 'y' and save_results != 'n':
                save_results = input(colored('Try [y/n] :','red'))
            if(save_results == 'y'):
                con.execute(f'INSERT INTO urls (domain, results) VALUES ("{domain}", "{search_urls}")')
                con.commit()
                print(colored(f'saved in {db_name}.','green'))
                success_message()
                for row in con.execute('SELECT * FROM urls '):
                    print(colored(row,'blue'))
                main()
                con.close()
        case 2:
            con.execute('SELECT * FROM urls')
            if con.execute('SELECT COUNT(*) FROM urls').fetchone()[0] == 0:
                print(colored('empty database.','red'))
            else:
                for row in con.execute('SELECT * FROM urls '):
                    print(colored(row,'blue'))
            time.sleep(1)
            main()
        case 3:
            delete_message()
            confirm_delete = input(colored('[-]are you sure? [y/n]','black','on_yellow'))
            if (confirm_delete == 'y'):
                print(colored('deleting...','red'))
                con.execute("drop table urls")
                time.sleep(1)
                con.execute('''CREATE TABLE IF NOT EXISTS urls
                    (id INTEGER PRIMARY KEY NOT NULL,
                        domain VARCHAR NOT NULL,
                        results VARCHAR NOT NULL);''')
            else:
                print(colored('canceling operation...','green'))
                time.sleep(1)
            main()
        case 4:
            with open('program/payloads.txt', 'r') as d:
                dork_file = d.read()
                see_payloads = (colored(dork_file,'yellow'))
                print('')
                print('Payloads:'+see_payloads)
                print('')
            time.sleep(1)
            main()
        case 5:
            con.close()
main()
