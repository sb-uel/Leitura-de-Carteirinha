from tkinter import messagebox
from cruds.Conexao import Conexao


def cadastrar_usuario(n_carteirinha, nome, email, id_curso):
    n_matricula = n_carteirinha[:10]
    query = (
        "INSERT INTO `usuário` (`N_Carteirinha`, `N_Matricula`, `Nome`, `Email`, `ID_Curso`)"
        "VALUES(%s,%s,%s,%s,%s)"
    )
    values = (n_carteirinha, n_matricula, nome, email, id_curso)
    conn = Conexao.get_conexao()
    try:
        with conn.cursor() as cursor:
            cursor.execute(query, values)
        messagebox.showinfo(
            title="Cadastro bem sucedido",
            message="O usuário foi cadastrado com sucesso!",
        )
    except Exception as e:
        messagebox.showerror(title="Erro ao inserir usuário no banco", message=e)


def consultar_usuario():
    ...


def atualizar_usuario():
    ...


def deletar_usuario():
    ...
