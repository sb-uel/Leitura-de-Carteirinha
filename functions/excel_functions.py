from datetime import date
from pathlib import Path
from tkinter import filedialog, messagebox

import openpyxl

from cruds.Reuniao import exportar_reuniao


def exportar_presencas(local_de_salvamento: str, data_inicial: date, data_final: date):
    if local_de_salvamento == "":
        messagebox.showwarning(
            "Local de salvamento", "O local de salvamento não foi escolhido!"
        )
        return
    caminho_arquivo = Path(local_de_salvamento) / "presenças.xlsx"
    cabeçalhos = ["Nº de matrícula", "Nome", "Nº de presenças"]
    dados_banco = exportar_reuniao(data_inicial, data_final)

    _criar_planilha(caminho_arquivo, cabeçalhos, dados_banco)
    messagebox.showinfo(
        "Exportado com sucesso", f"O arquivo foi salvo em {caminho_arquivo}"
    )

def obtem_planilha_importacao():
    caminho_planilha = filedialog.askopenfilename(
        filetypes=[
            ("Planilhas Excel", "*.xlsx;*.xlsm;*.xlsb;*.xls")
        ],
        title="Escolha uma planilha para importar",
    )
    if caminho_planilha:
        Path(caminho_planilha)
    else:
        messagebox.showwarning(
            "Local de salvamento", "O local de salvamento não foi escolhido!"
        )
        raise SystemExit()
    planilha = openpyxl.load_workbook(caminho_planilha)
    return planilha

def _criar_planilha(caminho_arquivo: Path, cabeçalhos, dados):
    workbook = openpyxl.Workbook()

    planilha = workbook.active

    planilha.append(cabeçalhos)

    for linha in dados:
        planilha.append(linha)

    workbook.save(caminho_arquivo)
