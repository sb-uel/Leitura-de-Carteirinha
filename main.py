import tkinter as tk
from tkinter import ttk
from Telas.defs import *
from tkinter import ttk
from tab_functions import (
    abrir_aba_cadastrar_usuario,
    abrir_aba_consultar_rg,
    abrir_aba_comecar_rg,
    abrir_aba_consultar_usuarios,
    abrir_aba_exportar,
)

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

# Telas principais ao abrir o programa
abrir_aba_comecar_rg(notebook, imagens_dict)
abrir_aba_consultar_rg(notebook, imagens_dict)
abrir_aba_consultar_usuarios(notebook, imagens_dict)
abrir_aba_cadastrar_usuario(notebook, imagens_dict)
abrir_aba_exportar(notebook, imagens_dict)


root.mainloop()
