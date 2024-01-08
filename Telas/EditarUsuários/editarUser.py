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


def criar_tela_edicao_usuarios(frame, imagens):
    # Imagens
    imagens["image_1"] = PhotoImage(file=relative_to_assets("image_1.png"))
    imagens["image_2"] = PhotoImage(file=relative_to_assets("image_2.png"))
    imagens["entry_1"] = PhotoImage(file=relative_to_assets("entry_1.png"))
    imagens["entry_2"] = PhotoImage(file=relative_to_assets("entry_2.png"))
    imagens["entry_3"] = PhotoImage(file=relative_to_assets("entry_3.png"))
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

    # Adiciona imagens, textos, retângulos ao canvas
    canvas.create_image(682.0, 384.0, image=imagens["image_1"])
    canvas.create_image(569.0, 648.0, image=imagens["image_2"])
    canvas.create_image(391.0, 152.5, image=imagens["entry_1"])
    canvas.create_image(458.0, 241.5, image=imagens["entry_2"])
    canvas.create_image(391.5, 424.5, image=imagens["entry_3"])
    canvas.create_rectangle(307.0, 484.0, 394.0, 529.0, fill="#FFFFFF", outline="")
    canvas.create_rectangle(743.0, 109.0, 1296.0, 175.0, fill="#D9D9D9", outline="")
    canvas.create_rectangle(743.0, 175.0, 1296.0, 659.0, fill="#FFFFFF", outline="")
    canvas.create_text(
        514.0,
        25.0,
        anchor="nw",
        text="EDIÇÃO DE USUÁRIOS",
        fill="#FFFFFF",
        font=(FONTE_TELAS, 48 * -1),
    )
    canvas.create_text(
        22.0,
        132.0,
        anchor="nw",
        text="NOME:",
        fill="#FFFFFF",
        font=(FONTE_TELAS, 40 * -1),
    )
    canvas.create_text(
        22.0,
        219.0,
        anchor="nw",
        text="N° DE MATRICULA:",
        fill="#FFFFFF",
        font=(FONTE_TELAS, 40 * -1),
    )
    canvas.create_text(
        22.0,
        302.0,
        anchor="nw",
        text="CURSO",
        fill="#FFFFFF",
        font=(FONTE_TELAS, 40 * -1),
    )
    canvas.create_text(
        22.0,
        403.0,
        anchor="nw",
        text="EMAIL:",
        fill="#FFFFFF",
        font=(FONTE_TELAS, 40 * -1),
    )
    canvas.create_text(
        22.0,
        484.0,
        anchor="nw",
        text="N° DE DIAS PRESENTES:",
        fill="#FFFFFF",
        font=(FONTE_TELAS, 40 * -1),
    )
    canvas.create_text(
        779.0,
        115.0,
        anchor="nw",
        text="Data da RG",
        fill="#000000",
        font=(FONTE_TELAS, 48 * -1),
    )
    canvas.create_text(
        1108.0,
        114.0,
        anchor="nw",
        text="Presente",
        fill="#000000",
        font=(FONTE_TELAS, 48 * -1),
    )

    # Entrada de texto
    entry_1 = Text(
        frame,
        bd=0,
        bg="#FFFFFF",
        fg="#000716",
        highlightthickness=0,
        font=(FONTE_INPUT, 25),
    )
    entry_1.place(x=126.0, y=130.0, width=530.0, height=43.0)

    entry_2 = Text(
        frame,
        bd=0,
        bg="#FFFFFF",
        fg="#000716",
        highlightthickness=0,
        font=(FONTE_INPUT, 25),
    )
    entry_2.place(x=272.0, y=219.0, width=372.0, height=43.0)

    entry_3 = Text(
        frame,
        bd=0,
        bg="#FFFFFF",
        fg="#000716",
        highlightthickness=0,
        font=(FONTE_INPUT, 25),
    )
    entry_3.place(x=139.0, y=402.0, width=505.0, height=43.0)

    # Botões
    button_1 = Button(
        frame,
        image=imagens["button_1"],
        borderwidth=0,
        highlightthickness=0,
        command=lambda: print("Confirmar"),
        relief="flat",
    )
    button_1.place(x=1111.0, y=190.0, width=51.0, height=51.0)

    button_2 = Button(
        frame,
        image=imagens["button_2"],
        borderwidth=0,
        highlightthickness=0,
        command=lambda: print("Negar"),
        relief="flat",
    )
    button_2.place(x=1206.0, y=190.0, width=51.0, height=51.0)

    button_3 = Button(
        frame,
        image=imagens["button_3"],
        borderwidth=0,
        highlightthickness=0,
        command=lambda: print("Salvar"),
        relief="flat",
    )
    button_3.place(x=125.0, y=606.0, width=325.0, height=84.0)

    # Caixa de seleção
    def changeMonth():
        comboExample["values"] = [
            "Engenharia Elétrica",
            "Ciência da Computação",
        ]

    comboExample = ttk.Combobox(
        frame,
        values=["Engenharia Elétrica", "Ciência da Computação"],
        postcommand=changeMonth,
        font=(FONTE_INPUT, 25, "bold"),
    )
    comboExample.pack()

    comboExample.option_add("*TCombobox*Listbox*Font", (FONTE_INPUT, 16))

    comboExample.config(width=21)
    comboExample.place(x=135, y=303)


# imagens = {}
# window = Tk()
# window.geometry(TAMANHO_JANELA)
# window.configure(bg="#FFFFFF")
# cria_tela_edicao_usuarios(window, imagens)
# window.mainloop()
