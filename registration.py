# registration page
from tkinter import *
from tkinter import messagebox
import mysql.connector
from PIL import Image, ImageTk

registering_screen = Tk()
registering_screen.geometry("700x900")
registering_screen.title("Register")
registering_screen.config(bg="#000")

# adding image
canvas = Canvas(registering_screen, width=400, height=300, bg="#000", borderwidth=0, highlightthickness=0)
canvas.place(relx=0.25, rely=0.02)
img_logo = ImageTk.PhotoImage(Image.open("lifechoices1.jpg"))
canvas.create_image(150, 5, anchor=N, image=img_logo)


class Registration(object):
    def __init__(self):
        self.heading = Label(registering_screen, text="Please enter your details:", fg="#71f72a", bg="#000",
                             font=("Arial", 20, "bold"))
        self.heading.place(relx=0.08, rely=0.12)
        # labels and entries
        # name
        self.name_label = Label(registering_screen, text="Name:", fg="white", bg="#000", font=("Arial", 15))
        self.name_label.place(relx=0.08, rely=0.17)
        self.name_entry = Entry(registering_screen, font=("Arial", 15))
        self.name_entry.place(relx=0.55, rely=0.17)
        # surname
        self.surname_label = Label(registering_screen, text="Surname:", fg="white", bg="#000", font=("Arial", 15))
        self.surname_label.place(relx=0.08, rely=0.24)
        self.surname_entry = Entry(registering_screen, font=("Arial", 15))
        self.surname_entry.place(relx=0.55, rely=0.24)
        # id number
        self.id_label = Label(registering_screen, text="ID Number:", fg="white", bg="#000", font=("Arial", 15))
        self.id_label.place(relx=0.08, rely=0.31)
        self.id_entry = Entry(registering_screen, font=("Arial", 15))
        self.id_entry.place(relx=0.55, rely=0.31)
        # contact number
        self.contact_label = Label(registering_screen, text="Contact Number:", fg="white", bg="#000", font=("Arial",
                                                                                                               15))
        self.contact_label.place(relx=0.08, rely=0.38)
        self.contact_entry = Entry(registering_screen, font=("Arial", 15))
        self.contact_entry.place(relx=0.55, rely=0.38)
        # password
        self.password_label = Label(registering_screen, text="Please enter a password:", fg="white", bg="#000",
                                    font=("Arial", 15))
        self.password_label.place(relx=0.08, rely=0.45)
        self.password_entry = Entry(registering_screen, font=("Arial", 15), show='*')
        self.password_entry.place(relx=0.55, rely=0.45)

        self.confirm_label = Label(registering_screen, text="Please confirm your password:", fg="white", bg="#000",
                                   font=("Arial", 15))
        self.confirm_label.place(relx=0.08, rely=0.52)
        self.confirm_entry = Entry(registering_screen, font=("Arial", 15), show='*')
        self.confirm_entry.place(relx=0.55, rely=0.52)
        # next of kin details
        self.nextOfKin_details = Label(registering_screen, text="Please enter your Next of Kin details:", fg="#71f72a",
                                       bg="#000", font=("Arial", 20, "bold"))
        self.nextOfKin_details.place(relx=0.08, rely=0.62)
        self.nextOfKin_name_label = Label(registering_screen, text="Name:", fg="white", bg="#000", font=("Arial",
                                                                                                            15))
        self.nextOfKin_name_label.place(relx=0.08, rely=0.67)
        self.nextOfKin_name_entry = Entry(registering_screen, font=("Arial", 15))
        self.nextOfKin_name_entry.place(relx=0.55, rely=0.67)
        # surname
        self.nextOfKin_surname_label = Label(registering_screen, text="Surname:", fg="white", bg="#000",
                                             font=("Arial", 15))
        self.nextOfKin_surname_label.place(relx=0.08, rely=0.74)
        self.nextOfKin_surname_entry = Entry(registering_screen, font=("Arial", 15))
        self.nextOfKin_surname_entry.place(relx=0.55, rely=0.74)
        # id number
        self.nextOfKin_contact_label = Label(registering_screen, text="ID Number:", fg="white", bg="#000",
                                             font=("Arial", 15))
        self.nextOfKin_contact_label.place(relx=0.08, rely=0.81)
        self.nextOfKin_contact_entry = Entry(registering_screen, font=("Arial", 15))
        self.nextOfKin_contact_entry.place(relx=0.55, rely=0.81)
        # buttons
        register_btn = Button(registering_screen, text="Register", padx=15, pady=10, borderwidth=5, fg="black",
                              bg="#71f72a",
                              font=("Arial", 13, "bold"), command=self.registering)
        register_btn.place(relx=0.55, rely=0.89)

        clear_btn = Button(registering_screen, text="Clear", padx=25, pady=10, borderwidth=5, fg="black",
                           bg="#fff",
                           font=("Arial", 13, "bold"), command=self.clear)
        clear_btn.place(relx=0.25, rely=0.89)

    # function to register
    def registering(self):
        if self.name_entry == "":
            messagebox.showinfo("Entry Error", "Please enter your name.")
        if self.password_entry == "":
            messagebox.showinfo("Entry Error", "Please enter your password.")
        if self.confirm_entry == "":
            messagebox.showinfo("Entry Error", "Please confirm your password.")
        if self.confirm_entry.get() != self.password_entry.get():
            messagebox.showinfo("Entry Error", "Please ensure that your passwords entered, correspond.")
        else:
            try:
                hospital_db = mysql.connector.connect(user='lifechoices', password='8-2fermENt2020', host='127.0.0.1',
                                                      database='Hospital', auth_plugin='mysql_native_password')
                mycursor = hospital_db.cursor()
                data = "INSERT INTO login (user, password) VALUES (%s, %s)"
                val = (self.name_entry.get(), self.password_entry.get())
                mycursor.execute(data, val)
                hospital_db.commit()
                messagebox.showinfo("Welcome", "Please note that you have successfully registered!")
                registering_screen.destroy()
                # import menu_page
            except ValueError:
                messagebox.showinfo("Entry Error", "Please ensure that your passwords entered, correspond.")
                self.name_entry.delete(0, END)
                self.password_entry.delete(0, END)
                self.confirm_entry.delete(0, END)

    def clear(self):
        self.name_entry.delete(0, END)
        self.password_entry.delete(0, END)
        self.confirm_entry.delete(0, END)


registering_user = Registration()
registering_screen.mainloop()
