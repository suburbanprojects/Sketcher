import tkinter as tk
from tkinter import *
from tkinter import ttk
from tkinter.colorchooser import askcolor

#put program frame here
app = tk.Tk()
app.title("Sketcher")

#button functions
def callclr():
    global result
    result = askcolor (title="Colour Picker")

def ClearCanvas():
    canvas.delete('all')

#drawing functions
def savePosn(event):
    global lastx, lasty
    lastx, lasty = event.x, event.y

def addLine(event):
    canvas.create_line((lastx, lasty, event.x, event.y),
                       fill=result[1], width=current_line_size, capstyle=ROUND)
    savePosn(event)

#gui stuff
tool_bar = ttk.Label(app)
tool_bar.pack(side=tk.TOP, fill=tk.X)

canvas = Canvas(app)
canvas.pack(fill=tk.BOTH, expand=True)
canvas.bind("<Button-1>", savePosn)
canvas.bind("<B1-Motion>", addLine)

#colour select 
colourButton = ttk.Button(tool_bar, text="Choose Colour", command=callclr)
colourButton.grid(row=0, column=2, padx=5)

#clear button
clearButton = ttk.Button(tool_bar, text="Clear Canvas", command=ClearCanvas)
clearButton.grid(row=0, column=3, padx=5)

#line size select
line_sizes = tk.IntVar()
line_select=ttk.Combobox(tool_bar, width=30, textvariable=line_sizes
                      ,state='readonly')
line_select['values']=tuple(range(5,30,5))
line_select.grid(row=0,column=0, padx=5)

#define line size function here
def changeSize(event=None):
    global current_line_size
    current_line_size = line_sizes.get()
line_select.bind("<<ComboboxSelected>>",changeSize)

app.mainloop()
