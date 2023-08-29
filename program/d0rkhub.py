from datetime import datetime
import tkinter as tk
from tkinter import *
root = Tk()
from tkinter import ttk
import sqlite3
import requests
from bs4 import BeautifulSoup
import time
import whois
import socket
import urllib.parse

db_name = 'd0rkhub_data'
con = sqlite3.connect(db_name)
con.execute('''CREATE TABLE IF NOT EXISTS saved_consults
               (id INTEGER PRIMARY KEY NOT NULL,
                domain VARCHAR NOT NULL,
                results VARCHAR NOT NULL);''')

class Funcs:
    def clear(self):
        self.domain_entry.delete(0, END)
        self.payloads_entry.delete(1.0,END)
        self.results_entry.delete(1.0,END) 
        self.whois_entry.delete(1.0,END)
    def request(self):
        domain = self.domain_entry.get()
        drop = self.dropdown.get()
        print(drop)
        print(domain)
    def dork_generation(self):
        if (self.dropdown.get() == 'XSS INJECTION'):
            with open('../payloads/xss.txt', 'r') as d:
                dork_file = d.read()
                xss_payloads = (dork_file)  
            self.payloads_entry.insert(tk.END,xss_payloads)
        elif (self.dropdown.get() == 'SQL INJECTION'):
            with open('../payloads/sql.txt', 'r') as d:
                dork_file = d.read()
                sql_payloads = (dork_file)
            self.payloads_entry.insert(tk.END,sql_payloads)  
        elif (self.dropdown.get() == 'HTML INJECTION'):
            with open('../payloads/html.txt', 'r') as d:
                dork_file = d.read()
                html_payloads = (dork_file)
            self.payloads_entry.insert(tk.END,html_payloads)   
        elif (self.dropdown.get() == 'DEFAULT'):
            with open('../payloads/default.txt', 'r') as d:
                dork_file = d.read()
                default_payloads = (dork_file) 
            self.payloads_entry.insert(tk.END,default_payloads) 
        else:
             self.payloads_entry.insert(tk.END,'Select the vulnerability!') 
    def consult(self):
            if (self.dropdown_con.get() != 'SQL INJECTION' and self.dropdown_con.get() != 'XSS INJECTION' and self.dropdown_con.get() != 'HTML INJECTION' and self.dropdown_con.get() != 'DEFAULT' and self.dropdown_con.get() != 'OPEN REDIRECT' ):
                self.label_error = Label(self.frame_1,text='select a vulnerability!',bg="white",fg="red")
                self.label_error.place(x=47,y=198)
                self.label_error.config(font=('Courier new',8))
                root.after(1000,self.label_error.destroy)
            elif(self.dropdown_con.get() == 'SQL INJECTION'):
                def google_search_urls(query):
                    search_query = "https://www.google.com/search?q=" + query.replace(' ', '+')

                    response = requests.get(search_query)

                    soup = BeautifulSoup(response.content, 'html.parser')

                    search_results = soup.find_all('a')
                    urls = [link['href'] for link in search_results if link['href'].startswith('/url?q=')]

                    clean_urls = [url.split('/url?q=')[1].split('&')[0] for url in urls]

                    return clean_urls
                
                with open('../dorks/sql_injection.txt', 'r') as d:
                    dork_file = d.read()
                    sql_payloads = (dork_file)  
                
                domain = self.domain_entry.get()
                search_urls = google_search_urls(sql_payloads + f' site: {domain}') 
                for line in search_urls:
                    self.consult_entry.insert(tk.END,f'{urllib.parse.unquote(line)}\n')

            elif(self.dropdown_con.get() == 'HTML INJECTION'):
                def google_search_urls(query):
                    search_query = "https://www.google.com/search?q=" + query.replace(' ', '+')

                    response = requests.get(search_query)

                    soup = BeautifulSoup(response.content, 'html.parser')

                    search_results = soup.find_all('a')
                    urls = [link['href'] for link in search_results if link['href'].startswith('/url?q=')]

                    clean_urls = [url.split('/url?q=')[1].split('&')[0] for url in urls]

                    return clean_urls
                
                with open('../dorks/html_injection.txt', 'r') as d:
                    dork_file = d.read()
                    html_payloads = (dork_file)  
                
                domain = self.domain_entry.get()
                search_urls = google_search_urls(html_payloads + f' site: {domain}') 
                for line in search_urls:
                    self.consult_entry.insert(tk.END,f'{urllib.parse.unquote(line)}\n')


            elif(self.dropdown_con.get() == 'XSS INJECTION'):
                def google_search_urls(query):
                    search_query = "https://www.google.com/search?q=" + query.replace(' ', '+')

                    response = requests.get(search_query)

                    soup = BeautifulSoup(response.content, 'html.parser')

                    search_results = soup.find_all('a')
                    urls = [link['href'] for link in search_results if link['href'].startswith('/url?q=')]

                    clean_urls = [url.split('/url?q=')[1].split('&')[0] for url in urls]

                    return clean_urls
                
                with open('../dorks/xss_dorks.txt', 'r') as d:
                    dork_file = d.read()
                    xss_payloads = (dork_file)  

                domain = self.domain_entry.get()
                search_urls = google_search_urls(xss_payloads + f' site: {domain}') 
                for line in search_urls:
                    self.consult_entry.insert(tk.END,f'{urllib.parse.unquote(line)}\n')


            elif(self.dropdown_con.get() == 'DEFAULT'):
                def google_search_urls(query):
                    search_query = "https://www.google.com/search?q=" + query.replace(' ', '+')

                    response = requests.get(search_query)

                    soup = BeautifulSoup(response.content, 'html.parser')

                    search_results = soup.find_all('a')
                    urls = [link['href'] for link in search_results if link['href'].startswith('/url?q=')]

                    clean_urls = [url.split('/url?q=')[1].split('&')[0] for url in urls]

                    return clean_urls
                
                with open('../dorks/default.txt', 'r') as d:
                    dork_file = d.read()
                    default_payloads = (dork_file)

                domain = self.domain_entry.get()
                search_urls = google_search_urls(default_payloads + f' site: {domain}') 
                for line in search_urls:
                    self.consult_entry.insert(tk.END,f'{line}\n')

            elif(self.dropdown_con.get() == 'OPEN REDIRECT'):
                def google_search_urls(query):
                    search_query = "https://www.google.com/search?q=" + query.replace(' ', '+')

                    response = requests.get(search_query)

                    soup = BeautifulSoup(response.content, 'html.parser')

                    search_results = soup.find_all('a')
                    urls = [link['href'] for link in search_results if link['href'].startswith('/url?q=')]

                    clean_urls = [url.split('/url?q=')[1].split('&')[0] for url in urls]

                    return clean_urls
                
                with open('../dorks/default.txt', 'r') as d:
                    dork_file = d.read()
                    open_redirect = (dork_file)

                domain = self.domain_entry.get()
                search_urls = google_search_urls(open_redirect + f' site: {domain}') 
                for line in search_urls:
                    self.consult_entry.insert(tk.END,f'{urllib.parse.unquote(line)}\n')
            else:
                print('ELSEEEEEE')
    def whois(self):
        domain = self.domain_entry.get()
        consult = whois.whois(domain)
        self.whois_entry.insert(tk.END,consult)
        get_ip = socket.gethostbyname(domain)
        #self.label_ip = Label(self.frame_1,text=f'IP:{get_ip}',bg="white",fg="green")
        #self.label_ip.place(relx=0.03,rely=0.7)
        #self.label_ip.config(font=('Helvetica neue',10))
        
