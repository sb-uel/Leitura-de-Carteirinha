from tkinter import messagebox
from cruds.Conexao import Conexao
import mysql.connector as mysql

def consultar_cursos():
    conn = Conexao.get_conexao()
    try:
        with conn.cursor() as cursor:
            cursor.execute("SELECT ID_Curso, Curso FROM curso")
            resultados = cursor.fetchall()
        return resultados
    except Exception as e:
        messagebox.showerror(title="Erro ao obter cursos", message=e)
