from tkinter import *
from time import *

# creating root window
window = Tk()

# giving title to window
window.title("Clock")

# setting window dimensions
window.geometry("500x500")

# add background color to your root window
window.config(bg="alice blue")


# creating a function to update time
def update():
    time_string = strftime("%I:%M:%S %p")
    time.config(text=time_string)
    time.after(1000, update)

    date_string = strftime("%B %d, %Y")
    date.config(text=date_string)
    date.after(1000, update)


# creating a label
time_label = Label(window, text="Current Time: ", fg="crimson", bg="alice blue", font=("Times New Roman", 20))

# placing label inside windows
time_label.place(x=50, y=180)

# creating a label
time = Label(window, fg="crimson", bg="alice blue", font=("Digital-7", 20))

# placing label inside windows
time.place(x=210, y=183)

# creating a label
date_label = Label(window, text="Date: ", fg="crimson", bg="alice blue", font=("Times New Roman", 20))

# placing label inside windows
date_label.place(x=140, y=250)

# creating a label
date = Label(window, fg="crimson", bg="alice blue", font=("Digital-7", 18))

# placing label inside windows
date.place(x=210, y=253)

# updating current time and date
update()

# calling mainloop
window.mainloop()
