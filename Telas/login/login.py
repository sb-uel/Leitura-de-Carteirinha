from pathlib import Path
import sys
import tkinter as tk
from tkinter import ttk
from tkinter import messagebox

ROOT_PATH = Path(__file__).parent.parent.parent
if str(ROOT_PATH) not in sys.path:
    sys.path.append(str(ROOT_PATH))
from cruds.Conexao import Conexao


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
    ip_var = tk.StringVar()
    user_var = tk.StringVar()
    password_var = tk.StringVar()
    db_name_var = tk.StringVar()
    remember_me_var = tk.StringVar()

    # Input IP
    ttk.Label(root, text="IP:").grid(column=0, row=0, sticky=tk.W)
    ip_input = ttk.Entry(root, width=30, textvariable=ip_var)
    ip_input.grid(column=1, row=0, sticky=tk.W)

    # Input Usuário
    ttk.Label(root, text="Usuario:").grid(column=0, row=1, sticky=tk.W)
    user_input = ttk.Entry(root, width=30, textvariable=user_var)
    user_input.grid(column=1, row=1, sticky=tk.W)

    # Input Senha
    ttk.Label(root, text="Senha:").grid(column=0, row=2, sticky=tk.W)
    password_input = ttk.Entry(root, width=30, textvariable=password_var, show="*")
    password_input.grid(column=1, row=2, sticky=tk.W)

    # Input Nome do Banco
    ttk.Label(root, text="DB Name:").grid(column=0, row=3, sticky=tk.W)
    db_name_input = ttk.Entry(root, width=30, textvariable=db_name_var)
    db_name_input.grid(column=1, row=3, sticky=tk.W)

    # Lembrar de mim
    remember_me_check = ttk.Checkbutton(
        root,
        text="Lembrar de mim",
        variable=remember_me_var,
        command=lambda: print(remember_me_var.get()),
    )
    remember_me_check.grid(column=0, row=4, sticky=tk.W)

    # Função para lidar com o botão de login
    def logar():
        ip = ip_var.get()
        usuario = user_var.get()
        senha = password_var.get()
        db_name = db_name_var.get()

        if validar_login(ip, usuario, senha, db_name):
            Conexao.configurar(
                host=ip,
                user=usuario,
                password=senha,
                db_name=db_name,
            )
            if Conexao.is_connected():
                root.destroy()

    ttk.Button(root, text="Logar", command=logar).grid(column=1, row=4, sticky=tk.E)

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
