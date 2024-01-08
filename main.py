import tkinter as tk
from tkinter import ttk
from Telas.ComeçarRG.começar import criar_tela_comecar_rg
from Telas.defs import *
from tab_functions import abrir_aba_editar_rg, abrir_aba_editar_usuario, abrir_abas_principais

# Root window
root = tk.Tk()
root.title("Leitura de Carteirinha")
root.geometry(TAMANHO_JANELA)
root.resizable(True, True)

# Cria o notebook
notebook = ttk.Notebook(root)
notebook.pack(fill="both", expand=True)

# Dicionário aninhado para armazenar imagens em cada aba
imagens = {
    "Leitura": {},
    "Exportar": {},
    "EditarUsuario": {},
    "EditarRG": {},
    "ConsultarUsuarios": {},
    "ComecarRG": {},
    "CadastroUsuario": {},
    "BuscarRG": {},
}

# Tela principal ao abrir o programa

# Adiciona tela de Começar RG
frame_comecar_rg = ttk.Frame(
    notebook, width=notebook.winfo_width(), height=notebook.winfo_height()
)
frame_comecar_rg.pack(fill="both", expand=True)
criar_tela_comecar_rg(frame_comecar_rg, imagens["ComecarRG"])
notebook.add(frame_comecar_rg, text="Começar RG")

abrir_abas_principais(notebook, imagens)
abrir_aba_editar_rg(notebook, imagens)
abrir_aba_editar_usuario(notebook, imagens)
root.mainloop()