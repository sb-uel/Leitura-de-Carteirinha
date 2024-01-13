from tkinter import ttk
import tkinter as tk
from Telas.defs import *
from cruds.Curso import consultar_cursos


def cria_menu_cursos(frame: ttk.Frame, id_curso_var: tk.StringVar, x : int, y : int):
    # Menu de seleção
    cursos_dict = {}

    # Função a ser chamada quando o menu for acionado
    def atualizar_menu_cursos():
        # Atualizar os valores do Combobox
        nonlocal cursos_dict
        cursos = consultar_cursos()
        menu_cursos["values"] = [curso[1] for curso in cursos]
        # Criar um dicionário para mapear nomes de cursos para IDs
        cursos_dict = {curso[1]: curso[0] for curso in cursos}

    # Função para obter o id do curso selecionado
    def obter_id_curso_selecionado():
        nonlocal id_curso_var
        curso_selecionado = menu_cursos.get()
        id_curso_selecionado = cursos_dict.get(curso_selecionado)
        id_curso_var.set(id_curso_selecionado)

    menu_cursos = ttk.Combobox(
        frame,
        font=(FONTE_INPUT, 25, "bold"),
        state="readonly",
        postcommand=lambda: atualizar_menu_cursos(),
        width=21,
    )
    menu_cursos.place(x=x, y=y)
    menu_cursos.option_add("*TCombobox*Listbox*Font", (FONTE_INPUT, 16))
    menu_cursos.bind("<<ComboboxSelected>>", lambda event: obter_id_curso_selecionado())
    atualizar_menu_cursos()
    
    return menu_cursos

