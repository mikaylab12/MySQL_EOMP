# Mikayla Beelders' End Of Module Project
from tkinter import *
import mysql.connector
from tkinter import messagebox
from PIL import Image, ImageTk

login_screen = Tk()
login_screen.geometry("800x900")
login_screen.config(bg="#3556e8")
login_screen.title("Login Page")

# adding image
canvas = Canvas(login_screen, width=620, height=300, bg="#3c5be6", borderwidth=0, highlightthickness=0)
canvas.place(relx=0.1, rely=0.1)
img_logo = ImageTk.PhotoImage(Image.open("lifechoices-2.jpg"))
canvas.create_image(310, -10, anchor=N, image=img_logo)


class Login(object):
    def __init__(self):
        # heading
        self.heading = Label(login_screen, text="Welcome To:", fg="white", bg="#3556e8",
                             font=("Arial", 25, "bold"))
        self.heading.place(relx=0.37, rely=0.04)
        # instruction heading
        self.instruction_heading = Label(login_screen, text="Please enter your login details:", fg="#7bfa05",
                                         bg="#3556e8", font=("Arial", 21, "bold"))
        self.instruction_heading.place(relx=0.1, rely=0.48)
        # labels and entries
        self.id_label = Label(login_screen, text="ID number:", fg="white", bg="#3556e8", font=("Arial", 15,
                                                                                                     "bold"))
        self.id_label.place(relx=0.1, rely=0.58)
        self.id_entry = Entry(login_screen, font=("Arial", 15))
        self.id_entry.place(relx=0.35, rely=0.58)

        self.password_label = Label(login_screen, text="Password:", fg="white", bg="#3556e8", font=("Arial", 15,
                                                                                                    "bold"))
        self.password_label.place(relx=0.1, rely=0.65)
        self.password_entry = Entry(login_screen, font=("Arial", 15), show='*')
        self.password_entry.place(relx=0.35, rely=0.65)
        # buttons
        self.login_btn = Button(login_screen, text="Login", padx=15, pady=10, borderwidth=5, fg="black", bg="#71f72a",
                                font=("Arial", 13, "bold"), command=self.login)
        self.login_btn.place(relx=0.75, rely=0.77)

        self.register_btn = Button(login_screen, text="Register New User", padx=15, pady=10, borderwidth=5, fg="black",
                                   bg="#71f72a", font=("Arial", 13, "bold"), command=self.registering)
        self.register_btn.place(relx=0.35, rely=0.77)

        self.clear_btn = Button(login_screen, text="Clear", padx=15, pady=10, borderwidth=5, fg="black",
                                bg="#fff", font=("Arial", 13, "bold"), command=self.clear)
        self.clear_btn.place(relx=0.1, rely=0.77)

    def login(self):
        hospital = mysql.connector.connect(user='lifechoices', password='8-2fermENt2020', host='127.0.0.1',
                                           database='Hospital', auth_plugin='mysql_native_password')
        mycursor = hospital.cursor()
        xy = mycursor.execute('SELECT * FROM login')
        if self.id_entry == "":
            messagebox.showinfo("Entry Error", "Please enter your ID number.")
        if self.password_entry == "":
            messagebox.showinfo("Entry Error", "Please enter your password.")
        else:
            for i in mycursor:
                if self.id_entry.get() == i[0] and self.password_entry.get() == i[1]:
                    messagebox.showinfo("Successful", "Login Successful!\nEnjoy your day.")
                    login_screen.destroy()
                    # import menu_page
                    break
            for i in mycursor:
                if self.id_entry.get() != i[0] and self.password_entry.get() != i[1]:
                    messagebox.showinfo("Error", "Access denied!\nPlease visit reception.")
                    self.id_entry.delete(0, END)
                    self.password_entry.delete(0, END)

    def registering(self):
        messagebox.showinfo("New User", "You will be redirected to enter your credentials!")
        login_screen.destroy()
        import registration

    def clear(self):
        self.id_entry.delete(0, END)
        self.password_entry.delete(0, END)


logging_in = Login()
login_screen.mainloop()
