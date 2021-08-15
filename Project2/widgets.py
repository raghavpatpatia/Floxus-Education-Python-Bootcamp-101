from tkinter import *
# from tkinter import messagebox
# from tkinter import colorchooser

# creating root window
window = Tk()

# giving title to window
window.title("Widgets")

# defining size of window
window.geometry("500x500")

# add background color to your root window
window.config(bg="alice blue")


# add a label by Label(parent window, text, text formatting)
# label = Label(window, text="This button prints \"Hello, world!\"", bg="alice blue", fg="crimson",
#               font=("Times New Roman", 14))

# place label inside window
# label.place(x=120, y=220)

# counting every time button is clicked
# window.counter = 0


# def submit():
    # window.counter += 1 # creating a function for button to print "Hello, world!" and counting every time button is clicked
    # print(str(window.counter) + '.', "Hello, world!")
    # val = entry.get() # to print text
    # print(val)
    # entry.delete(-1) # delete last character from given string
    # entry.delete(0, END) # delete entire string from text box
    # messagebox.showerror(title="Error", message="Error 404") # create a messagebox
    # window.config(bg=colorchooser.askcolor()[1]) # change color by selecting color

# creating a text box
# entry = Entry(window, font=("Times New Roman", 16), bg="Black", fg="crimson", show="*")

# placing entry inside window
# entry.place(x= 120, y= 190)

# creating button by Button(parent window, text, font-formatting, command)
# button = Button(window, text="submit", command=submit)

# place button inside window
# button.place(x=200, y=250)

# creating a checkbox
# checkbox = Checkbutton(window, text="Click me.")
# checkbox1 = Checkbutton(window, text="Click here.")

# placing checkbox inside windows
# checkbox.place(x=120, y=200)
# checkbox1.place(x=120, y=220)

# creating radiobutton
# radio = Radiobutton(window, text="1", variable="var", value=1, anchor="w")
# radio1 = Radiobutton(window, text="2", variable="var", value=2, anchor="w")

# placing radiobutton inside window
# radio.place(x=120, y=220)
# radio1.place(x=120, y=240)

# mainloop
window.mainloop()
