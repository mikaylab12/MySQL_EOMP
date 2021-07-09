from tkinter import *
from tkinter import ttk
import mysql.connector
from tkinter import messagebox
from PIL import Image, ImageTk
import rsaidnumber
from datetime import datetime

# admin_login = Tk()
# admin_login.title("Admin Login")
# admin_login.config(bg="#1a1a18")
# admin_login.geometry("800x900")

# # declaring text variables
# name = StringVar()
# person_id = IntVar()
# surname = StringVar()
# password = IntVar()
# contact = IntVar()

# connecting mysql to python
lifechoices_db = mysql.connector.connect(user='lifechoices', password='8-2fermENt2020', host='127.0.0.1',
                                         database='Lifechoices_Online', auth_plugin='mysql_native_password')
my_cursor = lifechoices_db.cursor(buffered=True)

# for exact date and time
current_date = datetime.now().date().strftime("%Y-%m-%d")
current_time = datetime.now().time().strftime("%H:%M:%S")

date = datetime.today().date().strftime("%H:%M:%S")
#
# # adding image
# canvas = Canvas(admin_login, width=400, height=400, bg="#1a1a18", borderwidth=0, highlightthickness=0)
# canvas.place(relx=0.25, rely=0.05)
# img_logo = ImageTk.PhotoImage(Image.open("lclogo.png"))
# canvas.create_image(200, 5, anchor=N, image=img_logo)
#
# admin_heading = Label(admin_login, text="Welcome Admin!", bg="#1a1a18", fg="white", font=("Arial", 30, "bold"))
# admin_heading.place(relx=0.3, rely=0.47)
#
#
# class AdminLoginPage(object):
#     def __init__(self):
#         self.instruction_heading = Label(admin_login, text="Please enter your:", fg="#7bfa05",
#                                          bg="#1a1a18", font=("Arial", 21, "bold"))
#         self.instruction_heading.place(relx=0.3, rely=0.58)
#         # labels and entries
#         self.id_label = Label(admin_login, text="ID number:", fg="white", bg="#1a1a18", font=("Arial", 15,
#                                                                                               "bold"))
#         self.id_label.place(relx=0.3, rely=0.65)
#         self.id_entry = Entry(admin_login, font=("Arial", 14))
#         self.id_entry.place(relx=0.45, rely=0.65)
#
#         self.password_label = Label(admin_login, text="Password:", fg="white", bg="#1a1a18", font=("Arial", 15,
#                                                                                                     "bold"))
#         self.password_label.place(relx=0.3, rely=0.72)
#         self.password_entry = Entry(admin_login, font=("Arial", 14), show='*')
#         self.password_entry.place(relx=0.45, rely=0.72)
#         # buttons
#         self.login_btn = Button(admin_login, text="Login", padx=30, pady=10, borderwidth=5, fg="black", bg="#71f72a",
#                                 font=("Arial", 13, "bold"), command=self.login)
#         self.login_btn.place(relx=0.55, rely=0.8)
#
#         self.clear_btn = Button(admin_login, text="Clear", padx=30, pady=10, borderwidth=5, fg="black",
#                                 bg="#fff", font=("Arial", 13, "bold"), command=self.clear)
#         self.clear_btn.place(relx=0.3, rely=0.8)
#
#     # function for admin to log in
#     def login(self):
#         try:
#             my_cursor.execute('SELECT * FROM Admin')
#             for i in my_cursor:
#                 if int(self.id_entry.get()) == int(i[0]) and self.password_entry.get() == i[6]:
#                     messagebox.showinfo("Congratulations", "Successful login")
#                     admin_login.destroy()
#                     self.admin_page()
#                 elif int(self.id_entry.get()) != int(i[0]) and self.password_entry.get() == i[6]:
#                     messagebox.showerror("Error", "ID number is incorrect")
#                     self.id_entry.delete(0, END)
#                 else:
#                     if int(self.id_entry.get()) == int(i[0]) and self.password_entry.get() != i[6]:
#                         messagebox.showerror("Error", "Password is incorrect")
#                         self.password_entry.delete(0, END)
#         except ValueError:
#             messagebox.showerror("Error", "Please ensure that your ID consists of digits")
#
#     def clear(self):
#         self.id_entry.delete(0, END)
#         self.password_entry.delete(0, END)
#         # group_selector.set("Select One")
#
#     def admin_page(self):
admin_page = Tk()
admin_page.title("Admin Login")
admin_page.config(bg="white")
admin_page.geometry("1450x900")
frame1 = Frame(admin_page, bg="#a3ff52", highlightbackground="white", highlightthickness=5, width=1270, height=500)
frame1.place(relx=0.06, rely=0.23)

