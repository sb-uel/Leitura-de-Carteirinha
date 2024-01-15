from tkinter import messagebox
from cruds.Conexao import Conexao
from datetime import date

from cruds.Presenca import atualizar_presencas_pela_reuniao, deletar_presencas


def cadastrar_reuniao():
    data_atual = date.today()
    resultados = None

    # Verifica se já não existe uma reunião com a data de hoje
    print("EXECUTADO SELECT REUNIOES")
    conn = Conexao.get_conexao()
    sql = "SELECT `ID_Reuniões` FROM `reuniões` WHERE `Data` = %s"
    try:
        with conn.cursor() as cursor:
            cursor.execute(sql, (data_atual,))
            resultados = cursor.fetchone()
    except Exception as e:
        messagebox.showerror(title="Erro ao obter reuniões", message=e)

    # Se existir pergunte ao usuário se deseja continuar a partir dela, caso não exista crie uma nova
    if resultados:
        resposta = messagebox.askyesno(
            "Reunião existente",
            f"Já existe uma reunião com a data de hoje {data_atual.strftime('%d/%m/%Y')}\nDeseja continuar a partir dela?",
        )
        if resposta:
            return resultados[0]
        else:
            return None
    else:
        sql = "INSERT INTO `reuniões` (`Data`) VALUES (%s)"
        id_inserido = None
        try:
            with conn.cursor() as cursor:
                cursor.execute(sql, (data_atual,))
                id_inserido = cursor.lastrowid
                # Inicializa com os ids presentes na tabela usuário e com as presenças como falso (0)
                # E usando o id da reunião criada anteriormente
                sql = (
                    "INSERT INTO `presenças` (`ID_Usuário`, `Presente`, `ID_Reuniões`)"
                    "SELECT `ID_Usuário`, 0, %s FROM `usuário`"
                )
                cursor.execute(sql, (id_inserido,))
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
        "SELECT r.ID_Reuniões, r.Data, COUNT(p.ID_Presenças) AS TotalPresencas "
        "FROM reuniões r LEFT JOIN presenças p ON r.ID_Reuniões = p.ID_Reuniões AND p.Presente = 1 "
    )
    params = None
    if data is not None:
        sql += " WHERE r.Data = %s"
        sql += "GROUP BY r.ID_Reuniões, r.Data"
        params = (data,)
    else:
        sql += "GROUP BY r.ID_Reuniões, r.Data ORDER BY Data"
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
    sql = "SELECT Data FROM reuniões WHERE ID_Reuniões = %s"
    try:
        with conn.cursor() as cursor:
            cursor.execute(sql, (id,))
            resultados = cursor.fetchone()
        return resultados[0]
    except Exception as e:
        messagebox.showerror(title="Erro ao obter reunião", message=e)


def buscar_reuniao(data_inicial: date, data_final: date):
    conn = Conexao.get_conexao()
    sql = "SELECT ID_Reuniões,Data FROM reuniões WHERE Data BETWEEN %s AND %s"
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
        "SELECT u.N_Matricula, u.Nome, SUM(p.Presente) AS TotalPresencas "
        "FROM usuário u "
        "LEFT JOIN presenças p ON u.ID_Usuário = p.ID_Usuário "
        "LEFT JOIN reuniões r ON p.ID_Reuniões = r.ID_Reuniões "
        "WHERE r.Data BETWEEN %s AND %s GROUP BY u.N_Matricula, u.Nome"
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
    sql = "UPDATE reuniões SET Data = %s WHERE (ID_Reuniões = %s)"
    try:
        with conn.cursor() as cursor:
            cursor.execute(sql, (data, id_reuniao))
        messagebox.showinfo("Reunião Salva", message="Reunião salva com sucesso!")
    except Exception as e:
        messagebox.showerror(title="Erro ao salvar reunião", message=e)


def deletar_reunioes(id_reuniao: int):
    conn = Conexao.get_conexao()
    deletar_presencas(id_reuniao)
    sql = "DELETE FROM reuniões WHERE ID_Reuniões = %s"
    try:
        with conn.cursor() as cursor:
            cursor.execute(sql, (id_reuniao,))
        messagebox.showinfo(
            "Reunião Deletada", message="Reunião e presenças deletadas com sucesso!"
        )
    except Exception as e:
        messagebox.showerror(title="Erro ao deletar reunião", message=e)
