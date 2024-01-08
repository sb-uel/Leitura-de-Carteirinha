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


def criar_tela_leitura(frame: ttk.Frame, imagens : dict[str, dict])  :
    # Imagens
    imagens["image_1"] = PhotoImage(file=relative_to_assets("image_1.png"))
    imagens["image_2"] = PhotoImage(file=relative_to_assets("image_2.png"))
    imagens["entry_image"] = PhotoImage(file=relative_to_assets("entry_1.png"))
    imagens["button_image_1"] = PhotoImage(file=relative_to_assets("button_1.png"))
    imagens["button_image_2"] = PhotoImage(file=relative_to_assets("button_2.png"))

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

    # Adiciona imagens ao canvas
    canvas.create_image(682.0, 384.0, image=imagens["image_1"])
    canvas.create_image(683.0, 275.0, image=imagens["image_2"])
    canvas.create_image(703.5, 524.0, image=imagens["entry_image"])

    # Entrada de texto
    entry_1 = Text(
        frame,
        bd=0,
        bg="#FFFFFF",
        fg="#000716",
        highlightthickness=0,
        font=(FONTE_INPUT, 35),
    )
    entry_1.place(x=520.0, y=490.0, width=367.0, height=66.0)

    # Botões
    button_1 = Button(
        frame,
        image=imagens["button_image_1"],
        borderwidth=0,
        highlightthickness=0,
        command=lambda: print("Enviar"),
        relief="flat",
    )
    button_1.place(x=552.0, y=610.0, width=261.0, height=92.0)

    button_2 = Button(
        frame,
        image=imagens["button_image_2"],
        borderwidth=0,
        highlightthickness=0,
        command=lambda: print("Voltar"),
        relief="flat",
    )
    button_2.place(x=33.0, y=681.0, width=143.0, height=47.0)


# imagens = {}
# window = Tk()
# window.geometry(TAMANHO_JANELA)
# window.configure(bg="#FFFFFF")
# cria_tela_leitura(window, imagens)
# window.mainloop()
