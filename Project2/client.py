import socket
import threading
from tkinter import *

PORT = 51000
SERVER = "192.168.0.106"
ADDRESS = (SERVER, PORT)
FORMAT = "utf-8"

client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client.connect(ADDRESS)


class chatbox:
    def __init__(self):
        # chat window which is currently hidden
        self.root = Tk()
        self.root.withdraw()

        # login window for user to add names and connect with server
        self.login = Toplevel()

        # set the title for login window
        self.login.title("Login")
        self.login.resizable(width=False, height=False)
        self.login.configure(width=500, height=400)

        # create a label
        self.label = Label(self.login, text="Login", justify=CENTER, font=("Times New Roman", 14), fg="#585858")
        self.label.place(relheight=0.15, relx=0.5, rely=0.07)

        # create a Label
        self.labelName = Label(self.login, text="Enter Name: ", font=("Times New Roman", 12), fg="#585858")
        self.labelName.place(relheight=0.2, relx=0.1, rely=0.2)

        # creating an entry box
        self.entryName = Entry(self.login, font=("Times New Roman", 10), fg="#CC1559")
        self.entryName.place(relwidth=0.4, relheight=0.12, relx=0.35, rely=0.2)

        # set the focus of the cursor
        self.entryName.focus()

        # create a continue button along with action
        self.go = Button(self.login, text="Submit", font=("Times New Roman", 14), fg="#585858",
                         command=lambda: self.toChatWindow(self.entryName.get()))
        self.go.place(relx=0.4, rely=0.55)
        self.root.mainloop()

    def toChatWindow(self, name):
        self.login.destroy()
        self.layout(name)

        # thread created to receive messages
        rev = threading.Thread(target=self.receive)
        rev.start()

    # The main layout of the chat
    def layout(self, name):
        self.name = name
        # to show chat window
        self.root.deiconify()
        self.root.title("Chat room")
        self.root.resizable(width=False, height=False)
        self.root.configure(width=470, height=550, bg="#3F404C")
        self.labelHead = Label(self.root, bg="#3F404C", fg="#DFD4CA", text=self.name,
                               font=("Times New Roman", 14, "bold"), pady=5)
        self.labelHead.place(relwidth=1)
        self.line = Label(self.root, width=580, bg="#FE6726")
        self.line.place(relwidth=1, rely=0.07, relheight=0.012)
        self.textCons = Text(self.root, width=20, height=2, bg="#3F404C", fg="#ECEADF", font=("Times New Roman", 14),
                             padx=5, pady=5)
        self.textCons.place(relheight=0.745, relwidth=1, rely=0.08)
        self.labelBottom = Label(self.root, bg="#DFD4CA", height=80)
        self.labelBottom.place(relwidth=1, rely=0.825)
        self.entryMsg = Entry(self.labelBottom, bg="#DFD4CA", fg="#3F404C")
        self.entryMsg.place(relwidth=0.74, relheight=0.06, rely=0.008, relx=0.011)
        self.entryMsg.focus()

        self.buttonMsg = Button(self.labelBottom, text="Send", font=("Times New Roman", 10), width=20, bg="#DFD4CA",
                                activebackground="#DFD4CA",
                                fg="#FE6726", activeforeground="#FE6726",
                                command=lambda: self.sendButton(self.entryMsg.get()))
        self.buttonMsg.place(relx=0.77, rely=0.008, relheight=0.06, relwidth=0.22)
        self.textCons.config(cursor="arrow")

        scrollbar = Scrollbar(self.textCons)
        scrollbar.place(relheight=1, relx=0.974)
        scrollbar.config(command=self.textCons.yview)

        self.textCons.config(state=DISABLED)

    def sendButton(self, msg):
        self.textCons.config(state=DISABLED)
        self.msg = msg
        self.entryMsg.delete(0, END)
        snd = threading.Thread(target=self.sendMessage)
        snd.start()

    def receive(self):
        while True:
            try:
                message = client.recv(1050).decode(FORMAT)

                if message == 'NAME':
                    client.send(self.name.encode(FORMAT))
                else:
                    self.textCons.config(state=NORMAL)
                    self.textCons.insert(END, message + "\n\n")
                    self.textCons.config(state=DISABLED)
                    self.textCons.see(END)
            except:
                print("AN ERROR OCCURED!")
                client.close()
                break

    def sendMessage(self):
        self.textCons.config(state=DISABLED)
        while True:
            message = (f"{self.name}: {self.msg}")
            client.send(message.encode(FORMAT))
            break


g = chatbox()
