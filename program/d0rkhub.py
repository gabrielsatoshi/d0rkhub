#Importando todos os módulos necessários.

import tkinter as tk
from tkinter import *
from tkinter import ttk
import sqlite3
import requests
from bs4 import BeautifulSoup
import whois
import socket
import urllib.parse

#Definindo janela root.

root = Tk()

#Criando o banco de dados.

db_name = 'banco_dorkhub'
con = sqlite3.connect(db_name)
con.execute('''CREATE TABLE IF NOT EXISTS saved_consults
            (id INTEGER PRIMARY KEY NOT NULL,
                domain VARCHAR NOT NULL,
                results VARCHAR NOT NULL);''')

# Definindo a classe de funcionalidades.
class Funcs:

    def limpar_consult(self):
        self.consult_entry.delete(1.0,END)

    def banco(self):
        self.frame_3.destroy() 
        self.frame_3 = Frame(self.root,bd=4,bg="black",highlightbackground="#787878",highlightthickness=1)
        self.frame_3.place(relx="0.03",y="70",relwidth=0.94,relheight=0.4)

        
        self.btn_try = Button(self.frame_3,text="executar",fg="white", border="0",width=8,highlightbackground="#ec7070",highlightthickness=1,bg="#ff5a5a", command=self.consult)
        self.btn_try.place(x=537,rely=0.1,height=25)
        self.btn_try.configure(cursor="pirate",font=('Helvetica neue', 10))

    def painel(self):
        self.frame_3.destroy()

    #Funcionalidade de limpar campos.
    def clear(self):
        self.domain_entry.delete(0, END)
        self.payloads_entry.delete(1.0,END)
        self.results_entry.delete(1.0,END) 
        self.consult_entry.delete(1.0,END)
    
    #Capturando campos.
    def request(self):
        domain = self.domain_entry.get()
        drop = self.dropdown.get()


    #Criação dos payloads para cada vulnerabilidade.
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
    
    #Criação das consultas por sites, utilizando parametro por vulnerabilidade.
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
                
                with open('../google_dorks/sqli.txt', 'r') as d:
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
                
                with open('../google_dorks/htmli.txt', 'r') as d:
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
                
                with open('../google_dorks/xss.txt', 'r') as d:
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
                
                with open('../google_dorks/default.txt', 'r') as d:
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
                
                with open('../google_dorks/default.txt', 'r') as d:
                    dork_file = d.read()
                    open_redirect = (dork_file)

                domain = self.domain_entry.get()
                search_urls = google_search_urls(open_redirect + f' site: {domain}') 
                for line in search_urls:
                    self.consult_entry.insert(tk.END,f'{urllib.parse.unquote(line)}\n')
            else:
                print('ELSEEEEEE')
    
    #Realizando consulta no Whois.
    def whois(self):
        domain = self.domain_entry.get()
        consult = getinformation.a()
        self.payloads_entry(tk.END,consult)

