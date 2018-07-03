from Tkinter import *
import tkMessageBox
import mysql.connector

root=Tk()

root.geometry('1000x500+400+200')
root.title("login(admin)")
root.configure(bg="cyan")

def exit():
    root.destroy()
    

def done():
    conn= mysql.connector.connect(user="root",password="",host="localhost",database="time_table")
    cursor=conn.cursor()
    cursor.execute("select * from admin where Username='"+res1.get()+"' and Password='"+res2.get()+"'")
    if(res1.get()==('') or res2.get()==('')):
        tkMessageBox.showinfo("Alert","Please fill a Username/Password")
    elif(cursor.fetchone()):
        conn.commit()
        root.destroy()
        import login_page_1
    else:
        tkMessageBox.showinfo("Alert","Error / Try again and Choose valid Entry")
    
    



res1=StringVar()
res2=StringVar()


l2=Label(root,text="UserId",font=("arial",20,"bold"),bg="cyan",fg="red")
l2.place(x=200,y=100)

e1=Entry(root,font=("arial",20),fg="black",textvariable=res1)
e1.place(x=500,y=100)

l2=Label(root,text="password",font=("arial",20,"bold"),bg="cyan",fg="red")
l2.place(x=200,y=150)

e2=Entry(root,font=("arial",20),fg="black",textvariable=res2,show="*")
e2.place(x=500,y=150)


b1=Button(root,text="Login",padx=15,pady=5,bg="white",fg="black",command=done)
b1.place(x=300,y=250)



b3=Button(root,text="exit",padx=15,pady=5,bg="white",fg="black",command=exit)
b3.place(x=600,y=250)







root.mainloop()
