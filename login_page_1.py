from Tkinter import *
import tkMessageBox
import mysql.connector

root=Tk()

root.geometry('1000x500+300+100')
root.title("Home Page(admin)")
root.configure(bg="aqua")



menubar=Menu(root)
facultymenu=Menu(menubar,tearoff=0)
menubar.add_cascade(label="Faculty",menu=facultymenu)

cscmenu=Menu(menubar,tearoff=0)
facultymenu.add_cascade(label="Computer Science",menu=cscmenu)
cscmenu.add_command(label="COL100")
cscmenu.add_command(label="COL200")
cscmenu.add_command(label="COL300")
facultymenu.add_separator()
eemenu=Menu(menubar,tearoff=0)
facultymenu.add_cascade(label="Electrical Engineering",menu=eemenu)
eemenu.add_command(label="Ell100")
eemenu.add_command(label="Ell200")
eemenu.add_command(label="Ell300")
facultymenu.add_separator()
cvlmenu=Menu(menubar,tearoff=0)
facultymenu.add_cascade(label="Civil Engineering",menu=cvlmenu)
cvlmenu.add_command(label="CVL100")
cvlmenu.add_command(label="CVL200")
cvlmenu.add_command(label="CVL300")
facultymenu.add_separator()
cmlmenu=Menu(menubar,tearoff=0)
facultymenu.add_cascade(label="Chemical Engineering",menu=cmlmenu)
cmlmenu.add_command(label="CML00")
cmlmenu.add_command(label="CML200")
cmlmenu.add_command(label="CML300")
facultymenu.add_separator()
facultymenu.add_separator()

timetablemenu=Menu(menubar,tearoff=0)
menubar.add_cascade(label="Time Table",menu=timetablemenu)
timetablemenu.add_command(label="View time table")
timetablemenu.add_separator()
timetablemenu.add_command(label="Edit time table")
timetablemenu.add_separator()
timetablemenu.add_command(label="Swap time table")
timetablemenu.add_separator()
timetablemenu.add_separator()

helpmenu=Menu(menubar,tearoff=0)
menubar.add_cascade(label="Help",menu=helpmenu)
helpmenu.add_command(label="Index")
helpmenu.add_separator()
moremenu=Menu(menubar,tearoff=0)
helpmenu.add_cascade(label="More",menu=moremenu)
moremenu.add_command(label="Developer")
moremenu.add_command(label="Contact No.")
moremenu.add_command(label="Version")
helpmenu.add_separator()
helpmenu.add_separator()
root.config(menu=menubar)

l1=Label(root,text="CHOOSE FROM ABOVE OPTIONS ADMIN",fg="black",font=("arial",24))
l1.place(x=250,y=225)

root.mainloop()
