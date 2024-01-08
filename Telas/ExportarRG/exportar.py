# This file was generated by the Tkinter Designer by Parth Jadhav
# https://github.com/ParthJadhav/Tkinter-Designer


from pathlib import Path
from tkinter import Tk, Canvas, Entry, Text, Button, PhotoImage, ttk
import sys

OUTPUT_PATH = Path(__file__).parent
ASSETS_PATH = OUTPUT_PATH / "assets" / "frame0"
sys.path.append(str(OUTPUT_PATH.parent))
from defs import *


def relative_to_assets(path: str) -> Path:
    return ASSETS_PATH / Path(path)


def cria_tela_exportar(frame, imagens):
    # Imagens
    imagens["image_1"] = PhotoImage(file=relative_to_assets("image_1.png"))
    imagens["image_2"] = PhotoImage(file=relative_to_assets("image_2.png"))
    imagens["entry_1"] = PhotoImage(file=relative_to_assets("entry_1.png"))
    imagens["entry_2"] = PhotoImage(file=relative_to_assets("entry_2.png"))
    imagens["button_1"] = PhotoImage(file=relative_to_assets("button_1.png"))
    imagens["button_2"] = PhotoImage(file=relative_to_assets("button_2.png"))
    imagens["button_3"] = PhotoImage(file=relative_to_assets("button_3.png"))

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
    canvas.create_image(1180.0, 448.0, image=imagens["image_2"])
    canvas.create_image(262.0, 69.0, image=imagens["entry_1"])
    canvas.create_image(724.0, 69.0, image=imagens["entry_2"])
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
    canvas.create_rectangle(153.0, 44.0, 354.0, 89.0, fill="#FFFFFF", outline="")
    canvas.create_rectangle(615.0, 44.0, 816.0, 89.0, fill="#FFFFFF", outline="")
    canvas.create_rectangle(22.0, 182.0, 994.0, 251.0, fill="#D9D9D9", outline="")
    canvas.create_rectangle(22.0, 251.0, 994.0, 719.0, fill="#FFFFFF", outline="")

    # Entrada de texto
    entry_1 = Text(
        frame,
        bd=0,
        bg="#FFFFFF",
        fg="#000716",
        highlightthickness=0,
        font=(FONTE_INPUT, 20),
    )
    entry_1.place(x=181.0, y=54.0, width=162.0, height=28.0)

    entry_2 = Text(
        frame,
        bd=0,
        bg="#FFFFFF",
        fg="#000716",
        highlightthickness=0,
        font=(FONTE_INPUT, 20),
    )
    entry_2.place(x=643.0, y=54.0, width=162.0, height=28.0)

    # Botões
    button_1 = Button(
        frame,
        image=imagens["button_1"],
        borderwidth=0,
        highlightthickness=0,
        command=lambda: print("Selecionar"),
        relief="flat",
    )
    button_1.place(x=1072.0, y=31.0, width=206.0, height=64.0)

    button_2 = Button(
        frame,
        image=imagens["button_2"],
        borderwidth=0,
        highlightthickness=0,
        command=lambda: print("Local"),
        relief="flat",
    )
    button_2.place(x=1027.0, y=182.0, width=307.0, height=73.0)

    button_3 = Button(
        frame,
        image=imagens["button_3"],
        borderwidth=0,
        highlightthickness=0,
        command=lambda: print("Exportar"),
        relief="flat",
    )
    button_3.place(x=1076.0, y=642.0, width=209.0, height=77.0)


# root = Tk()
# root.title("Sua Demo")
# root.geometry(TAMANHO_JANELA)
# root.resizable(True, True)
# imagens = {}
# frame = ttk.Frame(root)
# frame.pack(expand=True, fill="both")
# cria_tela_exportar(frame, imagens)
# root.mainloop()
