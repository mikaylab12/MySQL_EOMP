# registration page
from tkinter import *
from tkinter import messagebox
import mysql.connector
from PIL import Image, ImageTk
from tkinter.ttk import Combobox
from datetime import datetime

registering_screen = Tk()
registering_screen.geometry("700x900")
registering_screen.title("Register")
registering_screen.config(bg="#000")

# adding image
canvas = Canvas(registering_screen, width=400, height=300, bg="#000", borderwidth=0, highlightthickness=0)
canvas.place(relx=0.25, rely=0.02)
img_logo = ImageTk.PhotoImage(Image.open("lifechoices1.jpg"))
canvas.create_image(150, 5, anchor=N, image=img_logo)

lifechoices_db = mysql.connector.connect(user='lifechoices', password='8-2fermENt2020', host='127.0.0.1',
                                         database='Lifechoices_Online', auth_plugin='mysql_native_password')
my_cursor = lifechoices_db.cursor()
# time = datetime.time()
# date = datetime.date()

# combo box
group = StringVar(registering_screen)
group_list = ['Student', 'Admin', 'Guest']
group_selector = Combobox(registering_screen, textvariable=group.set, font=("Arial", 13), width=19)
group_selector.set("Select One")
group_selector['values'] = group_list
group_selector['state'] = 'readonly'
group_selector.place(relx=0.55, rely=0.17)

current_date = datetime.now().date().strftime("%Y-%m-%d")
current_time = datetime.now().time().strftime("%H:%M:%S")
# then used mycursor.execute to put the values in the columns


