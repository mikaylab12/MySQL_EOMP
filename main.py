# Mikayla Beelders' End Of Module Project
from tkinter import *
import mysql.connector
from tkinter import messagebox
from PIL import Image, ImageTk
from tkinter.ttk import Combobox
from datetime import datetime
import rsaidnumber

login_screen = Tk()
login_screen.geometry("800x900")
login_screen.config(bg="#3556e8")
login_screen.title("Login Page")


def admin_page(event):
    login_screen.destroy()
    import admin


login_screen.bind("<Control-a>", admin_page)

# adding image
canvas = Canvas(login_screen, width=620, height=300, bg="#3c5be6", borderwidth=0, highlightthickness=0)
canvas.place(relx=0.1, rely=0.1)
img_logo = ImageTk.PhotoImage(Image.open("lifechoices-2.jpg"))
canvas.create_image(310, -15, anchor=N, image=img_logo)

# combo box
group = StringVar(login_screen)
group_list = ['Student', 'Visitor']
group_selector = Combobox(login_screen, textvariable=group.set, font=("Arial", 13), width=19)
group_selector.set("Select One")
group_selector['values'] = group_list
group_selector['state'] = 'readonly'
group_selector.place(relx=0.35, rely=0.665)

# connecting mysql to python
lifechoices_db = mysql.connector.connect(user='lifechoices', password='8-2fermENt2020', host='127.0.0.1',
                                         database='Lifechoices_Online', auth_plugin='mysql_native_password')
my_cursor = lifechoices_db.cursor(buffered=True)

# for exact date and time
current_date = datetime.now().date().strftime("%Y-%m-%d")
current_time = datetime.now().time().strftime("%H:%M:%S")


