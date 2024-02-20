from datetime import date
from tkinter import messagebox

from cruds.Conexao import Conexao
from cruds.Presenca import atualizar_presencas_pela_reuniao, deletar_presencas


def cadastrar_reuniao(data_reuniao: date = None, show_msg: bool = True) -> int:
    """
    Cadastra a reunião com a data de hoje, caso não seja especificada, e retorna o id da reunião criada.

    Args:
        data_reuniao (date, optional): Data da reunião a ser criada. Padrão é None.
        show_msg (bool, optional): Define se exibe uma messagebox ao usuário ou não. Padrão é True.

    Returns:
        int: Retorna o id da reunião criada no banco de dados
    """
    if data_reuniao is None:
        data_reuniao = date.today()
    resultados = None

    # Verifica se já não existe uma reunião com a data de hoje
    print("EXECUTADO SELECT REUNIOES")
    conn = Conexao.get_conexao()
    sql = "SELECT id_reuniao FROM reunioes WHERE data = %s"
    try:
        with conn.cursor() as cursor:
            cursor.execute(sql, (data_reuniao,))
            resultados = cursor.fetchone()
    except Exception as e:
        messagebox.showerror(title="Erro ao obter reuniões", message=e)

    # Se existir pergunte ao usuário se deseja continuar a partir dela, caso não exista crie uma nova
    if resultados:
        resposta = messagebox.askyesno(
            "Reunião existente",
            f"Já existe uma reunião com a data de hoje {data_reuniao.strftime('%d/%m/%Y')}\nDeseja continuar a partir dela?",
        )
        if resposta:
            return resultados[0]
        else:
            return None
    else:
        sql = "INSERT INTO reunioes (data) VALUES (%s)"
        id_inserido = None
        try:
            with conn.cursor() as cursor:
                cursor.execute(sql, (data_reuniao,))
                id_inserido = cursor.lastrowid
                # Inicializa com os ids presentes na tabela usuário e com as presenças como falso (0)
                # E usando o id da reunião criada anteriormente
                sql = (
                    "INSERT INTO presencas (id_usuario, presente, id_reuniao)"
                    "SELECT id_usuario, 0, %s FROM usuarios"
                )
                cursor.execute(sql, (id_inserido,))
                if show_msg:
                    messagebox.showinfo(
                        title="Reunião iniciada",
                        message="Reunião iniciada com sucesso!",
                    )
                return id_inserido
        except Exception as e:
            messagebox.showerror(title="Erro ao iniciar reunião", message=e)


def consultar_reunioes(data: date = None) -> list[tuple[int, date, int]]:
    """
    Consulta as reuniões no banco de dados.

    Args:
        data (date, optional): Se informado pesquisa pela data especificada. Padrão é None.

    Returns:
        list[tuple[int, date, int]]: Retorna uma lista de tuplas contendo o id da reunião, a data da reunião e
        o número de presenças da reunião
            Exemplo: [(1, '2022-05-30', 23), ...]
    """
    print("EXECUTANDO SELECT REUNIOES + PRESENCAS")
    conn = Conexao.get_conexao()
    sql = (
        "SELECT r.id_reuniao, r.data, COUNT(p.id_presenca) AS TotalPresencas "
        "FROM reunioes r LEFT JOIN presencas p ON r.id_reuniao = p.id_reuniao AND p.presente = 1 "
    )
    params = None
    if data is not None:
        sql += " WHERE r.data = %s"
        sql += "GROUP BY r.id_reuniao, r.data"
        params = (data,)
    else:
        sql += "GROUP BY r.id_reuniao, r.data ORDER BY data"
    try:
        with conn.cursor() as cursor:
            cursor.execute(sql, params)
            resultados = cursor.fetchall()
        return resultados
    except Exception as e:
        messagebox.showerror(title="Erro ao obter reuniões", message=e)


