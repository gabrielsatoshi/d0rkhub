from tkinter import *

root = Tk()


def frame1():
    
    global frame_1
    frame_1 = Frame(root,bd=0,bg="red")
    frame_1.grid(ipadx=502, ipady=267,padx=31,pady=70)

    botao = Button(frame_1,text='VERMELHO')
    botao.grid()
    botao1.config(state=DISABLED)
    botao2.config(state=ACTIVE)
    botao3.config(state=ACTIVE)
    botao4.config(state=ACTIVE)

    frame_4.grid_forget()
    frame_2.grid_forget()
    frame_3.grid_forget()
def frame2():
    global frame_2
    frame_2 = Frame(root,bd=0,bg="green")
    frame_2.grid(ipadx=502, ipady=267,padx=31,pady=70)
    botao = Button(frame_2,text='VERDE')
    botao.grid()
    botao2.config(state=DISABLED)
    botao1.config(state=ACTIVE)
    botao3.config(state=ACTIVE)
    botao4.config(state=ACTIVE)

    frame_1.grid_forget()
    frame_3.grid_forget()
    frame_4.grid_forget()
def frame3():
    global frame_3
    frame_3 = Frame(root,bd=0,bg="yellow")
    frame_3.grid(ipadx=502, ipady=267,padx=31,pady=70)
    botao = Button(frame_3,text='AMARELO')
    botao.grid()
    botao3.config(state=DISABLED)
    botao1.config(state=ACTIVE)
    botao2.config(state=ACTIVE)
    botao4.config(state=ACTIVE)
    frame_1.grid_forget()
    frame_2.grid_forget()
    frame_4.grid_forget()
def frame4():
    global frame_4
    frame_4 = Frame(root,bd=0,bg="blue")
    frame_4.grid(ipadx=502, ipady=267,padx=31,pady=70)
    botao = Button(frame_4,text='AMARELO')
    botao.grid()
    botao3.config(state=ACTIVE)
    botao1.config(state=ACTIVE)
    botao2.config(state=ACTIVE)
    botao4.config(state=DISABLED)
    frame_1.grid_forget()
    frame_2.grid_forget()
    frame_3.grid_forget()


        

botao1 = Button(root,text='Vermelho',command=frame1)
botao1.grid()


botao2 = Button(root,text='Verde',command=frame2)
botao2.grid() 


botao3 = Button(root,text='Amarelo',command=frame3)
botao3.grid() 

botao4 = Button(root,text='azul',command=frame4)
botao4.grid() 


root.mainloop()
