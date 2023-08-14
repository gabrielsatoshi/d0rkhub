import sqlite3
import requests
from bs4 import BeautifulSoup
import time
import os
os.system('color 3')

db_name = 'save_payloads'
con = sqlite3.connect(db_name)
con.execute('''CREATE TABLE IF NOT EXISTS urls
               (id INTEGER PRIMARY KEY NOT NULL,
                domain VARCHAR NOT NULL,
                results VARCHAR NOT NULL);''')

def delete_message():
    symbol = ('[!]')
    message = ('You will erase all data!.')
    print(symbol+message)
def success_message():
    symbol = ('[+]')
    message = ('Success!')
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
print('_________________________________________________________________________')
print(ascii_d0rkhub)
print('                       created by l1nu$ & artico')
print('_________________________________________________________________________')
print('')


#################INFORMATION################
warning = ('[!]')
information = ('d0rkhub is a tool that should be used for academic purposes only\nit was not created to hurt or attack any government or institution.\n')
print(warning+information)
print('https://github.com/gabrielsatoshi/d0rkhub\n\n')
#################VIEW PAYLOADS##############
number1_menu = ('[1]DorkHub')
number2_menu = ('[2]View data')
number3_menu = ('[3]Delete data')
number4_menu = ('[4]View payloads')
number5_menu = ('[5]Exit ')

print('_________________________________________________________________________')
print(number1_menu+number2_menu+number3_menu+number4_menu+number5_menu)
def main():
    os.system('color 3')
    print('')
    menu_q = int(input('~ Chose a number ~ :'))


    def google_search_urls(query):
        search_query = "https://www.google.com/search?q=" + query.replace(' ', '+')


        response = requests.get(search_query)


        soup = BeautifulSoup(response.content, 'html.parser')


        search_results = soup.find_all('a')
        urls = [link['href'] for link in search_results if link['href'].startswith('/url?q=')]


        clean_urls = [url.split('/url?q=')[1].split('&')[0] for url in urls]


        return clean_urls

    with open('payloads.txt', 'r') as d:
        dork_file = d.read()


    match  menu_q:
        case 1:
            print('')
            time.sleep(1)
            print('~ Give me a target domain ~')
            domain = input('+ ')  
            query = domain
            with open('payloads.txt', 'r') as d:
                dork_file = d.read()
            search_urls = google_search_urls(dork_file + f' site: {domain}')
            print('')
            print(f'~ Results for : "{domain}" ~')
            for line in search_urls:
                print(line,'yellow')
            print('')
            save_results = input('~ Save results? [y/n] ~')
            
            print('')
            while save_results != 'y' and save_results != 'n':
                save_results = input('Try [y/n] :')
            if(save_results == 'y'):
                os.system('color 6')
                time.sleep(2)
                con.execute(f'INSERT INTO urls (domain, results) VALUES ("{domain}", "{search_urls}")')
                con.commit()
                print(f'saved in {db_name}.')
                success_message()
                for row in con.execute('SELECT * FROM urls '):
                    print((row))
                main()
                con.close()
        case 2:
            os.system('color 2')
            time.sleep(2)
            con.execute('SELECT * FROM urls')
            if con.execute('SELECT COUNT(*) FROM urls').fetchone()[0] == 0:
                os.system('color 4')
                print('empty database.')
            else:
                os.system('color 2')
                time.sleep(2)
                for row in con.execute('SELECT * FROM urls '):
                    print(row)
            time.sleep(1)
            main()
        case 3:
            os.system('color 4')
            delete_message()
            confirm_delete = input('[-]are you sure? [y/n]')
            if (confirm_delete == 'y'):
                os.system('color 2')
                print('deleting...')
                con.execute("drop table urls")
                time.sleep(1)
                con.execute('''CREATE TABLE IF NOT EXISTS urls
                    (id INTEGER PRIMARY KEY NOT NULL,
                        domain VARCHAR NOT NULL,
                        results VARCHAR NOT NULL);''')
            else:
                os.system('color 2')
                print('canceling operation...')
                time.sleep(1)
            main()
        case 4:
            os.system('color 6')
            with open('payloads.txt', 'r') as d:
                dork_file = d.read()
                see_payloads = (dork_file)
                print('')
                print('Payloads:'+see_payloads)
                print('')
            time.sleep(1)
            main()
        case 5:
            con.close()
main()
