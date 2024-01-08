import tkinter as tk
from tkinter import ttk
from Telas.defs import *
from Telas.Leitura.leitura import cria_tela_leitura
from Telas.ExportarRG.exportar import cria_tela_exportar
from Telas.EditarUsuários.editarUser import cria_tela_edicao_usuarios

# Root window
root = tk.Tk()
root.title("Leitura de Carteirinha")
root.geometry(TAMANHO_JANELA)
root.resizable(True, True)

# Cria o notebook
notebook = ttk.Notebook(root)
notebook.pack(fill="both", expand=True)

# Dicionário aninhado para armazenar imagens em cada aba
imagens = {"Leitura": {}, "Exportar": {}, "EditarUsuario": {}}

# Adiciona as abas das telas principais

# Adiciona tela de Leitura
frame_leitura = ttk.Frame(
    notebook, width=notebook.winfo_width(), height=notebook.winfo_height()
)
frame_leitura.pack(fill="both", expand=True)
cria_tela_leitura(frame_leitura, imagens["Leitura"])
notebook.add(frame_leitura, text="Leitura")

# Adiciona tela de Exportação
frame_exportar = ttk.Frame(
    notebook, width=notebook.winfo_width(), height=notebook.winfo_height()
)
frame_exportar.pack(fill="both", expand=True)
cria_tela_exportar(frame_exportar, imagens["Exportar"])
notebook.add(frame_exportar, text="Exportar")

# Adiciona tela de Edição de Usuario
frame_editar_usuario = ttk.Frame(
    notebook, width=notebook.winfo_width(), height=notebook.winfo_height()
)
frame_editar_usuario.pack(fill="both", expand=True)
cria_tela_edicao_usuarios(frame_editar_usuario, imagens["EditarUsuario"])
notebook.add(frame_editar_usuario, text="EditarUsuario")

root.mainloop()
