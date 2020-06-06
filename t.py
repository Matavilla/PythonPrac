import tkinter
from tkinter import scrolledtext

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

#btnFrame = tkinter.Frame()
#fileFrame = tkinter.Frame()

fileName = tkinter.Entry(mainWindow, bd = 4, relief = tkinter.GROOVE, width = '25')
fileName.grid(row = 1, column = 1)

openBtn = tkinter.Button(mainWindow, text = 'Open file', font = 'Arial 24', bd = 5)
openBtn.grid(row = 1, column = 2)
openBtn.bind('<Button>', lambda event: print(1))

saveBtn = tkinter.Button(mainWindow, text = 'Save', font = 'Arial 24', bd = 5)
saveBtn.grid(row = 1, column = 3)
saveBtn.bind('<Button>', lambda event: print(2))

saveAsBtn = tkinter.Button(mainWindow, text = 'Save As', font = 'Arial 24', bd = 5)
saveAsBtn.grid(row = 1, column = 4)
saveAsBtn.bind('<Button>', lambda event: print(2))

text = tkinter.Text(bg='#FFFFE0')
yScroll = tkinter.Scrollbar(mainWindow, command = text.yview)
xScroll = tkinter.Scrollbar(orient = tkinter.HORIZONTAL, command = text.xview)
text.configure(yscrollcommand = yScroll.set, xscrollcommand = xScroll.set)
text.grid(row = 2, column = 1, columnspan = 2, padx = 20, pady = 20)
yScroll.grid(row = 2, column = 3)
xScroll.grid(row = 2, column = 3)

#btnFrame.pack()
#fileName.pack(side = tkinter.LEFT)
#openBtn.pack(side = tkinter.LEFT)
#saveBtn.pack(side = tkinter.LEFT)

#fileFrame.pack(fill = tkinter.BOTH, expand = 1)
#text.pack(side = tkinter.LEFT, fill = tkinter.BOTH, expand = 1)
#xScroll.pack(side = tkinter.LEFT, fill = tkinter.Y)
#yScroll.pack(side = tkinter.BOTTOM, fill = tkinter.X)
mainWindow.mainloop()
