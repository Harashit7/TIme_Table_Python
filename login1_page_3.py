from Tkinter import *
import tkMessageBox
import mysql.connector

root=Tk()

root.geometry('1300x600+200+100')
root.title("Add_2(admin) Page")
root.configure(bg="aqua")

ans = StringVar()
c = StringVar()
d = StringVar()
e = StringVar()


f=open("teacher.txt","r")
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
conn.commit()


def back():
    root.destroy()
    import login_page_2




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

c1 = Checkbutton(root,activebackground="red",text="First",font=(20),activeforeground="green",bd=3,highlightcolor="green",height=2,width=4)
c1.place(x=200,y=400)
c1 = Checkbutton(root,activebackground="red",text="Second",font=(20),activeforeground="green",bd=3,highlightcolor="green",height=2,width=7)
c1.place(x=350,y=400)
c1 = Checkbutton(root,activebackground="red",text="Third",font=(20),activeforeground="green",bd=3,highlightcolor="green",height=2,width=5)
c1.place(x=500,y=400)
c1 = Checkbutton(root,activebackground="red",text="Fourth",font=(20),activeforeground="green",bd=3,highlightcolor="green",height=2,width=6)
c1.place(x=650,y=400)
c1 = Checkbutton(root,activebackground="red",text="Fifth",font=(20),activeforeground="green",bd=3,highlightcolor="green",height=2,width=5)
c1.place(x=800,y=400)

b1 = Button(root,text="Done",bg="yellow",fg="black",width=18,height=1,bd=5,font=("bold",22))
b1.place(x=400,y=500)

b2 = Button(root,text="Back",bg="green",fg="white",width=18,height=1,bd=5,font=("bold",22),command=back)
b2.place(x=900,y=500)

root.mainloop()


