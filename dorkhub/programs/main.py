#                               --- Importando modulos essenciais ( Todos os módulos utilizados para o Programa ser executado) ---

import sqlite3,requests,socket,customtkinter,pyperclip,urllib.parse,webbrowser
import tkinter as tk 
from tkinter import *
from tkinter import ttk
from bs4 import BeautifulSoup


root = Tk()


#                               --- Definindo classe principal do programa ---

class Funcs:

    def limpar_r(self):

        self.resultados.delete(1.0,END)

    def copiar_r(self):

        copiando =  self.resultados.get(1.0,END)

        pyperclip.copy(copiando)
    
    def copiar_s(self):

        copiando = self.gerar_scripts.get(1.0,END)

        pyperclip.copy(copiando)

    def limpar_s(self):

        self.gerar_scripts.delete(1.0,END)

    def abrir_github(self):
        webbrowser.open("https://github.com/gabrielsatoshi/d0rkhub")
    def abrir_info(self):
        webbrowser.open("https://github.com/gabrielsatoshi/d0rkhub#readme")

    def salvar_c (self):
        vuln = self.dropdown_vuln.get()
        resultados = self.resultados.get(1.0,END)
        consulta = self.consultar.get()
        if (consulta == ''):
            consulta = 'Default'

#                               --- Definindo o nome do banco ( variável banco recebe string com o nome do banco ) ---

        banco = 'banco_consultas'

#                               --- Criando tabela para consultas ( se não existir ainda ) ---

        con = sqlite3.connect(banco)

        query_tabela = '''CREATE TABLE IF NOT EXISTS consultas
                    (id INTEGER PRIMARY KEY NOT NULL,
                        vulnerabilidade VARCHAR NOT NULL,
                        dominio VARCHAR NOT NULL,
                        resultados VARCHAR NOT NULL);'''
        con.execute(query_tabela)
        query_insert = '''INSERT INTO consultas (vulnerabilidade,dominio,resultados) VALUES (?,?,?)'''
        query_insert_tuple = (vuln,consulta,resultados)
        cursor = con.cursor()
        cursor.execute(query_insert,query_insert_tuple)
        con.commit()
        con.close()
              

class Application(Funcs):

#                               --- Função para definir o escopo padrão da classe ( Funções que serão puxadas quando a classe for chamada )---

    def __init__(self):

        self.root = root
        self.tela()
        self.textos()
        self.nav_bar()
        self.entradas()
        self.dropdown()
        self.botoes() 
        root.mainloop()

#                               --- Função para definir os paramêtros da tela ( Caracteristicas gerais da tela Tamanho,Nome,Cor.. ) ---

    def tela(self):

        self.root.title("Dorkhub")
        self.root.resizable(False,False)
        self.root.geometry("1068x620")
        self.root.configure(background="#313131")
        self.root.iconbitmap("public/logo.ico")

#                               --- Função para definir os Textos exibidos na tela(Titulos,Mensagens,etc..) ---


    def textos(self):

#                               --- Label Dork(Primeira parte do Titulo DorkHub) ---

        self.dork = Label(root,text="Dork")
        self.dork.place(relx=0.03,y=10)
        self.dork.config(font=("Helvetica neue",48),bg="#313131",fg="white")

#                               --- Label Hub (Segunda parte do Titulo DorkHub) ---

        self.hub = Label(root,text="Hub")
        self.hub.place(x=172,y=10)
        self.hub.config(font=("Helvetica neue",48),bg="#313131",fg="#ff3e3e")

#                               --- Função para a criação de uma nav bar(Barra de navegação) ---

    def nav_bar(self):

#                               --- Variável para definir um parametro de alturav ---        
        
        altura = 40

#                               --- Definindo botão GitHub (Irá realizar o redirecionamento para o GitHub.) ---

        self.github = Button(self.root,text="Github",command=self.abrir_github)
        self.github.place(x =345,y=altura)
        self.github.config(font=("Helvetica neue",15),bg="#313131",fg="white",border=0,cursor="pirate")

#                               --- Definindo botão Config(Irá realizar o redirecionamento para as configurações do programa.) ---

        self.config = Button(self.root,text="Config",command=self.abrir_info)
        self.config.place(x =440,y=altura)
        self.config.config(font=("Helvetica neue",15),bg="#313131",fg="white",border=0,cursor="pirate")

#                               --- Definindo botão salvos (Irá mostrar todos as consultas salvas no banco de dados.) ---
        
        self.salvos = Button(self.root,text="Salvos")
        self.salvos.place(x =540,y=altura)
        self.salvos.config(font=("Helvetica neue",15),bg="#313131",fg="white",border=0,cursor="pirate")

#                               --- Definindo botão Help (Irá redirecionar o usuário para uma página de Ajuda.) ---

        self.help = Button(self.root,text="Help",command=self.abrir_info)
        self.help.place(x =720,y=altura)
        self.help.config(font=("Helvetica neue",15),bg="#313131",fg="white",border=0,cursor="pirate")

#                               --- Definindo botão Info(Irá redirecionar o usuário para uma página explicativa.) ---

        self.info = Button(self.root,text="Info",command=self.abrir_info)
        self.info.place(x =640,y=altura)
        self.info.config(font=("Helvetica neue",15),bg="#313131",fg="white",border=0,cursor="pirate")

