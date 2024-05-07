from tkinter import *
FONT = "Arial"
BEIGE = "#D7A86E"

window = Tk()
window.title("Temperature Converter...")
window.minsize(width=400, height=300)
window.config(padx=50, pady=40)


def convert_c_to_f():
    input_val = float(celsius_input.get())
    answer = round(input_val * 9/5 + 32, 1)
    f_label.config(text=answer)


def convert_f_to_c():
    f_input_value = float(fahrenheit_input.get())
    calculation = round((f_input_value - 32) * 5/9, 1)
    cel_label.config(text=calculation)


# Celsius to Fahrenheit
temp_label = Label(text="°C to °F Converter", fg="green", font=(FONT, 30))
temp_label.grid(column=1, row=0)
temp_label.config(pady=20)

celsius_input = Entry(width=5)
celsius_input.grid(column=1, row=1)

# Labels
c_label = Label(text="°C",fg="green", font=(FONT, 20))
c_label.grid(column=2, row=1)

equal_to_label = Label(text="is equal to", fg="green", font=(FONT, 20))
equal_to_label.grid(column=0, row=2)

f_label = Label(text="0", font=(FONT, 30))
f_label.grid(column=1, row=2)
f_label.config(pady=20)

f_sign = Label(text="°F", fg="green", font=(FONT, 20))
f_sign.grid(column=2, row=2)

btn = Button(text="Calculate", fg="green", font=(FONT, 20, "bold"), command=convert_c_to_f)
btn.grid(column=1, row=3)
btn.config(pady=10)

# Fahrenheit to Celsius
temp_label = Label(text="°F to °C Converter", fg=BEIGE, font=(FONT, 30))
temp_label.grid(column=1, row=5)
temp_label.config(padx=20, pady=20)

fahrenheit_input = Entry(width=5)
fahrenheit_input.grid(column=1, row=6)

# Labels
fah_label = Label(text="°F",fg=BEIGE, font=(FONT, 20))
fah_label.grid(column=2, row=6)

equal_to_label = Label(text="is equal to", fg=BEIGE, font=(FONT, 20))
equal_to_label.grid(column=0, row=7)

cel_label = Label(text="0", font=(FONT, 30))
cel_label.grid(column=1, row=7)
cel_label.config(pady=20)

f_sign = Label(text="°C", fg=BEIGE, font=(FONT, 20))
f_sign.grid(column=2, row=7)

btn = Button(text="Calculate", fg=BEIGE, font=(FONT, 20, "bold"), command=convert_f_to_c)
btn.grid(column=1, row=8)
btn.config(pady=10)



window.mainloop()