from tkinter import *


def calculate():
    miles = miles_entry.get()
    kilometers = round(float(miles) * 1.609, 2)
    km_label.config(text=str(kilometers))


window = Tk()
window.title("Mile to Km Converter")
window.minsize(width=200, height=100)
window.config(padx=20, pady=20)
window.config(padx=20, pady=20)

# is_equal_to
equal_label = Label(text="is equal to")
equal_label.grid(column=0, row=1)

# miles_entry
miles_entry = Entry(width=8)
miles_entry.grid(column=1, row=0)

# km_label
km_label = Label(text="0")
km_label.grid(column=1, row=1)

# calculate_button
calculate_button = Button(text="calculate", command=calculate)
calculate_button.grid(column=1, row=2)

# miles_text
miles_label = Label(text="Miles")
miles_label.grid(column=2, row=0)

# kilometers_text
miles_label = Label(text="Km")
miles_label.grid(column=2, row=1)

window.mainloop()