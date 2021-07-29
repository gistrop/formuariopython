from tkinter import *

def send_data(): 
    username_data =username.get()
    password_data =str(password.get())
    fullname_data =fullname.get()
    age_data =str(age.get())

    print(username_data, password_data, fullname_data, age_data)

window = Tk()
window.geometry("360x400")
window.title("Regístrate o Vete")
window.resizable(False,False)
window.config(background="black")
main_title = Label(text="Regístrate rápido o Lárgate ya jiji :D", font=("modern love", 14), bg="grey", fg="white", width="550", height="2")
main_title.pack()

username_label = Label(text="Agregar Usuario", bg="skyblue")
username_label.place(x=22, y=70)
password_label = Label(text="Agregar Contraseña", bg="skyblue")
password_label.place(x=22, y=130)
fullname_label = Label(text="Agregar Apellido", bg="skyblue")
fullname_label.place(x=22, y=190)
age_label = Label(text="Agregar Edad", bg="skyblue")
age_label.place(x=22, y=250)

username = StringVar()
password = StringVar()
fullname = StringVar()
age = StringVar()

username_entry = Entry(textvariable=username, width="40")
password_entry = Entry(textvariable=password, width="40")
fullname_entry = Entry(textvariable=fullname, width="40")
age_entry = Entry(textvariable=age, width="40")

username_entry.place(x=22, y=100)
password_entry.place(x=22, y=160)
fullname_entry.place(x=22, y=220)
age_entry.place(x=22, y=280)

submit_btn = Button(window, text="Subir Registro", command=send_data, width="30", height="2", bg="red")
submit_btn.place(x=22, y=330)

window.mainloop()