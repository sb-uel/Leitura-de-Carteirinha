import tkinter as tk
from tkinter import ttk
from Telas.defs import *
from Telas.Leitura.leitura import cria_tela_leitura

# Root window
root = tk.Tk()
root.title('Notebook Demo')
root.geometry(TAMANHO_JANELA)
root.resizable(True, True)

# Cria o notebook
notebook = ttk.Notebook(root)
notebook.pack(fill="both", expand=True)
imagens = {}
# Adiciona as abas das telas principais
frame_leitura = ttk.Frame(notebook, width=notebook.winfo_width(), height=notebook.winfo_height())
frame_leitura.pack(fill="both", expand=True)
cria_tela_leitura(frame_leitura,imagens)
notebook.add(frame_leitura, text='Leitura')
notebook.add(ttk.Frame(notebook), text='Outra Guia')

root.mainloop()