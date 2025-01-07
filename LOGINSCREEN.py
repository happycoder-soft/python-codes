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



def on_click(event):    
    tp1=Toplevel(window)
    tp1.title("Forget password")
    tp1.config(bg="white")
    tp1.iconbitmap(r"D:\user.ico.ico")
    tp1.geometry("1100x600")
    tp1.resizable(False,False)
    tp1.iconbitmap(r"D:\user.ico.ico")
    
def register(event):
    tp=Toplevel(window)
    tp.title("Register Now")
    tp.config(bg="white")
    tp.iconbitmap(r"D:\user.ico.ico")
    tp.geometry("1100x600")
    tp.resizable(False,False)
    # photo1=PhotoImage(file="D:\ register.png")
    
    label2=window.Label(tp,text="hii",font=(50))
    label2.place(x=20,y=90)
    
def clear_entry():
    entry_box.delete(0,END)
    entry_box1.delete(0,END)

def connect_database():
    username1 = entry_box.get()
    password1 = entry_box1.get()
    print("id: {}".format(var.get())) 
    print("pass: {}".format(var2.get())) 
     
    if username1 == "admin" and password1 == "123456789":
        messagebox.showinfo("Login Successful", "Welcome! Login Successful")
    else:
        messagebox.showerror("Login Failed", "Invalid username or password")
        
        
def HIDE():
    closeeye.config(file="D:\eye (1).png")
    entry_box1.config(show="*")
    eyebutton.config(command=show)
    
    
def show():
    closeeye.config(file="D:\hidden.png")
    entry_box1.config(show="")
    eyebutton.config(command=HIDE)
    
                            

var=StringVar()
var2=StringVar() 
 


label=Label(window,image=photo,bg="white")
label.place(x=30,y=30)

login=Label(window,text="Login",font=('Microsoft YaHei UI Light',30),bg="white")
login.place(x=780,y=80)
username=Label(window,text="USERNAME",font=('Microsoft YaHei UI Light',13),bg="white")
username.place(x=650,y=190)


password=Label(window,text="PASSWORD",font=('Microsoft YaHei UI Light',13),bg="white")
password.place(x=650,y=290)

forget_password=Label(window,text="Forget Password?",font=('Microsoft YaHei UI Light',10),bg="white",cursor="hand2")
forget_password.place(x=900,y=355)

new_user=Label(window,text="New User ?",font=('Microsoft YaHei UI Light',10),bg="white")
new_user.place(x=760,y=520)

register_here=Label(window,text="Register Here",font=('Microsoft YaHei UI Light',10),bg="white",cursor="hand2")
register_here.place(x=830,y=519)


entry_box=Entry(window,font=(30),textvariable=var,bd=3,relief="groove")
entry_box.place(x=655,y=220,width=350,height=40)

entry_box1=Entry(window,font=(30),textvariable=var2,bd=3,relief="groove")
entry_box1.place(x=655,y=320,width=350,height=40)

closeeye=PhotoImage(file="D:\hidden.png")
eyebutton=Button(window,image=closeeye,bd=0,bg="white",activebackground="white",cursor="hand2",command=HIDE)
eyebutton.place(x=980,y=330)


login_button=Button(window,text="LOGIN",font=(15),bg="#BBC6EE",relief="groove",command=connect_database)
login_button.place(x=680,y=430,height=40,width=100)

clear_button=Button(window,text="CLEAR",font=(15),bg="#BBC6EE",relief="groove",command=clear_entry)
clear_button.place(x=880,y=430,height=40,width=100)

custom_font = font.Font(family="Helvetica", size=12)


forget_password.bind("<Button-1>", on_click)
register_here.bind("<Button-1>", register)

window.mainloop()