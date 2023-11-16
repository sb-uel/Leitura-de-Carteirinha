
# This file was generated by the Tkinter Designer by Parth Jadhav
# https://github.com/ParthJadhav/Tkinter-Designer


from pathlib import Path

# from tkinter import *
# Explicit imports to satisfy Flake8
from tkinter import Tk, Canvas, Entry, Text, Button, PhotoImage
from Telas.defs import *

OUTPUT_PATH = Path(__file__).parent
ASSETS_PATH = OUTPUT_PATH / "assets" / "frame0"


def relative_to_assets(path: str) -> Path:
    return ASSETS_PATH / Path(path)


window = Tk()

window.geometry(TAMANHO_JANELA)
window.configure(bg = "#FFFFFF")


canvas = Canvas(
    window,
    bg = "#FFFFFF",
    height = 768,
    width = 1365,
    bd = 0,
    highlightthickness = 0,
    relief = "ridge"
)

canvas.place(x = 0, y = 0)
image_image_1 = PhotoImage(
    file=relative_to_assets("image_1.png"))
image_1 = canvas.create_image(
    682.0,
    384.0,
    image=image_image_1
)

image_image_2 = PhotoImage(
    file=relative_to_assets("image_2.png"))
image_2 = canvas.create_image(
    682.0,
    520.0,
    image=image_image_2
)

canvas.create_text(
    80.0,
    60.0,
    anchor="nw",
    text="Data:",
    fill="#FFFFFF",
    font=(FONTE_TELAS, 48 * -1)
)

canvas.create_rectangle(
    180.0,
    67.0,
    381.0,
    112.0,
    fill="#FFFFFF",
    outline="")

entry_image_1 = PhotoImage(
    file=relative_to_assets("entry_1.png"))
entry_bg_1 = canvas.create_image(
    289.0,
    92.0,
    image=entry_image_1
)
entry_1 = Text(
    bd=0,
    bg="#FFFFFF",
    fg="#000716",
    highlightthickness=0,
    font=(FONTE_INPUT, 20)
)
entry_1.place(
    x=208.0,
    y=77.0,
    width=162.0,
    height=28.0
)

canvas.create_rectangle(
    70.0,
    190.0,
    1084.0,
    256.0,
    fill="#D9D9D9",
    outline="")

canvas.create_rectangle(
    70.0,
    256.0,
    1084.0,
    322.0,
    fill="#FFFFFF",
    outline="")

canvas.create_text(
    156.0,
    195.0,
    anchor="nw",
    text="Data",
    fill="#000000",
    font=(FONTE_TELAS, 48 * -1)
)

canvas.create_text(
    450.0,
    195.0,
    anchor="nw",
    text="N° de presenças",
    fill="#000000",
    font=(FONTE_TELAS, 48 * -1)
)

canvas.create_text(
    872.0,
    195.0,
    anchor="nw",
    text="Ações",
    fill="#000000",
    font=(FONTE_TELAS, 48 * -1)
)

button_image_1 = PhotoImage(
    file=relative_to_assets("button_1.png"))
button_1 = Button(
    image=button_image_1,
    borderwidth=0,
    highlightthickness=0,
    command=lambda: print("Editar"),
    relief="flat"
)
button_1.place(
    x=855.0,
    y=262.0,
    width=138.0,
    height=49.0
)

button_image_2 = PhotoImage(
    file=relative_to_assets("button_2.png"))
button_2 = Button(
    image=button_image_2,
    borderwidth=0,
    highlightthickness=0,
    command=lambda: print("Buscar"),
    relief="flat"
)
button_2.place(
    x=610.0,
    y=58.0,
    width=164.0,
    height=69.0
)

button_image_3 = PhotoImage(
    file=relative_to_assets("button_3.png"))
button_3 = Button(
    image=button_image_3,
    borderwidth=0,
    highlightthickness=0,
    command=lambda: print("Voltar"),
    relief="flat"
)
button_3.place(
    x=33.0,
    y=681.0,
    width=143.0,
    height=47.0
)
window.resizable(False, False)
window.mainloop()
