import tkinter
FONT = ('Arial', 18)


def calculate():
    output = float(entry.get()) / .6214
    km_label.config(text=f"{output:0.1f}")


window = tkinter.Tk()
window.title("Mile to Km Converter")
window.minsize()
window.config(padx=20, pady=20)

entry = tkinter.Entry(width=10)
entry.grid(row=0, column=1)

miles_unit_label = tkinter.Label(text='Miles', font=FONT)
miles_unit_label.grid(row=0, column=2)

equal_label = tkinter.Label(text='is equal to', font=FONT)
equal_label.grid(row=1, column=0)

km_label = tkinter.Label(text='0.0', font=FONT)
km_label.grid(row=1, column=1)

km_unit_label = tkinter.Label(text='Km', font=FONT)
km_unit_label.grid(row=1, column=2)

calculate_button = tkinter.Button(text="Calculate", command=calculate)
calculate_button.grid(row=2, column=1)

window.mainloop()
