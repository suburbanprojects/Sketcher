import tkinter as tk
from tkinter import *
from tkinter import ttk, filedialog
from PIL import Image, ImageDraw
from tkinter.colorchooser import askcolor

class ImageGenerator2:
    def __init__(self,app):
        self.root = app
        self.imageGen_layout()

    def imageGen_layout(self):
        #create toolbar for menu
        self.tool_bar = ttk.Label(app)
        self.tool_bar.pack(side=tk.TOP, fill=tk.X)
        #put the buttons here
        self.colourButton = ttk.Button(self.tool_bar, text="Choose Colour", command=self.callclr)
        self.colourButton.grid(row=0, column=1, padx=5)
        self.SaveButton=ttk.Button(self.tool_bar, text="Save", command=self.save)
        self.SaveButton.grid(row=0, column=2, padx=5)
        self.ClearButton=ttk.Button(self.tool_bar,text="Clear",command=self.clear)
        self.ClearButton.grid(row=0, column=3, padx=5)
        #put the linesize dropdown here
        self.line_sizes = tk.IntVar()
        self.line_select=ttk.Combobox(self.tool_bar, width=30, textvariable=self.line_sizes, state='readonly')
        self.line_select['values']=tuple(range(5,30,5))
        self.line_select.grid(row=0,column=0, padx=5)
        
        self.labelMessage = tk.Label(app, text="Select size and colour before drawing")
        self.labelMessage.pack(side=tk.BOTTOM, fill=tk.X)
        #create canvas
        self.canvas = Canvas(app)
        self.canvas.pack(fill=tk.BOTH, expand=True)
        self.canvas.configure(bg="black")
        #drawing on canvas actions go here
        self.canvas.bind("<Button-1>", self.savePosn)
        self.canvas.bind("<B1-Motion>", self.addLine)
        #how to draw
        self.image=Image.new("RGB",(500,500))
        #350 by 350 is image dimension, 255,255,255 in rgb is white
        self.draw=ImageDraw.Draw(self.image)

    def save(self):
            filename = filedialog.asksaveasfile(mode='w', defaultextension=".jpg")
            if filename:
                self.image.save(filename)
                filename.close()

    def clear(self):
        self.canvas.delete("all")
        #a new image will be created
        #otherwise the new image won't be saved
        self.image=Image.new("RGB",(500,500))  
        self.draw=ImageDraw.Draw(self.image)
    
    def callclr(self):
        self.result = askcolor(title="Colour Picker")

    def savePosn(self,event):
        self.lastx, self.lasty = event.x, event.y
    
    def addLine(self,event):
        self.current_line_size = self.line_sizes.get()
        self.canvas.create_line((self.lastx, self.lasty, event.x, event.y),
                                fill=self.result[1], width=self.current_line_size,
                                capstyle=ROUND)
        self.draw.line(((self.lastx,self.lasty),(event.x,event.y)),(self.result[1]),
                       width=self.current_line_size, joint='curve')
        self.savePosn(event)

if __name__ == "__main__":
    app = tk.Tk()
    app.title("Sketcher")
    app.geometry('500x500')
    app2 = ImageGenerator2(app)
    app.mainloop()
