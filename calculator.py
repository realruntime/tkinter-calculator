from tkinter import *
from functools import partial

root = Tk(className="Calculator")

expression_input = Entry(root, width=40)
expression_input.grid(row=0, columnspan=4, padx=10, pady=20, ipadx=20, ipady=10)

expression = ""


def add_to_expression(val):
	global expression
	expression += str(val)
	expression_input.delete(0, END)
	expression_input.insert(0, expression)


digit = 1

for row in range(1, 4):
	for col in range(1, 4):
		button = Button(root, text=digit, padx=46, pady=40, command=partial(add_to_expression, digit))
		button.grid(row=row, column=col)
		digit += 1

zero_button = Button(root, text=0, padx=45, pady=40, command=partial(add_to_expression, 0))
zero_button.grid(row=4, column=1)

add_button = Button(root, text="+", padx=46, pady=40, command=partial(add_to_expression, "+"))
add_button.grid(row=4, column=2)

subtract_button = Button(root, text="-", padx=46, pady=40, command=partial(add_to_expression, "-"))
subtract_button.grid(row=4, column=3)

multiply_button = Button(root, text="*", padx=45, pady=40, command=partial(add_to_expression, "*"))
multiply_button.grid(row=5, column=2)

divide_button = Button(root, text="/", padx=45, pady=40, command=partial(add_to_expression, "/"))
divide_button.grid(row=5, column=3)


def evaluate():
	global expression
	try:
		evaluated_expression = eval(expression)
		expression = str(evaluated_expression)
		expression_input.delete(0, END)
		expression_input.insert(0, evaluated_expression)
	except (SyntaxError, ZeroDivisionError):
		expression_input.delete(0, END)
		expression_input.insert(0, "Error")
		expression = ""


equal_button = Button(root, text="=", padx=45, pady=40, command=evaluate, fg="white", bg="orange")
equal_button.grid(row=5, column=1)


def clear_expression():
	global expression
	expression_input.delete(0, END)
	expression_input.insert(0, "")
	expression = ""


clear_button = Button(root, text="CLEAR", padx=20, pady=20, command=clear_expression, fg="white", bg="crimson")
clear_button.grid(row=6, columnspan=4, pady=20)

root.mainloop()
