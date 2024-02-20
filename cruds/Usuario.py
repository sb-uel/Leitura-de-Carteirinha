import re
from tkinter import messagebox

from cruds.Conexao import Conexao


def validar_campos(n_carteirinha: str, nome: str, email: str) -> bool:
    """
    Valida os campos de entrada do formulário.

    Args:
        n_carteirinha (str): Número da carteirinha
        nome (str): Nome completo
        email (str): Email do usuário

    Returns:
        bool: Retorna True se todos os campos estiverem preenchidos corretamente e False caso algum
        campo esteja inválido e além disso exibe uma messagebox específica para cada campo
    """
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
    """
    Cadastra um novo usuário no banco de dados.

    Args:
        n_carteirinha (str | int): Número da carteirinha
        nome (str): Nome do usuário
        email (str): Email do usuário
        id_curso (int): Id do curso do usuário
        show_msg (bool, optional): Define se é mostrada uma messagebox ao usuário quando é
        efetivada com sucesso a operação. Padrão é True.
    """
    if not isinstance(n_carteirinha, str):
        n_carteirinha = str(n_carteirinha)
    if not validar_campos(n_carteirinha, nome, email):
        return
    n_matricula = n_carteirinha[:10]

    sql = (
        "INSERT INTO usuarios (n_carteirinha, n_matricula, nome, email, id_curso)"
        "VALUES(%s,%s,%s,%s,%s)"
    )
    values = (n_carteirinha, f"20{n_matricula}", nome, email, id_curso)
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


def consultar_usuarios(termo: str = None) -> list[tuple[int, str, str, str]]:
    """
    Retorna todos os usuários ou apenas os usuários pesquisados.

    Args:
        termo (str, optional): Nome do usuário a ser pesquisado. Padrão é None.

    Returns:
        list[tuple[int,str,str,str]]:  Uma lista de tuplas contendo o id, nome, número de matrícula e o nome do curso
        dos usuários.
            Exemplo:  [(id,"Nome","Número de matrícula","Curso"),...]
    """
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


def consultar_usuario_pelo_id(id: int) -> list[tuple[str, str, str, str]]:
    """
    Busca um usuário pelo seu id.

    Args:
        id (int): Id do usuário a ser consultado

    Returns:
        list[tuple[str,str,str,str]]: Retorna uma lista de tuplas contendo o nome do usuário o número de carteirinha
        o email do usuário e o nome do curso
    """
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


def atualizar_usuario(
    id_usuario: int, n_carteirinha: str, nome: str, email: str, id_curso: int
):
    """
    Atualiza o usuário do id especificado com os dados fornecidos

    Args:
        id_usuario (int): Id do usuário a ser atualizado
        n_carteirinha (str): Número da carteirinha
        nome (str): Nome do usuário
        email (str): Email do usuário
        id_curso (int): Id do curso do usuário
    """
    if not validar_campos(n_carteirinha, nome, email):
        return
    n_matricula = n_carteirinha[:10]

    sql = (
        "UPDATE usuarios SET n_carteirinha = %s, n_matricula = %s, nome = %s, email = %s, id_curso = %s "
        "WHERE (id_usuario = %s)"
    )
    values = (n_carteirinha, f"20{n_matricula}", nome, email, id_curso, id_usuario)
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
    """
    Deleta todos usuários especificados pelo id dentro da lista

    Args:
        ids (list[int]): Lista contendo o id de todos os usuários a serem deletados
    """
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
