from tkinter import*
import pymysql
from tkinter import messagebox


window=Tk()
window.geometry("1100x600")
window.iconbitmap(r"D:\user.ico.ico")
window.config(bg="#f5bc8e")
window.resizable(False,False)
window.title("Register")
photo=PhotoImage(file="D:\coding\icons\document.png")
photo1=PhotoImage(file="D:\coding\icons\log-in.png")


def clear_all():
    name_entrybox.delete(0,END)
    email_entrybox.delete(0,END)
    username_entrybox.delete(0,END)
    newpassword_entrybox.delete(0,END)
    confirmpassword_entrybox.delete(0,END)
    
def log():
    window.destroy()  
    import LOGINSCREEN
    
def HIDE():
    closeeye.config(file="D:\eye (1).png")
    newpassword_entrybox.config(show="*")
    confirmpassword_entrybox.config(show="*")
    eyebutton.config(command=show)
    
def show():
    closeeye.config(file="D:\hidden.png")
    newpassword_entrybox.config(show="")
    confirmpassword_entrybox.config(show="")
    eyebutton.config(command=HIDE)
    
def connect_database():
    if name_entrybox.get()=="" or username_entrybox.get()=="" or email_entrybox.get()=="" or newpassword_entrybox.get()=="" or confirmpassword_entrybox.get()=="" :
        messagebox.showerror("Error","All Fields Are Required")
    elif newpassword_entrybox.get() != confirmpassword_entrybox.get():
         messagebox.showerror("Error","Password Mismatch")
    
    else:
        try:
            con=pymysql.connect(host='localhost',user0='root',password="1234")
            mycursor=con.cursor()
        except:
            messagebox.showerror("Error","database connecivity problem! please try again after some time")
            return
        
        query="create database userdata"
        mycursor.execute(query)
        query='use userdata'
        mycursor.execute(query)
        query='create table data(id int auto_increment primary key not null, email varchar(50),username varchar(100),password varchar(20))'
        mycursor.execute(query)
            
        
    
pic=Label(window,image=photo,bg="#f5bc8e")    
pic.place(x=800,y=150)    
pic=Label(window,image=photo1,bg="#f5bc8e")    
pic.place(x=620,y=150,width=150)   

label=Label(window,text="NEW REGISTRATION",font=("DayPosterShadowNF",35),bg="#f5bc8e",fg="black")
label.place(x=80,y=40)

name=Label(window,text="Name",font=("Microsoft YaHei UI Light",16),bg="#f5bc8e")
name.place(x=40,y=140)

email=Label(window,text="Email ID",font=("Microsoft YaHei UI Light",16),bg="#f5bc8e")
email.place(x=40,y=210)

username=Label(window,text="Username",font=("Microsoft YaHei UI Light",16),bg="#f5bc8e")
username.place(x=40,y=270)

new_password=Label(window,text="New Password",font=("Microsoft YaHei UI Light",16),bg="#f5bc8e")
new_password.place(x=40,y=330)

confirm_password=Label(window,text="Confirm Password",font=("Microsoft YaHei UI Light",16),bg="#f5bc8e")
confirm_password.place(x=40,y=390)

name_entrybox=Entry(window,font=(30),bd=3,relief="groove",bg="#c7ffeb")
name_entrybox.place(x=280,y=140,width=300,height=30)

email_entrybox=Entry(window,font=(30),bd=3,relief="groove",bg="#c7ffeb")
email_entrybox.place(x=280,y=210,width=300,height=30)

username_entrybox=Entry(window,font=(30),bd=3,relief="groove",bg="#c7ffeb")
username_entrybox.place(x=280,y=270,width=300,height=30)

newpassword_entrybox=Entry(window,font=(30),bd=3,relief="groove",bg="#c7ffeb")
newpassword_entrybox.place(x=280,y=330,width=300,height=30)

confirmpassword_entrybox=Entry(window,font=(30),bd=3,relief="groove",bg="#c7ffeb")
confirmpassword_entrybox.place(x=280,y=390,width=300,height=30)

save_button=Button(window,text="SAVE",font=(15),bg="#c7ffeb",relief="groove",command=connect_database)
save_button.place(x=100,y=480,height=40,width=100)

login_button=Button(window,text="Login",font=(15),bg="#c7ffeb",relief="groove",command=log)
login_button.place(x=250,y=480,height=40,width=100)

clear_button=Button(window,text="CLEAR",font=(15),bg="#c7ffeb",relief="groove",command=clear_all)
clear_button.place(x=400,y=480,height=40,width=100)

closeeye=PhotoImage(file="D:\hidden.png")
eyebutton=Button(window,image=closeeye,bd=0,bg="#c7ffeb",activebackground="#c7ffeb",cursor="hand2",command=HIDE)
eyebutton.place(x=555,y=335)


window.mainloop()