# registration page
from tkinter import *
from tkinter import messagebox
import mysql.connector
from PIL import Image, ImageTk
from tkinter.ttk import Combobox
from datetime import datetime
import rsaidnumber

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

# combo box
group = StringVar(registering_screen)
group_list = ['Student', 'Admin', 'Visitor']
group_selector = Combobox(registering_screen, textvariable=group.set, font=("Arial", 13), width=19)
group_selector.set("Select One")
group_selector['values'] = group_list
group_selector['state'] = 'readonly'
group_selector.place(relx=0.55, rely=0.17)

current_date = datetime.now().date().strftime("%Y-%m-%d")
current_time = datetime.now().time().strftime("%H:%M:%S")


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
                              font=("Arial", 13, "bold"), command=self.validating_inputs)
        register_btn.place(relx=0.55, rely=0.89)

        clear_btn = Button(registering_screen, text="Clear", padx=25, pady=10, borderwidth=5, fg="black",
                           bg="#fff",
                           font=("Arial", 13, "bold"), command=self.clear)
        clear_btn.place(relx=0.25, rely=0.89)

    # function to register
    def validating_inputs(self):
        if self.name_entry == "":
            messagebox.showinfo("Entry Error", "Please enter your name.")
        if self.surname_entry == "":
            messagebox.showinfo("Entry Error", "Please enter your surname.")
        if self.id_entry == "":
            messagebox.showinfo("Entry Error", "Please enter your ID number.")
        if self.password_entry == "":
            messagebox.showinfo("Entry Error", "Please enter your password.")
        if self.confirm_entry == "":
            messagebox.showinfo("Entry Error", "Please confirm your password.")
        if self.nextOfKin_name_entry == "":
            messagebox.showinfo("Entry Error", "Please enter your Next of Kin's name.")
        if self.nextOfKin_surname_entry == "":
            messagebox.showinfo("Entry Error", "Please enter your Next of Kin's surname.")
        elif self.confirm_entry.get() != self.password_entry.get():
            messagebox.showinfo("Entry Error", "Please ensure that your passwords entered, correspond.")
        else:
            try:
                def age_calc():
                    try:
                        user_id = self.id_entry.get()
                        while user_id:
                            id_number = rsaidnumber.parse(user_id)
                            valid_id = id_number
                            while valid_id:
                                return 1
                    except ValueError:
                        messagebox.showinfo("Invalid ID", "\nPlease enter a valid South African ID "
                                                          "number that consists of 13"
                                                          " digits.")

                def cell_num_validation():
                    try:
                        tel = (self.contact_entry.get())
                        if int(len(tel)) == 10:
                            return 1
                        elif int(len(tel)) > 10:
                            messagebox.showinfo('Error', 'Please ensure that your cellphone number contains only 10 digits.')
                        elif int(len(tel)) < 10:
                            messagebox.showinfo('Error', 'Please note that you have not entered 10 digits '
                                                         'for your contact number')
                    except ValueError:
                        messagebox.showinfo('Error', 'Please enter a valid cellphone number that only consists of digits. ')

                def next_of_kin_cell():
                    try:
                        next_of_kin_tel = (self.nextOfKin_contact_entry.get())
                        if int(len(next_of_kin_tel)) == 10:
                            return 1
                        elif int(len(next_of_kin_tel)) > 10:
                            messagebox.showinfo('Error', "Please ensure that your Next of Kin's cellphone "
                                                         "number contains only 10 digits.")
                        elif int(len(next_of_kin_tel)) < 10:
                            messagebox.showinfo('Error', "Please note that you have not entered 10 digits "
                                                         "for your Next of Kin's contact number")
                    except ValueError:
                        messagebox.showinfo('Error', "Please enter a valid cellphone number, for your Next of Kin's "
                                                     "contact details, that only consists of digits. ")

                if age_calc() == 1 and cell_num_validation() == 1 and next_of_kin_cell() == 1:
                # if self.name_entry == "":
                #     messagebox.showinfo("Entry Error", "Please enter your name.")
                # if self.surname_entry == "":
                #     messagebox.showinfo("Entry Error", "Please enter your surname.")
                # if self.id_entry == "":
                #     messagebox.showinfo("Entry Error", "Please enter your ID number.")
                # if self.contact_entry == "":
                #     messagebox.showinfo("Entry Error", "Please enter your contact number.")
                # if self.password_entry == "":
                #     messagebox.showinfo("Entry Error", "Please enter your password.")
                # if self.confirm_entry == "":
                #     messagebox.showinfo("Entry Error", "Please confirm your password.")
                # # if self.nextOfKin_name_entry == "" or self.nextOfKin_surname_entry == "" or self.nextOfKin_contact_entry == "":
                # #     messagebox.showinfo("Next OF Kin Entry Error", "Please ensure that your have filled in all the "
                # #                                                    "required details of your next of Kin.")
                # if self.confirm_entry.get() != self.password_entry.get():
                #     messagebox.showinfo("Entry Error", "Please ensure that your passwords entered, correspond.")
                # else:
                #     if self.nextOfKin_name_entry == "":
                #         messagebox.showinfo("Entry Error", "Please enter your Next of Kin's name.")
                #     if self.nextOfKin_surname_entry == "":
                #         messagebox.showinfo("Entry Error", "Please enter your Next of Kin's surname.")
                #     if self.nextOfKin_contact_entry == "":
                #         messagebox.showinfo("Entry Error", "Please enter your Next of Kin's contact number.")
                    try:
                        if group_selector.get() == 'Student':
                            stud_data = "INSERT INTO Students VALUES (%s, %s, %s, %s, %s, %s, %s)"
                            stud_val = (self.id_entry.get(),  self.name_entry.get(), self.surname_entry.get(),
                                        self.contact_entry.get(), current_date, current_time, self.password_entry.get())
                            stud_next_of_kin_data = "INSERT INTO Next_Of_Kin (stud_id, next_of_kin_name, " \
                                                    "next_of_kin_surname, next_of_kin_contact) VALUES (%s, %s, %s, %s)"
                            stud_next_of_kin_val = (self.id_entry.get(), self.nextOfKin_name_entry.get(),
                                                    self.nextOfKin_surname_entry.get(), self.nextOfKin_contact_entry.get())
                            my_cursor.execute(stud_data, stud_val)
                            my_cursor.execute(stud_next_of_kin_data, stud_next_of_kin_val)
                            lifechoices_db.commit()
                            messagebox.showinfo("Welcome", "Please note that you have successfully registered as a Student!")
                            import main
                            registering_screen.destroy()
                        elif group_selector.get() == 'Admin':
                            adm_data = "INSERT INTO Admin VALUES (%s, %s, %s, %s, %s, %s, %s)"
                            adm_val = (self.id_entry.get(), self.name_entry.get(), self.surname_entry.get(),
                                       self.contact_entry.get(), current_date, current_time, self.password_entry.get())
                            adm_next_of_kin_data = "INSERT INTO Next_Of_Kin (admin_id, next_of_kin_name, " \
                                                   "next_of_kin_surname, next_of_kin_contact) VALUES (%s, %s, %s, %s)"
                            adm_next_of_kin_val = (self.id_entry.get(), self.nextOfKin_name_entry.get(),
                                                   self.nextOfKin_surname_entry.get(), self.nextOfKin_contact_entry.get())
                            my_cursor.execute(adm_data, adm_val)
                            my_cursor.execute(adm_next_of_kin_data, adm_next_of_kin_val)
                            lifechoices_db.commit()
                            messagebox.showinfo("Welcome", "Please note that you have successfully registered as Admin!")
                            import main
                            registering_screen.destroy()
                        elif group_selector.get() == 'Visitor':
                            # signIn_time = datetime.time(self)
                            # signIn_date = datetime.date(self)
                            visi_data = "INSERT INTO Visitors VALUES (%s, %s, %s, %s, %s, %s, %s)"
                            visi_val = (self.id_entry.get(), self.name_entry.get(), self.surname_entry.get(),
                                        self.contact_entry.get(), current_date, current_time, self.password_entry.get())
                            visi_next_of_kin_data = "INSERT INTO Next_Of_Kin (visitor_id, next_of_kin_name, " \
                                                    "next_of_kin_surname, next_of_kin_contact) VALUES (%s, %s, %s, %s)"
                            visi_next_of_kin_val = (self.id_entry.get(), self.nextOfKin_name_entry.get(),
                                                    self.nextOfKin_surname_entry.get(), self.nextOfKin_contact_entry.get())
                            my_cursor.execute(visi_data, visi_val)
                            my_cursor.execute(visi_next_of_kin_data, visi_next_of_kin_val)
                            lifechoices_db.commit()
                            messagebox.showinfo("Welcome", "Please note that you have successfully registered as a Visitor!")
                            import main
                            registering_screen.destroy()
                    except ValueError:
                        messagebox.showinfo("Entry Error", "Please ensure that your passwords entered, correspond.")
                        self.name_entry.delete(0, END)
                        self.password_entry.delete(0, END)
                        self.confirm_entry.delete(0, END)
            except ValueError:
                messagebox.showinfo("Entry Error", "hi")

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

        # def age_calc():
        #     try:
        #         # current date
        #         # current_date = datetime.today()
        #         # in order to validate id number entered
        #         id_number = rsaidnumber.parse(self.id_entry.get())
        #         valid_id = id_number
        #         # while valid_id:
        #         #     dob = id_number.date_of_birth
        #         #      current_age = int((current_date - dob) // timedelta(days=365.25))
        #             # if int(current_age) >= 18:
        #             #     return 1
        #             # else:
        #             #     messagebox.showinfo("Underage", "You are too young to play.\nPlease try again in " + str(
        #             #         18 - int(current_age)) + " years")
        #     except ValueError:
        #         messagebox.showinfo("Invalid ID", "\nPlease enter a valid South African ID number that consists of 13"
        #                             " digits.")
        #
        # def cell_num_validation():
        #     try:
        #         tel = (self.contact_entry.get())
        #         if int(len(tel)) == 10:
        #             return 1
        #         elif int(len(tel)) > 10:
        #             messagebox.showinfo('Error', 'Please ensure that your cellphone number contains only 10 digits.')
        #         elif int(len(tel)) < 10:
        #             messagebox.showinfo('Error', 'Please note that you have not entered 10 digits '
        #                                 'for your contact number')
        #     except ValueError:
        #         messagebox.showinfo('Error', 'Please enter a valid cellphone number that only consists of digits. ')
        #
        # def next_of_kin_cell():
        #     try:
        #         next_of_kin_tel = (self.contact_entry.get())
        #         if int(len(next_of_kin_tel)) == 10:
        #             return 1
        #         elif int(len(next_of_kin_tel)) > 10:
        #             messagebox.showinfo('Error', 'Please ensure that your cellphone number contains only 10 digits.')
        #         elif int(len(next_of_kin_tel)) < 10:
        #             messagebox.showinfo('Error', 'Please note that you have not entered 10 digits '
        #                                 'for your contact number')
        #     except ValueError:
        #         messagebox.showinfo('Error', 'Please enter a valid cellphone number that only consists of digits. ')
        #
        # if age_calc() == 1 and cell_num_validation() == 1 and next_of_kin_cell() == 1:
        #     fh = open("Player_info.txt", "a")
        #     fh.write("\nName and Surname: " + self.name_entry.get() + '\n')
        #     fh.write("ID Number: " + self.id_entry.get() + '\n')
        #     fh.write("Email: " + self.email_entry.get() + '\n')
        #     fh.write("Number: " + self.telephone_number_entry.get() + '\n')
        #     fh.write("Residential Address: " + self.residential_address_entry.get() + "\n")
        #     fh.close()
        #     messagebox.showinfo("Valid Details", "Let's Play!")
        #     login_screen.destroy()
        #     self.screen_2()

registering_user = Registration()
registering_screen.mainloop()
