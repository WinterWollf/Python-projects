from tkinter import *
from tkinter.ttk import *
from tkinter.messagebox import *

# Functions
def write_on_screen(unit):
    output.config(text=unit)

def calculate():
    selection_1 = unit_1.get()
    unit = float(input.get())

    selection_2 = unit_2.get()

    if selection_1 == "km":
        unit *= 1000
    elif selection_1 == "m":
        pass
    elif selection_1 == "cm":
        unit *= 0.01
    elif selection_1 == "mm":
        unit *= 0.001
    elif selection_1 == "mile":
        unit *= 1609.344
    elif selection_1 == "inch":
        unit *= 0.0254
    elif selection_1 == "foot":
        unit *= 0.3048
    elif selection_1 == "yard":
        unit *= 0.9144

    if selection_2 == "km":
        unit *= 0.001
    elif selection_2 == "m":
        pass
    elif selection_2 == "cm":
        unit *= 100
    elif selection_2 == "mm":
        unit *= 1000
    elif selection_2 == "mile":
        unit *= 0.000621371192
    elif selection_2 == "inch":
        unit *= 39.3700787
    elif selection_2 == "foot":
        unit *= 3.2808399
    elif selection_2 == "yard":
        unit *= 1.0936133

    write_on_screen(unit)

# Screen
screen = Tk()
screen.minsize(width=400, height=200)
screen.title("Unit Converter")
screen.config(padx=100, pady=20)

# Combobox
unit_1 = Combobox(
    width=6,
    justify="center",
    state="readonly",
    values=["km", "m", "cm", "mm", "mile", "inch", "foot", "yard"]
)

unit_2 = Combobox(
    width=6,
    justify="center",
    state="readonly",
    values=["km", "m", "cm", "mm", "mile", "inch", "foot", "yard"]
)

# Button
button = Button(text="Calculate", command=calculate)

# Entry
input = Entry()

# Label
output = Label(width=20, background="white")

# White Boxes
label_1 = Label()
label_2 = Label()
label_3 = Label()
label_1.grid(column=2, row=2)
label_2.grid(column=3, row=2)
label_3.grid(column=2, row=4)

# Placement
unit_1.grid(column=3, row=1)
unit_2.grid(column=3, row=3)
input.grid(column=2, row=1)
output.grid(column=2, row=3)
button.grid(column=2, row=5)
button.config(padding=5)


# Main Loop
screen.mainloop()
