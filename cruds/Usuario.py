import re
from tkinter import messagebox

from cruds.Conexao import Conexao


def validar_campos(n_carteirinha: str, nome: str, email: str):
    email_pattern = r"[^@ \t\r\n]+@[^@ \t\r\n]+\.[^@ \t\r\n]+"
    if not (n_carteirinha.strip() and nome.strip()):
        messagebox.showerror(
            "Erro de validação", "Todos os campos obrigatórios devem ser preenchidos."
        )
        return False
    elif email is not None and not re.match(email_pattern, email) and email.strip():
        messagebox.showerror("Erro de validação", "O e-mail inserido não é válido.")
        return False
    elif not (n_carteirinha.isdigit() and len(n_carteirinha) >= 10):
        messagebox.showerror(
            "Erro de validação", "O número da carteirinha inserido não é válido."
        )
        return False
    return True


def cadastrar_usuario(
    n_carteirinha: str | int,
    nome: str,
    email: str,
    id_curso: int,
    show_msg: bool = True,
):
    if not isinstance(n_carteirinha, str):
        n_carteirinha = str(n_carteirinha)
    if not validar_campos(n_carteirinha, nome, email):
        return
    n_matricula = n_carteirinha[:10]

    sql = (
        "INSERT INTO usuarios (n_carteirinha, n_matricula, nome, email, id_curso)"
        "VALUES(%s,%s,%s,%s,%s)"
    )
    values = (n_carteirinha, n_matricula, nome, email, id_curso)
    conn = Conexao.get_conexao()
    try:
        with conn.cursor() as cursor:
            cursor.execute(sql, values)
        if show_msg:
            messagebox.showinfo(
                title="Cadastro bem sucedido",
                message="O usuário foi cadastrado com sucesso!",
            )
    except Exception as e:
        messagebox.showerror(title="Erro ao inserir usuário no banco", message=e)


def consultar_usuarios(termo: str = None):
    print("EXECUTADO SELECT USUARIOS")
    conn = Conexao.get_conexao()
    sql = (
        "SELECT u.id_usuario, u.nome, u.n_matricula, c.curso FROM usuarios u "
        "INNER JOIN cursos c ON u.id_curso = c.id_curso"
    )
    params = None
    if termo is not None and termo.strip() != "":
        sql += " WHERE u.nome LIKE %s"
        params = (f"%{termo}%",)
    sql += " ORDER BY u.nome"
    try:
        with conn.cursor() as cursor:
            cursor.execute(sql, params)
            resultados = cursor.fetchall()
        return resultados
    except Exception as e:
        messagebox.showerror(title="Erro ao obter usuários", message=e)


def consultar_usuario_pelo_id(id: int):
    print(f"EXECUTADO SELECT USUARIO ID={id}")
    conn = Conexao.get_conexao()
    sql = (
        "SELECT u.nome, u.n_carteirinha, u.email, c.curso "
        "FROM usuarios u "
        "INNER JOIN cursos c ON u.id_curso = c.id_curso "
        "WHERE u.id_usuario = %s"
    )
    try:
        with conn.cursor() as cursor:
            cursor.execute(sql, (id,))
            resultados = cursor.fetchone()
        return resultados
    except Exception as e:
        messagebox.showerror(title="Erro ao obter usuários", message=e)


def atualizar_usuario(id_usuario, n_carteirinha, nome, email, id_curso):
    if not validar_campos(n_carteirinha, nome, email):
        return
    n_matricula = n_carteirinha[:10]

    sql = (
        "UPDATE usuarios SET n_carteirinha = %s, n_matricula = %s, nome = %s, email = %s, id_curso = %s "
        "WHERE (id_usuario = %s)"
    )
    values = (n_carteirinha, n_matricula, nome, email, id_curso, id_usuario)
    conn = Conexao.get_conexao()
    try:
        with conn.cursor() as cursor:
            cursor.execute(sql, values)
        messagebox.showinfo(
            title="Edição bem sucedida",
            message="O usuário foi atualizado com sucesso!",
        )
    except Exception as e:
        messagebox.showerror(title="Erro ao atualizar o usuário no banco", message=e)


def deletar_usuarios(ids: list[int]):
    # Cria os placeholders com base no número de ids
    placeholders = ", ".join(["%s" for _ in ids])
    sql = f"DELETE FROM usuarios WHERE id_usuario IN ({placeholders})"

    conn = Conexao.get_conexao()
    try:
        with conn.cursor() as cursor:
            cursor.execute(sql, ids)
        messagebox.showinfo(
            title="Exclusão bem sucedida",
            message="Os usuários foram excluídos com sucesso!",
        )
    except Exception as e:
        messagebox.showerror(title="Erro ao excluir do banco", message=e)