class Registration(object):
    def __init__(self):
        self.heading = Label(registering_screen, text="Please enter your details:", fg="#71f72a", bg="#000",
                             font=("Arial", 20, "bold"))
        self.heading.place(relx=0.08, rely=0.12)
        self.combobox_label = Label(registering_screen, text="Group:", fg="white", bg="#000", font=("Arial", 15))
        self.combobox_label.place(relx=0.08, rely=0.17)
        # labels and entries
        # name
        self.name_label = Label(registering_screen, text="Name:", fg="white", bg="#000", font=("Arial", 15))
        self.name_label.place(relx=0.08, rely=0.22)
        self.name_entry = Entry(registering_screen, font=("Arial", 13))
        self.name_entry.place(relx=0.55, rely=0.22)
        # surname
        self.surname_label = Label(registering_screen, text="Surname:", fg="white", bg="#000", font=("Arial", 15))
        self.surname_label.place(relx=0.08, rely=0.28)
        self.surname_entry = Entry(registering_screen, font=("Arial", 13))
        self.surname_entry.place(relx=0.55, rely=0.28)
        # id number
        self.id_label = Label(registering_screen, text="ID Number:", fg="white", bg="#000", font=("Arial", 15))
        self.id_label.place(relx=0.08, rely=0.34)
        self.id_entry = Entry(registering_screen, font=("Arial", 13))
        self.id_entry.place(relx=0.55, rely=0.34)
        # contact number
        self.contact_label = Label(registering_screen, text="Contact Number:", fg="white", bg="#000", font=("Arial",
                                                                                                               15))
        self.contact_label.place(relx=0.08, rely=0.4)
        self.contact_entry = Entry(registering_screen, font=("Arial", 13))
        self.contact_entry.place(relx=0.55, rely=0.4)
        # password
        self.password_label = Label(registering_screen, text="Please enter a password:", fg="white", bg="#000",
                                    font=("Arial", 15))
        self.password_label.place(relx=0.08, rely=0.46)
        self.password_entry = Entry(registering_screen, font=("Arial", 13), show='*')
        self.password_entry.place(relx=0.55, rely=0.46)

        self.confirm_label = Label(registering_screen, text="Please confirm your password:", fg="white", bg="#000",
                                   font=("Arial", 15))
        self.confirm_label.place(relx=0.08, rely=0.52)
        self.confirm_entry = Entry(registering_screen, font=("Arial", 13), show='*')
        self.confirm_entry.place(relx=0.55, rely=0.52)
        # next of kin details
        self.nextOfKin_details = Label(registering_screen, text="Please enter your Next of Kin details:", fg="#71f72a",
                                       bg="#000", font=("Arial", 20, "bold"))
        self.nextOfKin_details.place(relx=0.08, rely=0.62)
        self.nextOfKin_name_label = Label(registering_screen, text="Name:", fg="white", bg="#000", font=("Arial",
                                                                                                         15))
        self.nextOfKin_name_label.place(relx=0.08, rely=0.67)
        self.nextOfKin_name_entry = Entry(registering_screen, font=("Arial", 13))
        self.nextOfKin_name_entry.place(relx=0.55, rely=0.67)
        # surname
        self.nextOfKin_surname_label = Label(registering_screen, text="Surname:", fg="white", bg="#000",
                                             font=("Arial", 15))
        self.nextOfKin_surname_label.place(relx=0.08, rely=0.74)
        self.nextOfKin_surname_entry = Entry(registering_screen, font=("Arial", 13))
        self.nextOfKin_surname_entry.place(relx=0.55, rely=0.74)
        # id number
        self.nextOfKin_contact_label = Label(registering_screen, text="Contact Number:", fg="white", bg="#000",
                                             font=("Arial", 15))
        self.nextOfKin_contact_label.place(relx=0.08, rely=0.81)
        self.nextOfKin_contact_entry = Entry(registering_screen, font=("Arial", 13))
        self.nextOfKin_contact_entry.place(relx=0.55, rely=0.81)
        # self.
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
        if self.surname_entry == "":
            messagebox.showinfo("Entry Error", "Please enter your surname.")
        if self.id_entry == "":
            messagebox.showinfo("Entry Error", "Please enter your ID number.")
        if self.contact_entry == "":
            messagebox.showinfo("Entry Error", "Please enter your contact number.")
        if self.password_entry == "":
            messagebox.showinfo("Entry Error", "Please enter your password.")
        if self.confirm_entry == "":
            messagebox.showinfo("Entry Error", "Please confirm your password.")
        if self.nextOfKin_name_entry == "" or self.nextOfKin_surname_entry == "" or self.nextOfKin_contact_entry == "":
            messagebox.showinfo("Next OF Kin Entry Error", "Please ensure that your have filled in all the required "
                                                           "details of your next of Kin.")
        if self.confirm_entry.get() != self.password_entry.get():
            messagebox.showinfo("Entry Error", "Please ensure that your passwords entered, correspond.")
        else:
            try:
                if group_selector.get() == 'Student':
                    data = "INSERT INTO Students VALUES (%s, %s, %s, %s, %s, %s, %s)"
                    val = (self.id_entry.get(),  self.name_entry.get(), self.surname_entry.get(),
                           self.contact_entry.get(), current_date, current_time, self.password_entry.get())
                    next_of_kin_data = "INSERT INTO Next_Of_Kin (stud_id, next_of_kin_name, " \
                                       "next_of_kin_surname, next_of_kin_contact) VALUES (%s, %s, %s, %s)"
                    next_of_kin_val = (self.id_entry.get(), self.nextOfKin_name_entry.get(),
                                       self.nextOfKin_surname_entry.get(), self.nextOfKin_contact_entry.get())
                    my_cursor.execute(data, val)
                    my_cursor.execute(next_of_kin_data, next_of_kin_val)
                    lifechoices_db.commit()
                    messagebox.showinfo("Welcome", "Please note that you have successfully registered!")
                    registering_screen.destroy()
                    import main
                elif group_selector == 'Admin':
                    # signIn_time = datetime.time(self)
                    # signIn_date = datetime.date(self)
                    data = "INSERT INTO Admin (admin_id, admin_name, admin_surname, admin_contact, " \
                           "admin_sign_in_date, admin_sign_in_time, admin_password) VALUES (%s, %s, %s, %s, %s)"
                    val = (self.id_entry.get(), self.name_entry.get(), self.surname_entry.get(),
                           self.contact_entry.get(), current_date, current_time, self.password_entry.get())
                    my_cursor.execute(data, val)
                    lifechoices_db.commit()
                    next_of_kin_data = "INSERT INTO Next_Of_Kin (admin_id, stud_id, visitor_id, next_of_kin_name, " \
                                       "next_of_kin_surname, next_of_kin_contact VALUES (%s, %s, %s, %s, %s, %s, %s)"
                    next_of_kin_val = (self.id_entry.get(), "N/A", "N/A", self.nextOfKin_name_entry.get(),
                                       self.nextOfKin_surname_entry.get(), self.nextOfKin_contact_entry.get())
                    my_cursor.execute(next_of_kin_data, next_of_kin_val)
                    lifechoices_db.commit()
                    messagebox.showinfo("Welcome", "Please note that you have successfully registered!")
                    registering_screen.destroy()
                elif group_selector == 'Visitor':
                    # signIn_time = datetime.time(self)
                    # signIn_date = datetime.date(self)
                    data = "INSERT INTO Visitors (visitor_id, visitor_name, visitor_surname, visitor_contact, " \
                           "visitor_sign_in_date, visitor_sign_in_time, visitor_password) VALUES (%s, %s, %s, %s, %s)"
                    val = (self.id_entry.get(), self.name_entry.get(), self.surname_entry.get(),
                           self.contact_entry.get(), current_date, current_time, self.password_entry.get())
                    my_cursor.execute(data, val)
                    lifechoices_db.commit()
                    next_of_kin_data = "INSERT INTO Next_Of_Kin (admin_id, stud_id, visitor_id, next_of_kin_name, " \
                                       "next_of_kin_surname, next_of_kin_contact VALUES (%s, %s, %s, %s, %s, %s, %s)"
                    next_of_kin_val = ("N/A", "N/A", self.id_entry.get(), self.nextOfKin_name_entry.get(),
                                       self.nextOfKin_surname_entry.get(), self.nextOfKin_contact_entry.get())
                    my_cursor.execute(next_of_kin_data, next_of_kin_val)
                    lifechoices_db.commit()
                    messagebox.showinfo("Welcome", "Please note that you have successfully registered!")
                    registering_screen.destroy()
            except ValueError:
                messagebox.showinfo("Entry Error", "Please ensure that your passwords entered, correspond.")
                self.name_entry.delete(0, END)
                self.password_entry.delete(0, END)
                self.confirm_entry.delete(0, END)

    def clear(self):
        self.name_entry.delete(0, END)
        self.surname_entry.delete(0, END)
        self.id_entry.delete(0, END)
        self.contact_entry.delete(0, END)
        self.password_entry.delete(0, END)
        self.confirm_entry.delete(0, END)
        self.nextOfKin_name_entry.delete(0, END)
        self.nextOfKin_surname_entry.delete(0, END)
        self.nextOfKin_contact_entry.delete(0, END)


registering_user = Registration()
registering_screen.mainloop()
