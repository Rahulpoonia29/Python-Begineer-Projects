import tkinter as tk
import tkinter.ttk as ttk
import num2words as nw

# Initilysing tkinter
root = tk.Tk()
root.title("Number to words")
root.geometry("800x600")

# Initilysing variables
ent_var = tk.StringVar()


def convert():
    # Get the string value from the StringVar
    string_value = ent_var.get()
    try:
        # Converting the input to string
        given_num = int(ent_var.get())
        converted_num = nw.num2words(float(given_num))
        lbl_val.config(text=converted_num.capitalize())

    except ValueError:
        # Handle the case where the string cannot be converted to an integer
        print("Invalid input: Not an integer")


# Entry box
ent_num = ttk.Entry(master=root, textvariable=ent_var, background="cyan")

# Button
but_click = ttk.Button(master=root, text="Convert", command=convert)

# Label
lbl_val = tk.Label(master=root, text="Enter the number", border=2, relief="solid")

# Packing the elements
ent_num.pack(pady=30)
but_click.pack(pady=10)
lbl_val.pack(pady=10)

tk.mainloop()
