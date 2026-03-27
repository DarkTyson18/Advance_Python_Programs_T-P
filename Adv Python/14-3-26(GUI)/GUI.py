from tkinter import *
from PIL import Image, ImageTk

root = Tk()
root.title("Student Form")

root.iconbitmap(r"C:\Users\Shashi Ranjan\Downloads\star.png.png")

root.geometry('500x500+0+0')



root.configure(background="#D9FA49")

# image
img = Image.open(r"C:\Users\Shashi Ranjan\Downloads\star.png.png")
resize_img = img.resize((100,70))
img = ImageTk.PhotoImage(resize_img)

img_label = Label(root,image=img,bg="#5CFBF5")
img_label.pack(pady=10,padx=20)

# text label
text_label = Label(root,text="HomePage",font=('Arial',18,'bold'),bg="#37D4F0",fg='white')
text_label.pack(pady=10,padx=20)

email_label = Label(root,text="Email",font=('Arial',18,'bold'),bg="#3CD6F1",fg='white')
email_label.pack(pady=(20,5))

email_entry = Entry(root,font=('Arial',18,'bold'),fg='white',bg='grey')
email_entry.pack(pady=(5,10))

password_label = Label(root,text="Password",font=('Arial',18,'bold'),bg="#47E8FA",fg='white')
password_label.pack(pady=(20,5))

password_entry = Entry(root,font=('Arial',18,'bold'),fg='white',bg='grey')
password_entry.pack(pady=(5,10))

login_btn = Button(root,text="Login",font=('Arial',18,'bold'),bg="#44DFFB",fg='white')
login_btn.pack(pady=(5,10))

root.mainloop()