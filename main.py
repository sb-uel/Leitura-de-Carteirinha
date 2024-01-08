from global_vars import *
from tkinter import ttk
from Telas.ComeçarRG.começar import criar_tela_comecar_rg
from tab_functions import (
    abrir_aba_editar_rg,
    abrir_aba_editar_usuario,
    abrir_abas_principais,
)

# Tela principal ao abrir o programa

# Adiciona tela de Começar RG
frame_comecar_rg = ttk.Frame(
    notebook, width=notebook.winfo_width(), height=notebook.winfo_height()
)
frame_comecar_rg.pack(fill="both", expand=True)
criar_tela_comecar_rg(frame_comecar_rg, imagens_dict["ComecarRG"])
notebook.add(frame_comecar_rg, text="Começar RG")

abrir_abas_principais(notebook, imagens_dict)
abrir_aba_editar_rg(notebook, imagens_dict)
abrir_aba_editar_usuario(notebook, imagens_dict)
root.mainloop()
