import re
from tkinter import messagebox
from cruds.Conexao import Conexao


def validar_campos(n_carteirinha: str, nome: str, email: str):
    email_pattern = r"[^@ \t\r\n]+@[^@ \t\r\n]+\.[^@ \t\r\n]+"
    if not (n_carteirinha.strip() and nome.strip() and email.strip()):
        messagebox.showerror(
            "Erro de validação", "Todos os campos devem ser preenchidos."
        )
        return False
    elif not re.match(email_pattern, email):
        messagebox.showerror("Erro de validação", "O e-mail inserido não é válido.")
        return False
    elif not (n_carteirinha.isdigit() and len(n_carteirinha) >= 10):
        messagebox.showerror(
            "Erro de validação", "O número da carteirinha inserido não é válido."
        )
        return False
    return True


def cadastrar_usuario(n_carteirinha, nome, email, id_curso):
    if not validar_campos(n_carteirinha, nome, email):
        return
    n_matricula = n_carteirinha[:10]

    sql = (
        "INSERT INTO `usuário` (`N_Carteirinha`, `N_Matricula`, `Nome`, `Email`, `ID_Curso`)"
        "VALUES(%s,%s,%s,%s,%s)"
    )
    values = (n_carteirinha, n_matricula, nome, email, id_curso)
    conn = Conexao.get_conexao()
    try:
        with conn.cursor() as cursor:
            cursor.execute(sql, values)
        messagebox.showinfo(
            title="Cadastro bem sucedido",
            message="O usuário foi cadastrado com sucesso!",
        )
    except Exception as e:
        messagebox.showerror(title="Erro ao inserir usuário no banco", message=e)


def consultar_usuarios(termo: str = None):
    print("EXECUTADO SELECT USUARIOS")
    conn = Conexao.get_conexao()
    sql = "SELECT `ID_Usuário`, `Nome`, `N_Matricula`, `Email` FROM `usuário`"
    params = None
    if termo is not None and termo.strip() != "":
        sql += " WHERE `Nome` LIKE %s"
        params = (f"%{termo}%",)
    sql += " ORDER BY `Nome`"
    try:
        with conn.cursor() as cursor:
            cursor.execute(sql, params)
            resultados = cursor.fetchall()
        return resultados
    except Exception as e:
        messagebox.showerror(title="Erro ao obter usuários", message=e)

def consultar_usuario(id : int):
    print(f"EXECUTADO SELECT USUARIO ID={id}")
    conn = Conexao.get_conexao()
    sql = "SELECT `ID_Usuário`, `Nome`, `N_Matricula`, `Email` FROM `usuário` WHERE `ID_Usuário` = %s"
    try:
        with conn.cursor() as cursor:
            cursor.execute(sql, (id,))
            resultados = cursor.fetchone()
        return resultados
    except Exception as e:
        messagebox.showerror(title="Erro ao obter usuários", message=e)

def atualizar_usuario():
    ...


def deletar_usuario():
    ...
