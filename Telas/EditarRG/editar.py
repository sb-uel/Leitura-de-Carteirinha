# This file was generated by the Tkinter Designer by Parth Jadhav
# https://github.com/ParthJadhav/Tkinter-Designer

from pathlib import Path
from tkinter import Tk, Canvas, Entry, Text, Button, PhotoImage
import sys


ASSETS_PATH = Path(__file__).parent / "assets" / "frame0"
ROOT_PATH = Path(__file__).parent.parent.parent
if str(ROOT_PATH) not in sys.path:
    sys.path.append(str(ROOT_PATH))
from Telas.defs import *


def relative_to_assets(path: str) -> Path:
    return ASSETS_PATH / Path(path)


from tkinter import Tk, Canvas, Text, Button, PhotoImage


def criar_tela_editar_rg(frame, imagens):
    # Imagens
    imagens["image_1"] = PhotoImage(file=relative_to_assets("image_1.png"))
    imagens["entry_1"] = PhotoImage(file=relative_to_assets("entry_1.png"))
    imagens["button_1"] = PhotoImage(file=relative_to_assets("button_1.png"))
    imagens["button_2"] = PhotoImage(file=relative_to_assets("button_2.png"))

    # Canvas
    canvas = Canvas(
        frame,
        bg="#FFFFFF",
        height=768,
        width=1365,
        bd=0,
        highlightthickness=0,
        relief="ridge",
    )
    canvas.place(x=0, y=0)

    # Adiciona imagens, textos, retângulos ao canvas
    canvas.create_image(682.0, 384.0, image=imagens["image_1"])
    canvas.create_image(289.0, 92.0, image=imagens["entry_1"])
    canvas.create_rectangle(36.0, 185.0, 1050.0, 251.0, fill="#D9D9D9", outline="")
    canvas.create_rectangle(36.0, 251.0, 1050.0, 735.0, fill="#FFFFFF", outline="")
    canvas.create_rectangle(180.0, 67.0, 381.0, 112.0, fill="#FFFFFF", outline="")
    canvas.create_text(
        122.0,
        190.0,
        anchor="nw",
        text="Nome",
        fill="#000000",
        font=(FONTE_TELAS, 48 * -1),
    )
    canvas.create_text(
        514.0,
        191.0,
        anchor="nw",
        text="Curso",
        fill="#000000",
        font=(FONTE_TELAS, 48 * -1),
    )
    canvas.create_text(
        838.0,
        190.0,
        anchor="nw",
        text="Presente",
        fill="#000000",
        font=(FONTE_TELAS, 48 * -1),
    )
    canvas.create_text(
        81.0,
        57.0,
        anchor="nw",
        text="Data:",
        fill="#FFFFFF",
        font=(FONTE_TELAS, 48 * -1),
    )
    canvas.create_text(
        36.0,
        142.0,
        anchor="nw",
        text="Lista de usuários:",
        fill="#FFFFFF",
        font=(FONTE_TELAS, 40 * -1),
    )

    # Entrada de texto
    entry_1 = Text(
        frame,
        bd=0,
        bg="#FFFFFF",
        fg="#000716",
        highlightthickness=0,
        font=(FONTE_INPUT, 20),
    )
    entry_1.place(x=208.0, y=77.0, width=162.0, height=28.0)

    # Botões
    button_1 = Button(
        frame,
        image=imagens["button_1"],
        borderwidth=0,
        highlightthickness=0,
        command=lambda: print("Salvar RG"),
        relief="flat",
    )
    button_1.place(x=1154.0, y=342.0, width=170.0, height=68.0)

    button_2 = Button(
        frame,
        image=imagens["button_2"],
        borderwidth=0,
        highlightthickness=0,
        command=lambda: print("Deletar RG"),
        relief="flat",
    )
    button_2.place(x=1154.0, y=486.0, width=170.0, height=68.0)


# imagens = {}
# window = Tk()
# window.geometry(TAMANHO_JANELA)
# window.configure(bg="#FFFFFF")
# cria_tela_editar_rg(window, imagens)
# window.mainloop()