# Definindo a classe aplication.
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
    
    #Configurações da tela
    def tela(self):
        self.root.title("D0rkhub")
        self.root.resizable(False,False)
        self.root.geometry("1068x650")
        self.root.lift
        self.root.configure(background="#fcfffe")
    
    #Separação da tela.
    def frames(self):
        self.frame_1 = Frame(self.root,bd=4,bg="#ffffff",highlightbackground="#787878",highlightthickness=1)
        self.frame_1.place(relx="0.03",rely="0.09",relwidth=0.94,relheight=0.4)
       
        self.frame_2 = Frame(self.root,bd=4,bg="#ffffff",highlightbackground="#787878",highlightthickness=1)
        self.frame_2.place(relx="0.03",y="345",relwidth=0.94,relheight=0.4)


    # Botões da barra de navegação.
    def nav_bar(self):
    
        self.btn_d0rkhub = Button(self.root,text="Site",bg="#fcfffe",fg="black", border="0")
        self.btn_d0rkhub.place(x=28,y=15)
        self.btn_d0rkhub.configure(cursor="pirate")
        
        self.btn_config = Button(self.root,text="Github",bg="#fcfffe",fg="black", border="0")
        self.btn_config.place(x=60,y=15)
        self.btn_config.configure(cursor="pirate")

        self.btn_info = Button(self.root,text="Configurações",bg="#fcfffe",fg="black", border="0")
        self.btn_info.place(x=113,y=15)
        self.btn_info.configure(cursor="pirate")


    #Textos do primeiro frame
    def labels_frame1(self):
        self.label_url = Label(self.frame_1,text='url',bg="white",fg="#333333")
        self.label_url.place(relx=0.03,rely=0.1)
        self.label_url.config(font=('Helvetica neue',10))

    #Campos de entrada do segundo frame
    def entrys_frame2(self):
        self.payloads_entry = Text(self.frame_2,highlightbackground="#787878",highlightthickness=1,border="0",bg="#f4f4f4")
        self.payloads_entry.place(x=50,y=70)
        self.payloads_entry.configure(width=107,height=9)
        
        self.dropdown = ttk.Combobox(self.frame_2, values=['XSS INJECTION', 'SQL INJECTION', 'HTML INJECTION','DEFAULT'],width=42)
        self.dropdown.insert(0,'Payloads')
        self.dropdown.place(x=50,y=20,height=25)


    #Botões do segundo frame
    def buttons_frame2(self): 

        self.btn_clean = Button(self.frame_2,text="limpar",fg="white", border="0",width=11,highlightbackground="#ec7070",highlightthickness=1,bg="#ff5a5a", command=self.clear)
        self.btn_clean.place(x=615,y=20,height=25)
        self.btn_clean.configure(cursor="pirate")

        self.btn_copiar_payload = Button(self.frame_2,text="copiar",fg="white", border="0",width=11,highlightbackground="#ec7070",highlightthickness=1,bg="#ff5a5a", command=self.clear)
        self.btn_copiar_payload.place(x=490,y=20,height=25)
        self.btn_copiar_payload.configure(cursor="pirate")

        self.generate_payload = Button(self.frame_2,text='gerar',bg="#ff5a5a",fg="white", border="0",width=11,command=self.dork_generation)
        self.generate_payload.place(x=370,y=20,height=25)


    #Campos de entrada primeiro frame.
    def entrys_frame1(self):
        self.domain_entry = Entry(self.frame_1,highlightbackground="#787878",highlightthickness=1,border="0",bg="white")
        self.domain_entry.place(relx=0.05,rely=0.1,height=25)
        self.domain_entry.configure(width=30,font=('Arial', 9))    

        self.dropdown_con = ttk.Combobox(self.frame_1, values=['XSS INJECTION', 'SQL INJECTION', 'HTML INJECTION','OPEN REDIRECT','DEFAULT'],width=34)
        self.dropdown_con.insert(0,'Vulnerability')
        self.dropdown_con.place(x=290,rely=0.1,height=25)

        self.consult_entry = Text(self.frame_1,highlightbackground="#787878",highlightthickness=1,border="0",bg="#f4f4f4")
        self.consult_entry.place(x=50,y=70)
        self.consult_entry.configure(width=107,height=10)

    #Botões primeiro frame
    def buttons_frame1(self):        
        self.btn_painel = Button(self.root,text="Painel",fg="#3b3b3b", border="1",width=14,highlightbackground="#dddddd",highlightthickness=2,bg="#f4f4f4", command=self.painel)
        self.btn_painel.place(x=32,y=45,height=25)
        self.btn_painel.configure(cursor="pirate")

        self.btn_banco = Button(self.root,text="Banco",fg="#3b3b3b", border="1",width=13,highlightbackground="#dddddd",highlightthickness=2,bg="#f4f4f4", command=self.banco)
        self.btn_banco.place(x=138,y=45,height=25)
        self.btn_banco.configure(cursor="pirate")

        self.btn_payloads = Button(self.root,text="Payloads",fg="#3b3b3b", border="1",width=13,highlightbackground="#dddddd",highlightthickness=2,bg="#f4f4f4", command=self.consult)
        self.btn_payloads.place(x=235,y=45,height=25)
        self.btn_payloads.configure(cursor="pirate")

        self.btn_comparador = Button(self.root,text="Comparador",fg="#3b3b3b", border="1",width=13,highlightbackground="#dddddd",highlightthickness=2,bg="#f4f4f4", command=self.consult)
        self.btn_comparador.place(x=335,y=45,height=25)
        self.btn_comparador.configure(cursor="pirate")

        self.btn_codificador = Button(self.root,text="Codificador",fg="#3b3b3b", border="1",width=13,highlightbackground="#dddddd",highlightthickness=2,bg="#f4f4f4", command=self.consult)
        self.btn_codificador.place(x=435,y=45,height=25)
        self.btn_codificador.configure(cursor="pirate")

        self.btn_log = Button(self.root,text="Log",fg="#3b3b3b", border="1",width=13,highlightbackground="#dddddd",highlightthickness=2,bg="#f4f4f4", command=self.consult)
        self.btn_log.place(x=535,y=45,height=25)
        self.btn_log.configure(cursor="pirate")

        self.btn_sniper = Button(self.root,text="Sniper",fg="#3b3b3b", border="1",width=13,highlightbackground="#dddddd",highlightthickness=2,bg="#f4f4f4", command=self.consult)
        self.btn_sniper.place(x=635,y=45,height=25)
        self.btn_sniper.configure(cursor="pirate")

        self.btn_whois = Button(self.root,text="Whois",fg="#3b3b3b", border="1",width=13,highlightbackground="#dddddd",highlightthickness=2,bg="#f4f4f4", command=self.consult)
        self.btn_whois.place(x=735,y=45,height=25)
        self.btn_whois.configure(cursor="pirate")

        self.btn_ping = Button(self.root,text="Ping",fg="#3b3b3b", border="1",width=13,highlightbackground="#dddddd",highlightthickness=2,bg="#f4f4f4", command=self.consult)
        self.btn_ping.place(x=835,y=45,height=25)
        self.btn_ping.configure(cursor="pirate")

        self.btn_port_scan = Button(self.root,text="PortScan",fg="#3b3b3b", border="1",width=13,highlightbackground="#dddddd",highlightthickness=2,bg="#f4f4f4", command=self.consult)
        self.btn_port_scan.place(x=935,y=45,height=25)
        self.btn_port_scan.configure(cursor="pirate")




        self.btn_try = Button(self.frame_1,text="executar",fg="white", border="0",width=8,highlightbackground="#ec7070",highlightthickness=1,bg="#ff5a5a", command=self.consult)
        self.btn_try.place(x=537,rely=0.1,height=25)
        self.btn_try.configure(cursor="pirate",font=('Helvetica neue', 10))

        self.save_data_ = Button(self.frame_1,text="salvar",bg="#ff5a5a",fg="#ffffff", border="0",width=10)
        self.save_data_.place(x=620,rely=0.1,height=25)
        self.save_data_.configure(cursor="pirate",font=('Helvetica neue', 10))

        self.copiar_ = Button(self.frame_1,text="copiar",bg="#ff5a5a",fg="#ffffff", border="0",width=10,command=self.whois)
        self.copiar_.place(x=720,rely=0.1,height=25)
        self.copiar_.configure(cursor="pirate",font=('Helvetica neue', 10))

        self.clear_ = Button(self.frame_1,text="limpar",bg="#ff5a5a",fg="#ffffff", border="0",width=10,command=self.limpar_consult)
        self.clear_.place(x=820,rely=0.1,height=25)
        self.clear_.configure(cursor="pirate",font=('Helvetica neue', 10))

    
#Chamada de classe
Application()



#Códigos isolados.

#get_ip = socket.gethostbyname(domain)
#self.label_ip = Label(self.frame_1,text=f'IP:{get_ip}',bg="white",fg="green")
#self.label_ip.place(relx=0.03,rely=0.7)
#self.label_ip.config(font=('Helvetica neue',10))