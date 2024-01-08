from tkinter import ttk
from tkinter.tix import NoteBook
from Telas.BuscarReunião.buscarReuniao import criar_tela_buscar_rg
from Telas.Cadastro.cadastro import criar_tela_cadastro_usuarios
from Telas.ExportarRG.exportar import criar_tela_exportar
from Telas.Leitura.leitura import criar_tela_leitura
from Telas.ConsultarUsuários.consultar import criar_tela_consultar_usuarios
from Telas.EditarRG.editar import criar_tela_editar_rg
from Telas.EditarUsuários.editarUser import criar_tela_edicao_usuarios


def abrir_abas_principais(notebook: NoteBook, imagens: dict[str, dict]):
    # Telas principais quando iniciada a reunião

    # Adiciona tela de Leitura
    frame_leitura = ttk.Frame(
        notebook, width=notebook.winfo_width(), height=notebook.winfo_height()
    )
    frame_leitura.pack(fill="both", expand=True)
    criar_tela_leitura(frame_leitura, imagens["Leitura"])
    notebook.add(frame_leitura, text="Leitura")

    # Adiciona tela de Buscar RG
    frame_buscar_rg = ttk.Frame(
        notebook, width=notebook.winfo_width(), height=notebook.winfo_height()
    )
    frame_buscar_rg.pack(fill="both", expand=True)
    criar_tela_buscar_rg(frame_buscar_rg, imagens["BuscarRG"])
    notebook.add(frame_buscar_rg, text="Reuniões")

    # Adiciona tela de Consultar Usuários
    frame_consultar_usuario = ttk.Frame(
        notebook, width=notebook.winfo_width(), height=notebook.winfo_height()
    )
    frame_consultar_usuario.pack(fill="both", expand=True)
    criar_tela_consultar_usuarios(frame_consultar_usuario, imagens["ConsultarUsuarios"])
    notebook.add(frame_consultar_usuario, text="Usuários")

    # Adiciona tela de Cadastrar Usuário
    frame_cadastrar_usuario = ttk.Frame(
        notebook, width=notebook.winfo_width(), height=notebook.winfo_height()
    )
    frame_cadastrar_usuario.pack(fill="both", expand=True)
    criar_tela_cadastro_usuarios(frame_cadastrar_usuario, imagens["CadastroUsuario"])
    notebook.add(frame_cadastrar_usuario, text="Cadastrar Usuário")

    # Adiciona tela de Exportação
    frame_exportar = ttk.Frame(
        notebook, width=notebook.winfo_width(), height=notebook.winfo_height()
    )
    frame_exportar.pack(fill="both", expand=True)
    criar_tela_exportar(frame_exportar, imagens["Exportar"])
    notebook.add(frame_exportar, text="Exportar")


def abrir_aba_editar_usuario(notebook: NoteBook, imagens: dict[str, dict]):
    # Adiciona tela de Edição de Usuario
    frame_editar_usuario = ttk.Frame(
        notebook, width=notebook.winfo_width(), height=notebook.winfo_height()
    )
    frame_editar_usuario.pack(fill="both", expand=True)
    criar_tela_edicao_usuarios(frame_editar_usuario, imagens["EditarUsuario"])
    notebook.add(frame_editar_usuario, text="Editar Usuario")


def abrir_aba_editar_rg(notebook: NoteBook, imagens: dict[str, dict]):
    # Adiciona tela de Edição de RG
    frame_editar_rg = ttk.Frame(
        notebook, width=notebook.winfo_width(), height=notebook.winfo_height()
    )
    frame_editar_rg.pack(fill="both", expand=True)
    criar_tela_editar_rg(frame_editar_rg, imagens["EditarRG"])
    notebook.add(frame_editar_rg, text="Editar RG")
