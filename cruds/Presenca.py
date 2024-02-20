from tkinter import messagebox

from plyer import notification

from cruds.Conexao import Conexao


def ler_carteirinha(n_carteirinha: str, id_reuniao: int, show_notif: bool = True):
    """
    Verifica se um usuário com o número da carteirinha especificada está cadastrado no sistema e, 
    se estiver, confirma sua presença em uma reunião.

    Args:
        n_carteirinha (str): O número da carteirinha do usuário.
        id_reuniao (int): O id da reunião na qual a presença será confirmada.
        show_notif (bool, optional): Se True, uma notificação será exibida quando a presença for confirmada. Padrão é True.
    """
    resultados = None

    # Verifica se existe um usuário com a carteirinha especificada
    print("EXECUTADO SELECT USUÁRIOS")
    conn = Conexao.get_conexao()
    sql = "SELECT id_usuario,nome FROM usuarios WHERE n_carteirinha = %s"
    try:
        with conn.cursor() as cursor:
            cursor.execute(sql, (n_carteirinha,))
            resultados = cursor.fetchone()
    except Exception as e:
        messagebox.showerror(title="Erro ao verificar usuários", message=e)

    # Se existe então confirma presença
    if resultados:
        id_usuario = resultados[0]
        sql = "UPDATE presencas SET presente = 1 WHERE (id_usuario = %s AND id_reuniao = %s)"
        try:
            with conn.cursor() as cursor:
                cursor.execute(sql, (id_usuario, id_reuniao))
                # Notifica que a presença foi confirmada
                if show_notif:
                    notification.notify(
                        title="Presença confirmada",
                        message=f"{resultados[1]} está presente!",
                        timeout=2,
                    )
        except Exception as e:
            messagebox.showerror(title="Erro ao contabilizar presença", message=e)
    else:
        messagebox.showwarning(
            title="Usuário não cadastrado",
            message=f"Este número de carteirinha não foi encontrado no sistema {n_carteirinha}",
        )


def consultar_presencas_pela_reuniao(id_reuniao: int) -> list[tuple[int, str, str, bool]]:
    """
    Consulta as presenças dos usuários em uma reunião específica.

    Args:
        id_reuniao (int): O id da reunião.

    Returns:
        list[tuple[int, str, str, bool]]: Uma lista de tuplas, onde cada tupla contém o id do usuário, o nome do usuário, 
        o curso do usuário e se o usuário estava presente ou não.
            Exemplo: [(1, 'João', 'Computação', True), (2, 'Maria', 'Elétrica', False), ...]
    """
    print(f"EXECUTANDO SELECT PRESENCAS -> REUNIAO ID={id_reuniao}")
    conn = Conexao.get_conexao()
    sql = (
        "SELECT u.id_usuario, u.nome, c.curso, p.presente "
        "FROM presencas p "
        "INNER JOIN usuarios u ON p.id_usuario = u.id_usuario "
        "INNER JOIN cursos c ON u.id_curso = c.id_curso "
        "WHERE p.id_reuniao = %s ORDER BY u.nome"
    )
    try:
        with conn.cursor() as cursor:
            cursor.execute(sql, (id_reuniao,))
            resultados = cursor.fetchall()
        return resultados
    except Exception as e:
        messagebox.showerror(title="Erro ao obter reunião", message=e)



def consultar_dias_presentes(id_usuario: int) -> int:
    """
    Recebe o id do usuário e contabiliza o total de dias presentes dele 
    e retorna a quantidade desses dias.
    
    Args:
        id_usuario (int): O id do usuário

    Returns:
        int: Retorna o número de dias presentes deste usuário
    """
    print(f"CONTANDO DIAS PRESENTES ID={id_usuario}")
    conn = Conexao.get_conexao()
    sql = (
        "SELECT COUNT(DISTINCT id_reuniao) AS TotalPresenças "
        "FROM presencas WHERE id_usuario = %s AND presente = 1"
    )
    try:
        with conn.cursor() as cursor:
            cursor.execute(sql, (id_usuario,))
            resultados = cursor.fetchone()
        return resultados[0]
    except Exception as e:
        messagebox.showerror(title="Erro ao obter número de presenças", message=e)


def atualizar_presencas_pela_reuniao(id_reuniao: int, presencas: list[tuple[int,bool]]):
    """
    Atualiza as presenças dos usuários de uma determinada reunião

    Args:
        id_reuniao (int): ID da reunião a ser atualizada
        presencas (list[tuple[int,bool]]): Uma lista de tuplas com os ids dos usuários e seus respectivos estados de presença
            Exemplo: [(1, True), (2, False), ...]
    """
    conn = Conexao.get_conexao()
    sql = "UPDATE presencas SET presente = CASE id_usuario "  # Atualize a tabela presenças nos seguintes casos
    placeholders = []

    for id_usuario, presente in presencas:
        sql += "WHEN %s THEN %s "  # Quando o id do usuário for ... então presente = ...
        placeholders.extend([id_usuario, presente])

    sql += "END WHERE id_reuniao = %s"  # Onde id da reunião for ...
    placeholders.append(id_reuniao)
    try:
        with conn.cursor() as cursor:
            cursor.execute(sql, placeholders)
    except Exception as e:
        messagebox.showerror(title="Erro ao atualizar presenças", message=e)


def atualizar_presencas_pelo_usuario(id_usuario: int, presencas: list[tuple[int,bool]]):
    """
    Atualiza as presenças de um determinado usuário nas reuniões

    Args:
        id_reuniao (int): ID do usuário a ser atualizado
        presencas (list[tuple[int,bool]]): Uma lista de tuplas com os ids das reuniões e seus respectivos estados de presença
            Exemplo: [(1, True), (2, False), ...]
    """
    conn = Conexao.get_conexao()
    sql = "UPDATE presencas SET presente = CASE id_reuniao "  # Atualize a tabela presenças nos seguintes casos
    placeholders = []

    for id_reuniao, presente in presencas:
        sql += "WHEN %s THEN %s "  # Quando o id da reunião for ... então presente = ...
        placeholders.extend([id_reuniao, presente])

    sql += "END WHERE id_usuario = %s"  # Onde id do usuário for ...
    placeholders.append(id_usuario)
    try:
        with conn.cursor() as cursor:
            cursor.execute(sql, placeholders)
    except Exception as e:
        messagebox.showerror(title="Erro ao atualizar presenças", message=e)


def deletar_presencas_pela_reuniao(id_reuniao: int):
    """
    Deleta as presenças de uma determinada reunião

    Args:
        id_reuniao (int): O id da reunião a ser deletada
    """
    conn = Conexao.get_conexao()
    sql = "DELETE FROM presencas WHERE id_reuniao = %s"
    try:
        with conn.cursor() as cursor:
            cursor.execute(sql, (id_reuniao,))
    except Exception as e:
        messagebox.showerror(title="Erro ao deletar presenças", message=e)
        
def deletar_presencas_pelo_usuario(id_usuario: int):
    """
    Deleta as presenças de um determinado usuário

    Args:
        id_usuario (int): O id do usuário a ser deletado
    """
    conn = Conexao.get_conexao()
    sql = "DELETE FROM presencas WHERE id_usuario = %s"
    try:
        with conn.cursor() as cursor:
            cursor.execute(sql, (id_usuario,))
    except Exception as e:
        messagebox.showerror(title="Erro ao deletar presenças", message=e)
