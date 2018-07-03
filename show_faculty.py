from Tkinter import *
import ttk
import tkMessageBox
import mysql.connector

root=Tk()

root.geometry('1000x500+300+100')
root.title("Add(faulty) Page")
root.configure(bg="aqua")

value=StringVar()
ans=StringVar()
c = StringVar()
d = StringVar()
e = StringVar()
h = StringVar()
g = StringVar()

f=open("teacher1.txt","r")
value=f.read()
ans.set(value)
f.close()

conn= mysql.connector.connect(user="root",password="",host="localhost",database="time_table")
cursor=conn.cursor()
cursor.execute("select * from teacher where Name='"+ans.get()+"'")
b = cursor.fetchone()
l=list(b)
c.set(l[4])
d.set( l[5])
e.set (l[6])
h.set(l[7])
g.set(l[8])

conn.commit()


l1 = Label(root,text="Name",bg="aqua",font=("comic sans",20),fg="black")
l1.place(x=200,y=50)
l2=Label(root,textvariable=ans,bg="aqua",fg="black",font=("comic sans",20))
l2.place(x=400,y=50)
l3 = Label(root,text="Course",bg="aqua",font=("comic sans",20),fg="black")
l3.place(x=200,y=100)
l4 = Label(root,textvariable=c,bg="aqua",font=("comic sans",20),fg="black")
l4.place(x=400,y=100)
l5 = Label(root,text="Subject",bg="aqua",font=("comic sans",20),fg="black")
l5.place(x=200,y=150)
l6 = Label(root,textvariable=d,bg="aqua",font=("comic sans",20),fg="black")
l6.place(x=400,y=150)
l7 = Label(root,text="Semester",bg="aqua",font=("comic sans",20),fg="black")
l7.place(x=200,y=200)
l8 = Label(root,textvariable=e,bg="aqua",font=("comic sans",20),fg="black")
l8.place(x=400,y=200)

l9 = Label(root,text="Mobile NO:",bg="aqua",font=("comic sans",20),fg="black")
l9.place(x=200,y=250)
l10=Label(root,textvariable=h,bg="aqua",fg="black",font=("comic sans",20))
l10.place(x=400,y=250)
l11 = Label(root,text="Email ID:",bg="aqua",font=("comic sans",20),fg="black")
l11.place(x=200,y=300)
l12=Label(root,textvariable=g,bg="aqua",fg="black",font=("comic sans",20))
l12.place(x=400,y=300)

root.mainloop()




