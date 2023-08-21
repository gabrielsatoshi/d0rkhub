

import tkinter as tk

root = tk.Tk()
root.geometry('300x200')

text1 = tk.Text(root)
text1.pack(pady=10, padx=10)

# Adicionar texto ao texto1
text1.insert(tk.END, "Olá Mundo\nNovo texto\nTerceiro texto")

root.mainloop()
