# This file was generated by the Tkinter Designer by Parth Jadhav
# https://github.com/ParthJadhav/Tkinter-Designer


from pathlib import Path
from tkinter import Tk, Canvas, Entry, Text, Button, PhotoImage, ttk
import sys


ASSETS_PATH = Path(__file__).parent / "assets" / "frame0"
ROOT_PATH = Path(__file__).parent.parent.parent
if str(ROOT_PATH) not in sys.path:
    sys.path.append(str(ROOT_PATH))
from Telas.defs import *


def relative_to_assets(path: str) -> Path:
    return ASSETS_PATH / Path(path)


def criar_tela_exportar(frame: ttk.Frame, imagens: dict[str, dict]):
    def carregar_imagens():
        imagens["image_1"] = PhotoImage(file=relative_to_assets("image_1.png"))
        imagens["image_2"] = PhotoImage(file=relative_to_assets("image_2.png"))
        imagens["entry_1"] = PhotoImage(file=relative_to_assets("entry_1.png"))
        imagens["entry_2"] = PhotoImage(file=relative_to_assets("entry_2.png"))
        imagens["button_1"] = PhotoImage(file=relative_to_assets("button_1.png"))
        imagens["button_2"] = PhotoImage(file=relative_to_assets("button_2.png"))
        imagens["button_3"] = PhotoImage(file=relative_to_assets("button_3.png"))

    def criar_canvas():
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

        canvas.create_image(682.0, 384.0, image=imagens["image_1"])
        canvas.create_image(1180.0, 448.0, image=imagens["image_2"])
        canvas.create_image(262.0, 69.0, image=imagens["entry_1"])
        canvas.create_image(724.0, 69.0, image=imagens["entry_2"])
        canvas.create_rectangle(153.0, 44.0, 354.0, 89.0, fill="#FFFFFF", outline="")
        canvas.create_rectangle(615.0, 44.0, 816.0, 89.0, fill="#FFFFFF", outline="")
        canvas.create_rectangle(22.0, 182.0, 994.0, 251.0, fill="#D9D9D9", outline="")
        canvas.create_rectangle(22.0, 251.0, 994.0, 719.0, fill="#FFFFFF", outline="")
        canvas.create_text(
            36.0,
            37.0,
            anchor="nw",
            text="Inicio:",
            fill="#FFFFFF",
            font=(FONTE_TELAS, 48 * -1),
        )
        canvas.create_text(
            515.0,
            37.0,
            anchor="nw",
            text="Fim:",
            fill="#FFFFFF",
            font=(FONTE_TELAS, 48 * -1),
        )
        canvas.create_text(
            85.0,
            185.0,
            anchor="nw",
            text="Data da RG",
            fill="#000000",
            font=(FONTE_TELAS, 48 * -1),
        )

    def criar_entrada_texto(x, y, width, height):
        entry = Text(
            frame,
            bd=0,
            bg="#FFFFFF",
            fg="#000716",
            highlightthickness=0,
            font=(FONTE_INPUT, 20),
        )
        entry.place(x=x, y=y, width=width, height=height)
        return entry

    def criar_botao(x, y, image, command):
        button = Button(
            frame,
            image=image,
            borderwidth=0,
            highlightthickness=0,
            command=command,
            relief="flat",
        )
        button.place(x=x, y=y, width=image.width(), height=image.height())

    # Criação e configuração dos elementos da tela
    carregar_imagens()
    criar_canvas()
    entry_inicio = criar_entrada_texto(181.0, 54.0, 162.0, 28.0)
    entry_fim = criar_entrada_texto(643.0, 54.0, 162.0, 28.0)
    criar_botao(1072.0, 31.0, imagens["button_1"], lambda: print("Selecionar"))
    criar_botao(1027.0, 182.0, imagens["button_2"], lambda: print("Local"))
    criar_botao(1076.0, 642.0, imagens["button_3"], lambda: print("Exportar"))
