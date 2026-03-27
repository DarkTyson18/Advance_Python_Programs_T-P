from tkinter import *
from tkinter import messagebox
from PIL import Image, ImageTk

root = Tk()
root.title("Student Form")

root.geometry('500x500+0+0')
root.configure(background="#49FAD9")

# -------- Functions --------

def login():
    email = email_entry.get()
    password = password_entry.get()

    if email == "" or password == "":
        messagebox.showerror("Error","All fields are required")
    
    elif email == "admin@gmail.com" and password == "1234":
        messagebox.showinfo("Success","Login Successful")
    
    else:
        messagebox.showerror("Error","Invalid Email or Password")


def clear_fields():
    email_entry.delete(0,END)
    password_entry.delete(0,END)


def show_password():
    if password_entry.cget('show') == '*':
        password_entry.config(show='')
    else:
        password_entry.config(show='*')


# -------- Image --------

img = Image.open(r"C:\Users\Shashi Ranjan\OneDrive\Desktop\Adv Python\14-3-26(GUI)\download.jpg")
resize_img = img.resize((100,70))
img = ImageTk.PhotoImage(resize_img)

img_label = Label(root,image=img,bg="#DEFB5C")
img_label.pack(pady=10,padx=20)

# -------- Title --------

text_label = Label(root,text="HomePage",font=('Arial',15),bg="#FFF647",fg='black')
text_label.pack(pady=10,padx=20)

# -------- Email --------

email_label = Label(root,text="Email",font=('Arial',15),bg="#E2F13C",fg='black')
email_label.pack(pady=(20,5))

email_entry = Entry(root,font=('Arial',18,'bold'),fg='black',bg='white')
email_entry.pack(pady=(5,10))

# -------- Password --------

password_label = Label(root,text="Password",font=('Arial',15),bg="#EEFA47",fg='black')
password_label.pack(pady=(20,5))

password_entry = Entry(root,font=('Arial',18,'bold'),fg='black',bg='white',show='*')
password_entry.pack(pady=(5,10))

# -------- Show Password Button --------

show_btn = Button(root,text="Show/Hide Password",command=show_password)
show_btn.pack(pady=5)

# -------- Buttons --------

login_btn = Button(root,text="Login",font=('Arial',15),bg="#44DFFB",fg='white',command=login)
login_btn.pack(pady=(10,5))

clear_btn = Button(root,text="CLEAR",font=('Arial',15),bg="red",fg='white',command=clear_fields)
clear_btn.pack(pady=(5,10))

root.mainloop()