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
import customtkinter
import pyperclip
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
    #Funcionalidades frame 1
    def limpar_consulta(self):
        self.resultados_consulta.delete(1.0,END)
    def copiar_consulta(self):
        copiando =  self.resultados_consulta.get(1.0,END)
        pyperclip.copy(copiando)

    #Funcionalidades frame 2 
    def limpar_campo_payloads(self):
        self.inserir_payloads.delete(1.0,END)
    def copiar_campo_payloads(self):
        copiando =  self.inserir_payloads.get(1.0,END)
        pyperclip.copy(copiando)


    def banco_nav(self):
        global frame_banco
        frame_banco = Frame(root,bd=0,bg="green")
        frame_banco.grid(ipadx=470, ipady=257,padx=31,pady=70)
        botao = Button(frame_banco,text='AMARELO')
        botao.grid()
        
        
        self.dropdown_vulnerabilidades = ttk.Combobox(self.frame_banco, values=['XSS INJECTION', 'SQL INJECTION', 'HTML INJECTION','OPEN REDIRECT','DEFAULT'],width=34)
        self.dropdown_vulnerabilidades.insert(0,'Vulnerabilidades')
        self.dropdown_vulnerabilidades.grid(x=290,rely=0.1,height=25)
        
        
        self.banco_ver.config(state=DISABLED)
        self.comparar.config(state=ACTIVE)
        self.payloads_ver.config(state=ACTIVE)
        frame_comparador.grid_forget()
        frame_payloads.grid_forget()

    def comparador_nav(self):
        global frame_comparador
        frame_comparador = Frame(root,bd=0,bg="red")
        frame_comparador.grid(ipadx=502, ipady=267,padx=31,pady=70)
        self.comparar.config(state=DISABLED)
        self.banco_ver.config(state=ACTIVE)
        self.payloads_ver.config(state=ACTIVE)

        frame_banco.grid_forget()
        frame_payloads.grid_forget()
    def payloads_nav(self):
        global frame_payloads
        frame_payloads = Frame(root,bd=0,bg="blue")
        frame_payloads.grid(ipadx=502, ipady=267,padx=31,pady=70)
        
        self.payloads_ver.config(state=DISABLED)
        self.comparar.config(state=ACTIVE)
        self.banco_ver.config(state=ACTIVE)

        frame_banco.grid_forget()
        frame_comparador.grid_forget()
   
    def painel_nav(self):
        self.comparar.config(state=ACTIVE)
        self.banco_ver.config(state=ACTIVE)
        self.payloads_ver.config(state=ACTIVE)

        try:
            frame_payloads.grid_forget()
            frame_banco.grid_forget()
            frame_comparador.grid_forget()
        except Exception:    
            try:
                frame_banco.grid_forget()
            except Exception:
                try:
                    frame_payloads.grid_forget()
                except Exception:
                    try:
                        frame_comparador.grid_forget()
                    except Exception:
                        pass
    #Capturando campos.
    def request(self):
        domain = self.resultados_consulta.get()
        drop = self.dropdown_vulnerabilidades.get()


    #Criação dos payloads para cada vulnerabilidade.
    def dork_generation(self):
        if (self.dropdown_payloads.get() == 'XSS INJECTION'):
            with open('../payloads/xss.txt', 'r') as d:
                dork_file = d.read()
                xss_payloads = (dork_file)  
            self.inserir_payloads.insert(tk.END,xss_payloads)
        elif (self.dropdown_payloads.get() == 'SQL INJECTION'):
            with open('../payloads/sql.txt', 'r') as d:
                dork_file = d.read()
                sql_payloads = (dork_file)
            self.inserir_payloads.insert(tk.END,sql_payloads)  
        elif (self.dropdown_payloads.get() == 'HTML INJECTION'):
            with open('../payloads/html.txt', 'r') as d:
                dork_file = d.read()
                html_payloads = (dork_file)
            self.inserir_payloads.insert(tk.END,html_payloads)   
        elif (self.dropdown_payloads.get() == 'DEFAULT'):
            with open('../payloads/default.txt', 'r') as d:
                dork_file = d.read()
                default_payloads = (dork_file) 
            self.inserir_payloads.insert(tk.END,default_payloads) 
        else:
             self.inserir_payloads.insert(tk.END,'Select the vulnerability!') 
    
    #Criação das consultas por sites, utilizando parametro por vulnerabilidade.
    def consult(self):
            if (self.dropdown_vulnerabilidades.get() != 'SQL INJECTION' and self.dropdown_vulnerabilidades.get() != 'XSS INJECTION' and self.dropdown_vulnerabilidades.get() != 'HTML INJECTION' and self.dropdown_vulnerabilidades.get() != 'DEFAULT' and self.dropdown_vulnerabilidades.get() != 'OPEN REDIRECT' ):
                self.label_error = Label(self.frame_1,text='select a vulnerability!',bg="white",fg="red")
                self.label_error.place(x=47,y=198)
                self.label_error.config(font=('Courier new',8))
                root.after(1000,self.label_error.destroy)
            elif(self.dropdown_vulnerabilidades.get() == 'SQL INJECTION'):
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
                
                domain = self.consultar_site.get()
                search_urls = google_search_urls(sql_payloads + f' site: {domain}') 
                for line in search_urls:
                    self.resultados_consulta.insert(tk.END,f'{urllib.parse.unquote(line)}\n')

            elif(self.dropdown_vulnerabilidades.get() == 'HTML INJECTION'):
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
                
                domain = self.consultar_site.get()
                search_urls = google_search_urls(html_payloads + f' site: {domain}') 
                for line in search_urls:
                    self.resultados_consulta.insert(tk.END,f'{urllib.parse.unquote(line)}\n')


            elif(self.dropdown_vulnerabilidades.get() == 'XSS INJECTION'):
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

                domain = self.consultar_site.get()
                search_urls = google_search_urls(xss_payloads + f' site: {domain}') 
                for line in search_urls:
                    self.resultados_consulta.insert(tk.END,f'{urllib.parse.unquote(line)}\n')


            elif(self.dropdown_vulnerabilidades.get() == 'DEFAULT'):
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

                domain = self.consultar_site.get()
                search_urls = google_search_urls(default_payloads + f' site: {domain}') 
                for line in search_urls:
                    self.resultados_consulta.insert(tk.END,f'{line}\n')

            elif(self.dropdown_vulnerabilidades.get() == 'OPEN REDIRECT'):
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

                domain = self.consultar_site.get()
                search_urls = google_search_urls(open_redirect + f' site: {domain}') 
                for line in search_urls:
                    self.resultados_consulta.insert(tk.END,f'{urllib.parse.unquote(line)}\n')
            else:
                print('.')
    
    #Realizando consulta no Whois.
    def whois(self):
        domain = self.consultar_site.get()
        consult = getinformation.a()
        self.payloads_entry(tk.END,consult)

