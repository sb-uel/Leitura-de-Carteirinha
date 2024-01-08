import tkinter as tk
from tkinter import ttk
from Telas.defs import *
from tkinter import ttk
from Telas.ComeçarRG.começar import criar_tela_comecar_rg

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

# Tela principal ao abrir o programa

# Adiciona tela de Começar RG
frame_comecar_rg = ttk.Frame(
    notebook, width=notebook.winfo_width(), height=notebook.winfo_height()
)
frame_comecar_rg.pack(fill="both", expand=True)
criar_tela_comecar_rg(frame_comecar_rg, imagens_dict["ComecarRG"], notebook, imagens_dict)
notebook.add(frame_comecar_rg, text="Começar RG")

root.mainloop()