class Login(object):
    def __init__(self):
        # heading
        self.heading = Label(login_screen, text="Welcome To:", fg="white", bg="#3556e8",
                             font=("Arial", 35, "bold"))
        self.heading.place(relx=0.31, rely=0.04)
        # instruction heading
        self.instruction_heading = Label(login_screen, text="Please enter your login details:", fg="#7bfa05",
                                         bg="#3556e8", font=("Arial", 25, "bold"))
        self.instruction_heading.place(relx=0.1, rely=0.45)
        self.combobox_label = Label(login_screen, text="Group:", fg="white", bg="#3556e8", font=("Arial", 15,
                                                                                                 "bold"))
        self.combobox_label.place(relx=0.1, rely=0.665)

        # labels and entries
        self.id_label = Label(login_screen, text="ID number:", fg="white", bg="#3556e8", font=("Arial", 15,
                                                                                               "bold"))
        self.id_label.place(relx=0.1, rely=0.53)
        self.id_entry = Entry(login_screen, font=("Arial", 14))
        self.id_entry.place(relx=0.35, rely=0.53)

        self.password_label = Label(login_screen, text="Password:", fg="white", bg="#3556e8", font=("Arial", 15,
                                                                                                    "bold"))
        self.password_label.place(relx=0.1, rely=0.595)
        self.password_entry = Entry(login_screen, font=("Arial", 14), show='*')
        self.password_entry.place(relx=0.35, rely=0.595)
        # buttons
        self.login_btn = Button(login_screen, text="Login", padx=30, pady=10, borderwidth=5, fg="black", bg="#71f72a",
                                font=("Arial", 13, "bold"), command=self.login)
        self.login_btn.place(relx=0.72, rely=0.77)

        self.register_btn = Button(login_screen, text="Register New User", padx=30, pady=10, borderwidth=5, fg="black",
                                   bg="#71f72a", font=("Arial", 13, "bold"), command=self.register_screen)
        self.register_btn.place(relx=0.34, rely=0.77)

        self.clear_btn = Button(login_screen, text="Clear", padx=30, pady=10, borderwidth=5, fg="black",
                                bg="#fff", font=("Arial", 13, "bold"), command=self.clear)
        self.clear_btn.place(relx=0.1, rely=0.77)

    # login function
    def login(self):
        if group_selector.get() == "Select One":
            messagebox.showerror("Entry Error", "Please select your group.")
        elif self.id_entry.get() == "":
            messagebox.showerror("Entry Error", "Please enter your ID number.")
        elif self.password_entry.get() == "":
            messagebox.showerror("Entry Error", "Please enter your password.")
        else:
            try:
                if group_selector.get() == "Student":
                    my_cursor.execute('SELECT * FROM Students WHERE stud_id = "' + self.id_entry.get() + '"')
                    results = my_cursor.fetchall()
                    if results == []:
                        messagebox.showerror("Login Unsuccessful", "Please double-check the GROUP selected as well as your ID number or register as a new user.\n\nIf the issue persists, please see reception!")
                    elif str(self.id_entry.get()) == results[0][0] and str(self.password_entry.get()) == results[0][6]:
                        self.sign_in()
                    elif str(self.id_entry.get()) == results[0][0] and str(self.password_entry.get()) != results[0][6]:
                        messagebox.showerror("Error", "Password is incorrect")
                        self.password_entry.delete(0, END)
                elif group_selector.get() == "Visitor":
                    my_cursor.execute('SELECT * FROM Visitors WHERE visitor_id = "' + self.id_entry.get() + '"')
                    results = my_cursor.fetchall()
                    if results == []:
                        messagebox.showerror("Login Unsuccessful", "Please double-check the GROUP selected as well as your ID number or register as a new user.\n\nIf the issue persists, please see reception!")
                    elif str(self.id_entry.get()) == results[0][0] and str(self.password_entry.get()) == results[0][6]:
                        self.sign_in()
                    elif str(self.id_entry.get()) == results[0][0] and str(self.password_entry.get()) != results[0][6]:
                        messagebox.showerror("Error", "Password is incorrect")
                        self.password_entry.delete(0, END)
                else:
                    messagebox.showerror("Error", "Please select a group.")
            except TypeError:
                pass

    # function to execute sign in date and sign in time
    def sign_in(self):
        group_selector.bind("<<ComboboxSelected>>", self.sign_in)
        try:
            if group_selector.get() == 'Student':
                date_data = "UPDATE Students SET stud_sign_in_date=%s, stud_sign_out_date=NULL WHERE stud_id='" + self.id_entry.get() \
                            + "' AND stud_password = '" + self.password_entry.get() + "'"
                date_val = [current_date]
                time_data = "UPDATE Students SET stud_sign_in_time=%s , stud_sign_out_time=NULL WHERE stud_id='" + self.id_entry.get() \
                            + "' AND stud_password = '" + self.password_entry.get() + "'"
                time_val = [current_time]
                my_cursor.execute(date_data, date_val)
                my_cursor.execute(time_data, time_val)
                lifechoices_db.commit()
                messagebox.showinfo("Login Successful", "Enjoy your day!")
                login_screen.destroy()
                import sign_out
            elif group_selector.get() == 'Visitor':
                date_data = "UPDATE Visitors SET visitor_sign_in_date=%s, visitor_sign_out_date=NULL WHERE visitor_id='" + self.id_entry.get() \
                       + "' AND visitor_password = '" + self.password_entry.get() + "'"
                date_val = [current_date]
                time_data = "UPDATE Visitors SET visitor_sign_in_time=%s, visitor_sign_out_time=NULL WHERE visitor_id='" + self.id_entry.get() \
                       + "' AND visitor_password = '" + self.password_entry.get() + "'"
                time_val = [current_time]
                my_cursor.execute(date_data, date_val)
                my_cursor.execute(time_data, time_val)
                lifechoices_db.commit()
                messagebox.showinfo("Login Successful", "Enjoy your day!")
                login_screen.destroy()
                import sign_out
        except TypeError:
            pass

    # clear function
    def clear(self):
        self.id_entry.delete(0, END)
        self.password_entry.delete(0, END)
        group_selector.set("Select One")

    # function for register page
    def register_screen(self):
        login_screen.destroy()
        # registration page
        registering_screen = Tk()
        registering_screen.geometry("700x900")
        registering_screen.title("Register")
        registering_screen.config(bg="#000")

        # adding image
        reg_canvas = Canvas(registering_screen, width=400, height=300, bg="#000", borderwidth=0, highlightthickness=0)
        reg_canvas.place(relx=0.28, rely=0.01)
        reg_img_logo = ImageTk.PhotoImage(Image.open("lifechoices1.jpg"))
        reg_canvas.create_image(150, 5, anchor=N, image=reg_img_logo)

        lifechoices_db = mysql.connector.connect(user='lifechoices', password='8-2fermENt2020', host='127.0.0.1',
                                                 database='Lifechoices_Online', auth_plugin='mysql_native_password')
        my_cursor = lifechoices_db.cursor()

        # combo box
        reg_group = StringVar(registering_screen)
        reg_group_list = ['Student', 'Admin', 'Visitor']
        reg_group_selector = Combobox(registering_screen, textvariable=reg_group.set, font=("Arial", 13), width=19)
        reg_group_selector.set("Select One")
        reg_group_selector['values'] = reg_group_list
        reg_group_selector['state'] = 'readonly'
        reg_group_selector.place(relx=0.55, rely=0.17)

        class Registration(object):
            def __init__(self):
                self.heading = Label(registering_screen, text="Please enter your details:", fg="#71f72a", bg="#000",
                                     font=("Arial", 20, "bold"))
                self.heading.place(relx=0.08, rely=0.12)
                self.combobox_label = Label(registering_screen, text="Group:", fg="white", bg="#000",
                                            font=("Arial", 15))
                self.combobox_label.place(relx=0.08, rely=0.17)
                # labels and entries
                # name
                self.name_label = Label(registering_screen, text="Name:", fg="white", bg="#000", font=("Arial", 15))
                self.name_label.place(relx=0.08, rely=0.22)
                self.name_entry = Entry(registering_screen, font=("Arial", 13))
                self.name_entry.place(relx=0.55, rely=0.22)
                # surname
                self.surname_label = Label(registering_screen, text="Surname:", fg="white", bg="#000",
                                           font=("Arial", 15))
                self.surname_label.place(relx=0.08, rely=0.28)
                self.surname_entry = Entry(registering_screen, font=("Arial", 13))
                self.surname_entry.place(relx=0.55, rely=0.28)
                # id number
                self.id_label = Label(registering_screen, text="ID Number:", fg="white", bg="#000", font=("Arial", 15))
                self.id_label.place(relx=0.08, rely=0.34)
                self.id_entry = Entry(registering_screen, font=("Arial", 13))
                self.id_entry.place(relx=0.55, rely=0.34)
                # contact number
                self.contact_label = Label(registering_screen, text="Contact Number:", fg="white", bg="#000",
                                           font=("Arial", 15))
                self.contact_label.place(relx=0.08, rely=0.4)
                self.contact_entry = Entry(registering_screen, font=("Arial", 13))
                self.contact_entry.place(relx=0.55, rely=0.4)
                # password
                self.password_label = Label(registering_screen, text="Please enter a password:", fg="white", bg="#000",
                                            font=("Arial", 15))
                self.password_label.place(relx=0.08, rely=0.46)
                self.password_entry = Entry(registering_screen, font=("Arial", 13), show='*')
                self.password_entry.place(relx=0.55, rely=0.46)

                self.confirm_label = Label(registering_screen, text="Please confirm your password:", fg="white",
                                           bg="#000", font=("Arial", 15))
                self.confirm_label.place(relx=0.08, rely=0.52)
                self.confirm_entry = Entry(registering_screen, font=("Arial", 13), show='*')
                self.confirm_entry.place(relx=0.55, rely=0.52)
                # next of kin details
                self.nextOfKin_details = Label(registering_screen, text="Please enter your Next of Kin details:",
                                               fg="#71f72a", bg="#000", font=("Arial", 20, "bold"))
                self.nextOfKin_details.place(relx=0.08, rely=0.62)
                self.nextOfKin_name_label = Label(registering_screen, text="Name:", fg="white", bg="#000",
                                                  font=("Arial", 15))
                self.nextOfKin_name_label.place(relx=0.08, rely=0.67)
                self.nextOfKin_name_entry = Entry(registering_screen, font=("Arial", 13))
                self.nextOfKin_name_entry.place(relx=0.55, rely=0.67)
                # surname
                self.nextOfKin_surname_label = Label(registering_screen, text="Surname:", fg="white", bg="#000",
                                                     font=("Arial", 15))
                self.nextOfKin_surname_label.place(relx=0.08, rely=0.73)
                self.nextOfKin_surname_entry = Entry(registering_screen, font=("Arial", 13))
                self.nextOfKin_surname_entry.place(relx=0.55, rely=0.73)
                # id number
                self.nextOfKin_contact_label = Label(registering_screen, text="Contact Number:", fg="white", bg="#000",
                                                     font=("Arial", 15))
                self.nextOfKin_contact_label.place(relx=0.08, rely=0.79)
                self.nextOfKin_contact_entry = Entry(registering_screen, font=("Arial", 13))
                self.nextOfKin_contact_entry.place(relx=0.55, rely=0.79)
                # buttons
                register_btn = Button(registering_screen, text="Register", padx=15, pady=10, borderwidth=5, fg="black",
                                      bg="#71f72a",
                                      font=("Arial", 13, "bold"), command=self.validating_inputs)
                register_btn.place(relx=0.55, rely=0.89)

                clear_btn = Button(registering_screen, text="Clear", padx=25, pady=10, borderwidth=5, fg="black",
                                   bg="#fff",
                                   font=("Arial", 13, "bold"), command=self.clear)
                clear_btn.place(relx=0.25, rely=0.89)

            # function to register
            def validating_inputs(self):
                reg_group_selector.bind("<<ComboboxSelected>>", self.validating_inputs)
                if self.name_entry.get() == "":
                    messagebox.showerror("Entry Error", "Please enter your name.")
                elif self.surname_entry.get() == "":
                    messagebox.showerror("Entry Error", "Please enter your surname.")
                elif self.id_entry.get() == "":
                    messagebox.showerror("Entry Error", "Please enter your ID number.")
                elif self.password_entry.get() == "":
                    messagebox.showerror("Entry Error", "Please enter your password.")
                elif self.confirm_entry.get() == "":
                    messagebox.showerror("Entry Error", "Please confirm your password.")
                elif self.nextOfKin_name_entry.get() == "":
                    messagebox.showerror("Entry Error", "Please enter your Next of Kin's name.")
                elif self.nextOfKin_surname_entry.get() == "":
                    messagebox.showerror("Entry Error", "Please enter your Next of Kin's surname.")
                elif self.confirm_entry.get() != self.password_entry.get():
                    messagebox.showerror("Entry Error", "Please ensure that your passwords entered, correspond.")
                else:
                    try:
                        # checking if ID valid
                        def valid_id_check():
                            try:
                                user_id = self.id_entry.get()
                                while user_id:
                                    id_number = rsaidnumber.parse(user_id)
                                    valid_id = id_number
                                    while valid_id:
                                        return 1
                            except ValueError:
                                messagebox.showerror("Invalid ID", "\nPlease enter a valid South African ID "
                                                                  "number that consists of 13"
                                                                  " digits.")

                        # validating cell number
                        def cell_num_validation():
                            try:
                                tel = (self.contact_entry.get())
                                if int(len(tel)) == 10:
                                    return 1
                                elif int(len(tel)) > 10:
                                    messagebox.showerror('Error',
                                                        'Please ensure that your cellphone number contains only 10 digits.')
                                elif int(len(tel)) < 10:
                                    messagebox.showerror('Error', 'Please note that you have not entered 10 digits '
                                                                 'for your contact number')
                            except ValueError:
                                messagebox.showerror('Error',
                                                    'Please enter a valid cellphone number that only consists of digits. ')

                        # validating next of kins number
                        def next_of_kin_cell():
                            try:
                                next_of_kin_tel = (self.nextOfKin_contact_entry.get())
                                if int(len(next_of_kin_tel)) == 10:
                                    return 1
                                elif int(len(next_of_kin_tel)) > 10:
                                    messagebox.showerror('Error', "Please ensure that your Next of Kin's cellphone "
                                                                 "number contains only 10 digits.")
                                elif int(len(next_of_kin_tel)) < 10:
                                    messagebox.showerror('Error', "Please note that you have not entered 10 digits "
                                                                 "for your Next of Kin's contact number")
                            except ValueError:
                                messagebox.showerror('Error',
                                                    "Please enter a valid cellphone number, for your Next of Kin's "
                                                    "contact details, that only consists of digits. ")

                        if valid_id_check() == 1 and cell_num_validation() == 1 and next_of_kin_cell() == 1:
                            if reg_group_selector.get() == 'Select One':
                                messagebox.showerror('Selection Error',
                                                    "Please select the appropriate group.")
                            try:
                                if reg_group_selector.get() == 'Student':
                                    stud_data = "INSERT INTO Students (stud_id, stud_name, stud_surname, stud_contact, stud_sign_in_date, stud_sign_in_time, stud_password) VALUES (%s, %s, %s, %s, %s, %s, %s)"
                                    stud_val = (self.id_entry.get(), self.name_entry.get(), self.surname_entry.get(),
                                                self.contact_entry.get(), current_date, current_time,
                                                self.password_entry.get())
                                    stud_next_of_kin_data = "INSERT INTO Next_Of_Kin (stud_id, next_of_kin_name, " \
                                                            "next_of_kin_surname, next_of_kin_contact) VALUES (%s, %s, %s, %s)"
                                    stud_next_of_kin_val = (self.id_entry.get(), self.nextOfKin_name_entry.get(),
                                                            self.nextOfKin_surname_entry.get(),
                                                            self.nextOfKin_contact_entry.get())
                                    my_cursor.execute(stud_data, stud_val)
                                    my_cursor.execute(stud_next_of_kin_data, stud_next_of_kin_val)
                                    lifechoices_db.commit()
                                    messagebox.showinfo("Welcome",
                                                        "Please note that you have successfully registered as a Student!")
                                    messagebox.showinfo("Signing in", "Please note that you have automatically been signed in.")
                                    import sign_out
                                elif reg_group_selector.get() == 'Admin':
                                    adm_data = "INSERT INTO Admin (admin_id, admin_name, admin_surname, admin_contact, admin_sign_in_date, admin_sign_in_time, admin_password) VALUES (%s, %s, %s, %s, %s, %s, %s)"
                                    adm_val = (self.id_entry.get(), self.name_entry.get(), self.surname_entry.get(),
                                               self.contact_entry.get(), current_date, current_time,
                                               self.password_entry.get())
                                    adm_next_of_kin_data = "INSERT INTO Next_Of_Kin (admin_id, next_of_kin_name, " \
                                                           "next_of_kin_surname, next_of_kin_contact) VALUES (%s, %s, %s, %s)"
                                    adm_next_of_kin_val = (self.id_entry.get(), self.nextOfKin_name_entry.get(),
                                                           self.nextOfKin_surname_entry.get(),
                                                           self.nextOfKin_contact_entry.get())
                                    my_cursor.execute(adm_data, adm_val)
                                    my_cursor.execute(adm_next_of_kin_data, adm_next_of_kin_val)
                                    lifechoices_db.commit()
                                    messagebox.showinfo("Welcome",
                                                        "Please note that you have successfully registered as Admin!")
                                    registering_screen.destroy()
                                    import admin
                                elif reg_group_selector.get() == 'Visitor':
                                    visi_data = "INSERT INTO Visitor (visitor_id, visitor_name, visitor_surname, visitor_contact, visitor_sign_in_date, visitor_sign_in_time, visitor_password) VALUES (%s, %s, %s, %s, %s, %s, %s)"
                                    visi_val = (self.id_entry.get(), self.name_entry.get(), self.surname_entry.get(),
                                                self.contact_entry.get(), current_date, current_time,
                                                self.password_entry.get())
                                    visi_next_of_kin_data = "INSERT INTO Next_Of_Kin (visitor_id, next_of_kin_name, " \
                                                            "next_of_kin_surname, next_of_kin_contact) VALUES (%s, %s, %s, %s)"
                                    visi_next_of_kin_val = (self.id_entry.get(), self.nextOfKin_name_entry.get(),
                                                            self.nextOfKin_surname_entry.get(),
                                                            self.nextOfKin_contact_entry.get())
                                    my_cursor.execute(visi_data, visi_val)
                                    my_cursor.execute(visi_next_of_kin_data, visi_next_of_kin_val)
                                    lifechoices_db.commit()
                                    messagebox.showinfo("Welcome",
                                                        "Please note that you have successfully registered as a Visitor!")
                                    messagebox.showinfo("Signing in",
                                                        "Please note that you have automatically been signed in.")
                                    import sign_out
                            except ValueError:
                                messagebox.showerror("Entry Error",
                                                    "Please ensure that your passwords entered, correspond.")
                                self.name_entry.delete(0, END)
                                self.password_entry.delete(0, END)
                                self.confirm_entry.delete(0, END)
                    except ValueError:
                        pass

            # function to clear
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
                reg_group_selector.set("Select One")

        registering_user = Registration()
        registering_screen.mainloop()


logging_in = Login()
login_screen.mainloop()