class Application(Funcs):
    def __init__(self):
        self.root = root
        self.tela()
        self.frames()
        self.labels_frame1()
        self.nav_bar()
        self.buttons_frame1()
        self.buttons_frame2()
        self.entrys_frame2()
        self.entrys_frame1()
        root.mainloop()
    def tela(self):
        self.root.title("D0rkhub")
        self.root.resizable(False,False)
        self.root.geometry("1000x620")
        self.root.lift
        self.root.configure(background="#fcfffe")
    def frames(self):
        self.frame_1 = Frame(self.root,bd=4,bg="#ffffff",highlightbackground="#787878",highlightthickness=1)
        self.frame_1.place(relx="0.03",rely="0.06",relwidth=0.94,relheight=0.4)
       
        self.frame_2 = Frame(self.root,bd=4,bg="#ffffff",highlightbackground="#787878",highlightthickness=1)
        self.frame_2.place(relx="0.03",rely="0.5",relwidth=0.94,relheight=0.4)
    def nav_bar(self):
        #Botões nav bar
        self.btn_d0rkhub = Button(self.root,text="d0rkhub",bg="#fcfffe",fg="black", border="0")
        self.btn_d0rkhub.place(x=20,y=3)
        self.btn_d0rkhub.configure(cursor="pirate")


        self.btn_database = Button(self.root,text="database",bg="#fcfffe",fg="black", border="0")
        self.btn_database.place(x=80,y=3)
        self.btn_database.configure(cursor="pirate")
        
        self.btn_config = Button(self.root,text="config",bg="#fcfffe",fg="black", border="0")
        self.btn_config.place(x=140,y=3)
        self.btn_config.configure(cursor="pirate")


        self.btn_info = Button(self.root,text="info",bg="#fcfffe",fg="black", border="0")
        self.btn_info.place(x=190,y=3)
        self.btn_info.configure(cursor="pirate")


        self.btn_payloads = Button(self.root,text="payloads",bg="#fcfffe",fg="black", border="0")
        self.btn_payloads.place(x=225,y=3)
        self.btn_payloads.configure(cursor="pirate")


        self.btn_other = Button(self.root,text="other",bg="#fcfffe",fg="black", border="0")
        self.btn_other.place(x=290,y=3)
        self.btn_other.configure(cursor="pirate")


        self.btn_help = Button(self.root,text="help",bg="#fcfffe",fg="black", border="0")
        self.btn_help.place(x=335,y=3)
        self.btn_help.configure(cursor="pirate")


    def labels_frame1(self):
        self.label_title = Label(self.frame_1,text='D0rkhub',bg="white",fg="#333333")
        self.label_title.place(x=55,y=50)
        self.label_title.config(font=('Courier new',25))

    def entrys_frame2(self):
        self.payloads_entry = Text(self.frame_2,highlightbackground="#787878",highlightthickness=1,border="0",bg="#f4f4f4")
        self.payloads_entry.place(relx=0.02,rely=0.2)
        self.payloads_entry.configure(width=34,height=9)
        
        self.dropdown = ttk.Combobox(self.frame_2, values=['XSS INJECTION', 'SQL INJECTION', 'HTML INJECTION','DEFAULT'],width=42)
        self.dropdown.insert(0,'Payloads')
        self.dropdown.place(x=20,y=20)

        self.results_entry = Text(self.frame_2,highlightbackground="#787878",highlightthickness=1,border="0",bg="#f4f4f4")
        self.results_entry.place(relx=0.4,rely=0.2)
        self.results_entry.configure(width=64,height=9)


    def buttons_frame2(self): 
        self.btn_run = Button(self.frame_2,text="Run",bg="#5c5c5c",fg="white", border="0",width=11,command=self.consult)
        self.btn_run.place(relx=0.6,rely=0.05,height=28)
        self.btn_run.configure(cursor="pirate")

        self.btn_clean = Button(self.frame_2,text=" Clear",fg="white", border="0",width=11,highlightbackground="#ec7070",highlightthickness=1,bg="#5c5c5c", command=self.clear)
        self.btn_clean.place(relx=0.7,rely=0.05,height=28)
        self.btn_clean.configure(cursor="pirate")


        self.save_data = Button(self.frame_2,text="Save data",bg="#5c5c5c",fg="white", border="0",width=11)
        self.save_data.place(relx=0.5,rely=0.05,height=28)
        self.save_data.configure(cursor="pirate")

        self.generate_payload = Button(self.frame_2,text='generate',bg="#5c5c5c",fg="white", border="0",width=11,command=self.dork_generation)
        self.generate_payload.place(relx=0.4,rely=0.05,height=28)
        self.save_data.configure(cursor="pirate")

    def entrys_frame1(self):
        self.domain_entry = Entry(self.frame_1,highlightbackground="#787878",highlightthickness=1,border="0",bg="white")
        self.domain_entry.place(relx=0.05,rely=0.4,height=30)
        self.domain_entry.configure(width=18,font=('Arial', 12))    

        self.dropdown_con = ttk.Combobox(self.frame_1, values=['XSS INJECTION', 'SQL INJECTION', 'HTML INJECTION','OPEN REDIRECT','DEFAULT'],width=24)
        self.dropdown_con.insert(0,'Vulnerability')
        self.dropdown_con.place(x=47,y=130)

        self.consult_entry = Text(self.frame_1,highlightbackground="#787878",highlightthickness=1,border="0",bg="#f4f4f4")
        self.consult_entry.place(x=250,y=35)
        self.consult_entry.configure(width=60,height=10)

    def buttons_frame1(self):
        self.btn_try = Button(self.frame_1,text="Run",fg="white", border="0",width=8,highlightbackground="#ec7070",highlightthickness=1,bg="#65d8f9", command=self.consult)
        self.btn_try.place(x=97,y=165,height=30)
        self.btn_try.configure(cursor="pirate")

        self.save_data_ = Button(self.frame_1,text="Save data",bg="#5c5c5c",fg="#ffffff", border="0",width=10)
        self.save_data_.place(x=790,y=35,height=32)
        self.save_data_.configure(cursor="pirate",font=('Helvetica neue', 10))

        self.whois_ = Button(self.frame_1,text="Whois",bg="#5c5c5c",fg="#ffffff", border="0",width=10)
        self.whois_.place(x=790,y=78,height=32)
        self.whois_.configure(cursor="pirate",font=('Helvetica neue', 10))

        self.ip_ = Button(self.frame_1,text="Ip",bg="#5c5c5c",fg="#ffffff", border="0",width=10)
        self.ip_.place(x=790,y=123,height=32)
        self.ip_.configure(cursor="pirate",font=('Helvetica neue', 10))

        self.clear_ = Button(self.frame_1,text="Clear",bg="#5c5c5c",fg="#ffffff", border="0",width=10)
        self.clear_.place(x=790,y=167,height=32)
        self.clear_.configure(cursor="pirate",font=('Helvetica neue', 10))

Application()

