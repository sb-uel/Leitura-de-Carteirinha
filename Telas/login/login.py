import json
from pathlib import Path
import sys
import tkinter as tk
from tkinter import ttk
from tkinter import messagebox

ROOT_PATH = Path(__file__).parent.parent.parent
if str(ROOT_PATH) not in sys.path:
    sys.path.append(str(ROOT_PATH))
from cruds.Conexao import Conexao


def salvar_credenciais(credenciais: dict[str, tk.StringVar]):
    credenciais_serializaveis = {key: value.get() for key, value in credenciais.items()}
    with open("credenciais.json", "w") as file:
        json.dump(credenciais_serializaveis, file)


def carregar_credenciais(credenciais: dict[str, tk.StringVar]):
    try:
        with open("credenciais.json", "r") as file:
            credenciais_carregadas = json.load(file)
            for key, value in credenciais_carregadas.items():
                credenciais[key].set(value)
    except FileNotFoundError:
        # Se não encontrou é porque não tem salvo
        pass


def validar_login(ip, usuario, senha, db_name):
    if not ip or not usuario or not senha or not db_name:
        messagebox.showerror("Erro de Login", "Por favor, preencha todos os campos.")
        return False
    return True


def abrir_tela_login():
    root = tk.Tk()
    root.title("Conectar ao banco")
    root.resizable(False, False)

    # Variáveis para armazenar os valores dos campos de entrada
    credenciais = {
        "ip": tk.StringVar(value="localhost"),
        "usuario": tk.StringVar(),
        "senha": tk.StringVar(),
        "db_name": tk.StringVar(value="ramoieee"),
        "remember_me": tk.StringVar(),
    }

    # Tenta carregar as credenciais salvas
    carregar_credenciais(credenciais)

    # Input IP
    ttk.Label(root, text="IP:").grid(column=0, row=0, sticky=tk.W)
    ip_input = ttk.Entry(root, width=30, textvariable=credenciais["ip"])
    ip_input.grid(column=1, row=0, sticky=tk.W)

    # Input Usuário
    ttk.Label(root, text="Usuario:").grid(column=0, row=1, sticky=tk.W)
    user_input = ttk.Entry(root, width=30, textvariable=credenciais["usuario"])
    user_input.grid(column=1, row=1, sticky=tk.W)

    # Input Senha
    ttk.Label(root, text="Senha:").grid(column=0, row=2, sticky=tk.W)
    password_input = ttk.Entry(
        root, width=30, textvariable=credenciais["senha"], show="*"
    )
    password_input.grid(column=1, row=2, sticky=tk.W)

    # Input Nome do Banco
    ttk.Label(root, text="DB Name:").grid(column=0, row=3, sticky=tk.W)
    db_name_input = ttk.Entry(root, width=30, textvariable=credenciais["db_name"])
    db_name_input.grid(column=1, row=3, sticky=tk.W)

    # Lembrar de mim
    remember_me_check = ttk.Checkbutton(
        root,
        text="Lembrar de mim",
        variable=credenciais["remember_me"],
    )
    remember_me_check.grid(column=0, row=4, sticky=tk.W)

    # Função do botão de login
    def logar():
        ip = credenciais["ip"].get()
        usuario = credenciais["usuario"].get()
        senha = credenciais["senha"].get()
        db_name = credenciais["db_name"].get()

        if validar_login(ip, usuario, senha, db_name):
            Conexao.configurar(
                host=ip,
                user=usuario,
                password=senha,
                db_name=db_name,
            )
            if Conexao.is_connected():
                if credenciais["remember_me"].get():
                    salvar_credenciais(credenciais)
                root.destroy()

    # Botão de login
    btn = ttk.Button(root, text="Logar", command=logar)
    btn.grid(column=1, row=4, sticky=tk.E)
    root.bind("<Return>", lambda event: btn.invoke())

    # Adiciona espaçamento para cada widget
    for widget in root.winfo_children():
        widget.grid(padx=5, pady=5)

    centraliza_janela(root)

    root.mainloop()


def centraliza_janela(container: tk.Tk):
    # Atualiza a janela para garantir que as informações estejam disponíveis
    container.update_idletasks()

    # Calcula a posição centralizada
    largura_tela = container.winfo_screenwidth()
    altura_tela = container.winfo_screenheight()

    # Obtém as dimensões reais da janela
    largura_janela = container.winfo_width()
    altura_janela = container.winfo_height()

    # Calcula a posição centralizada
    pos_x = (largura_tela - largura_janela) // 2
    pos_y = (altura_tela - altura_janela) // 2

    # Define a geometria da janela
    container.geometry(f"+{pos_x}+{pos_y}")
