from tkinter import *
root = Tk()
from tkinter import ttk

class Application():
    def __init__(self):
        self.root = root
        self.tela()
        self.frames()
        self.labels_frame1()
        self.nav_bar()
        self.buttons_frame1()
        self.buttons_frame2()
        self.entrys_frame2()
        self.label_frame2()
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
        
        self.dropdown = ttk.Combobox(self.frame_2, values=['XSS INJECTION', 'SQL INJECTION', 'HTML INJECTION','OPEN REDIRECT'],width=42)
        self.dropdown.insert(0,'Vulnerability')
        self.dropdown.place(relx=0.02,rely=0.05)

        self.results_entry = Text(self.frame_2,highlightbackground="#787878",highlightthickness=1,border="0",bg="#dddddd")
        self.results_entry.place(relx=0.4,rely=0.2)
        self.results_entry.configure(width=34,height=9)

        self.range_entry = Entry(self.frame_2,highlightbackground="#787878",highlightthickness=1,border="0",bg="#dddddd")
        self.range_entry.place(relx=0.8,rely=0.7,height=45)
        self.range_entry.configure(width=5,font=('Arial', 18))

    def buttons_frame2(self): 
        self.btn_run = Button(self.frame_2,text="Run",bg="#5bc0de",fg="white", border="0",width=9)
        self.btn_run.place(relx=0.8,rely=0.2,height=30)
        self.btn_run.configure(cursor="pirate")

        self.save_data = Button(self.frame_2,text="Save data",bg="#66d76f",fg="white", border="0",width=9)
        self.save_data.place(relx=0.8,rely=0.4,height=30)
        self.save_data.configure(cursor="pirate") 
    def label_frame2(self):      
        self.label_title_range = Label(self.frame_2,text='Payload range',bg="white",fg="#333333")
        self.label_title_range.place(relx=0.8,rely=0.6)
        self.label_title_range.config(font=('Helvetica neue',7))

    def entrys_frame1(self):
        self.domain_entry = Entry(self.frame_1,highlightbackground="#787878",highlightthickness=1,border="0",bg="#dddddd")
        self.domain_entry.place(relx=0.03,rely=0.4,height=40)
        self.domain_entry.configure(width=40,font=('Arial', 10))
    def buttons_frame1(self):
        self.btn_clean = Button(self.frame_1,text=" Clear",fg="black", border="0",width=7,highlightbackground="#ec7070",highlightthickness=1,bg="#f87159")
        self.btn_clean.place(relx=0.4,rely=0.4,height=40)
        self.btn_clean.configure(cursor="pirate")

Application()

