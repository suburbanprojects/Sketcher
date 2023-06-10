from tkinter import * 
from tkinter.colorchooser import askcolor

canvas_width = 500
canvas_height = 150

def callclr():
    global result
    result = askcolor (title="Colour Picker")

def paint( event ):
    global result
    brush = result[1] #1 gets the hex value of the colour chosen
    x1, y1 = ( event.x - 1), ( event.y - 1 )
    x2, y2 = ( event.x + 1), ( event.y + 1 )
    w.create_oval(x1,y1,x2,y2, fill = brush )

def ClearCanvas(): 
    w.delete('all')

app = Tk()
app.title("Sketcher")

w = Canvas(app, width=canvas_width, height=canvas_height)
w.pack(expand = YES, fill = BOTH)
w.bind( "<B1-Motion>", paint )

message = Label( app, text = "Press and Drag Mouse To Draw")
message.pack( side = BOTTOM )

colourButton = Button(app, text="Choose Colour", command=callclr)
colourButton.pack(side = LEFT)
clearButton = Button(app, text="Clear Canvas", command = ClearCanvas)
clearButton.pack(side = LEFT)

app.mainloop()

