import tkinter as tk

# Create main window
root = tk.Tk()
root.title("Simple Calculator")
root.geometry("380x480")
root.resizable(False, False)

# Entry widget to display expressions
entry = tk.Entry(root, width=20, font=('Arial', 24), bd=10, insertwidth=2, borderwidth=4, relief='ridge', justify='right')
entry.grid(row=0, column=0, columnspan=4)

# Button click handler
def on_click(symbol):
    current = entry.get()
    entry.delete(0, tk.END)
    entry.insert(0, current + symbol)

def clear():
    entry.delete(0, tk.END)

def calculate():
    try:
        result = str(eval(entry.get()))
        entry.delete(0, tk.END)
        entry.insert(0, result)
    except Exception as e:
        entry.delete(0, tk.END)
        entry.insert(0, "Error")

# Button layout
buttons = [
    ('7', 1, 0), ('8', 1, 1), ('9', 1, 2), ('/', 1, 3),
    ('4', 2, 0), ('5', 2, 1), ('6', 2, 2), ('*', 2, 3),
    ('1', 3, 0), ('2', 3, 1), ('3', 3, 2), ('-', 3, 3),
    ('0', 4, 0), ('.', 4, 1), ('=', 4, 2), ('+', 4, 3),
]

for (text, row, col) in buttons:
    if text == '=':
        tk.Button(root, text=text, padx=20, pady=20, font=('Arial', 18), command=calculate).grid(row=row, column=col)
    else:
        tk.Button(root, text=text, padx=20, pady=20, font=('Arial', 18), command=lambda t=text: on_click(t)).grid(row=row, column=col)

# Clear button
tk.Button(root, text='C', padx=20, pady=20, font=('Arial', 18), bg='red', fg='white', command=clear).grid(row=5, column=0, columnspan=4, sticky="we")

# Run the app
root.mainloop()