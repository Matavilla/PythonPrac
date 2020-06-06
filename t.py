import tkinter
import os, subprocess
from tkinter import messagebox
from tkinter import filedialog as fd
from tkinter.scrolledtext import ScrolledText

NAME = ""

def OpenFile():
    global NAME
    NAME = fd.askopenfilename()
    try:
        process = subprocess.check_output(["xxd", "-g1", str(NAME)])
        text.delete(1.0, tkinter.END)
        text.insert(1.0, process)
    except:
        messagebox.showinfo("INFORMATION", "Something strange")

def SaveFile(name):
    try:
        fileForWrite = text.get(1.0, tkinter.END)
        f = open("tmp", "w")
        f.write(fileForWrite)
        f.close()
        process = subprocess.check_output(["xxd", "-r", "tmp"])
        file_2 = open(name, 'wb')
        file_2.write(process)
    except:
        messagebox.showerror("ERROR", "Something strange")

def SaveAsFile():
    SaveFile(fd.asksaveasfilename())


mainWindow = tkinter.Tk()

mainWindow.title('Editor')
mainWindow.protocol("WM_DELETE_WINDOW", lambda: (_ for _ in ()).throw(SystemExit(0)))

w = mainWindow.winfo_screenwidth()
h = mainWindow.winfo_screenheight()
mainWindow.geometry(f'{w // 2}x{h // 2}+{w // 2 - w // 4}+{h // 2 - h // 4}')
mainWindow.columnconfigure(1, weight = 1)
mainWindow.columnconfigure(3, weight = 1)
mainWindow.rowconfigure(1, weight = 1)
mainWindow.rowconfigure(5, weight = 1)

openBtn = tkinter.Button(mainWindow, text = 'Open file', font = 'Arial 24', bd = 5)
openBtn.grid(row = 1, column = 1)
openBtn.bind('<Button>', lambda event: OpenFile())

saveBtn = tkinter.Button(mainWindow, text = 'Save', font = 'Arial 24', bd = 5)
saveBtn.grid(row = 1, column = 2)
saveBtn.bind('<Button>', lambda event: SaveFile(NAME))

saveAsBtn = tkinter.Button(mainWindow, text = 'Save As', font = 'Arial 24', bd = 5)
saveAsBtn.grid(row = 1, column = 3)
saveAsBtn.bind('<Button>', lambda event: SaveAsFile())

text = ScrolledText(bg='#FFFFE0')
text.grid(row = 2, column = 0, columnspan = 4, rowspan = 3)

mainWindow.mainloop()
