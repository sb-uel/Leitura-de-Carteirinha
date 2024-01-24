import json
import tkinter as tk
from tkinter import ttk
from tkinter import messagebox
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


def criar_widgets_login(root, credenciais):
    ttk.Label(root, text="IP:").grid(column=0, row=0, sticky=tk.W)
    ttk.Entry(root, width=30, textvariable=credenciais["ip"]).grid(
        column=1, row=0, sticky=tk.W
    )

    ttk.Label(root, text="Usuário:").grid(column=0, row=1, sticky=tk.W)
    ttk.Entry(root, width=30, textvariable=credenciais["usuario"]).grid(
        column=1, row=1, sticky=tk.W
    )

    ttk.Label(root, text="Senha:").grid(column=0, row=2, sticky=tk.W)
    ttk.Entry(root, width=30, textvariable=credenciais["senha"], show="*").grid(
        column=1, row=2, sticky=tk.W
    )

    ttk.Label(root, text="DB Name:").grid(column=0, row=3, sticky=tk.W)
    ttk.Entry(root, width=30, textvariable=credenciais["db_name"]).grid(
        column=1, row=3, sticky=tk.W
    )

    ttk.Checkbutton(
        root,
        text="Lembrar de mim",
        variable=credenciais["remember_me"],
    ).grid(column=0, row=4, sticky=tk.W)

    ttk.Button(
        root,
        text="Logar",
        command=lambda: logar(root, credenciais),
    ).grid(column=1, row=4, sticky=tk.E)

    root.bind("<Return>", lambda event: logar(root, credenciais))

    for widget in root.winfo_children():
        widget.grid(padx=5, pady=5)


def logar(root, credenciais):
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


def abrir_tela_login():
    root = tk.Tk()
    root.title("Conectar ao banco")
    root.resizable(False, False)

    credenciais = {
        "ip": tk.StringVar(value="localhost"),
        "usuario": tk.StringVar(),
        "senha": tk.StringVar(),
        "db_name": tk.StringVar(value="ramoieee"),
        "remember_me": tk.StringVar(),
    }

    carregar_credenciais(credenciais)
    criar_widgets_login(root, credenciais)
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
