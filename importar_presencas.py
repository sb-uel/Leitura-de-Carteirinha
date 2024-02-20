from openpyxl.worksheet.worksheet import Worksheet
from Telas.login.login import abrir_tela_login

from cruds.Conexao import Conexao
from cruds.Presenca import ler_carteirinha
from cruds.Reuniao import cadastrar_reuniao
from excel_functions import obtem_planilha_importacao

# CONSIDERA-SE QUE A PLANILHA NÃO TENHA CABEÇALHO E OS DADOS ESTEJAM DISPOSTOS ASSIM:
# |  Data RG      | Data RG      |  Data RG      |
# |  N_Carterinha | N_Carterinha |  N_Carterinha |
# |  N_Carterinha | N_Carterinha |  N_Carterinha |
# |  N_Carterinha | N_Carterinha |  N_Carterinha |
# |  N_Carterinha | N_Carterinha |  N_Carterinha |
# Data RG deve estar em formato DIA/MES/ANO ex: 23/01/2024
abrir_tela_login()
if Conexao.is_connected():
    planilha = obtem_planilha_importacao()
    aba: Worksheet = planilha.active
    for coluna in aba.iter_cols(values_only=True):
        data, *n_carteirinhas = coluna
        if data is None:
            break
        id_reuniao = cadastrar_reuniao(data, False)
        for n_carteirinha in n_carteirinhas:
            if n_carteirinha is not None:
                ler_carteirinha(n_carteirinha, id_reuniao, False)
            else:
                break
        print(data, n_carteirinhas)
Conexao.fechar_conexao()
