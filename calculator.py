# A simple Python calculator program using the Tkinter GUI

# import everything from tkinter
from tkinter import *

#for the calculator to work we have to store inputs as a variable which will then be evaluated at the end.
#the input is simple the mathematical expression of the problem
# declare the problem variable
problem = ""


# create a Function to update problem statement or expression in the text entry box

def button_pressed(num):
	# point to the global variable called problem. this would contain all the user input for evaluation.
	global problem

	# continuous concatenation of string as user adds more levels to the arithmetics
	problem = problem + str(num)

	# update the problem by using set method
	equation.set(problem)


# Function to evaluate the final problem
def answer():
	# User try and except statement handle errors

	try:

		global problem

		# eval function evaluate the problem
		# and str function convert the result
		# into string
		total = str(eval(problem))

		equation.set(total)

		# initialize the problem variable
		# by empty string
		problem = ""

	# if an error is generated the error is handled by the except block
	except:

		equation.set(" error! invalid operation ")
		problem = ""


# Create a function to clear the contents of the display
def clear():
	global problem
	problem = ""
	equation.set("")


# Driver code gives this program a different behviour depending on whether it is being run by a user or a program
if __name__ == "__main__":
	# create a calculator GUI window by calling the Tk() module
	gui = Tk()


	# set the background colour of the calculator GUI window
	gui.configure(background="White")

	# set the title of the calculator GUI window
	gui.title("EDSA TEAM_1")

	# set the configuration of GUI window
	gui.geometry("250x310")

	# StringVar() is the variable class
	# we create an instance of this class
	equation = StringVar()

	# create the text entry box for showing the problem and displaying the solution.
	display_field = Entry(gui, textvariable=equation, font=("default",15))
	

	# grid method is used for giving a table-like structure to buttons and widgets .
	display_field.grid(columnspan=6, ipadx=70)

	# create Buttons and place at a particular
	# location inside the root window .
	# when user presses the button, the command or
	# function affiliated to that button is executed .
	button1 = Button(gui, text=' 1 ', fg='black', bg='white',
					command=lambda: button_pressed(1), height=2, width=7)
	button1.grid(row=3, column=0)

	button2 = Button(gui, text=' 2 ', fg='black', bg='white',
					command=lambda: button_pressed(2), height=2, width=7)
	button2.grid(row=3, column=1)

	button3 = Button(gui, text=' 3 ', fg='black', bg='white',
					command=lambda: button_pressed(3), height=2, width=7)
	button3.grid(row=3, column=2)

	button4 = Button(gui, text=' 4 ', fg='black', bg='white',
					command=lambda: button_pressed(4), height=2, width=7)
	button4.grid(row=4, column=0)

	button5 = Button(gui, text=' 5 ', fg='black', bg='white',
					command=lambda: button_pressed(5), height=2, width=7)
	button5.grid(row=4, column=1)

	button6 = Button(gui, text=' 6 ', fg='black', bg='white',
					command=lambda: button_pressed(6), height=2, width=7)
	button6.grid(row=4, column=2)

	button7 = Button(gui, text=' 7 ', fg='black', bg='white',
					command=lambda: button_pressed(7), height=2, width=7)
	button7.grid(row=5, column=0)

	button8 = Button(gui, text=' 8 ', fg='black', bg='white',
					command=lambda: button_pressed(8), height=2, width=7)
	button8.grid(row=5, column=1)

	button9 = Button(gui, text=' 9 ', fg='black', bg='white',
					command=lambda: button_pressed(9), height=2, width=7)
	button9.grid(row=5, column=2)

	button0 = Button(gui, text=' 0 ', fg='black', bg='white',
					command=lambda: button_pressed(0), height=2, width=7)
	button0.grid(row=6, column=1)

	plus = Button(gui, text=' + ', fg='black', bg='white',
				command=lambda: button_pressed("+"), height=2, width=7)
	plus.grid(row=7, column=0)

	minus = Button(gui, text=' - ', fg='black', bg='white',
				command=lambda: button_pressed("-"), height=2, width=7)
	minus.grid(row=7, column=1)

	multiply = Button(gui, text=' x ', fg='black', bg='white',
					command=lambda: button_pressed("*"), height=2, width=7)
	multiply.grid(row=7, column=2)

	divide = Button(gui, text=' / ', fg='black', bg='white',
					command=lambda: button_pressed("/"), height=2, width=7)
	divide.grid(row=8, column=0)

	equal = Button(gui, text=' = ', fg='black', bg='white',
				command=answer, height=2, width=7)
	equal.grid(row=6, column=2)

	clear = Button(gui, text='Clear', fg='black', bg='white',
				command=clear, height=2, width=7)
	clear.grid(row=9, column=0)

	Decimal= Button(gui, text='.', fg='black', bg='white',
					command=lambda: button_pressed('.'), height=2, width=7)
	Decimal.grid(row=6, column=0)
	parenthesis_left = Button(gui, text ='(', fg='black', bg='white',
                                  command=lambda:button_pressed('('), height=2, width=7)
	parenthesis_left.grid(row = 8, column =1)
	parenthesis_right = Button(gui, text =')', fg='black', bg='white',
                                  command=lambda:button_pressed(')'), height=2, width=7)
	parenthesis_right.grid(row = 8, column =2)
	# start the GUI
	gui.mainloop()
