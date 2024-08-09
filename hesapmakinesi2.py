import tkinter as tk

root = tk.Tk()
root.title("Hesap Makinesi")

root.geometry("360x400")
root.config(bg="#00bf00")


entry = tk.Entry(root, width=19 , font= ('Arial' , 24), borderwidth=2 , relief="solid")
entry.grid(row=0, column=0, columnspan=4, padx=3, pady=10)

buttons = [
    '7', '8', '9', '/',
    '4', '5', '6', '*',
    '1', '2', '3', '-',
    '0', 'C', '=', '+'
]
def button_click(value):
    if value == '=':
        try:
            result = eval(entry.get())
            entry.delete(0, tk.END)
            entry.insert(0, str(result))
        except:
            entry.delete(0, tk.END)
            entry.insert(0, "Hata")
    elif value == 'C':
        entry.delete(0, tk.END)
    
    else:
        current = entry.get()
        entry.delete(0, tk.END)
        entry.insert(0, current + value)
    
    
        


row_val = 1
col_val = 0
for button in buttons:
    btn = tk.Button(root, text=button, width=5, height=2, font=('Arial', 18) , command=lambda b=button : button_click(b), activebackground="#ff0000")
    btn.grid(row=row_val, column=col_val, padx=5, pady=5)
    col_val += 1
    if col_val > 3:
        col_val = 0
        row_val += 1

root.mainloop()