def consultar_reuniao_pelo_id(id_reuniao: int) -> date:
    """
    Retorna a data da reunião pelo id

    Args:
        id_reuniao (int): O id da reunião

    Returns:
        date: Data da reunião do id informado
    """
    print(f"EXECUTANDO SELECT REUNIAO ID={id_reuniao}")
    conn = Conexao.get_conexao()
    sql = "SELECT data FROM reunioes WHERE id_reuniao = %s"
    try:
        with conn.cursor() as cursor:
            cursor.execute(sql, (id_reuniao,))
            resultados = cursor.fetchone()
        return resultados[0]
    except Exception as e:
        messagebox.showerror(title="Erro ao obter reunião", message=e)


def buscar_reuniao(data_inicial: date, data_final: date) -> list[tuple[int, date]]:
    """
    Busca todas as reuniões de um determinado período

    Args:
        data_inicial (date): Data inicial para filtragem
        data_final (date): Data final para filtragem

    Returns:
        list[tuple[int,date]]:  Uma lista com os ids e datas das reuniões encontradas no intervalo informado
            Exemplo:  [(1,'2022-05-30'),(2,'2022-06-14')]
    """
    conn = Conexao.get_conexao()
    sql = "SELECT id_reuniao,data FROM reunioes WHERE data BETWEEN %s AND %s ORDER BY data"
    try:
        with conn.cursor() as cursor:
            cursor.execute(sql, (data_inicial, data_final))
            resultados = cursor.fetchall()
        return resultados
    except Exception as e:
        messagebox.showerror(title="Erro ao obter reuniões", message=e)


def exportar_reuniao(
    data_inicial: date, data_final: date
) -> list[tuple[int, str, int]]:
    """
    Consulta todos os dados da tabela reuniões entre a data inicial e a data final

    Args:
        data_inicial (date): Data inicial para filtragem
        data_final (date): Data final para filtragem

    Returns:
        list[tuple[int, str, int]]: Uma lista de tuplas contendo o número de matrícula, o nome do participante
        e o número de presenças
            Exemplo:  [(111111111,'Maria',10), (222222222,'João',8)]
    """
    conn = Conexao.get_conexao()
    sql = (
        "SELECT u.n_matricula, u.nome, SUM(p.presente) AS TotalPresencas "
        "FROM usuarios u "
        "LEFT JOIN presencas p ON u.id_usuario = p.id_usuario "
        "LEFT JOIN reunioes r ON p.id_reuniao = r.id_reuniao "
        "WHERE r.data BETWEEN %s AND %s GROUP BY u.n_matricula, u.nome ORDER BY r.data"
    )
    try:
        with conn.cursor() as cursor:
            cursor.execute(sql, (data_inicial, data_final))
            resultados = cursor.fetchall()
        return resultados
    except Exception as e:
        messagebox.showerror(title="Erro ao obter dados de exportação", message=e)


def atualizar_reuniao(id_reuniao: int, presencas: list[tuple[int, bool]], data: date):
    """
    Atualiza a reunião determinada pelo id com novos dados especificados

    Args:
        id_reuniao (int): O id da reunião a ser alterada
        presencas (list[tuple[int, bool]]): Uma lista de tuplas com os ids dos usuários e seus respectivos estados de presença
            Exemplo: [(1, True), (2, False), ...]
        data (date): A nova data da reunião
    """
    conn = Conexao.get_conexao()
    atualizar_presencas_pela_reuniao(id_reuniao, presencas)
    sql = "UPDATE reunioes SET data = %s WHERE (id_reuniao = %s)"
    try:
        with conn.cursor() as cursor:
            cursor.execute(sql, (data, id_reuniao))
        messagebox.showinfo("Reunião Salva", message="Reunião salva com sucesso!")
    except Exception as e:
        messagebox.showerror(title="Erro ao salvar reunião", message=e)


def deletar_reunioes(id_reuniao: int):
    """
    Deleta a reunião especificada pelo id

    Args:
        id_reuniao (int): O id da reunião a ser deletada
    """
    conn = Conexao.get_conexao()
    deletar_presencas(id_reuniao)
    sql = "DELETE FROM reunioes WHERE id_reuniao = %s"
    try:
        with conn.cursor() as cursor:
            cursor.execute(sql, (id_reuniao,))
        messagebox.showinfo(
            "Reunião Deletada", message="Reunião e presenças deletadas com sucesso!"
        )
    except Exception as e:
        messagebox.showerror(title="Erro ao deletar reunião", message=e)
