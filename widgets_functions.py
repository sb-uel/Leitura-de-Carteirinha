from tkinter import messagebox, ttk
import tkinter as tk
from Telas.defs import *
from cruds.Curso import consultar_cursos
from cruds.Usuario import consultar_usuario


def cria_menu_cursos(frame: ttk.Frame, id_curso_var: tk.StringVar):
    # Menu de seleção
    cursos_dict = {}

    # Função a ser chamada quando o menu for acionado
    def atualizar_menu_cursos(event=None):
        # Atualizar os valores do Combobox
        nonlocal cursos_dict
        cursos = consultar_cursos()
        menu_cursos["values"] = [curso[1] for curso in cursos]
        # Criar um dicionário para mapear nomes de cursos para IDs
        cursos_dict = {curso[1]: curso[0] for curso in cursos}

    # Função para obter o id do curso selecionado
    def obter_id_curso_selecionado(event=None):
        nonlocal id_curso_var
        curso_selecionado = menu_cursos.get()
        id_curso_selecionado = cursos_dict.get(curso_selecionado)
        id_curso_var.set(id_curso_selecionado)

    menu_cursos = ttk.Combobox(
        frame,
        font=(FONTE_INPUT, 25, "bold"),
        state="readonly",
        postcommand=atualizar_menu_cursos,
        width=21,
    )
    menu_cursos.place(x=199, y=430)
    menu_cursos.option_add("*TCombobox*Listbox*Font", (FONTE_INPUT, 16))
    menu_cursos.bind("<<ComboboxSelected>>", obter_id_curso_selecionado)


def cria_tabela_usuarios(frame_pai: ttk.Frame):
    global tabela  # Torna a variável global

    # Novo Frame para conter a tabela e a barra de rolagem
    frame_tabela = ttk.Frame(frame_pai)
    frame_tabela.place(x=36.0, y=185.0, width=1015.0, height=550.0, anchor="nw")

    tabela = ttk.Treeview(
        frame_tabela, columns=("nome", "matrícula"), show="headings"
    )
    tabela.heading("nome", text="Nome")
    tabela.heading("matrícula", text="Matrícula")
    tabela.grid(row=0, column=0, sticky="nsew")

    def atualizar_tabela(event=None):
        # Limpa os dados existentes na tabela
        tabela.delete(*tabela.get_children())

        # Obtém novos dados da função consultar_usuario
        usuarios = consultar_usuario()

        # Insere os novos dados na tabela
        for id, nome, matricula in usuarios:
            tabela.insert("", tk.END, iid=id, values=(nome, matricula))

    def obter_iid_selecionado(event):
        iid_selecionado = tabela.focus()
        print("IID do item selecionado:", iid_selecionado)
    
    # Adiciona o bind a função de recarregar a tabela
    frame_pai.bind("<F5>", atualizar_tabela)
    tabela.bind("<<TreeviewSelect>>",obter_iid_selecionado)
    # Adiciona uma barra de rolagem
    scrollbar = ttk.Scrollbar(frame_tabela, orient=tk.VERTICAL, command=tabela.yview)
    scrollbar.grid(row=0, column=1, sticky="ns")
    tabela.configure(yscrollcommand=scrollbar.set)

    # Configuração para expandir a tabela e a barra de rolagem com o tamanho do frame_tabela
    frame_tabela.columnconfigure(0, weight=1)
    frame_tabela.rowconfigure(0, weight=1)
