import tkinter


def miles_to_km():
    mile = float(user_input.get())
    kilometer = round(mile * 1.609, 2)
    km_result.config(text=f"{kilometer}")


window = tkinter.Tk()
window.title("Mile to Km Convertor")
window.config(padx=65, pady=20)

# Entry
user_input = tkinter.Entry(width=2)
user_input.grid(row=0, column=1)

# Label
miles = tkinter.Label(text="Miles")
miles.grid(row=0, column=2)

km_result = tkinter.Label(text="0")
km_result.grid(row=1, column=1)

km = tkinter.Label(text="Km")
km.grid(row=1, column=2)

equal = tkinter.Label(text="is equal to")
equal.grid(row=1, column=0)

# Button
calculate = tkinter.Button(text="Calculate", command=miles_to_km)
calculate.grid(row=2, column=1)

window.mainloop()
