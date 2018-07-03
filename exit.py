from Tkinter import *

def yes():
    top.destroy()

def no():
    top.destroy()
    import signup 


top=Tk()
top.title("exit")
top.geometry("300x150+700+300")
top.configure(background="aqua")

Label(top,text="Are you sure want to exit",
      font=10,bg="yellow",fg="blue",width=35,
      height=3).pack()

Button(top,text="Yes",command=yes,width=8,bg="green").place(x=50,y=90)
Button(top,text="no",command=no,width=8,bg="light blue").place(x=200,y=90)



top.mainloop()
