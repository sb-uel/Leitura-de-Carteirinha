from pathlib import Path
from tkinter import messagebox, ttk


def abrir_aba_leitura(
    notebook: ttk.Notebook,
    imagens_dict: dict[str, dict],
    id_reuniao: int,
    local_de_salvamento: Path,
):
    from Telas.Leitura.leitura import criar_tela_leitura

    frame_leitura = ttk.Frame(
        notebook, width=notebook.winfo_width(), height=notebook.winfo_height()
    )
    frame_leitura.pack(fill="both", expand=True)
    criar_tela_leitura(
        frame_leitura,
        imagens_dict["Leitura"],
        notebook,
        imagens_dict,
        id_reuniao,
        local_de_salvamento,
    )
    notebook.insert(0, frame_leitura, text="Leitura")  # Insere na primeira posição
    notebook.select(frame_leitura)


def abrir_aba_consultar_rg(notebook: ttk.Notebook, imagens_dict: dict[str, dict]):
    from Telas.ConsultarRG.buscarReuniao import criar_tela_buscar_rg

    frame_buscar_rg = ttk.Frame(
        notebook, width=notebook.winfo_width(), height=notebook.winfo_height()
    )
    frame_buscar_rg.pack(fill="both", expand=True)
    criar_tela_buscar_rg(
        frame_buscar_rg,
        imagens_dict["ConsultarRG"],
        notebook,
        imagens_dict,
    )
    notebook.add(frame_buscar_rg, text="Consultar RG")


def abrir_aba_consultar_usuarios(notebook: ttk.Notebook, imagens_dict: dict[str, dict]):
    from Telas.ConsultarUsuários.consultar import criar_tela_consultar_usuarios

    frame_consultar_usuario = ttk.Frame(
        notebook, width=notebook.winfo_width(), height=notebook.winfo_height()
    )
    frame_consultar_usuario.pack(fill="both", expand=True)
    criar_tela_consultar_usuarios(
        frame_consultar_usuario,
        imagens_dict["ConsultarUsuarios"],
        notebook,
        imagens_dict,
    )
    notebook.add(frame_consultar_usuario, text="Consultar Usuários")


def abrir_aba_cadastrar_usuario(notebook: ttk.Notebook, imagens_dict: dict[str, dict]):
    from Telas.CadastroUsuário.cadastro import criar_tela_cadastro_usuarios

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


def abrir_aba_editar_usuario(
    notebook: ttk.Notebook,
    imagens_dict: dict[str, dict],
    id: str,
):
    from Telas.EditarUsuários.editarUser import criar_tela_edicao_usuarios

    if id == "":
        messagebox.showerror(
            "Nenhum Usuário Selecionado", "Nenhum usuário foi selecionado na tabela"
        )
        return

    frame_editar_usuario = ttk.Frame(
        notebook, width=notebook.winfo_width(), height=notebook.winfo_height()
    )
    frame_editar_usuario.pack(fill="both", expand=True)
    criar_tela_edicao_usuarios(
        frame_editar_usuario, imagens_dict["EditarUsuario"], int(id)
    )
    notebook.add(frame_editar_usuario, text="Editar Usuário")
    notebook.select(frame_editar_usuario)
    notebook.bind(
        "<<NotebookTabChanged>>",
        lambda event: fechar_aba_ao_sair(notebook, frame_editar_usuario),
        add="+",
    )


def abrir_aba_editar_rg(
    notebook: ttk.Notebook,
    imagens_dict: dict[str, dict],
    id: str,
):
    from Telas.EditarRG.editar import criar_tela_editar_rg

    if id == "":
        messagebox.showerror(
            "Nenhuma Reunião Selecionada", "Nenhuma reunião foi selecionada na tabela"
        )
        return

    frame_editar_rg = ttk.Frame(
        notebook, width=notebook.winfo_width(), height=notebook.winfo_height()
    )
    frame_editar_rg.pack(fill="both", expand=True)
    criar_tela_editar_rg(frame_editar_rg, imagens_dict["EditarRG"])
    notebook.add(frame_editar_rg, text="Editar RG")
    notebook.select(frame_editar_rg)
    notebook.bind(
        "<<NotebookTabChanged>>",
        lambda event: fechar_aba_ao_sair(notebook, frame_editar_rg),
        add="+",
    )


def abrir_aba_comecar_rg(notebook: ttk.Notebook, imagens_dict: dict[str, dict]):
    from Telas.ComeçarRG.começar import criar_tela_comecar_rg

    frame_comecar_rg = ttk.Frame(
        notebook, width=notebook.winfo_width(), height=notebook.winfo_height()
    )
    frame_comecar_rg.pack(fill="both", expand=True)
    criar_tela_comecar_rg(
        frame_comecar_rg, imagens_dict["ComecarRG"], notebook, imagens_dict
    )
    if notebook.index("end") == 0:
        # Não existe nenhuma aba
        notebook.add(frame_comecar_rg, text="Começar RG")
    else:
        # Existe outra aba aberta então adicionamos no começo
        notebook.insert(0, frame_comecar_rg, text="Começar RG")
        notebook.select(frame_comecar_rg)


def fechar_aba_ao_sair(notebook: ttk.Notebook, frame: ttk.Frame):
    if notebook.index("current") != notebook.index(frame):
        notebook.unbind("<<NotebookTabChanged>>")
        notebook.bind(
            "<<NotebookTabChanged>>", lambda event: ao_trocar_aba(event, notebook)
        )
        notebook.forget(frame)


def atualizar_aba(aba_selecionada: str, frame_aba: ttk.Frame):
    frame_aba.focus_set()
    if aba_selecionada == "Consultar RG":
        frame_aba.event_generate("<F5>")
        print(f"Atualizando {aba_selecionada}")
    elif aba_selecionada == "Consultar Usuários":
        frame_aba.event_generate("<F5>")
        print(f"Atualizando {aba_selecionada}")
    elif aba_selecionada == "Exportar":
        frame_aba.event_generate("<F5>")
        print(f"Atualizando {aba_selecionada}")


def ao_trocar_aba(event, notebook: ttk.Notebook):
    aba_selecionada = notebook.tab(notebook.select(), "text")
    frame_aba = notebook.nametowidget(notebook.select())
    atualizar_aba(aba_selecionada, frame_aba)
