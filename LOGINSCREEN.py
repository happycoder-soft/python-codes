from tkinter import *
from tkinter import font
from tkinter import messagebox
from tkinter.messagebox import showinfo , showerror
import pymysql

window=Tk()
window.geometry("1100x600")
window.resizable(False,False)
window.title("Login")
window.iconbitmap(r"D:\user.ico.ico")
window.config(bg="white")
photo=PhotoImage(file="D:\login screen.png")


def forg():
    window.destroy()
    import forget
    
def regi():
    window.destroy()
    import REGISTER
    
def clear_entry():
    entry_box.delete(0,END)
    entry_box1.delete(0,END)

def connect_database():
    # username1 = entry_box.get()
    # password1 = entry_box1.get()
    # print("id: {}".format(var.get())) 
    # print("pass: {}".format(var2.get())) 
     
    # if username1 == "admin" and password1 == "123456789":
    #     messagebox.showinfo("Login Successful", "Welcome! Login Successful")
    # else:
    #     messagebox.showerror("Login Failed", "Invalid username or password")
    
    if entry_box.get()=="" or entry_box1.get()=="" :
           messagebox.showerror("Error0","All Feilds Are Required!")
    else:
       try:
           con=pymysql.connect(host="localhost",user="root",password="Mysql@14714700")
           mycursor=con.cursor()
       except:
           messagebox.showerror("Error","Connection lost! Please try again!")
    
    query="use details"
    mycursor.execute(query)
    query="select * from DATA where username=%s and password=%s"
    mycursor.execute(query,(entry_box.get(),entry_box1.get()))
    row=mycursor.fetchone()
    if row==None:
        messagebox.showerror("Error","Invalid Username and Password")
    else:
        messagebox.showinfo("Message","Login Successful")
        
        
        
def HIDE():
    closeeye.config(file="D:\eye (1).png")
    entry_box1.config(show="*")
    eyebutton.config(command=show)
    
    
def show():
    closeeye.config(file="D:\hidden.png")
    entry_box1.config(show="")
    eyebutton.config(command=HIDE)
    
                            

# var=StringVar()
# var2=StringVar() 
 


label=Label(window,image=photo,bg="white")
label.place(x=30,y=30)

login=Label(window,text="Login",font=('Microsoft YaHei UI Light',30),bg="white")
login.place(x=780,y=80)
username=Label(window,text="USERNAME",font=('Microsoft YaHei UI Light',13),bg="white")
username.place(x=650,y=190)


password=Label(window,text="PASSWORD",font=('Microsoft YaHei UI Light',13),bg="white")
password.place(x=650,y=290)

forget_password=Button(window,text="Forget Password?",font=('Microsoft YaHei UI Light',10),bg="white",cursor="hand2",relief="flat",command=forg)
forget_password.place(x=890,y=355)

new_user=Label(window,text="New User ?",font=('Microsoft YaHei UI Light',10),bg="white")
new_user.place(x=760,y=520)

register_here=Button(window,text="Register Here",font=('Microsoft YaHei UI Light',10),bg="white",
                     activebackground="white",activeforeground="black",cursor="hand2",command=regi,relief="flat")
register_here.place(x=832,y=516)


entry_box=Entry(window,font=(30),bd=3,relief="groove")
entry_box.place(x=655,y=220,width=350,height=40)

entry_box1=Entry(window,font=(30),bd=3,relief="groove")
entry_box1.place(x=655,y=320,width=350,height=40)

closeeye=PhotoImage(file="D:\hidden.png")
eyebutton=Button(window,image=closeeye,bd=0,bg="white",activebackground="white",cursor="hand2",command=HIDE)
eyebutton.place(x=980,y=330)


login_button=Button(window,text="LOGIN",font=(15),bg="#BBC6EE",relief="groove",command=connect_database)
login_button.place(x=680,y=430,height=40,width=100)

clear_button=Button(window,text="CLEAR",font=(15),bg="#BBC6EE",relief="groove",command=clear_entry)
clear_button.place(x=880,y=430,height=40,width=100)

custom_font = font.Font(family="Helvetica", size=12)


# forget_password.bind("<Button-1>", on_click)
# register_here.bind("<Button-1>", register)

window.mainloop()