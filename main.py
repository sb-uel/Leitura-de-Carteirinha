import tkinter as tk
from tkinter import ttk
from Telas.Cadastro.cadastro import cria_tela_cadastro_usuarios
from Telas.ComeçarRG.começar import cria_tela_comecar_rg
from Telas.ConsultarUsuários.consultar import cria_tela_consultar_usuarios
from Telas.defs import *
from Telas.EditarRG.editar import cria_tela_editar_rg
from Telas.EditarUsuários.editarUser import cria_tela_edicao_usuarios
from Telas.ExportarRG.exportar import cria_tela_exportar
from Telas.Leitura.leitura import cria_tela_leitura

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
}

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

# Adiciona tela de Edição de RG
frame_editar_rg = ttk.Frame(
    notebook, width=notebook.winfo_width(), height=notebook.winfo_height()
)
frame_editar_rg.pack(fill="both", expand=True)
cria_tela_editar_rg(frame_editar_rg, imagens["EditarRG"])
notebook.add(frame_editar_rg, text="EditarRG")

# Adiciona tela de Consultar Usuários
frame_consultar_usuario = ttk.Frame(
    notebook, width=notebook.winfo_width(), height=notebook.winfo_height()
)
frame_consultar_usuario.pack(fill="both", expand=True)
cria_tela_consultar_usuarios(frame_consultar_usuario, imagens["ConsultarUsuarios"])
notebook.add(frame_consultar_usuario, text="ConsultarUsuarios")

# Adiciona tela de Começar RG
frame_comecar_rg = ttk.Frame(
    notebook, width=notebook.winfo_width(), height=notebook.winfo_height()
)
frame_comecar_rg.pack(fill="both", expand=True)
cria_tela_comecar_rg(frame_comecar_rg, imagens["ComecarRG"])
notebook.add(frame_comecar_rg, text="ComecarRG")

# Adiciona tela de Cadastrar Usuário
frame_cadastrar_usuario = ttk.Frame(
    notebook, width=notebook.winfo_width(), height=notebook.winfo_height()
)
frame_cadastrar_usuario.pack(fill="both", expand=True)
cria_tela_cadastro_usuarios(frame_cadastrar_usuario, imagens["CadastroUsuario"])
notebook.add(frame_cadastrar_usuario, text="CadastroUsuario")

root.mainloop()
