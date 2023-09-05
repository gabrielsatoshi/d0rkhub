from tkinter import *

root = Tk()

botao1 = Button(root,text='botao1')
botao1.pack()
botao1.config(state=DISABLED)

botao2 = Button(root,text='botao2')
botao2.pack() 
botao2.config(state=DISABLED)

botao3 = Button(root,text='botao3')
botao3.pack() 
botao3.config(state=DISABLED)


root.mainloop()