# declaring text variables
name = StringVar()
person_id = StringVar()
surname = StringVar()
password = StringVar()
contact = StringVar()
nextOfKin_name = StringVar()
nextOfKin_surname = StringVar()
nextOfKin_contact = StringVar()

# adding image
access_canvas = Canvas(admin_page, width=200, height=150, bg="white", borderwidth=0, highlightthickness=0)
access_canvas.place(relx=0.05, rely=0.05)
access_img_logo = ImageTk.PhotoImage(Image.open("Life-Choices-150x150.jpg"))
access_canvas.create_image(120, 0, anchor=N, image=access_img_logo)

# adding image
access_canvas2 = Canvas(admin_page, width=200, height=150, bg="white", borderwidth=0, highlightthickness=0)
access_canvas2.place(relx=0.77, rely=0.05)
access_img_logo2 = ImageTk.PhotoImage(Image.open("Life-Choices-150x150.jpg"))
access_canvas2.create_image(120, 0, anchor=N, image=access_img_logo2)

# combo box
group = StringVar(frame1)
group_list = ['Student', 'Admin', 'Visitor']
group_selector = ttk.Combobox(frame1, textvariable=group.set, font=("Arial", 17), width=19)
group_selector.set("Select One")
group_selector['values'] = group_list
group_selector['state'] = 'readonly'
group_selector.place(relx=0.015, rely=0.1)


