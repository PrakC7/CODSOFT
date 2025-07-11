import tkinter as tk
import math

# Input Handling Functions
def click(event=None, key=None):
    btn_text = key if key else event.widget["text"]

    if btn_text == "C":
        entry_var.set("")
    elif btn_text == "←":
        entry_var.set(entry_var.get()[:-1])
    elif btn_text == "=" or key == "Return":
        try:
            expr = entry_var.get().replace("×", "*").replace("÷", "/").replace("^", "**")
            expr = expr.replace("√", "math.sqrt")
            result = eval(expr, {"math": math})
            entry_var.set(str(round(result, 5)))
        except Exception:
            entry_var.set("Error")
    else:
        entry_var.set(entry_var.get() + btn_text)

def key_event(event):
    key_map = {
        "\r": "=",    # Enter
        "\b": "←",    # Backspace
        "*": "×",
        "/": "÷",
        "^": "^"
    }
    key = key_map.get(event.char, event.char)
    click(key=key)

# App Setup
app = tk.Tk()
app.title("Standard Calculator")
app.geometry("360x600")
app.resizable(False, False)
app.configure(bg="#f7f7f7")
app.bind("<Key>", key_event)

# Display Field
entry_var = tk.StringVar()
entry = tk.Entry(app, textvariable=entry_var, font=("Segoe UI", 22), bd=0, relief="flat",
                 justify="right", bg="white", fg="#111827")
entry.pack(pady=20, padx=10, ipady=12, fill='x')

# Buttons Layout
btns_frame = tk.Frame(app, bg="#f7f7f7")
btns_frame.pack(padx=10, pady=5)

buttons = [
    ["C", "(", ")", "←"],
    ["7", "8", "9", "÷"],
    ["4", "5", "6", "×"],
    ["1", "2", "3", "-"],
    ["0", ".", "^", "+"],
    ["√", "%", "=", ""]
]

for row in buttons:
    row_frame = tk.Frame(btns_frame, bg="#f7f7f7")
    row_frame.pack(expand=True, fill="both")
    for btn_text in row:
        if btn_text == "":
            tk.Label(row_frame, text="", width=5, bg="#f7f7f7").pack(side="left", expand=True, fill="both", padx=2, pady=2)
            continue
        btn = tk.Button(row_frame, text=btn_text, font=("Segoe UI", 16), bd=0, relief="flat", bg="#e5e7eb",
                        fg="#111827", activebackground="#d1d5db", activeforeground="#111827",
                        height=2, width=5)
        btn.pack(side="left", expand=True, fill="both", padx=2, pady=2)
        btn.bind("<Button-1>", click)

# Footer
tk.Label(app, text="Made by Prakhar — CodSoft Task 1", font=("Segoe UI", 9),
         bg="#f7f7f7", fg="#6b7280").pack(pady=10)

app.mainloop()
