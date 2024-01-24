from openpyxl.worksheet.worksheet import Worksheet

from cruds.Conexao import Conexao
from cruds.Curso import consultar_cursos
from cruds.Usuario import cadastrar_usuario
from excel_functions import obtem_planilha_importacao
from Telas.login.login import abrir_tela_login

# CONSIDERA-SE QUE O CABEÇALHO DA PLANILHA ESTEJA PRESENTE E OS DADOS ESTEJAM DISPOSTOS ASSIM:
# | Nome | Número de Carteirinha | Curso | E-mail |

def obter_id_curso(nome_curso):
    for id_curso, nome in cursos.items():
        if nome == nome_curso:
            return id_curso

abrir_tela_login()
cursos = dict(consultar_cursos())
if Conexao.is_connected():
    planilha = obtem_planilha_importacao()
    aba : Worksheet = planilha.active
    for usuario in aba.iter_rows(max_col=4, values_only=True):
        nome, n_carteirinha, curso, email = usuario
        # Pula o cabeçalho
        if nome == "Nome":
            continue
        id_curso = obter_id_curso(curso)
        print(nome, n_carteirinha, id_curso, email)
        cadastrar_usuario(n_carteirinha,nome,email,id_curso,False)
Conexao.fechar_conexao()