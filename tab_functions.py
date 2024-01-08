from tkinter import ttk


def abrir_aba_leitura(notebook: ttk.Notebook, imagens_dict: dict[str, dict]):
    from Telas.Leitura.leitura import criar_tela_leitura

    frame_leitura = ttk.Frame(
        notebook, width=notebook.winfo_width(), height=notebook.winfo_height()
    )
    frame_leitura.pack(fill="both", expand=True)
    criar_tela_leitura(frame_leitura, imagens_dict["Leitura"])
    notebook.insert(0, frame_leitura, text="Leitura")  # Insere na primeira posição


def abrir_aba_consultar_rg(notebook: ttk.Notebook, imagens_dict: dict[str, dict]):
    from Telas.BuscarReunião.buscarReuniao import criar_tela_buscar_rg

    frame_buscar_rg = ttk.Frame(
        notebook, width=notebook.winfo_width(), height=notebook.winfo_height()
    )
    frame_buscar_rg.pack(fill="both", expand=True)
    criar_tela_buscar_rg(frame_buscar_rg, imagens_dict["BuscarRG"])
    notebook.add(frame_buscar_rg, text="Buscar RG")


def abrir_aba_consultar_usuarios(notebook: ttk.Notebook, imagens_dict: dict[str, dict]):
    from Telas.ConsultarUsuários.consultar import criar_tela_consultar_usuarios

    frame_consultar_usuario = ttk.Frame(
        notebook, width=notebook.winfo_width(), height=notebook.winfo_height()
    )
    frame_consultar_usuario.pack(fill="both", expand=True)
    criar_tela_consultar_usuarios(
        frame_consultar_usuario, imagens_dict["ConsultarUsuarios"]
    )
    notebook.add(frame_consultar_usuario, text="Consultar Usuários")


def abrir_aba_cadastrar_usuario(notebook: ttk.Notebook, imagens_dict: dict[str, dict]):
    from Telas.Cadastro.cadastro import criar_tela_cadastro_usuarios

    frame_cadastrar_usuario = ttk.Frame(
        notebook, width=notebook.winfo_width(), height=notebook.winfo_height()
    )
    frame_cadastrar_usuario.pack(fill="both", expand=True)
    criar_tela_cadastro_usuarios(
        frame_cadastrar_usuario, imagens_dict["CadastroUsuario"]
    )
    notebook.add(frame_cadastrar_usuario, text="Cadastrar Usuário")


def abrir_aba_exportar(notebook: ttk.Notebook, imagens_dict: dict[str, dict]):
    from Telas.ExportarRG.exportar import criar_tela_exportar

    frame_exportar = ttk.Frame(
        notebook, width=notebook.winfo_width(), height=notebook.winfo_height()
    )
    frame_exportar.pack(fill="both", expand=True)
    criar_tela_exportar(frame_exportar, imagens_dict["Exportar"])
    notebook.add(frame_exportar, text="Exportar")


def abrir_aba_editar_usuario(notebook: ttk.Notebook, imagens_dict: dict[str, dict]):
    from Telas.EditarUsuários.editarUser import criar_tela_edicao_usuarios

    frame_editar_usuario = ttk.Frame(
        notebook, width=notebook.winfo_width(), height=notebook.winfo_height()
    )
    frame_editar_usuario.pack(fill="both", expand=True)
    criar_tela_edicao_usuarios(frame_editar_usuario, imagens_dict["EditarUsuario"])
    notebook.add(frame_editar_usuario, text="Editar Usuário")


def abrir_aba_editar_rg(notebook: ttk.Notebook, imagens_dict: dict[str, dict]):
    from Telas.EditarRG.editar import criar_tela_editar_rg

    frame_editar_rg = ttk.Frame(
        notebook, width=notebook.winfo_width(), height=notebook.winfo_height()
    )
    frame_editar_rg.pack(fill="both", expand=True)
    criar_tela_editar_rg(frame_editar_rg, imagens_dict["EditarRG"])
    notebook.add(frame_editar_rg, text="Editar RG")


def abrir_aba_comecar_rg(notebook: ttk.Notebook, imagens_dict: dict[str, dict]):
    from Telas.ComeçarRG.começar import criar_tela_comecar_rg

    frame_comecar_rg = ttk.Frame(
        notebook, width=notebook.winfo_width(), height=notebook.winfo_height()
    )
    frame_comecar_rg.pack(fill="both", expand=True)
    criar_tela_comecar_rg(
        frame_comecar_rg, imagens_dict["ComecarRG"], notebook, imagens_dict
    )
    notebook.add(frame_comecar_rg, text="Começar RG")
