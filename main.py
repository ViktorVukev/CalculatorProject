from tkinter import *
from calculations import calculate
from controls import clear, clear_recent, delete, click_button

main = Tk()
main.resizable(0, 0)
main.title("Calculator")
main.configure(bg="#281d1d")

entry_var = StringVar()
entry = Entry(main, textvariable=entry_var, font=("Arial", 22), bd=0, insertwidth=2, width=19, justify='right', bg="#281d1d", fg="white")
entry.pack(fill="x", padx=10, pady=(10, 10))

buttons = [
    ('%', 0, 0), ('CE', 0, 1), ('C', 0, 2), ('⌫', 0, 3),
    ('¹⁄ₓ', 1, 0), ('x²', 1, 1), ('√x', 1, 2), ('÷', 1, 3),
    ('7', 2, 0), ('8', 2, 1), ('9', 2, 2), ('×', 2, 3),
    ('4', 3, 0), ('5', 3, 1), ('6', 3, 2), ('-', 3, 3),
    ('1', 4, 0), ('2', 4, 1), ('3', 4, 2), ('+', 4, 3),
    ('±', 5, 0), ('0', 5, 1), ('.', 5, 2), ('=', 5, 3)
]

button_frame = Frame(main, bg="#281d1d")
button_frame.pack()

for (text, row, col) in buttons:
    if text == '=':
        btn = Button(button_frame, text=text, font=("Arial", 16), width=6, height=2, bg="#61ccff", fg="white", bd=0,
                     command=lambda: calculate(entry_var))
    elif text == 'C':
        btn = Button(button_frame, text=text, font=("Arial", 16), width=6, height=2, bg="#3e3e3e", fg="white", bd=0,
                     command=lambda: clear(entry_var))
    elif text == 'CE':
        btn = Button(button_frame, text=text, font=("Arial", 16), width=6, height=2, bg="#3e3e3e", fg="white", bd=0,
                     command=lambda: clear_recent(entry_var))
    elif text == '⌫':
        btn = Button(button_frame, text=text, font=("Arial", 16), width=6, height=2, bg="#3e3e3e", fg="white", bd=0,
                     command=lambda: delete(entry_var))
    else:
        btn = Button(button_frame, text=text, font=("Arial", 16), width=6, height=2, bg="#3e3e3e", fg="white", bd=0,
                     command=lambda value=text: click_button(value, entry_var))
    btn.grid(row=row, column=col, padx=2, pady=2)

main.mainloop()