import tkinter as tk







class myapps:
    def __init__(self,root:tk.Tk,backgrounds:str,widths:int,heights:int,colors:str,steps:int,tiltes:str):
        self.root=root
        self.root.title(tiltes)
        self.root.geometry(str(widths)+"x"+str(heights))
        self.root.configure(background=backgrounds)
        self.canvas=tk.Canvas(background=backgrounds,width=widths,height=heights)
        self.canvas.pack(padx=1,pady=1)
        c = self.canvas
        c.delete("all")
        for a in range(0,heights,steps):
            c.create_line(0,a,widths,a,fill=colors)
        
        for a in range(0,widths,steps):
            c.create_line(a,0,a,heights,fill=colors)


def starts(backgrounds:str,widths:int,heights:int,colors:str,steps:int,tiltes:str):
    root=tk.Tk()
    apps=myapps(root,backgrounds,widths,heights,colors,steps,tiltes)
    root.mainloop()

backgrounds:str="black"
colors:str="white"
widths:int=640
heights:str=480
steps:int=20
tiltes:str="grid ..........."

starts(backgrounds,widths,heights,colors,steps,tiltes)
