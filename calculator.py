from tkinter import *

window = Tk()
window.title("Calculator")

def button_add():
    return




#Display Panel
display = Entry(window, width=50, borderwidth=2)
display.grid(row=0,
             column=0,
             columnspan=3,
             padx=8,
             pady=8
             )

# NumPad_button_declare

button0 = Button(window, text="0", padx=40, pady=20, command=button_add)
button1 = Button(window, text="1", padx=40, pady=20, command=button_add)
button2 = Button(window, text="2", padx=40, pady=20, command=button_add)
button3 = Button(window, text="3", padx=40, pady=20, command=button_add)
button4 = Button(window, text="4", padx=40, pady=20, command=button_add)
button5 = Button(window, text="5", padx=40, pady=20, command=button_add)
button6 = Button(window, text="6", padx=40, pady=20, command=button_add)
button7 = Button(window, text="7", padx=40, pady=20, command=button_add)
button8 = Button(window, text="8", padx=40, pady=20, command=button_add)
button9 = Button(window, text="9", padx=40, pady=20, command=button_add)

button_clear = Button(window, text="C", padx=40, pady=10, command=button_add)
button_multiply = Button(window, text="*", padx=40, pady=20, command=button_add)
button_subtraction = Button(window, text="-", padx=40, pady=20, command=button_add)
button_addition = Button(window, text="+", padx=40, pady=20, command=button_add)
button_divide = Button(window, text="/", padx=40, pady=20, command=button_add)
button_point = Button(window, text=".", padx=40, pady=20, command=button_add)
button_equals = Button(window, text="=", padx=40, pady=20, command=button_add)


# NumPad_button_display

button_clear.grid(row=0, column=3)

button7.grid(row=1, column=0)
button8.grid(row=1, column=1)
button9.grid(row=1, column=2)

button_multiply.grid(row=1, column=3)

button4.grid(row=2, column=0)
button5.grid(row=2, column=1)
button6.grid(row=2, column=2)

button_subtraction.grid(row=2, column=3)

button1.grid(row=3, column=0)
button2.grid(row=3, column=1)
button3.grid(row=3, column=2)

button_addition.grid(row=3, column=3)

button0.grid(row=4, column=0)

button_point.grid(row=4, column=1)
button_equals.grid(row=4, column=2)

button_divide.grid(row=4, column=3)


"""
# Label
name_label = Label(window, text="Name")
name_label.grid(row=0, column=0)

age_label = Label(window, text="Age")
age_label.grid(row=1, column=0)


# Text Input


u_age = Entry(window, width=50, borderwidth=2)
u_age.grid(row=1, column=1)


def on_click():
    print(f"User name is {u_name.get()}, and age is {u_age.get()}.")
    display_text = f"User name is {u_name.get()}, and age is {u_age.get()}."
    myLabel = Label(window,
                    text=display_text)
    myLabel.grid(row=3,column=1)


#Button
submit=Button(window,text="Submit", command=on_click)  #dont use parenthesis for function call -> call back function
submit.grid(row=2,column=1)
"""
window.mainloop()
