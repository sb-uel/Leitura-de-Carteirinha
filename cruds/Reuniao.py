from tkinter import messagebox
from cruds.Conexao import Conexao
from datetime import date


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
        sql +=  "GROUP BY r.ID_Reuniões, r.Data"
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
    ...


def atualizar_reuniao():
    ...


def deletar_reunioes(ids: list[int]):
    ...
