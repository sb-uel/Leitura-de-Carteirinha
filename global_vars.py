import tkinter as tk
from tkinter import ttk
from Telas.defs import *

# Root window
root = tk.Tk()
root.title("Leitura de Carteirinha")
root.geometry(TAMANHO_JANELA)
root.resizable(True, True)

# Cria o notebook
notebook = ttk.Notebook(root)
notebook.pack(fill="both", expand=True)

# Dicionário aninhado para armazenar imagens em cada aba
imagens_dict = {
    "Leitura": {},
    "Exportar": {},
    "EditarUsuario": {},
    "EditarRG": {},
    "ConsultarUsuarios": {},
    "ComecarRG": {},
    "CadastroUsuario": {},
    "BuscarRG": {},
}