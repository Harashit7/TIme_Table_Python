from Tkinter import *
import ttk
import tkMessageBox
import mysql.connector

root=Tk()

root.geometry('1000x500+300+100')
root.title("Add(faulty) Page")
root.configure(bg="aqua")


def done():
    f=open("teacher1.txt","w")
    f.write(combo1.get())
    f.close()
    conn=mysql.connector.connect(user="root",password="",host="localhost",database="time_table")
    cursor=conn.cursor()
    cursor.execute("select * from teacher where Name='"+combo1.get()+"'")
    if(cursor.fetchone()):
        
        conn.commit()
        root.destroy()
        import show_faculty
    else:
        tkMessageBox.showinfo("Alert","Invalid Entry/Try Again")
    

def back():
    root.destroy()
    import login_page_1
    
conn=mysql.connector.connect(user="root",password="",host="localhost",database="time_table")
cursor=conn.cursor()
cursor.execute("select Name from teacher where Course='COL100'")
list =[]
for i in cursor.fetchall():
    list.append(i[0])
conn.commit()

combo1=ttk.Combobox(root,font=('cestellar',12,"italic bold"))
combo1.set("please select")
combo1['values']=list
combo1.place(x=450,y=100)

L1=Label(root,text="Choose Faculty to know the Overview",font=('Helvetica',24,"bold"))
L1.pack()

b1 = Button(root,text="Done",bg="yellow",fg="black",width=18,height=1,bd=5,font=("bold",22),command=done)
b1.place(x=300,y=300)

b2 = Button(root,text="Back",bg="green",fg="white",width=18,height=1,bd=5,font=("bold",22),command=back)
b2.place(x=650,y=300)

root.mainloop()
                            
