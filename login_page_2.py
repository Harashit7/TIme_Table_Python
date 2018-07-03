from Tkinter import *
import ttk
import tkMessageBox
import mysql.connector

root=Tk()

root.geometry('1000x500+300+100')
root.title("Add(admin) Page")
root.configure(bg="aqua")

res1=StringVar()
res2=StringVar()
a=StringVar()
b=StringVar()
c=StringVar()




def done():
    f=open("teacher.txt","w")
    f.write(res1.get())
    f.close()
    conn= mysql.connector.connect(user="root",password="",host="localhost",database="time_table")
    cursor=conn.cursor()
    cursor.execute("select * from teacher where Name='"+res1.get()+"' and Branch='"+var1.get()+"' and Course='"+var2.get()+"' and Semester='"+var3.get()+"'") 
    if(res1.get()==('')):
        tkMessageBox.showinfo("Alert","Please fill a Name")
    elif(cursor.fetchone()):
        
        conn.commit()
        root.destroy()
        import login1_page_3
    else:
        tkMessageBox.showinfo("Alert","Error / Try again and Choose valid Entry")
    
    

l1 = Label(root,text="Name",bg="aqua",font=("comic sans",20),fg="black")
l1.place(x=200,y=100)
e1=Entry(root,width=30,font=(18),textvariable=res1)
e1.place(x=350,y=100)

l2 = Label(root,text="Select Branch",bg="aqua",font=("comic sans",20),fg="black")
l2.place(x=180,y=150)
var1=StringVar()
var1.set("Please Select")
option=OptionMenu(root,var1,"Computer Science","Electrial Engineering","Civil Engineeering","Chemical Engineering")
option.place(x=500,y=150)
def change_dropdown(*args):
    a=var1.get()
    lis=[]
    if(a == 'Computer Science'):
        lis=["COL100","COL200","COL300"]
    elif(a=='Electrial Engineering'):
        lis=["ELL100","ELL200","ELL300"]
    elif(a== 'Civil Engineeering'):
        lis=["CVL100","CVL200","CVL300"] 
    else:
        lis=["CML100","CML200","CML300"]
    option1=OptionMenu(root,var2,*lis)
    option1.place(x=500,y=200)
var1.trace('w',change_dropdown)

l3= Label(root,text="Select Course",bg="aqua",font=("comic sans",20),fg="black")
l3.place(x=180,y=200)
var2=StringVar()
var2.set("Please Select")




def change_dropdown2(*args):
    b=var2.get()
var2.trace('w',change_dropdown2)


l3= Label(root,text="Select Semester",bg="aqua",font=("comic sans",20),fg="black")
l3.place(x=180,y=250)
var3=StringVar()
var3.set("Please Select")
option=OptionMenu(root,var3,"Semester1","Semester2")
option.place(x=500,y=250)
def change_dropdown3(*args):
    c=var3.get()
var3.trace('w',change_dropdown3)


b1 = Button(root,text="Done",bg="yellow",fg="black",width=18,height=1,bd=5,font=("bold",22),command=done)
b1.place(x=250,y=300)

b2 = Button(root,text="Back",bg="green",fg="white",width=18,height=1,bd=5,font=("bold",22))
b2.place(x=650,y=300)




root.mainloop()
