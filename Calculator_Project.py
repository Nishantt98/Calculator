import tkinter as tk
def click(event):
    text = event.widget.cget("text")


    if text == "=":
        try:
            result = str(eval(screen.get()))
            screen.set(result)
        except Exception as e:
            screen.set("Error")
    elif text == "C":
        screen.set("  ")
    else:
        screen.set(screen.get() + text)

codsoft = tk.Tk()
codsoft.geometry("300x400")
codsoft.maxsize(300,400)
codsoft.minsize(300,400)
codsoft.title("Calculator By Nishant Singh")
codsoft.config(bg='#58667a')


screen = tk.StringVar()
screen.set("")

entry = tk.Entry(codsoft, textvar=screen, font="arial 20 bold")
entry.pack(fill=tk.BOTH, ipadx=8, padx=10, pady=10)
entry["bg"] = "#58667a"

button_frame = tk.Frame(codsoft)
button_frame.config(bg="#58667a")
button_frame.pack()

buttons = [
    "7", "8", "9", "+",
    "4", "5", "6", "-",
    "1", "2", "3", "*",
    "C", "0", "=", "/"
]

row_value = 1
column_value = 0

for button_text in buttons:
    button = tk.Button(button_frame, text=button_text, font="arial 25 bold", relief="ridge", border=2,fg="black")
    button.grid(row=row_value, column=column_value, padx=5, pady=5)
    button.config(bg="#58667a")
    column_value += 1
    if column_value > 3:
        column_value = 0
        row_value += 1

    button.bind("<Button-1>",click)

codsoft.mainloop()

