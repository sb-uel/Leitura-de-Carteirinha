from datetime import date
from tkinter import messagebox

from cruds.Conexao import Conexao
from cruds.Presenca import atualizar_presencas_pela_reuniao, deletar_presencas


def cadastrar_reuniao(data_reuniao : date = None, show_msg = True):
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


def consultar_reunioes(data: date = None):
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


def consultar_reuniao_pelo_id(id: int):
    print(f"EXECUTANDO SELECT REUNIAO ID={id}")
    conn = Conexao.get_conexao()
    sql = "SELECT data FROM reunioes WHERE id_reuniao = %s"
    try:
        with conn.cursor() as cursor:
            cursor.execute(sql, (id,))
            resultados = cursor.fetchone()
        return resultados[0]
    except Exception as e:
        messagebox.showerror(title="Erro ao obter reunião", message=e)


def buscar_reuniao(data_inicial: date, data_final: date):
    conn = Conexao.get_conexao()
    sql = "SELECT id_reuniao,data FROM reunioes WHERE data BETWEEN %s AND %s ORDER BY data"
    try:
        with conn.cursor() as cursor:
            cursor.execute(sql, (data_inicial, data_final))
            resultados = cursor.fetchall()
        return resultados
    except Exception as e:
        messagebox.showerror(title="Erro ao obter reuniões", message=e)


def exportar_reuniao(data_inicial: date, data_final: date):
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


def atualizar_reuniao(id_reuniao: int, presencas: list, data: date):
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