#                               --- Função para definir as entradas do sistema(Campos de preenchimento) ---

    def entradas(self):

#                               --- Definindo campo de busca (Definindo campo de busca utilizando uma Customização do Tkinter) ---

        self.consultar = customtkinter.CTkEntry(master=self.root,placeholder_text='www.google.com.br',border_width=1)
        self.consultar.place(x=40,y=100)
        self.consultar.configure(width=325,height=35)

#                               --- Definindo campo para retornar os resultados de consultas (Campo de resultados) ---

        self.resultados = Text(self.root,highlightbackground="#787878",highlightthickness=1,border="0",bg="#f4f4f4")
        self.resultados.place(x=40,y=150)
        self.resultados.configure(width=124,height=10)

#                               --- Definindo campo para retornar os resultados de scripts gerados (Campo de geração de Scripts) ---


        self.gerar_scripts = Text(self.root,highlightbackground="#787878",highlightthickness=1,border="0",bg="#f4f4f4")
        self.gerar_scripts.place(x=40,y=415)
        self.gerar_scripts.configure(width=124,height=10)

#                               --- Função para definir os Dropdown do sistema(Categorias,Seleção de Categoria) ---

    def dropdown(self):

#                               --- Definindo Dropdown que irá retornar as categorias de vulnerabilidades (Lista de vulnerabilidades) ---

        self.dropdown_vuln = ttk.Combobox(self.root, values=['XSS STORED','XSS REFLECTED', 'SQL INJECTION', 'HTML INJECTION','MYSQL ERROR','MARIA DB ERROR','INDEX OF'],width=35)
        self.dropdown_vuln.insert(0,'categorias')
        self.dropdown_vuln.place(x=390,y=100,height=35)

#                               --- Definindo Dropdown que irá retornar os scripts gerados pelo programa(Lista de scripts para gerar) ---

        self.dropdown_scripts = ttk.Combobox(self.root, values=['XSS STORED','XSS REFLECTED', 'SQL INJECTION', 'HTML INJECTION','MYSQL ERROR','MARIA DB ERROR','INDEX OF'],width=35)
        self.dropdown_scripts.insert(0,'scripts')
        self.dropdown_scripts.place(x=40,y=360,height=35)

#                               --- Função para definir os botões do sistema(Botões gerais(Exceto os botões especificos de funções)) ---

    def botoes(self):

#                               --- Definindo parametros para os botões(Parametros de posição y e da largura do botão) ---

        posicao_y = 100
        largura = 34

#                               --- Definindo botão Go(Botão para realizar a consulta) ---

        self.go = Button(self.root,text="Go")
        self.go.place(x=660,y=posicao_y,height=largura)
        self.go.config(font=("Arial black",10),bg="#ff3d3d",fg="white",border=0,cursor="pirate")
        self.go.configure(width=8)

#                               --- Definindo botão Copiar(Botão para copiar dados do campo de entrada) ---

        self.copiar = Button(self.root,text="Copiar",command=self.copiar_r)
        self.copiar.place(x=760,y=posicao_y,height=largura)
        self.copiar.config(font=("Arial black",10),bg="#ff3d3d",fg="white",border=0,cursor="pirate")
        self.copiar.configure(width=8)

#                               --- Definindo botão Limpar(Botão para limpar dados do campo de entrada) ---

        self.limpar = Button(self.root,text="Limpar",command=self.limpar_r)
        self.limpar.place(x=860,y=posicao_y,height=largura)
        self.limpar.config(font=("Arial black",10),bg="#ff3d3d",fg="white",border=0,cursor="pirate")
        self.limpar.configure(width=8)

#                               --- Definindo botão salvar(Botão para salvar os dados do campo de Resultados no banco de dados) ---

        self.salvar = Button(self.root,text="Salvar",command=self.salvar_c)
        self.salvar.place(x=960,y=posicao_y,height=largura)
        self.salvar.config(font=("Arial black",10),bg="#ff3d3d",fg="white",border=0,cursor="pirate")
        self.salvar.configure(width=8)

#                               --- Definindo parametro y(Definindo um parametro de posição Y) ---

        posicao_y_2 = 360

#                               --- Definindo botão Gerar(Botão para gerar scripts) ---

        self.gerar = Button(self.root,text="Gerar")
        self.gerar.place(x=300,y=posicao_y_2,height=largura)
        self.gerar.config(font=("Arial black",10),bg="#ff3d3d",fg="white",border=0,cursor="pirate")
        self.gerar.configure(width=8)

#                               --- Definindo segundo botão Copiar(Botão para copiar dados do campo de entrada) ---

        self.copiar2 = Button(self.root,text="Copiar",command=self.copiar_s)
        self.copiar2.place(x=410,y=posicao_y_2,height=largura)
        self.copiar2.config(font=("Arial black",10),bg="#ff3d3d",fg="white",border=0,cursor="pirate")
        self.copiar2.configure(width=8)

#                               --- Definindo segundo botão Limpar(Botão para limpar dados do campo de entrada) ---
 
        self.limpar2 = Button(self.root,text="Limpar",command=self.limpar_s)
        self.limpar2.place(x=520,y=posicao_y_2,height=largura)
        self.limpar2.config(font=("Arial black",10),bg="#ff3d3d",fg="white",border=0,cursor="pirate")
        self.limpar2.configure(width=8)

Application()
