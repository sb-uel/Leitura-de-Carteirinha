from tkinter import messagebox
from plyer import notification 
from cruds.Conexao import Conexao

def ler_carteirinha(n_carteirinha, id_reuniao):
    resultados = None

    # Verifica se existe um usuário com a carteirinha especificada
    print("EXECUTADO SELECT USUÁRIOS")
    conn = Conexao.get_conexao()
    sql = "SELECT `ID_Usuário` FROM `usuário` WHERE `N_Carteirinha` = %s"
    try:
        with conn.cursor() as cursor:
            cursor.execute(sql, (n_carteirinha,))
            resultados = cursor.fetchone()
    except Exception as e:
        messagebox.showerror(title="Erro ao verificar usuários", message=e)

    # Se existe então confirma presença
    if resultados:
        id_usuario = resultados[0]
        sql = "UPDATE `presenças` SET `Presente` = 1 WHERE (`ID_Usuário` = %s AND `ID_Reuniões` = %s)"
        try:
            with conn.cursor() as cursor:
                cursor.execute(sql, (id_usuario, id_reuniao))
                # Notifica que a presença foi confirmada
                notification.notify(
                    title="Presença confirmada",
                    message="A presença foi confirmada",
                    timeout=2,
                )
        except Exception as e:
            messagebox.showerror(title="Erro ao contabilizar presença", message=e)
    else:
        messagebox.showwarning(
            title="Usuário não cadastrado",
            message="Este número de carteirinha não foi encontrado no sistema",
        )

def consultar_presencas_pelo_id(id_reuniao: int):
    print(f"EXECUTANDO SELECT PRESENCAS -> REUNIAO ID={id_reuniao}")
    conn = Conexao.get_conexao()
    sql = (
        "SELECT u.ID_Usuário, u.Nome, c.Curso, p.Presente "
        "FROM presenças p "
        "INNER JOIN usuário u ON p.ID_Usuário = u.ID_Usuário "
        "INNER JOIN curso c ON u.ID_Curso = c.ID_Curso "
        "WHERE p.ID_Reuniões = %s"
    )
    try:
        with conn.cursor() as cursor:
            cursor.execute(sql, (id_reuniao,))
            resultados = cursor.fetchall()
        return resultados
    except Exception as e:
        messagebox.showerror(title="Erro ao obter reunião", message=e)
        
def atualizar_presencas(id_reuniao: int, presencas: list):
    conn = Conexao.get_conexao()
    sql = "UPDATE presencas SET Presente = CASE ID_Usuário "
    placeholders = []

    for id_usuario, presente in presencas:
        sql += "WHEN %s THEN %s "
        placeholders.extend([id_usuario, presente])

    sql += "END WHERE ID_Reunioes = %s"
    placeholders.append(id_reuniao)
    try:
        with conn.cursor() as cursor:
            cursor.execute(sql, placeholders)
    except Exception as e:
        messagebox.showerror(title="Erro ao atualizar presenças", message=e)