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
