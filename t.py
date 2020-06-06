import tkinter
import os, subprocess, sys
from tkinter import messagebox
from tkinter import filedialog as fd
from tkinter.scrolledtext import ScrolledText

FIRST_OPEN = ""
NAME = ""
SAVE_FILE = ""

def OpenFile():
    global NAME, FIRST_OPEN
    if FIRST_OPEN:
        NAME = FIRST_OPEN
        FIRST_OPEN = ""
    else:
        NAME = fd.askopenfilename()
    process = subprocess.run(["xxd", "-g1", str(NAME)], stdout = subprocess.PIPE, stderr = subprocess.PIPE)
    if process.returncode:
        messagebox.showerror("Error", process.stderr)
    else:
        mainWindow.title('Editor: ' + str(NAME))
        text.delete(1.0, tkinter.END)
        text.insert(1.0, process.stdout)

def SaveFile(name):
    try:
        fileForWrite = text.get(1.0, tkinter.END)
        f = open("tmp", "w")
        f.write(fileForWrite)
        f.close()
        process = subprocess.run(["xxd", "-r", "tmp"], stdout = subprocess.PIPE, stderr = subprocess.PIPE)
        file_2 = open(name, 'wb')
        file_2.write(process.stdout)
    except Exception as err:
        messagebox.showerror("Error", err)

def Save():
    global SAVE_FILE, NAME
    if SAVE_FILE:
        SaveFile(SAVE_FILE)
        SAVE_FILE = ""
    else:
        SaveFile(NAME)


def SaveAsFile():
    global NAME
    NAME = fd.asksaveasfilename()
    SaveFile(NAME)
    mainWindow.title('Editor: ' + str(NAME))

def Undo():
    try:
        text.edit_undo()
    except:
        return

def Redo():
    try:
        text.edit_redo()
    except:
        return


mainWindow = tkinter.Tk()

mainWindow.title('Editor')
mainWindow.protocol("WM_DELETE_WINDOW", lambda: (_ for _ in ()).throw(SystemExit(0)))

if len(sys.argv) == 2:
    FIRST_OPEN = sys.argv[1]
elif len(sys.argv) == 3:
    FIRST_OPEN = sys.argv[1]
    SAVE_FILE = sys.argv[2]

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
saveBtn.bind('<Button>', lambda event: Save())

saveAsBtn = tkinter.Button(mainWindow, text = 'Save As', font = 'Arial 24', bd = 5)
saveAsBtn.grid(row = 1, column = 3)
saveAsBtn.bind('<Button>', lambda event: SaveAsFile())

text = ScrolledText(bg='#FFFFE0', undo = True)
text.grid(row = 2, column = 0, columnspan = 4, rowspan = 3)

redoBtn = tkinter.Button(mainWindow, text = 'Redo', font = 'Arial 24', bd = 5)
redoBtn.grid(row = 2, column = 4)
redoBtn.bind('<Button>', lambda event: Redo())

undoBtn = tkinter.Button(mainWindow, text = 'Undo', font = 'Arial 24', bd = 5)
undoBtn.grid(row = 2, column = 5)
undoBtn.bind('<Button>', lambda event: Undo())

mainWindow.mainloop()