# Definindo a classe aplication.
class Application(Funcs):
    def __init__(self):
        self.root = root
        self.tela()
        self.frames()
        self.buttons_root()
        self.labels_frame1()
        self.nav_bar()
        self.buttons_frame1()
        self.buttons_frame2()
        self.entrys_frame2()
        self.entrys_frame1()
        root.mainloop()
    
    #Configurações da tela
    def tela(self):
        #
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
    
        self.link_site = Button(self.root,text="Site",bg="#fcfffe",fg="black", border="0")
        self.link_site.place(x=28,y=15)
        self.link_site.configure(cursor="pirate")
        
        self.link_github = Button(self.root,text="Github",bg="#fcfffe",fg="black", border="0")
        self.link_github.place(x=60,y=15)
        self.link_github.configure(cursor="pirate")

        self.configuracoes = Button(self.root,text="Configurações",bg="#fcfffe",fg="black", border="0")
        self.configuracoes.place(x=113,y=15)
        self.configuracoes.configure(cursor="pirate")


    #Textos do primeiro frame
    def labels_frame1(self):
        self.texto_url = Label(self.frame_1,text='url',bg="white",fg="#333333")
        self.texto_url.place(relx=0.03,rely=0.1)
        self.texto_url.config(font=('Helvetica neue',10))

    #Campos de entrada do segundo frame
    def entrys_frame2(self):
        self.inserir_payloads = Text(self.frame_2,highlightbackground="#787878",highlightthickness=1,border="0",bg="#f4f4f4")
        self.inserir_payloads.place(x=50,y=70)
        self.inserir_payloads.configure(width=107,height=9)
        
        self.dropdown_payloads = ttk.Combobox(self.frame_2, values=['XSS INJECTION', 'SQL INJECTION', 'HTML INJECTION','DEFAULT'],width=42)
        self.dropdown_payloads.insert(0,'Payloads')
        self.dropdown_payloads.place(x=50,y=20,height=25)


    #Botões do segundo frame
    def buttons_frame2(self): 

        self.limpar_payload = Button(self.frame_2,text="limpar",fg="white", border="0",width=11,highlightbackground="#ec7070",highlightthickness=1,bg="#ff5a5a", command=self.limpar_campo_payloads)
        self.limpar_payload.place(x=615,y=20,height=25)
        self.limpar_payload.configure(cursor="pirate")

        self.copiar_payload = Button(self.frame_2,text="copiar",fg="white", border="0",width=11,highlightbackground="#ec7070",highlightthickness=1,bg="#ff5a5a", command=self.copiar_campo_payloads)
        self.copiar_payload.place(x=490,y=20,height=25)
        self.copiar_payload.configure(cursor="pirate")

        self.gerar_payload = Button(self.frame_2,text='gerar',bg="#ff5a5a",fg="white", border="0",width=11,command=self.dork_generation)
        self.gerar_payload.place(x=370,y=20,height=25)


    #Campos de entrada primeiro frame.
    def entrys_frame1(self):
        self.consultar_site = customtkinter.CTkEntry(master=self.frame_1,placeholder_text='www.google.com.br',border_width=1)
        self.consultar_site.place(x=50,y=25)
        self.consultar_site.configure(width=210,height=25)


        self.dropdown_vulnerabilidades = ttk.Combobox(self.frame_1, values=['XSS INJECTION', 'SQL INJECTION', 'HTML INJECTION','OPEN REDIRECT','DEFAULT'],width=34)
        self.dropdown_vulnerabilidades.insert(0,'Vulnerabilidades')
        self.dropdown_vulnerabilidades.place(x=290,rely=0.1,height=25)


        self.resultados_consulta = Text(self.frame_1,highlightbackground="#787878",highlightthickness=1,border="0",bg="#f4f4f4")
        self.resultados_consulta.place(x=50,y=70)
        self.resultados_consulta.configure(width=107,height=10)

    #Botões primeiro frame
    def buttons_frame1(self):        
        self.executar_consulta = customtkinter.CTkButton(master=self.frame_1,text='Executar',border_width=0,fg_color='#ff5a5a',command=self.consult)
        self.executar_consulta.place(x=540,y=30)
        self.executar_consulta.configure(width=80,height=25)

        self.salvar_consulta_ = customtkinter.CTkButton(master=self.frame_1,text='Salvar',border_width=0,fg_color='#ff5a5a')
        self.salvar_consulta_ .place(x=620,y=30)
        self.salvar_consulta_ .configure(width=78,height=25)

        self.copiar_consulta_ = customtkinter.CTkButton(master=self.frame_1,text='Copiar',border_width=0,fg_color='#ff5a5a',command=self.copiar_consulta)
        self.copiar_consulta_.place(x=720,y=30)
        self.copiar_consulta_.configure(width=78,height=25)

        self.limpar_consulta_ = customtkinter.CTkButton(master=self.frame_1,text='Limpar',border_width=0,fg_color='#ff5a5a',command=self.limpar_consulta)
        self.limpar_consulta_.place(x=820,y=30)
        self.limpar_consulta_.configure(width=78,height=25)
    
    #Botões do root
    def buttons_root(self):
        self.painel_ver = Button(self.root,text="Painel",fg="#3b3b3b", border="1",width=14,highlightbackground="#dddddd",highlightthickness=2,bg="#f4f4f4",command=self.painel_nav)
        self.painel_ver.place(x=32,y=45,height=25)
        self.painel_ver.configure(cursor="pirate")

        self.banco_ver = Button(self.root,text="Banco",fg="#3b3b3b", border="1",width=13,highlightbackground="#dddddd",highlightthickness=2,bg="#f4f4f4", command=self.banco_nav)
        self.banco_ver.place(x=138,y=45,height=25)
        self.banco_ver.configure(cursor="pirate")

        self.payloads_ver = Button(self.root,text="Payloads",fg="#3b3b3b", border="1",width=13,highlightbackground="#dddddd",highlightthickness=2,bg="#f4f4f4", command=self.payloads_nav)
        self.payloads_ver.place(x=235,y=45,height=25)
        self.payloads_ver.configure(cursor="pirate")

        self.comparar = Button(self.root,text="Comparador",fg="#3b3b3b", border="1",width=13,highlightbackground="#dddddd",highlightthickness=2,bg="#f4f4f4", command=self.comparador_nav)
        self.comparar.place(x=335,y=45,height=25)
        self.comparar.configure(cursor="pirate")

        self.codificar = Button(self.root,text="Codificador",fg="#3b3b3b", border="1",width=13,highlightbackground="#dddddd",highlightthickness=2,bg="#f4f4f4", command=self.consult)
        self.codificar.place(x=435,y=45,height=25)
        self.codificar.configure(cursor="pirate")

        self.btn_log = Button(self.root,text="Log",fg="#3b3b3b", border="1",width=13,highlightbackground="#dddddd",highlightthickness=2,bg="#f4f4f4", command=self.consult)
        self.btn_log.place(x=535,y=45,height=25)
        self.btn_log.configure(cursor="pirate")

        self.sniper = Button(self.root,text="Sniper",fg="#3b3b3b", border="1",width=13,highlightbackground="#dddddd",highlightthickness=2,bg="#f4f4f4", command=self.consult)
        self.sniper.place(x=635,y=45,height=25)
        self.sniper.configure(cursor="pirate")

        self.consulta_whois = Button(self.root,text="Whois",fg="#3b3b3b", border="1",width=13,highlightbackground="#dddddd",highlightthickness=2,bg="#f4f4f4", command=self.consult)
        self.consulta_whois.place(x=735,y=45,height=25)
        self.consulta_whois.configure(cursor="pirate")

        self.pingar = Button(self.root,text="Ping",fg="#3b3b3b", border="1",width=13,highlightbackground="#dddddd",highlightthickness=2,bg="#f4f4f4", command=self.consult)
        self.pingar.place(x=835,y=45,height=25)
        self.pingar.configure(cursor="pirate")

        self.escanear_portas = Button(self.root,text="PortScan",fg="#3b3b3b", border="1",width=13,highlightbackground="#dddddd",highlightthickness=2,bg="#f4f4f4", command=self.consult)
        self.escanear_portas.place(x=935,y=45,height=25)
        self.escanear_portas.configure(cursor="pirate")
    
Application()



#Códigos isolados.

#get_ip = socket.gethostbyname(domain)
#self.label_ip = Label(self.frame_1,text=f'IP:{get_ip}',bg="white",fg="green")
#self.label_ip.place(relx=0.03,rely=0.7)
#self.label_ip.config(font=('Helvetica neue',10))