from tkinter import *
from tkinter import messagebox




window=Tk()
window.geometry("1050x550")
window.iconbitmap(r"D:\user.ico.ico")
window.title("Forget Password")
window.resizable(FALSE,FALSE)
window.config(bg="white")
photo=PhotoImage(file="D:\coding\icons\pic.png")

def save():
    if username_entrybox.get()=="" or new_password_entrybox.get() =="":
       messagebox.showerror("Error","All Fields Are Required!")
    else:
       messagebox.showinfo("Message","Your Password Is Successfully Changed!")
      
      
def log():
     window.destroy()
     import LOGINSCREEN

def all_del():
    username_entrybox.delete(0,END)
    new_password_entrybox.delete(0,END)


pic=Label(window,image=photo,bg="white")
pic.place(x=700,y=160)

head=Label(window,text="FORGET PASSWORD",fg="black",font=("calibri",30),background="white")
head.place(x=150,y=60)

username=Label(window,text="USERNAME          :",font=("Microsoft YaHei UI Light",20),background="white",fg="black")
username.place(x=70,y=170)

new_password=Label(window,text="NEW PASSWORD :",font=("Microsoft YaHei UI Light",20),background="white",fg="black")
new_password.place(x=70,y=270)

username_entrybox=Entry(window,font=("calibri",15),background="#85b4ff",fg="black",relief="sunken")
username_entrybox.place(x=320,y=180,height=30,width=250)

new_password_entrybox=Entry(window,font=("calibri",15),background="#85b4ff",fg="black",relief="sunken")
new_password_entrybox.place(x=320,y=277,height=30,width=250)

save=Button(window,text="SAVE",font=("calibri",15),background="#a3faff",fg="black",command=save)
save.place(x=110,y=400,height=35,width=100)

login=Button(window,text="LOGIN",font=("calibri",15),background="#a3faff",fg="black",command=log)
login.place(x=270,y=400,height=35,width=100)

clear=Button(window,text="CLEAR",font=("calibri",15),background="#a3faff",fg="black",command=all_del)
clear.place(x=430,y=400,height=35,width=100)


window.mainloop()