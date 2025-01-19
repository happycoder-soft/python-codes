from tkinter import *
from tkinter import messagebox

import pymysql



#create full windows setup
window=Tk()
window.geometry("1050x550")
window.iconbitmap(r"D:\user.ico.ico")
window.title("Forget Password")
window.resizable(FALSE,FALSE)
window.config(bg="white")

#adding photo for later use
photo=PhotoImage(file="D:\coding\icons\pic.png")


#function for save button
def save():
    if username_entrybox.get()=="" or new_password_entrybox.get() =="":
       messagebox.showerror("Error","All Fields Are Required!")
    else:
       con=pymysql.connect(host="localhost",user="root",password="Mysql@14714700",database="details")
       mycursor=con.cursor()
       query='select * from DATA where username=%s'
       mycursor.execute(query,(username_entrybox.get()))
       row=mycursor.fetchone()
       if row==None:
           messagebox.showerror("Error","Incorrect username")
       else:
           query='update DATA set password=%s where username=%s'
           mycursor.execute(query,(new_password_entrybox.get(),username_entrybox.get()))
           con.commit()
           con.close()
           messagebox.showinfo("Message","Password is successfully changed")
           window.destroy()     
           import LOGINSCREEN
 
#function for login button      
def log():
     window.destroy()
     import LOGINSCREEN

#create function for clear button
def all_del():
    username_entrybox.delete(0,END)
    new_password_entrybox.delete(0,END)

#adding image
pic=Label(window,image=photo,bg="white")
pic.place(x=700,y=160)


#create lable on upper side
head=Label(window,text="FORGET PASSWORD",fg="black",font=("calibri",30),background="white")
head.place(x=150,y=60)

#create username font
username=Label(window,text="USERNAME          :",font=("Microsoft YaHei UI Light",20),background="white",fg="black")
username.place(x=70,y=170)

#create new password font
new_password=Label(window,text="NEW PASSWORD :",font=("Microsoft YaHei UI Light",20),background="white",fg="black")
new_password.place(x=70,y=270)

#create username entry box
username_entrybox=Entry(window,font=("calibri",15),background="#85b4ff",fg="black",relief="sunken")
username_entrybox.place(x=320,y=180,height=30,width=250)

#create new password entry box
new_password_entrybox=Entry(window,font=("calibri",15),background="#85b4ff",fg="black",relief="sunken")
new_password_entrybox.place(x=320,y=277,height=30,width=250)

#create save button 
save=Button(window,text="SAVE",font=("calibri",15),background="#a3faff",fg="black",command=save)
save.place(x=110,y=400,height=35,width=100)

#create login button
login=Button(window,text="LOGIN",font=("calibri",15),background="#a3faff",fg="black",command=log)
login.place(x=270,y=400,height=35,width=100)

#create login button
clear=Button(window,text="CLEAR",font=("calibri",15),background="#a3faff",fg="black",command=all_del)
clear.place(x=430,y=400,height=35,width=100)

#and last here is window loop for running
window.mainloop()