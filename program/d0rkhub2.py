import tkinter as tk
from tkinter import *
root = Tk()
from tkinter import ttk
import sqlite3
import requests
from bs4 import BeautifulSoup
import time
import whois

db_name = 'd0rkhub data'
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
            with open('program/xss_dorks.txt', 'r') as d:
                dork_file = d.read()
                xss_payloads = (dork_file)  
            self.payloads_entry.insert(tk.END,xss_payloads)
        elif (self.dropdown.get() == 'SQL INJECTION'):
            with open('program/sql_injection_dorks.txt', 'r') as d:
                dork_file = d.read()
                sql_payloads = (dork_file)
            self.payloads_entry.insert(tk.END,sql_payloads)  
        elif (self.dropdown.get() == 'HTML INJECTION'):
            with open('program/html_injection.txt', 'r') as d:
                dork_file = d.read()
                html_payloads = (dork_file)
            self.payloads_entry.insert(tk.END,html_payloads)  
        elif (self.dropdown.get() == 'OPEN REDIRECT'):
            with open('program/open_redirect_dorks.txt', 'r') as d:
                dork_file = d.read()
                open_redirect_payloads = (dork_file)
            self.payloads_entry.insert(tk.END,open_redirect_payloads)  
        elif (self.dropdown.get() == 'DEFAULT'):
            with open('program/default_dorks.txt', 'r') as d:
                dork_file = d.read()
                default_payloads = (dork_file) 
            self.payloads_entry.insert(tk.END,default_payloads) 
        else:
             self.payloads_entry.insert(tk.END,'Select the vulnerability!') 
    def consult(self):
            def google_search_urls(query):
                search_query = "https://www.google.com/search?q=" + query.replace(' ', '+')


                response = requests.get(search_query)


                soup = BeautifulSoup(response.content, 'html.parser')


                search_results = soup.find_all('a')
                urls = [link['href'] for link in search_results if link['href'].startswith('/url?q=')]


                clean_urls = [url.split('/url?q=')[1].split('&')[0] for url in urls]


                return clean_urls
            domain = self.domain_entry.get()
            search_urls = google_search_urls('intitle:index of ' + f' site: {domain}') 
            print('')
            print(f'~ Results for : "{domain}" ~')
            for line in search_urls:
                self.results_entry.insert(tk.END,line)
    def whois(self):
        domain = self.domain_entry.get()
        consult = whois.whois(domain)
        self.whois_entry.insert(tk.END,consult)
    
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
        self.root.geometry("800x520")
        self.root.lift
        self.root.configure(background="#dddddd")
    def frames(self):
        self.frame_1 = Frame(self.root,bd=4,bg="#ffffff",highlightbackground="#787878",highlightthickness=1)
        self.frame_1.place(relx="0.03",rely="0.06",relwidth=0.94,relheight=0.4)
       
        self.frame_2 = Frame(self.root,bd=4,bg="#ffffff",highlightbackground="#787878",highlightthickness=1)
        self.frame_2.place(relx="0.03",rely="0.5",relwidth=0.94,relheight=0.4)
    def nav_bar(self):
        #Botões nav bar
        self.btn_d0rkhub = Button(self.root,text="d0rkhub",bg="#dddddd",fg="black", border="0")
        self.btn_d0rkhub.place(x=20,y=3)
        self.btn_d0rkhub.configure(cursor="pirate")


        self.btn_database = Button(self.root,text="database",bg="#dddddd",fg="black", border="0")
        self.btn_database.place(x=80,y=3)
        self.btn_database.configure(cursor="pirate")
        
        self.btn_config = Button(self.root,text="config",bg="#dddddd",fg="black", border="0")
        self.btn_config.place(x=140,y=3)
        self.btn_config.configure(cursor="pirate")


        self.btn_info = Button(self.root,text="info",bg="#dddddd",fg="black", border="0")
        self.btn_info.place(x=190,y=3)
        self.btn_info.configure(cursor="pirate")


        self.btn_payloads = Button(self.root,text="payloads",bg="#dddddd",fg="black", border="0")
        self.btn_payloads.place(x=225,y=3)
        self.btn_payloads.configure(cursor="pirate")


        self.btn_other = Button(self.root,text="other",bg="#dddddd",fg="black", border="0")
        self.btn_other.place(x=290,y=3)
        self.btn_other.configure(cursor="pirate")


        self.btn_help = Button(self.root,text="help",bg="#dddddd",fg="black", border="0")
        self.btn_help.place(x=335,y=3)
        self.btn_help.configure(cursor="pirate")


    def labels_frame1(self):
        self.label_title = Label(self.frame_1,text='The D0rkhub',bg="white",fg="#333333")
        self.label_title.place(relx=0.03,rely=0.05)
        self.label_title.config(font=('Helvetica neue',15))

        self.label_domain = Label(self.frame_1,text='target domain ',bg="white",fg="#333333")
        self.label_domain.place(relx=0.03,rely=0.2,height=45)
        self.label_domain.config(font=('Helvetica neue',8))
    def entrys_frame2(self):
        self.payloads_entry = Text(self.frame_2,highlightbackground="#787878",highlightthickness=1,border="0",bg="#dddddd")
        self.payloads_entry.place(relx=0.02,rely=0.2)
        self.payloads_entry.configure(width=34,height=9)
        
        self.dropdown = ttk.Combobox(self.frame_2, values=['XSS INJECTION', 'SQL INJECTION', 'HTML INJECTION','OPEN REDIRECT','DEFAULT'],width=42)
        self.dropdown.insert(0,'Vulnerability')
        self.dropdown.place(relx=0.02,rely=0.05)

        self.results_entry = Text(self.frame_2,highlightbackground="#787878",highlightthickness=1,border="0",bg="#dddddd")
        self.results_entry.place(relx=0.4,rely=0.2)
        self.results_entry.configure(width=53,height=9)


    def buttons_frame2(self): 
        self.btn_run = Button(self.frame_2,text="Run",bg="#5bc0de",fg="black", border="0",width=9,command=self.consult)
        self.btn_run.place(relx=0.6,rely=0.05)
        self.btn_run.configure(cursor="pirate")

        self.btn_clean = Button(self.frame_2,text=" Clear",fg="black", border="0",width=7,highlightbackground="#ec7070",highlightthickness=1,bg="#f87159", command=self.clear)
        self.btn_clean.place(relx=0.7,rely=0.05)
        self.btn_clean.configure(cursor="pirate")


        self.save_data = Button(self.frame_2,text="Save data",bg="#66d76f",fg="black", border="0",width=9)
        self.save_data.place(relx=0.5,rely=0.05)
        self.save_data.configure(cursor="pirate")

        self.generate_payload = Button(self.frame_2,text='generate',bg="#F8FB8E",fg="black", border="0",width=9,command=self.dork_generation)
        self.generate_payload.place(relx=0.4,rely=0.05)
        self.save_data.configure(cursor="pirate")

    def entrys_frame1(self):
        self.domain_entry = Entry(self.frame_1,highlightbackground="#787878",highlightthickness=1,border="0",bg="#dddddd")
        self.domain_entry.place(relx=0.03,rely=0.4,height=40)
        self.domain_entry.configure(width=40,font=('Arial', 10))

        self.whois_entry = Text(self.frame_1,highlightbackground="#787878",highlightthickness=1,border="0",bg="#dddddd")
        self.whois_entry.place(relx=0.5,rely=0.1)
        self.whois_entry.configure(width=43,height=10)

    def buttons_frame1(self):
        self.btn_try = Button(self.frame_1,text=" Try",fg="black", border="0",width=7,highlightbackground="#ec7070",highlightthickness=1,bg="#7975FA", command=self.whois)
        self.btn_try.place(relx=0.4,rely=0.4,height=40)
        self.btn_try.configure(cursor="pirate")

Application()

