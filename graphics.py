import tkinter as tk







class myapps:
    def __init__(self,root:tk.Tk):
        self.root=root
        self.root.title("graphics....")
        self.root.geometry("640x480")
        self.root.configure(background="black")
        self.canvas=tk.Canvas(background="black",width=640,height=480)
        self.canvas.pack(padx=1,pady=1)
        c = self.canvas
        c.delete("all")
        for a in range(0,480,20):
            c.create_line(0,a,640,a,fill="white")
        
        for a in range(0,640,20):
            c.create_line(a,0,a,480,fill="white")

root=tk.Tk()
apps=myapps(root)
root.mainloop()
