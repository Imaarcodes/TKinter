from tkinter import *
def checkboxes():
   #from tkinter import *
    master = Tk()
    var1 = IntVar()
    Checkbutton(master, text='male', variable=var1).grid(row=0, sticky=W)
    var2 = IntVar()
    Checkbutton(master, text='female', variable=var2).grid(row=1, sticky=W)
    var3 = IntVar()
    Checkbutton(master, text='other', variable=var2).grid(row=2, sticky=W)
    var4 = IntVar()
    Checkbutton(master, text='Goofball', variable=var2).grid(row=3, sticky=W)

def text_entry():
    master = Tk()
    Label(master, text='First Name').grid(row=4)
    Label(master, text='Last Name').grid(row=5)
    Label(master, text='Are You Cool?').grid(row=6)
    Label(master, text='Are you worthy?').grid(row=7)
    e1 = Entry(master)
    e2 = Entry(master)
    e3 = Entry(master)
    e4 = Entry(master)
    e1.grid(row=4, column=1)
    e2.grid(row=5, column=1)
    e3.grid(row=6, column=1)
    e4.grid(row=7, column=1)

def slider():
    master = Tk()
    w = Scale(master, from_=0, to=42)
    w.pack()
    w = Scale(master, from_=0, to=200, orient=HORIZONTAL)
    w.pack()


def label():

    root = Tk()
    w = Label(root, text='Label 1')
    w.pack()
    w2 = Label(root, text='Label 2')
    w2.pack()
    w3 = Label(root, text='Label 3')
    w3.pack()
    w4 = Label(root, text='Label 4')
    w4.pack()


def button():
    import tkinter as tk
    r = tk.Tk()
    #Button number 1
    r.title('Buttons!')
    button = tk.Button(r, text='Button 1', width=25, command=r.destroy)
    button.pack()
    #Button number 2
    button2 = tk.Button(r, text='Button 2', width=25, command=r.destroy)
    button2.pack()
    #Button number 3
    button3 = tk.Button(r, text='Button 3', width=25, command=r.destroy)
    button3.pack()
    #Button number 4
    button4 = tk.Button(r, text='Button 4', width=25, command=r.destroy)
    button4.pack()
def menu():
    top = Tk()
    mb = Menubutton ( top, text = "This Is A Menu")
    mb.grid()
    mb.menu = Menu ( mb, tearoff = 0 )
    mb["menu"] = mb.menu
    cVar = IntVar()
    aVar = IntVar()
    mb.menu.add_checkbutton ( label ='Contact', variable = cVar )
    mb.menu.add_checkbutton ( label = 'About', variable = aVar )
    mb.pack()


def message():
    main = Tk()
    ourMessage ='This is a message box!'
    messageVar = Message(main, text = ourMessage)
    messageVar.config(bg='white')
    messageVar.pack( )



def radio():
    root = Tk()
    v = IntVar()
    Radiobutton(root, text='Are you in Science', variable=v, value=1).pack(anchor=W)
    Radiobutton(root, text='Are you in Math', variable=v, value=2).pack(anchor=W)
    Radiobutton(root, text='Are you in Lang & Lit', variable=v, value=3).pack(anchor=W)
    Radiobutton(root, text='Are you in Computer Science', variable=v, value=4).pack(anchor=W)
    Radiobutton(root, text='Are you in ECON', variable=v, value=5).pack(anchor=W)



def spinbox():
    master = Tk()
    w = Spinbox(master, from_ = 0, to = 10)
    w.pack()
    mainloop()


def calling_functions():
    checkboxes()
    text_entry()
    slider()
    label()
    button()
    menu()
    message()
    radio()
    spinbox()
calling_functions()