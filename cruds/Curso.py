from tkinter import messagebox

import mysql.connector as mysql

from cruds.Conexao import Conexao


def consultar_cursos() -> list[tuple[int, str]]:
    """
    Consulta todos os cursos disponíveis no banco de dados.

    Returns:
        list: Uma lista de tuplas, onde cada tupla contém um id de curso e o nome do curso.
            Exemplo: [(1, 'Ciência da Computação'), (2, 'Engenharia Elétrica'), ...]
    """
    print("EXECUTADO SELECT CURSOS")
    conn = Conexao.get_conexao()
    try:
        with conn.cursor() as cursor:
            cursor.execute("SELECT id_curso, curso FROM cursos")
            resultados = cursor.fetchall()
        return resultados
    except Exception as e:
        messagebox.showerror(title="Erro ao obter cursos", message=e)