class AdminAccess(object):
    def __init__(self):
        self.search_btn = Button(frame1, text="Search", command=self.group_treeview, pady=10, padx=15,
                                 borderwidth=5, font=("Arial", 15))
        self.search_btn.place(relx=0.25, rely=0.07)
        self.heading = Label(admin_page, text="Admin Page", font=("Arial", 100, "bold"), bg="white", fg="grey")
        self.heading.place(relx=0.23, rely=0.04)

        # treeview
        self.treeview_table = ttk.Treeview(frame1, columns=(1, 2, 3, 4, 5, 6, 7, 8, 9), show="headings")
        self.treeview_table.place(relx=0.015, rely=0.23)
        self.treeview_table.column('#0', width=0, stretch=NO)
        self.treeview_table.column(1, anchor=CENTER, width=130)
        self.treeview_table.column(2, anchor=CENTER, width=120)
        self.treeview_table.column(3, anchor=CENTER, width=120)
        self.treeview_table.column(4, anchor=CENTER, width=120)
        self.treeview_table.column(5, anchor=CENTER, width=150)
        self.treeview_table.column(6, anchor=CENTER, width=150)
        self.treeview_table.column(7, anchor=CENTER, width=120)
        self.treeview_table.column(8, anchor=CENTER, width=150)
        self.treeview_table.column(9, anchor=CENTER, width=150)

        self.treeview_table.heading('#0', text='', anchor=CENTER)
        self.treeview_table.heading(1, text='ID', anchor=CENTER)
        self.treeview_table.heading(2, text='Name', anchor=CENTER)
        self.treeview_table.heading(3, text='Surname', anchor=CENTER)
        self.treeview_table.heading(4, text='Contact', anchor=CENTER)
        self.treeview_table.heading(5, text='Sign in Date', anchor=CENTER)
        self.treeview_table.heading(6, text='Sign in Time', anchor=CENTER)
        self.treeview_table.heading(7, text='Password', anchor=CENTER)
        self.treeview_table.heading(8, text='Sign out Date', anchor=CENTER)
        self.treeview_table.heading(9, text='Sign out Time', anchor=CENTER)

        delete_entries = Button(frame1, text="Delete", bg="red", fg="black", command=self.delete, padx=15,
                                pady=10,
                                borderwidth=5, font=("Arial", 15))
        delete_entries.place(relx=0.82, rely=0.8)
        insert_entries = Button(frame1, text="Insert", bg="#83f740", fg="black", command=lambda: self.insert_data(),
                                padx=15, pady=10,
                                borderwidth=5, font=("Arial", 15))
        insert_entries.place(relx=0.15, rely=0.8)
        update_entries = Button(frame1, text="Update", bg="#d5f538", fg="black", command=lambda: self.selected_data(),
                                padx=15, pady=10,
                                borderwidth=5, font=("Arial", 15))
        update_entries.place(relx=0.48, rely=0.8)
        count_btn = Button(admin_page, text="Count", command=self.count, bg='black', fg='white',
                           padx=15, pady=10, borderwidth=5, font=("Arial", 20))
        count_btn.place(relx=0.15, rely=0.8)
        sign_out_btn = Button(admin_page, text="Admin Sign Out", command=self.sign_out(), bg='black', fg='white',
                              padx=15, pady=10, borderwidth=5, font=("Arial", 20))
        sign_out_btn.place(relx=0.775, rely=0.85)

    # function to display data on treeview from mysql tables
    def group_treeview(self):
        try:
            for i in self.treeview_table.get_children():
                self.treeview_table.delete(i)
            if group_selector.get() == 'Student':
                lifechoices_db = mysql.connector.connect(user='lifechoices', password='8-2fermENt2020', host='127.0.0.1',
                                                         database='Lifechoices_Online', auth_plugin='mysql_native_password')
                my_cursor = lifechoices_db.cursor()
                sql = "SELECT * FROM Students"
                my_cursor.execute(sql)

                rows = my_cursor.fetchall()

                for i in rows:
                    self.treeview_table.insert("", 'end', values=i)

            elif group_selector.get() == 'Admin':
                lifechoices_db = mysql.connector.connect(user='lifechoices', password='8-2fermENt2020', host='127.0.0.1',
                                                         database='Lifechoices_Online', auth_plugin='mysql_native_password')
                my_cursor = lifechoices_db.cursor()

                sql = "SELECT * FROM Admin"
                my_cursor.execute(sql)

                rows = my_cursor.fetchall()

                for i in rows:
                    self.treeview_table.insert("", 'end', values=i)
            elif group_selector.get() == 'Visitor':
                lifechoices_db = mysql.connector.connect(user='lifechoices', password='8-2fermENt2020', host='127.0.0.1',
                                                         database='Lifechoices_Online', auth_plugin='mysql_native_password')
                my_cursor = lifechoices_db.cursor()

                sql = "SELECT * FROM Visitors"
                my_cursor.execute(sql)

                rows = my_cursor.fetchall()
                # total = my_cursor.rowcount

                for i in rows:
                    self.treeview_table.insert("", 'end', values=i)
            group_selector.bind("<<ComboboxSelected>>", self.group_treeview)
        except TypeError:
            pass

    # function to delete data in treeview as well as mysql tables
    def delete(self):
        if group_selector.get() == "Student":
            item = self.treeview_table.selection()[0]
            selected_item = self.treeview_table.item(item)['values'][0]
            delete = "DELETE FROM Students WHERE stud_id= %s"
            selected_data = (selected_item,)
            my_cursor.execute(delete, selected_data)
            lifechoices_db.commit()
            self.treeview_table.delete(item)
            messagebox.showinfo("Success", "User Data Removed")
        elif group_selector.get() == 'Admin':
            item = self.treeview_table.selection()[0]
            selected_item = self.treeview_table.item(item)['values'][0]
            delete = "DELETE FROM Admin WHERE admin_id= %s"
            selected_data = (selected_item,)
            my_cursor.execute(delete, selected_data)
            lifechoices_db.commit()
            self.treeview_table.delete(item)
            messagebox.showinfo("Success", "User Data Removed")
        elif group_selector.get() == 'Visitor':
            item = self.treeview_table.selection()[0]
            selected_item = self.treeview_table.item(item)['values'][0]
            delete = "DELETE FROM Visitors WHERE visitor_id= %s"
            selected_data = (selected_item,)
            my_cursor.execute(delete, selected_data)
            lifechoices_db.commit()
            self.treeview_table.delete(item)
            messagebox.showinfo("Success", "User Data Removed")
        group_selector.bind("<<ComboboxSelected>>", self.delete)

    # function to create frame in order to insert users
    def insert_data(self):
        frame = Frame(admin_page, width=700, height=600, bg="black")
        frame.place(relx=0.3, rely=0.2)
        heading = Label(frame, text="Insert Details:", bg="black", fg="white", font=("Arial", 20, "bold"))
        heading.place(relx=0.05, rely=0.05)
        namelbl= Label(frame, text="Name:", bg="black", fg="white", font=("Arial", 15))
        nameent = Entry(frame, textvariable=name, width=25, font=("Arial", 15))
        namelbl.place(relx=0.1, rely=0.2)
        nameent.place(relx=0.45, rely=0.2)

        insert_group = StringVar(frame)
        insert_group_list = ['Student', 'Admin', 'Visitor']
        insert_group_selector = ttk.Combobox(frame, textvariable=insert_group.set, font=("Arial", 17), width=19)
        insert_group_selector.set("Select One")
        insert_group_selector['values'] = insert_group_list
        insert_group_selector['state'] = 'readonly'
        insert_group_selector.place(relx=0.45, rely=0.13)
        group_label = Label(frame, text="Group:", bg="black", fg="white", font=("Arial", 15))
        group_label.place(relx=0.1, rely=0.13)

        idlbl = Label(frame, text="ID number:", bg="black", fg="white", font=("Arial", 15))
        ident = Entry(frame, textvariable=person_id, width=25, font=("Arial", 15))
        idlbl.place(relx=0.1, rely=0.34)
        ident.place(relx=0.45, rely=0.34)

        surnamelbl = Label(frame, text="Surname:", bg="black", fg="white", font=("Arial", 15))
        surnamelbl.place(relx=0.1, rely=0.27)
        surnameent = Entry(frame, textvariable=surname, width=25, font=("Arial", 15))
        surnameent.place(relx=0.45, rely=0.27)

        contactlbl = Label(frame, text="Phone number:", bg="black", fg="white", font=("Arial", 15))
        contactlbl.place(relx=0.1, rely=0.41)
        contactent = Entry(frame, textvariable=contact, width=25, font=("Arial", 15))
        contactent.place(relx=0.45, rely=0.41)

        passwordlbl = Label(frame, text="Password:", bg="black", fg="white", font=("Arial", 15))
        passwordlbl.place(relx=0.1, rely=0.48)
        passwordent = Entry(frame, textvariable=password, width=25, font=("Arial", 15))
        passwordent.place(relx=0.45, rely=0.48)

        nextOfKin_namelbl = Label(frame, text="Next Of Kin Name:", bg="black", fg="white", font=("Arial", 15))
        nextOfKin_nameent = Entry(frame, textvariable=nextOfKin_name, width=25, font=("Arial", 15))
        nextOfKin_namelbl.place(relx=0.1, rely=0.55)
        nextOfKin_nameent.place(relx=0.45, rely=0.55)

        nextOfKin_surnamelbl = Label(frame, text="Next Of Kin Surname:", bg="black", fg="white", font=("Arial", 15))
        nextOfKin_surnamelbl.place(relx=0.1, rely=0.62)
        nextOfKin_surnameent = Entry(frame, textvariable=nextOfKin_surname, width=25, font=("Arial", 15))
        nextOfKin_surnameent.place(relx=0.45, rely=0.62)

        nextOfKin_contactlbl = Label(frame, text="Next Of Kin Contact:", bg="black", fg="white", font=("Arial", 15))
        nextOfKin_contactlbl.place(relx=0.1, rely=0.69)
        nextOfKin_contactent = Entry(frame, textvariable=nextOfKin_contact, width=25, font=("Arial", 15))
        nextOfKin_contactent.place(relx=0.45, rely=0.69)

        # function to destroy insert frame
        def ins_destroy():
            MsgBox2 = messagebox.askquestion('Exit Application', 'Are you sure you want to exit the application',
                                             icon='warning')
            if MsgBox2 == 'yes':
                frame.destroy()
            else:
                messagebox.showinfo('Return', 'Returning to main application')

        ins_cancel_btn = Button(frame, text="Cancel Insert", command=ins_destroy, bg='red', fg='black', padx=15, pady=10,
                                borderwidth=5, font=("Arial", 15))
        ins_cancel_btn.place(relx=0.45, rely=0.82)

        # function to insert data into treeview as well as mysql tables
        def add_data():
            nonlocal nameent, ident, surnameent, contactent, passwordent, nextOfKin_nameent, nextOfKin_surnameent, \
                nextOfKin_contactent
            user_name = name.get()
            user_id = person_id.get()
            user_surname = surname.get()
            user_password = password.get()
            user_contact = contact.get()
            nok_name = nextOfKin_name.get()
            nok_surname = nextOfKin_surname.get()
            nok_contact = nextOfKin_contact.get()

            def valid_id_check():
                try:
                    valid_user_id = user_id
                    while valid_user_id:
                        id_number = rsaidnumber.parse(valid_user_id)
                        valid_id = id_number
                        while valid_id:
                            return 1
                except ValueError:
                    messagebox.showinfo("Invalid ID", "\nPlease enter a valid South African ID "
                                                      "number that consists of 13"
                                                      " digits.")

            def cell_num_validation():
                try:
                    tel = user_contact
                    if int(len(tel)) == 10:
                        return 1
                    elif int(len(tel)) > 10:
                        messagebox.showinfo('Error',
                                            'Please ensure that your cellphone number contains only 10 digits.')
                    elif int(len(tel)) < 10:
                        messagebox.showinfo('Error', 'Please note that you have not entered 10 digits '
                                                     'for your contact number')
                except ValueError:
                    messagebox.showinfo('Error',
                                        'Please enter a valid cellphone number that only consists of digits. ')

            def next_of_kin_cell():
                try:
                    next_of_kin_tel = nok_contact
                    if int(len(next_of_kin_tel)) == 10:
                        return 1
                    elif int(len(next_of_kin_tel)) > 10:
                        messagebox.showinfo('Error', "Please ensure that your Next of Kin's cellphone "
                                                     "number contains only 10 digits.")
                    elif int(len(next_of_kin_tel)) < 10:
                        messagebox.showinfo('Error', "Please note that you have not entered 10 digits "
                                                     "for your Next of Kin's contact number")
                except ValueError:
                    messagebox.showinfo('Error',
                                        "Please enter a valid cellphone number, for your Next of Kin's "
                                        "contact details, that only consists of digits. ")

            if valid_id_check() == 1 and cell_num_validation() == 1 and next_of_kin_cell() == 1:
                try:
                    if insert_group_selector.get() == 'Student':
                        my_cursor.execute(
                            "INSERT INTO Students(stud_id, stud_name, stud_surname, stud_contact, stud_sign_in_date, stud_sign_in_time, stud_password) "
                            "VALUES(%s, %s, %s, %s,%s, %s, %s)",
                            (user_id, user_name, user_surname, user_contact, current_date, current_time,
                             user_password))
                        my_cursor.execute(
                            "INSERT INTO Next_Of_Kin(stud_id, next_of_kin_name, next_of_kin_surname, next_of_kin_contact) "
                            "VALUES(%s, %s, %s, %s)",
                            (user_id, nok_name, nok_surname, nok_contact))
                        lifechoices_db.commit()
                        self.treeview_table.insert('', 'end', text='', values=(user_id, user_name, user_surname, user_contact, current_date, current_time,
                                                                               user_password))
                        messagebox.showinfo("Success", "Student Registered")
                        nameent.delete(0, END)
                        ident.delete(0, END)
                        surnameent.delete(0, END)
                        contactent.delete(0, END)
                        passwordent.delete(0, END)
                        frame.destroy()
                    elif insert_group_selector.get() == 'Admin':
                        my_cursor.execute("INSERT INTO Admin(admin_id, admin_name, admin_surname, admin_contact, admin_sign_in_date, admin_sign_in_time, admin_password) "
                                          "VALUES(%s, %s, %s, %s,%s, %s, %s)",(user_id, user_name, user_surname, user_contact, current_date, current_time,
                                                                                  user_password))
                        my_cursor.execute(
                            "INSERT INTO Next_Of_Kin(admin_id, next_of_kin_name, next_of_kin_surname, next_of_kin_contact) "
                            "VALUES(%s, %s, %s, %s)",
                            (user_id, nok_name, nok_surname, nok_contact))
                        lifechoices_db.commit()
                        self.treeview_table.insert('', 'end', text='', values=(user_id, user_name, user_surname, user_contact, current_date, current_time,
                                                                               user_password))
                        messagebox.showinfo("Success", "Admin Registered")
                        nameent.delete(0, END)
                        ident.delete(0, END)
                        surnameent.delete(0, END)
                        contactent.delete(0, END)
                        passwordent.delete(0, END)
                        frame.destroy()
                    elif insert_group_selector.get() == "Visitor":
                        my_cursor.execute(
                            "INSERT INTO Visitors(visitor_id, visitor_name, visitor_surname, visitor_contact, visitor_sign_in_date, visitor_sign_in_time, visitor_password) "
                            "VALUES(%s, %s, %s, %s,%s, %s, %s)",
                            (user_id, user_name, user_surname, user_contact, current_date, current_time,
                             user_password))
                        my_cursor.execute(
                            "INSERT INTO Next_Of_Kin(visitor_id, next_of_kin_name, next_of_kin_surname, next_of_kin_contact) "
                            "VALUES(%s, %s, %s, %s)",
                            (user_id, nok_name, nok_surname, nok_contact))
                        lifechoices_db.commit()
                        self.treeview_table.insert('', 'end', text='', values=(
                        user_id, user_name, user_surname, user_contact, current_date, current_time,
                        user_password))
                        messagebox.showinfo("Success", "visitor Registered")
                        nameent.delete(0, END)
                        ident.delete(0, END)
                        surnameent.delete(0, END)
                        contactent.delete(0, END)
                        passwordent.delete(0, END)
                        frame.destroy()
                except TypeError:
                    pass
        group_selector.bind("<<ComboboxSelected>>", add_data)
        ins_submit_btn = Button(frame, text="Submit Insert", command=add_data, bg='green', fg='black', padx=15,
                                pady=10, borderwidth=5, font=("Arial", 15))
        ins_submit_btn.place(relx=0.1, rely=0.82)

    # function to create frame for updating info in treeview as well as mysql
    def selected_data(self):
        item = self.treeview_table.focus()
        value = self.treeview_table.item(item, "values")
        frame2 = Frame(admin_page, width=600, height=400, bg="black")
        frame2.place(x=100, y=150)
        name_lbl = Label(frame2, text="Name:", bg="black", fg="white", font=("Arial", 15))
        name_lbl.place(relx=0.07, rely=0.2)
        name_ent = Entry(frame2, textvariable=name, font=("Arial", 15))
        name_ent.place(relx=0.35, rely=0.2)

        id_lbl = Label(frame2, text="ID number:", bg="black", fg="white", font=("Arial", 15))
        id_lbl.place(relx=0.07, rely=0.29)
        id_ent = Entry(frame2, textvariable=person_id, font=("Arial", 15))
        id_ent.place(relx=0.35, rely=0.29)

        surname_lbl = Label(frame2, text="Surname:", bg="black", fg="white", font=("Arial", 15))
        surname_lbl.place(relx=0.07, rely=0.38)
        surname_ent = Entry(frame2, textvariable=surname, font=("Arial", 15))
        surname_ent.place(relx=0.35, rely=0.38)

        contact_lbl = Label(frame2, text="Phone number:", bg="black", fg="white", font=("Arial", 15))
        contact_lbl.place(relx=0.07, rely=0.47)
        contact_ent = Entry(frame2, textvariable=contact, font=("Arial", 15))
        contact_ent.place(relx=0.35, rely=0.47)

        password_lbl = Label(frame2, text="Password:", bg="black", fg="white", font=("Arial", 15))
        password_lbl.place(relx=0.07, rely=0.56)
        password_ent = Entry(frame2, textvariable=password, font=("Arial", 15))
        password_ent.place(relx=0.35, rely=0.56)

        id_ent.insert(0, value[0])
        name_ent.insert(0, value[1])
        surname_ent.insert(0, value[2])
        contact_ent.insert(0, value[3])
        password_ent.insert(0, value[6])

        # function to close update frame
        def upd_destroy():
            MsgBox = messagebox.askquestion('Exit Application', 'Are you sure you want to exit the application',
                                            icon='warning')
            if MsgBox == 'yes':
                frame2.destroy()
            else:
                messagebox.showinfo('Return', 'Returning to main application')

        upd_cancel_btn = Button(frame2, text="Cancel Update", command=upd_destroy, bg='red', fg='black', padx=15, pady=10,
                                borderwidth=5)
        upd_cancel_btn.place(relx=0.5, rely=0.8)

        # function to update data in treeview as well as mysql tables
        def update_data():
            nonlocal item, value, name_ent, id_ent, surname_ent, contact_ent, password_ent
            user_name = name.get()
            user_id = person_id.get()
            user_surname = surname.get()
            user_password = password.get()
            user_contact = contact.get()
            if group_selector.get() == "Student":
                sql = "UPDATE Students SET stud_id=%s, stud_name=%s, stud_surname=%s, stud_contact=%s , stud_password=%s WHERE stud_id =%s"
                val = (user_id, user_name, user_surname, user_contact, user_password, value[0])
                my_cursor.execute(sql, val)
                lifechoices_db.commit()
                messagebox.showinfo("Success", "Student Data Updated\nPlease click on the search button in order to see updates")
                name_ent.delete(0, END)
                id_ent.delete(0, END)
                surname_ent.delete(0, END)
                contact_ent.delete(0, END)
                password_ent.delete(0, END)
                frame2.destroy()
            elif group_selector.get() == "Admin":
                sql = "UPDATE Admin SET admin_id=%s, admin_name=%s, admin_surname=%s, admin_contact=%s , admin_password=%s WHERE admin_id =%s"
                val = (user_id, user_name, user_surname, user_contact, user_password, value[0])
                my_cursor.execute(sql, val)
                lifechoices_db.commit()
                messagebox.showinfo("Success", "Admin Data Updated\nPlease click on the search button in order to see updates")
                name_ent.delete(0, END)
                id_ent.delete(0, END)
                surname_ent.delete(0, END)
                contact_ent.delete(0, END)
                password_ent.delete(0, END)
                frame2.destroy()
            elif group_selector.get() == "Visitor":
                sql = "UPDATE Visitors SET visitor_id=%s, visitor_name=%s, visitor__surname=%s, visitor_contact=%s , visitor_password=%s WHERE visitor_id =%s"
                val = (user_id, user_name, user_surname, user_contact, user_password, value[0])
                my_cursor.execute(sql, val)
                lifechoices_db.commit()
                messagebox.showinfo("Success", "Visitor Data Updated\nPlease click on the search button in order to see updates")
                name_ent.delete(0, END)
                id_ent.delete(0, END)
                surname_ent.delete(0, END)
                contact_ent.delete(0, END)
                password_ent.delete(0, END)
                frame2.destroy()
        group_selector.bind("<<ComboboxSelected>>", update_data)

        upd_submit_btn = Button(frame2, text="Submit Update", command=update_data, bg='green', fg='black',
                                padx=15, pady=10, borderwidth=5)
        upd_submit_btn.place(relx=0.15, rely=0.8)

    def count(self):
        count_frame = Frame(admin_page, width=600, height=400, bg="black")
        count_frame.place(relx=0.3, rely=0.2)

        self.heading = Label(count_frame, text="The number of people in the building:", font=("Arial", 18, "bold"),
                             bg="black", fg="white")
        self.heading.place(relx=0.03, rely=0.04)

        self.stud_count_lbl = Label(count_frame, text="Number of Students:", bg="black", fg="white", font=("Arial", 15))
        self.stud_count_lbl.place(relx=0.07, rely=0.2)
        self.stud_count_amount = Label(count_frame, bg="grey", fg="white", font=("Arial", 15), width=20)
        self.stud_count_amount.place(relx=0.45, rely=0.2)

        self.admin_count_lbl = Label(count_frame, text="Number of Admin:", bg="black", fg="white", font=("Arial", 15))
        self.admin_count_amount = Label(count_frame, bg="grey", fg="white", font=("Arial", 15), width=20)
        self.admin_count_lbl.place(relx=0.07, rely=0.4)
        self.admin_count_amount.place(relx=0.45, rely=0.4)

        self.visitor_count_lbl = Label(count_frame, text="Number of Visitors:", bg="black", fg="white", font=("Arial", 15))
        self.visitor_count_lbl.place(relx=0.07, rely=0.6)
        self.visitor_count_amount = Label(count_frame, bg="grey", fg="white", font=("Arial", 15), width=20)
        self.visitor_count_amount.place(relx=0.45, rely=0.6)

        self.total_lbl = Label(count_frame, text="Total:", bg="black", fg="white", font=("Arial", 18))
        self.total_lbl.place(relx=0.07, rely=0.8)
        self.total_amount = Label(count_frame, bg="grey", fg="white", font=("Arial", 15), width=20)
        self.total_amount.place(relx=0.45, rely=0.8)

        my_cursor.execute("SELECT COUNT('stud_sign_in_time') FROM Students WHERE stud_sign_in_date='" + current_date + "'")
        stud_result = my_cursor.fetchall()

        self.stud_count_amount.config(text=stud_result)

        my_cursor.execute(
            "SELECT COUNT(admin_sign_in_time) FROM Admin WHERE admin_sign_in_date='" + current_date + "'")
        admin_result = my_cursor.fetchall()

        self.admin_count_amount.config(text=admin_result)

        my_cursor.execute(
            "SELECT COUNT('visitor_sign_in_time') FROM Visitors WHERE visitor_sign_in_date='" + current_date + "'")
        visitor_result = my_cursor.fetchall()

        self.visitor_count_amount.config(text=visitor_result)

        # total = int(float(stud_result)) + int(float(admin_result)) + int(float(visitor_result))
        total = map(float, stud_result[0].split("*")) + map(float, admin_result[0].split("*"))
        self.total_amount.config(text=total)


    # function for admin to sign out and record time and date
    def sign_out(self):
        pass
    #     so_date = datetime.now().date().strftime('%Y-%m-%d')
    #     so_time = datetime.now().time().strftime('%H:%M:%S')
    #     date_signoutsql = "UPDATE Admin SET admin_sign_out_date=%s WHERE admin_id='" \
    #                       + self.id_entry.get() + "' AND admin_password='" + self.password_entry.get() + "'"
    #     date_signoutval = [so_date]
    #     time_signoutsql = "UPDATE Admin SET admin_sign_out_time=%s WHERE admin_id='" \
    #                       + self.id_entry.get() + "' AND admin_password='" + self.password_entry.get() + "'"
    #     time_signoutval = [so_time]
    #     my_cursor.execute(date_signoutsql, date_signoutval)
    #     my_cursor.execute(time_signoutsql, time_signoutval)
    #     lifechoices_db.commit()
    #     messagebox.showinfo('Sign Out successful', 'Enjoy the rest of your day!')


admin_control = AdminAccess()
admin_page.mainloop()
#
#
# admin_logging_in = AdminLoginPage()
# admin_login.mainloop()
