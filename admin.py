from tkinter import *
from tkinter import ttk
import mysql.connector
from tkinter import messagebox
from PIL import Image, ImageTk
import rsaidnumber
from datetime import datetime

admin_login = Tk()
admin_login.title("Admin Login")
admin_login.config(bg="#1a1a18")
admin_login.geometry("800x900")

# connecting mysql to python
lifechoices_db = mysql.connector.connect(user='lifechoices', password='8-2fermENt2020', host='127.0.0.1',
                                         database='Lifechoices_Online', auth_plugin='mysql_native_password')
my_cursor = lifechoices_db.cursor(buffered=True)

# for exact date and time
current_date = datetime.now().date().strftime("%Y-%m-%d")
current_time = datetime.now().time().strftime("%H:%M:%S")

date = datetime.today().date().strftime("%H:%M:%S")

# adding image
canvas = Canvas(admin_login, width=400, height=400, bg="#1a1a18", borderwidth=0, highlightthickness=0)
canvas.place(relx=0.25, rely=0.05)
img_logo = ImageTk.PhotoImage(Image.open("lclogo.png"))
canvas.create_image(200, 5, anchor=N, image=img_logo)

admin_heading = Label(admin_login, text="Welcome Admin!", bg="#1a1a18", fg="white", font=("Arial", 30, "bold"))
admin_heading.place(relx=0.3, rely=0.47)


class AdminLoginPage(object):
    def __init__(self):
        self.instruction_heading = Label(admin_login, text="Please enter your:", fg="#7bfa05",
                                         bg="#1a1a18", font=("Arial", 21, "bold"))
        self.instruction_heading.place(relx=0.3, rely=0.58)
        # labels and entries
        self.id_label = Label(admin_login, text="ID number:", fg="white", bg="#1a1a18", font=("Arial", 15,
                                                                                              "bold"))
        self.id_label.place(relx=0.3, rely=0.65)
        self.id_entry = Entry(admin_login, font=("Arial", 14))
        self.id_entry.place(relx=0.45, rely=0.65)

        self.password_label = Label(admin_login, text="Password:", fg="white", bg="#1a1a18", font=("Arial", 15,
                                                                                                    "bold"))
        self.password_label.place(relx=0.3, rely=0.72)
        self.password_entry = Entry(admin_login, font=("Arial", 14), show='*')
        self.password_entry.place(relx=0.45, rely=0.72)
        # buttons
        self.login_btn = Button(admin_login, text="Login", padx=40, pady=10, borderwidth=5, fg="black", bg="#71f72a",
                                font=("Arial", 13, "bold"), command=self.login)
        self.login_btn.place(relx=0.53, rely=0.89)

        self.clear_btn = Button(admin_login, text="Clear", padx=40, pady=10, borderwidth=5, fg="black",
                                bg="#fff", font=("Arial", 13, "bold"), command=self.clear)
        self.clear_btn.place(relx=0.3, rely=0.89)
        register_btn = Button(admin_login, text="Register New User", padx=79, pady=10, borderwidth=5, fg="black",
                              bg="#71f72a",
                              font=("Arial", 13, "bold"), command=self.register)
        register_btn.place(relx=0.3, rely=0.8)

    # function for admin to log in
    def login(self):
        try:
            my_cursor.execute('SELECT * FROM Admin WHERE admin_id = "' + self.id_entry.get() + '"')
            results = my_cursor.fetchall()
            if results == []:
                messagebox.showerror("Login Unsuccessful",
                                     "The ID number entered is incorrect or does not exist in our Admin database.\n\nIf the issue persists, please see reception!")
            elif str(self.id_entry.get()) == results[0][0] and str(self.password_entry.get()) == results[0][6]:
                self.admin_sign_in()
            elif str(self.id_entry.get()) == results[0][0] and str(self.password_entry.get()) != results[0][6]:
                messagebox.showerror("Error", "Password is incorrect.")
                self.password_entry.delete(0, END)
        except ValueError:
            messagebox.showerror("Error", "Please ensure that your ID consists of digits.")

    # function for admin sign in time and date to be updated
    def admin_sign_in(self):
        try:
            date_data = "UPDATE Admin SET admin_sign_in_date=%s, admin_sign_out_date=NULL WHERE admin_id='" + self.id_entry.get() \
                        + "' AND admin_password = '" + self.password_entry.get() + "'"
            date_val = [current_date]
            time_data = "UPDATE Admin SET admin_sign_in_time=%s , admin_sign_out_time=NULL WHERE admin_id='" + self.id_entry.get() \
                        + "' AND admin_password = '" + self.password_entry.get() + "'"
            time_val = [current_time]
            my_cursor.execute(date_data, date_val)
            my_cursor.execute(time_data, time_val)
            lifechoices_db.commit()
            messagebox.showinfo("Login Successful", "Enjoy your day!")
            admin_login.destroy()
            self.admin_page()
        except TypeError:
            pass

    # function to register admin user
    def register(self):
        admin_login.destroy()
        import main

    # function to clear
    def clear(self):
        self.id_entry.delete(0, END)
        self.password_entry.delete(0, END)
        # group_selector.set("Select One")

    # function to open admin page and have access to its functions
    def admin_page(self):
        admin_page = Tk()
        admin_page.title("Admin Login")
        admin_page.config(bg="white")
        admin_page.geometry("1450x900")
        treeview_frame = Frame(admin_page, bg="#a3ff52", highlightbackground="white", highlightthickness=5, width=1270, height=700)
        treeview_frame.place(relx=0.06, rely=0.18)

        # declaring text variables
        name = StringVar()
        person_id = StringVar()
        surname = StringVar()
        password = StringVar()
        contact = StringVar()
        adm_id = StringVar()
        stud_id = StringVar()
        visi_id = StringVar()
        nextOfKin_name = StringVar()
        nextOfKin_surname = StringVar()
        nextOfKin_contact = StringVar()

        # adding image
        access_canvas = Canvas(admin_page, width=200, height=150, bg="white", borderwidth=0, highlightthickness=0)
        access_canvas.place(relx=0.05, rely=0)
        access_img_logo = ImageTk.PhotoImage(Image.open("Life-Choices-150x150.jpg"))
        access_canvas.create_image(120, 0, anchor=N, image=access_img_logo)

        # adding image
        access_canvas2 = Canvas(admin_page, width=200, height=150, bg="white", borderwidth=0, highlightthickness=0)
        access_canvas2.place(relx=0.77, rely=0)
        access_img_logo2 = ImageTk.PhotoImage(Image.open("Life-Choices-150x150.jpg"))
        access_canvas2.create_image(120, 0, anchor=N, image=access_img_logo2)

        # combo box
        group = StringVar(treeview_frame)
        group_list = ['Student', 'Admin', 'Visitor']
        group_selector = ttk.Combobox(treeview_frame, textvariable=group.set, font=("Arial", 17), width=19)
        group_selector.set("Select One")
        group_selector['values'] = group_list
        group_selector['state'] = 'readonly'
        group_selector.place(relx=0.015, rely=0.045)

        class AdminAccess(object):
            def __init__(self):
                self.search_btn = Button(treeview_frame, text="Search", command=self.group_treeview, pady=5, padx=10,
                                         borderwidth=5, font=("Arial", 15))
                self.search_btn.place(relx=0.24, rely=0.03)
                self.nokSearch_btn = Button(treeview_frame, text="Next of Kin Search", command=self.nok_treeview, pady=5, padx=10,
                                            borderwidth=5, font=("Arial", 15))
                self.nokSearch_btn.place(relx=0.015, rely=0.47)
                self.heading = Label(admin_page, text="Admin Page", font=("Arial", 100, "bold"), bg="white", fg="grey")
                self.heading.place(relx=0.23, rely=0)

                # treeview for users
                self.treeview_table = ttk.Treeview(treeview_frame, columns=(1, 2, 3, 4, 5, 6, 7, 8, 9), show="headings")
                self.treeview_table.place(relx=0.015, rely=0.13)
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

                self.treeview_table.heading('#0', text="", anchor=CENTER)
                self.treeview_table.heading(1, text='ID', anchor=CENTER)
                self.treeview_table.heading(2, text='Name', anchor=CENTER)
                self.treeview_table.heading(3, text='Surname', anchor=CENTER)
                self.treeview_table.heading(4, text='Contact', anchor=CENTER)
                self.treeview_table.heading(5, text='Sign in Date', anchor=CENTER)
                self.treeview_table.heading(6, text='Sign in Time', anchor=CENTER)
                self.treeview_table.heading(7, text='Password', anchor=CENTER)
                self.treeview_table.heading(8, text='Sign out Date', anchor=CENTER)
                self.treeview_table.heading(9, text='Sign out Time', anchor=CENTER)

                # treeview for next of kin details
                self.nokTreeview_table = ttk.Treeview(treeview_frame, columns=(1, 2, 3, 4, 5, 6), show="headings")
                self.nokTreeview_table.place(relx=0.015, rely=0.55)
                self.nokTreeview_table.column('#0', width=0, stretch=NO)
                self.nokTreeview_table.column(1, anchor=CENTER, width=201)
                self.nokTreeview_table.column(2, anchor=CENTER, width=201)
                self.nokTreeview_table.column(3, anchor=CENTER, width=201)
                self.nokTreeview_table.column(4, anchor=CENTER, width=202)
                self.nokTreeview_table.column(5, anchor=CENTER, width=202)
                self.nokTreeview_table.column(6, anchor=CENTER, width=202)

                self.nokTreeview_table.heading('#0', text='', anchor=CENTER)
                self.nokTreeview_table.heading(1, text='Admin ID', anchor=CENTER)
                self.nokTreeview_table.heading(2, text='Student ID', anchor=CENTER)
                self.nokTreeview_table.heading(3, text='Visitor ID', anchor=CENTER)
                self.nokTreeview_table.heading(4, text='Next of Kin Name', anchor=CENTER)
                self.nokTreeview_table.heading(5, text='Next of Kin Surname', anchor=CENTER)
                self.nokTreeview_table.heading(6, text='Next of Kin Contact', anchor=CENTER)

                delete_entries = Button(treeview_frame, text="Delete", bg="red", fg="black", command=self.delete, pady=5, padx=10,
                                        borderwidth=5, font=("Arial", 15))
                delete_entries.place(relx=0.9, rely=0.03)
                insert_entries = Button(treeview_frame, text="Insert", bg="#83f740", fg="black", command=lambda: self.insert_data(),
                                        pady=5, padx=10,
                                        borderwidth=5, font=("Arial", 15))
                insert_entries.place(relx=0.58, rely=0.03)
                update_entries = Button(treeview_frame, text="Update", bg="#d5f538", fg="black", command=lambda: self.selected_data(),
                                        pady=5, padx=10,
                                        borderwidth=5, font=("Arial", 15))
                update_entries.place(relx=0.74, rely=0.03)
                nokUpd_entries = Button(treeview_frame, text="Next of Kin Update", bg="#d5f538", fg="black", command=lambda: self.nokSelected_data(),
                                        pady=5, padx=10,
                                        borderwidth=5, font=("Arial", 15))
                nokUpd_entries.place(relx=0.58, rely=0.47)
                nokDelete_entries = Button(treeview_frame, text="Delete Next Of Kin", bg="red", fg="black", command=self.nokDelete, pady=5,
                                        padx=10,
                                        borderwidth=5, font=("Arial", 15))
                nokDelete_entries.place(relx=0.82, rely=0.47)
                in_count_btn = Button(admin_page, text="Signed In", command=self.in_count, bg='black', fg='white',
                                      pady=5, padx=10, borderwidth=5, font=("Arial", 20))
                in_count_btn.place(relx=0.075, rely=0.87)
                out_count_btn = Button(admin_page, text="Signed Out", command=self.out_count, bg='black', fg='white',
                                       pady=5, padx=10, borderwidth=5, font=("Arial", 20))
                out_count_btn.place(relx=0.425, rely=0.87)
                sign_out_btn = Button(admin_page, text="Admin Sign Out", command=self.sign_out, bg='black', fg='white',
                                      pady=5, padx=10, borderwidth=5, font=("Arial", 20))
                sign_out_btn.place(relx=0.75, rely=0.87)

            # function to display data on user treeview from mysql tables
            def group_treeview(self):
                try:
                    # to clear previous entries on treeview
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
                        for i in rows:
                            self.treeview_table.insert("", 'end', values=i)
                    else:
                        messagebox.showerror("Selection Error", "Please select the group.")
                except TypeError:
                    pass

            # function display next of kin details on treeview
            def nok_treeview(self):
                try:
                    for x in self.nokTreeview_table.get_children():
                        self.nokTreeview_table.delete(x)
                    if group_selector.get() == 'Student':
                        lifechoices_db = mysql.connector.connect(user='lifechoices', password='8-2fermENt2020',
                                                                 host='127.0.0.1',
                                                                 database='Lifechoices_Online',
                                                                 auth_plugin='mysql_native_password')
                        my_cursor = lifechoices_db.cursor()
                        nokSql = "SELECT * FROM Next_Of_Kin"
                        my_cursor.execute(nokSql)
                        rows = my_cursor.fetchall()
                        for x in rows:
                            self.nokTreeview_table.insert("", 'end', values=x)
                        messagebox.showinfo("Students ONLY",
                                            "Please note that you are ONLY able to edit information with a student ID!\n\nAny other user updates will be null and void.")
                    elif group_selector.get() == 'Admin':
                        lifechoices_db = mysql.connector.connect(user='lifechoices', password='8-2fermENt2020',
                                                                 host='127.0.0.1',
                                                                 database='Lifechoices_Online',
                                                                 auth_plugin='mysql_native_password')
                        my_cursor = lifechoices_db.cursor()
                        nokSql = "SELECT * FROM Next_Of_Kin"
                        my_cursor.execute(nokSql)
                        rows = my_cursor.fetchall()
                        for x in rows:
                            self.nokTreeview_table.insert("", 'end', values=x)
                        messagebox.showinfo("Admin ONLY",
                                            "Please note that you are ONLY able to edit information with an admin ID!\n\nAny other user updates will be null and void.")
                    elif group_selector.get() == 'Visitor':
                        lifechoices_db = mysql.connector.connect(user='lifechoices', password='8-2fermENt2020', host='127.0.0.1',
                                                                 database='Lifechoices_Online', auth_plugin='mysql_native_password')
                        my_cursor = lifechoices_db.cursor()
                        nokSql = "SELECT * FROM Next_Of_Kin"
                        my_cursor.execute(nokSql)
                        rows = my_cursor.fetchall()
                        for x in rows:
                            self.nokTreeview_table.insert("", 'end', values=x)
                        messagebox.showinfo("Visitors ONLY", "Please note that you are ONLY able to edit information with a visitor ID!\nAny other user updates will be null and void.")
                    else:
                        messagebox.showerror("Selection Error", "Please select the group")
                except TypeError:
                    pass

            # function to delete data in user treeview and next of kin treeview as well as corresponding mysql tables
            def delete(self):
                if group_selector.get() == "Student":
                    item = self.treeview_table.selection()[0]
                    selected_item = self.treeview_table.item(item)['values'][0]
                    remove_nokDetails = "DELETE FROM Next_Of_Kin WHERE stud_id=%s"
                    remove_student = "DELETE FROM Students WHERE stud_id=%s"
                    selected_data = (selected_item,)
                    my_cursor.execute(remove_nokDetails, selected_data)
                    my_cursor.execute(remove_student, selected_data)
                    lifechoices_db.commit()
                    self.treeview_table.delete(item)
                    # self.nokTreeview_table.delete(item)
                    messagebox.showinfo("Success", "Student Data Removed.\nPlease click the 'Next of Kin Search' button to view the updates.")
                elif group_selector.get() == 'Admin':
                    item = self.treeview_table.selection()[0]
                    selected_item = self.treeview_table.item(item)['values'][0]
                    remove_nokDetails = "DELETE FROM Next_Of_Kin WHERE admin_id=%s"
                    remove_admin = "DELETE FROM Admin WHERE admin_id=%s"
                    selected_data = (selected_item,)
                    my_cursor.execute(remove_nokDetails, selected_data)
                    my_cursor.execute(remove_admin, selected_data)
                    lifechoices_db.commit()
                    self.treeview_table.delete(item)
                    # self.nokTreeview_table.delete(item)
                    messagebox.showinfo("Success", "Admin Data Removed.\nPlease click the 'Next of Kin Search' button to view the updates.")
                elif group_selector.get() == 'Visitor':
                    item = self.treeview_table.selection()[0]
                    selected_item = self.treeview_table.item(item)['values'][0]
                    remove_nokDetails = "DELETE FROM Next_Of_Kin WHERE visitor_id=%s"
                    remove_visitor = "DELETE FROM Visitors WHERE visitor_id=%s"
                    selected_data = (selected_item,)
                    my_cursor.execute(remove_nokDetails, selected_data)
                    my_cursor.execute(remove_visitor, selected_data)
                    lifechoices_db.commit()
                    self.treeview_table.delete(item)
                    # self.nokTreeview_table.delete(item)
                    messagebox.showinfo("Success", "Visitor Data Removed.\nPlease click the 'Next of Kin Search' button to view the updates.")
                group_selector.bind("<<ComboboxSelected>>", self.delete)

            # function to create frame in order to insert users
            def insert_data(self):
                insert_frame = Frame(admin_page, width=700, height=600, bg="black")
                insert_frame.place(relx=0.3, rely=0.2)
                insert_heading = Label(insert_frame, text="Insert Details:", bg="black", fg="white", font=("Arial", 20, "bold"))
                insert_heading.place(relx=0.05, rely=0.05)
                namelbl= Label(insert_frame, text="Name:", bg="black", fg="white", font=("Arial", 15))
                nameent = Entry(insert_frame, textvariable=name, width=25, font=("Arial", 15))
                namelbl.place(relx=0.1, rely=0.2)
                nameent.place(relx=0.45, rely=0.2)
                # combobox
                insert_group = StringVar(insert_frame)
                insert_group_list = ['Student', 'Admin', 'Visitor']
                insert_group_selector = ttk.Combobox(insert_frame, textvariable=insert_group.set, font=("Arial", 17), width=20)
                insert_group_selector.set("Select One")
                insert_group_selector['values'] = insert_group_list
                insert_group_selector['state'] = 'readonly'
                insert_group_selector.place(relx=0.45, rely=0.13)
                group_label = Label(insert_frame, text="Group:", bg="black", fg="white", font=("Arial", 15))
                group_label.place(relx=0.1, rely=0.13)

                idlbl = Label(insert_frame, text="ID number:", bg="black", fg="white", font=("Arial", 15))
                ident = Entry(insert_frame, textvariable=person_id, width=25, font=("Arial", 15))
                idlbl.place(relx=0.1, rely=0.34)
                ident.place(relx=0.45, rely=0.34)

                surnamelbl = Label(insert_frame, text="Surname:", bg="black", fg="white", font=("Arial", 15))
                surnamelbl.place(relx=0.1, rely=0.27)
                surnameent = Entry(insert_frame, textvariable=surname, width=25, font=("Arial", 15))
                surnameent.place(relx=0.45, rely=0.27)

                contactlbl = Label(insert_frame, text="Phone number:", bg="black", fg="white", font=("Arial", 15))
                contactlbl.place(relx=0.1, rely=0.41)
                contactent = Entry(insert_frame, textvariable=contact, width=25, font=("Arial", 15))
                contactent.place(relx=0.45, rely=0.41)

                passwordlbl = Label(insert_frame, text="Password:", bg="black", fg="white", font=("Arial", 15))
                passwordlbl.place(relx=0.1, rely=0.48)
                passwordent = Entry(insert_frame, textvariable=password, width=25, font=("Arial", 15))
                passwordent.place(relx=0.45, rely=0.48)

                nextOfKin_namelbl = Label(insert_frame, text="Next Of Kin Name:", bg="black", fg="white", font=("Arial", 15))
                nextOfKin_nameent = Entry(insert_frame, textvariable=nextOfKin_name, width=25, font=("Arial", 15))
                nextOfKin_namelbl.place(relx=0.1, rely=0.55)
                nextOfKin_nameent.place(relx=0.45, rely=0.55)

                nextOfKin_surnamelbl = Label(insert_frame, text="Next Of Kin Surname:", bg="black", fg="white", font=("Arial", 15))
                nextOfKin_surnamelbl.place(relx=0.1, rely=0.62)
                nextOfKin_surnameent = Entry(insert_frame, textvariable=nextOfKin_surname, width=25, font=("Arial", 15))
                nextOfKin_surnameent.place(relx=0.45, rely=0.62)

                nextOfKin_contactlbl = Label(insert_frame, text="Next Of Kin Contact:", bg="black", fg="white", font=("Arial", 15))
                nextOfKin_contactlbl.place(relx=0.1, rely=0.69)
                nextOfKin_contactent = Entry(insert_frame, textvariable=nextOfKin_contact, width=25, font=("Arial", 15))
                nextOfKin_contactent.place(relx=0.45, rely=0.69)

                # function to destroy insert frame
                def ins_destroy():
                    MsgBox2 = messagebox.askquestion('Exit Application', 'Are you sure you want to exit the application?',
                                                     icon='warning')
                    if MsgBox2 == 'yes':
                        insert_frame.destroy()
                    else:
                        messagebox.showinfo('Return', 'Returning to the application.')

                ins_cancel_btn = Button(insert_frame, text="Cancel Insert", command=ins_destroy, bg='red', fg='black', padx=15, pady=10,
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
                    # if user_name == "" or user_surname == "" or nok_name == "" or nok_surname == "":
                    #     messagebox.showerror("Entry Error", "Please fill in all the required information")
                    if nameent.get() == "":
                        messagebox.showerror("Entry Error", "Please enter the user's name.")
                    elif surnameent.get() == "":
                        messagebox.showerror("Entry Error", "Please enter the user's surname.")
                    elif passwordent.get() == "":
                        messagebox.showerror("Entry Error", "Please enter the user's password.")
                    elif nextOfKin_nameent.get() == "":
                        messagebox.showerror("Entry Error", "Please enter the user's Next of Kin's name.")
                    elif nextOfKin_surnameent.get() == "":
                        messagebox.showerror("Entry Error", "Please enter the user's Next of Kin's surname.")
                    else:
                        try:
                            # id validation
                            def valid_id_check():
                                try:
                                    valid_user_id = user_id
                                    while valid_user_id:
                                        id_number = rsaidnumber.parse(valid_user_id)
                                        valid_id = id_number
                                        while valid_id:
                                            return 1
                                except ValueError:
                                    messagebox.showerror("Invalid ID", "\nPlease enter a valid South African ID "
                                                                      "number that consists of 13"
                                                                      " digits.")

                            # cell validation
                            def cell_num_validation():
                                try:
                                    tel = user_contact
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

                            # next of kin contact validation function
                            def next_of_kin_cell():
                                try:
                                    next_of_kin_tel = nok_contact
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
                                        messagebox.showinfo("Success", "Student Registered!")
                                        nameent.delete(0, END)
                                        ident.delete(0, END)
                                        surnameent.delete(0, END)
                                        contactent.delete(0, END)
                                        passwordent.delete(0, END)
                                        nextOfKin_nameent.delete(0, END)
                                        nextOfKin_surnameent.delete(0, END)
                                        nextOfKin_contactent.delete(0, END)
                                        insert_frame.destroy()
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
                                        messagebox.showinfo("Success", "Admin Registered!")
                                        nameent.delete(0, END)
                                        ident.delete(0, END)
                                        surnameent.delete(0, END)
                                        contactent.delete(0, END)
                                        passwordent.delete(0, END)
                                        nextOfKin_nameent.delete(0, END)
                                        nextOfKin_surnameent.delete(0, END)
                                        nextOfKin_contactent.delete(0, END)
                                        insert_frame.destroy()
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
                                        messagebox.showinfo("Success", "Visitor Registered!")
                                        nameent.delete(0, END)
                                        ident.delete(0, END)
                                        surnameent.delete(0, END)
                                        contactent.delete(0, END)
                                        passwordent.delete(0, END)
                                        nextOfKin_nameent.delete(0, END)
                                        nextOfKin_surnameent.delete(0, END)
                                        nextOfKin_contactent.delete(0, END)
                                        insert_frame.destroy()
                                    else:
                                        messagebox.showerror("Selection Error", "Please select a group.")
                                except TypeError:
                                    pass
                        except ValueError:
                            messagebox.showerror("Error", "Please ensure the name and surname fields only consist of letters and not digits.")
                group_selector.bind("<<ComboboxSelected>>", add_data)
                ins_submit_btn = Button(insert_frame, text="Submit Insert", command=add_data, bg='green', fg='black', padx=15,
                                        pady=10, borderwidth=5, font=("Arial", 15))
                ins_submit_btn.place(relx=0.1, rely=0.82)

            # function to create frame for updating USER info in treeview as well as mysql
            def selected_data(self):
                try:
                    item = self.treeview_table.focus()
                    value = self.treeview_table.item(item, "values")
                    update_frame = Frame(admin_page, width=600, height=400, bg="black")
                    update_frame.place(relx=0.3, rely=0.2)
                    update_heading = Label(update_frame, text="Update Details:", bg="black", fg="white", font=("Arial", 20, "bold"))
                    update_heading.place(relx=0.05, rely=0.05)
                    name_lbl = Label(update_frame, text="Name:", bg="black", fg="white", font=("Arial", 15))
                    name_lbl.place(relx=0.1, rely=0.2)
                    name_ent = Entry(update_frame, textvariable=name, font=("Arial", 15))
                    name_ent.place(relx=0.45, rely=0.2)

                    id_lbl = Label(update_frame, text="ID number:", bg="black", fg="white", font=("Arial", 15))
                    id_lbl.place(relx=0.1, rely=0.38)
                    id_ent = Entry(update_frame, textvariable=person_id, font=("Arial", 15))
                    id_ent.place(relx=0.45, rely=0.38)

                    surname_lbl = Label(update_frame, text="Surname:", bg="black", fg="white", font=("Arial", 15))
                    surname_lbl.place(relx=0.1, rely=0.29)
                    surname_ent = Entry(update_frame, textvariable=surname, font=("Arial", 15))
                    surname_ent.place(relx=0.45, rely=0.29)

                    contact_lbl = Label(update_frame, text="Phone number:", bg="black", fg="white", font=("Arial", 15))
                    contact_lbl.place(relx=0.1, rely=0.47)
                    contact_ent = Entry(update_frame, textvariable=contact, font=("Arial", 15))
                    contact_ent.place(relx=0.45, rely=0.47)

                    password_lbl = Label(update_frame, text="Password:", bg="black", fg="white", font=("Arial", 15))
                    password_lbl.place(relx=0.1, rely=0.56)
                    password_ent = Entry(update_frame, textvariable=password, font=("Arial", 15))
                    password_ent.place(relx=0.45, rely=0.56)

                    upd_cancel_btn1 = Button(update_frame, text="Cancel Update", command=lambda: update_frame.destroy(), bg='red', fg='black',
                                            padx=15, pady=10,
                                            borderwidth=5)
                    upd_cancel_btn1.place(relx=0.5, rely=0.8)

                    id_ent.insert(0, value[0])
                    name_ent.insert(0, value[1])
                    surname_ent.insert(0, value[2])
                    contact_ent.insert(0, value[3])
                    password_ent.insert(0, value[6])

                    # function to close update frame
                    def upd_destroy():
                        MsgBox = messagebox.askquestion('Exit Application', 'Are you sure you want to exit the application?',
                                                        icon='warning')
                        if MsgBox == 'yes':
                            name_ent.delete(0, END)
                            id_ent.delete(0, END)
                            surname_ent.delete(0, END)
                            contact_ent.delete(0, END)
                            password_ent.delete(0, END)
                            update_frame.destroy()
                        else:
                            messagebox.showinfo('Return', 'Returning to the application.')

                    upd_cancel_btn = Button(update_frame, text="Cancel Update", command=upd_destroy, bg='red', fg='black', padx=15, pady=10,
                                            borderwidth=5)
                    upd_cancel_btn.place(relx=0.5, rely=0.8)

                    # function to update data in USER treeview as well as mysql tables
                    def update_data():
                        nonlocal item, value, name_ent, id_ent, surname_ent, contact_ent, password_ent
                        user_name = name.get()
                        user_id = person_id.get()
                        user_surname = surname.get()
                        user_password = password.get()
                        user_contact = contact.get()
                        try:
                            if group_selector.get() == "Student":
                                sql = "UPDATE Students SET stud_id=%s, stud_name=%s, stud_surname=%s, stud_contact=%s , stud_password=%s WHERE stud_id =%s"
                                val = (user_id, user_name, user_surname, user_contact, user_password, value[0])
                                my_cursor.execute(sql, val)
                                lifechoices_db.commit()
                                messagebox.showinfo("Success",
                                                    "Student Data Updated\nPlease click on the 'Search' button in order to see updates")
                                name_ent.delete(0, END)
                                id_ent.delete(0, END)
                                surname_ent.delete(0, END)
                                contact_ent.delete(0, END)
                                password_ent.delete(0, END)
                                update_frame.destroy()
                            elif group_selector.get() == "Admin":
                                sql = "UPDATE Admin SET admin_id=%s, admin_name=%s, admin_surname=%s, admin_contact=%s , admin_password=%s WHERE admin_id =%s"
                                val = (user_id, user_name, user_surname, user_contact, user_password, value[0])
                                my_cursor.execute(sql, val)
                                lifechoices_db.commit()
                                messagebox.showinfo("Success",
                                                    "Admin Data Updated\nPlease click on the 'Search' button in order to see updates")
                                name_ent.delete(0, END)
                                id_ent.delete(0, END)
                                surname_ent.delete(0, END)
                                contact_ent.delete(0, END)
                                password_ent.delete(0, END)
                                update_frame.destroy()
                            elif group_selector.get() == "Visitor":
                                sql = "UPDATE Visitors SET visitor_id=%s, visitor_name=%s, visitor_surname=%s, visitor_contact=%s , visitor_password=%s WHERE visitor_id =%s"
                                val = (user_id, user_name, user_surname, user_contact, user_password, value[0])
                                my_cursor.execute(sql, val)
                                lifechoices_db.commit()
                                messagebox.showinfo("Success",
                                                    "Visitor Data Updated\nPlease click on the 'Search' button in order to see updates")
                                name_ent.delete(0, END)
                                id_ent.delete(0, END)
                                surname_ent.delete(0, END)
                                contact_ent.delete(0, END)
                                password_ent.delete(0, END)
                                update_frame.destroy()
                        except TypeError:
                            pass

                    upd_submit_btn = Button(update_frame, text="Submit Update", command=update_data, bg='green', fg='black',
                                            padx=15, pady=10, borderwidth=5)
                    upd_submit_btn.place(relx=0.15, rely=0.8)
                except IndexError:
                    messagebox.showerror('Error', 'Please select the data from the table when trying to update details.')

            # function to create frame for updating info in NEXT OF KIN treeview as well as mysql
            def nokSelected_data(self):
                try:
                    nok_item = self.nokTreeview_table.focus()
                    nok_value = self.nokTreeview_table.item(nok_item, "values")
                    nokUpd_frame = Frame(admin_page, width=600, height=400, bg="black")
                    nokUpd_frame.place(relx=0.3, rely=0.2)
                    nokUpdate_heading = Label(nokUpd_frame, text="Update Details:", bg="black", fg="white", font=("Arial", 20, "bold"))
                    nokUpdate_heading.place(relx=0.05, rely=0.05)
                    adminId_lbl = Label(nokUpd_frame, text="Admin ID:", bg="black", fg="white", font=("Arial", 15))
                    adminId_lbl.place(relx=0.1, rely=0.2)
                    adminId_ent = Entry(nokUpd_frame, textvariable=adm_id, font=("Arial", 15))
                    adminId_ent.place(relx=0.45, rely=0.2)

                    studentId_lbl = Label(nokUpd_frame, text="Student ID:", bg="black", fg="white", font=("Arial", 15))
                    studentId_lbl .place(relx=0.1, rely=0.38)
                    studentId_ent = Entry(nokUpd_frame, textvariable=stud_id, font=("Arial", 15))
                    studentId_ent.place(relx=0.45, rely=0.38)

                    visitorId_lbl = Label(nokUpd_frame, text="Visitor ID:", bg="black", fg="white", font=("Arial", 15))
                    visitorId_lbl.place(relx=0.1, rely=0.29)
                    visitorId_ent = Entry(nokUpd_frame, textvariable=visi_id, font=("Arial", 15))
                    visitorId_ent.place(relx=0.45, rely=0.29)

                    nextOfKin_name_lbl = Label(nokUpd_frame, text="Next Of Kin Name:", bg="black", fg="white", font=("Arial", 15))
                    nextOfKin_name_ent = Entry(nokUpd_frame, textvariable=nextOfKin_name, font=("Arial", 15))
                    nextOfKin_name_lbl.place(relx=0.1, rely=0.47)
                    nextOfKin_name_ent.place(relx=0.45, rely=0.47)

                    nextOfKin_surname_lbl = Label(nokUpd_frame, text="Next Of Kin Surname:", bg="black", fg="white",
                                                  font=("Arial", 15))
                    nextOfKin_surname_lbl.place(relx=0.1, rely=0.56)
                    nextOfKin_surname_ent = Entry(nokUpd_frame, textvariable=nextOfKin_surname, font=("Arial", 15))
                    nextOfKin_surname_ent.place(relx=0.45, rely=0.56)

                    nextOfKin_contact_lbl = Label(nokUpd_frame, text="Next Of Kin Contact:", bg="black", fg="white",
                                                  font=("Arial", 15))
                    nextOfKin_contact_lbl.place(relx=0.1, rely=0.65)
                    nextOfKin_contact_ent = Entry(nokUpd_frame, textvariable=nextOfKin_contact, font=("Arial", 15))
                    nextOfKin_contact_ent.place(relx=0.45, rely=0.65)

                    nokUpd_cancel_btn = Button(nokUpd_frame, text="Cancel Update", command=lambda: nokUpd_frame.destroy(), bg='red',
                                               fg='black', padx=15,
                                               pady=10,
                                               borderwidth=5)
                    nokUpd_cancel_btn.place(relx=0.5, rely=0.8)

                    adminId_ent.insert(0, nok_value[0])
                    studentId_ent.insert(0, nok_value[1])
                    visitorId_ent.insert(0, nok_value[2])
                    nextOfKin_name_ent.insert(0, nok_value[3])
                    nextOfKin_surname_ent.insert(0, nok_value[4])
                    nextOfKin_contact_ent.insert(0, nok_value[5])

                    # function to close update frame
                    def nokUpd_destroy():
                        MsgBox = messagebox.askquestion('Exit Application', 'Are you sure you want to exit the application?',
                                                        icon='warning')
                        if MsgBox == 'yes':
                            adminId_ent.delete(0, END)
                            studentId_ent.delete(0, END)
                            visitorId_ent.delete(0, END)
                            nextOfKin_name_ent.delete(0, END)
                            nextOfKin_surname_ent.delete(0, END)
                            nextOfKin_contact_ent.delete(0, END)
                            nokUpd_frame.destroy()
                        else:
                            messagebox.showinfo('Return', 'Returning to the application')

                    nokUpd_cancel_btn = Button(nokUpd_frame, text="Cancel Update", command=nokUpd_destroy, bg='red', fg='black', padx=15,
                                            pady=10,
                                            borderwidth=5)
                    nokUpd_cancel_btn.place(relx=0.5, rely=0.8)

                    #  fucntion to update NEXT OF KIN treeview and mysql table
                    def upd_nextOfKin():
                        nonlocal nok_item, nok_value, adminId_ent, studentId_ent, visitorId_ent, nextOfKin_name_ent, nextOfKin_surname_ent, nextOfKin_contact_ent
                        nok_name = nextOfKin_name.get()
                        nok_surname = nextOfKin_surname.get()
                        nok_contact = nextOfKin_contact.get()
                        try:
                            if group_selector.get() == "Student":
                                my_cursor.execute(
                                    "UPDATE Next_Of_Kin SET next_of_kin_name=%s, next_of_kin_surname=%s, next_of_kin_contact=%s WHERE stud_id=%s ",
                                    (nok_name, nok_surname, nok_contact, nok_value[1]))
                                lifechoices_db.commit()
                                messagebox.showinfo("Success",
                                                    "Student Next Of Kin Data Updated.\nClick on 'Next of Kin Search' button to see updates.")
                                adminId_ent.delete(0, END)
                                studentId_ent.delete(0, END)
                                visitorId_ent.delete(0, END)
                                nextOfKin_name_ent.delete(0, END)
                                nextOfKin_surname_ent.delete(0, END)
                                nextOfKin_contact_ent.delete(0, END)
                                nokUpd_frame.destroy()
                            elif group_selector.get() == "Admin":
                                my_cursor.execute(
                                    "UPDATE Next_Of_Kin SET next_of_kin_name=%s, next_of_kin_surname=%s, next_of_kin_contact=%s WHERE admin_id=%s ",
                                    (nok_name, nok_surname, nok_contact, nok_value[0]))
                                lifechoices_db.commit()
                                messagebox.showinfo("Success",
                                                    "Admin Next Of Kin Data Updated.\nClick on 'Next of Kin Search' button to see updates.")
                                adminId_ent.delete(0, END)
                                studentId_ent.delete(0, END)
                                visitorId_ent.delete(0, END)
                                nextOfKin_name_ent.delete(0, END)
                                nextOfKin_surname_ent.delete(0, END)
                                nextOfKin_contact_ent.delete(0, END)
                                nokUpd_frame.destroy()
                            elif group_selector.get() == "Visitor":
                                my_cursor.execute(
                                    "UPDATE Next_Of_Kin SET next_of_kin_name=%s, next_of_kin_surname=%s, next_of_kin_contact=%s WHERE visitor_id=%s ",
                                    (nok_name, nok_surname, nok_contact, nok_value[2]))
                                lifechoices_db.commit()
                                messagebox.showinfo("Success",
                                                    "Visitor Next Of Kin Data Updated.\nClick on 'Next of Kin Search' button to see updates.")
                                adminId_ent.delete(0, END)
                                studentId_ent.delete(0, END)
                                visitorId_ent.delete(0, END)
                                nextOfKin_name_ent.delete(0, END)
                                nextOfKin_surname_ent.delete(0, END)
                                nextOfKin_contact_ent.delete(0, END)
                                nokUpd_frame.destroy()
                        except TypeError:
                            pass

                    nokUpd_submit_btn = Button(nokUpd_frame, text="Submit Update", command=upd_nextOfKin, bg='green', fg='black',
                                               padx=15, pady=10, borderwidth=5)
                    nokUpd_submit_btn.place(relx=0.15, rely=0.8)
                except IndexError:
                    messagebox.showerror('Error',
                                         'Please select the data from the table when trying to update details.')

            # function to delete data in NEXT OF KIN treeview as well as mysql table
            def nokDelete(self):
                if group_selector.get() == "Student":
                    item = self.nokTreeview_table.selection()[0]
                    selected_item = self.nokTreeview_table.item(item)['values'][1]
                    delete = "DELETE FROM Next_Of_Kin WHERE stud_id= %s"
                    selected_data = (selected_item,)
                    my_cursor.execute(delete, selected_data)
                    lifechoices_db.commit()
                    self.nokTreeview_table.delete(item)
                    messagebox.showinfo("Success", "User Data Removed")
                elif group_selector.get() == 'Admin':
                    item = self.nokTreeview_table.selection()[0]
                    selected_item = self.nokTreeview_table.item(item)['values'][0]
                    delete = "DELETE FROM Next_Of_Kin WHERE admin_id= %s"
                    selected_data = (selected_item,)
                    my_cursor.execute(delete, selected_data)
                    lifechoices_db.commit()
                    self.nokTreeview_table.delete(item)
                    messagebox.showinfo("Success", "User Data Removed")
                elif group_selector.get() == 'Visitor':
                    item = self.nokTreeview_table.selection()[0]
                    selected_item = self.nokTreeview_table.item(item)['values'][2]
                    delete = "DELETE FROM Next_Of_Kin WHERE visitor_id= %s"
                    selected_data = (selected_item,)
                    my_cursor.execute(delete, selected_data)
                    lifechoices_db.commit()
                    self.nokTreeview_table.delete(item)
                    messagebox.showinfo("Success", "User Data Removed")
                group_selector.bind("<<ComboboxSelected>>", self.nokDelete)

            # function to calculate users signed in
            def in_count(self):
                inCount_frame = Frame(admin_page, width=600, height=400, bg="black")
                inCount_frame.place(relx=0.3, rely=0.2)

                self.heading = Label(inCount_frame, text="The number of people signed in", font=("Arial", 20, "bold"),
                                     bg="black", fg="white")
                self.heading.place(relx=0.03, rely=0.04)

                self.stud_lbl = Label(inCount_frame, text="As Students today:", bg="black", fg="white", font=("Arial", 16))
                self.stud_lbl.place(relx=0.07, rely=0.24)
                self.stud_amount = Label(inCount_frame, bg="grey", fg="white", font=("Arial", 16), width=10)
                self.stud_amount.place(relx=0.75, rely=0.24)
                self.stud_count_lbl = Label(inCount_frame, text="Students still signed in:", bg="black", fg="white",
                                            font=("Arial", 16))
                self.stud_count_lbl.place(relx=0.07, rely=0.31)
                self.stud_count_amount = Label(inCount_frame, bg="grey", fg="white", font=("Arial", 16), width=10)
                self.stud_count_amount.place(relx=0.75, rely=0.31)

                self.admin_lbl = Label(inCount_frame, text="As Admin today:", bg="black", fg="white", font=("Arial", 15))
                self.admin_amount = Label(inCount_frame, bg="grey", fg="white", font=("Arial", 16), width=10)
                self.admin_lbl.place(relx=0.07, rely=0.45)
                self.admin_amount.place(relx=0.75, rely=0.45)
                self.admin_count_lbl = Label(inCount_frame, text="Admin members still signed in:", bg="black", fg="white", font=("Arial", 16))
                self.admin_count_amount = Label(inCount_frame, bg="grey", fg="white", font=("Arial", 16), width=10)
                self.admin_count_lbl.place(relx=0.07, rely=0.52)
                self.admin_count_amount.place(relx=0.75, rely=0.52)

                self.visitor_lbl = Label(inCount_frame, text="As Visitors today:", bg="black", fg="white", font=("Arial", 16))
                self.visitor_amount = Label(inCount_frame, bg="grey", fg="white", font=("Arial", 16), width=10)
                self.visitor_lbl.place(relx=0.07, rely=0.66)
                self.visitor_amount.place(relx=0.75, rely=0.66)
                self.visitor_count_lbl = Label(inCount_frame, text="Visitors still signed in:", bg="black", fg="white", font=("Arial", 16))
                self.visitor_count_lbl.place(relx=0.07, rely=0.73)
                self.visitor_count_amount = Label(inCount_frame, bg="grey", fg="white", font=("Arial", 16), width=10)
                self.visitor_count_amount.place(relx=0.75, rely=0.73)

                # still signed in count
                my_cursor.execute("SELECT COUNT(stud_sign_in_date) FROM Students WHERE stud_sign_in_date='" + current_date + "' AND stud_sign_out_time is NULL")
                stud_result = my_cursor.fetchall()
                # signed in today count
                my_cursor.execute("SELECT COUNT(stud_id) FROM Students WHERE stud_sign_in_date = '"+ current_date +"'")
                stud_amount = my_cursor.fetchall()
                self.stud_count_amount.config(text=stud_result)
                self.stud_amount.config(text=stud_amount)
                # admin count
                my_cursor.execute("SELECT COUNT(admin_sign_in_date) FROM Admin WHERE admin_sign_in_date='" + current_date + "' AND admin_sign_out_time is NULL")
                admin_result = my_cursor.fetchall()
                my_cursor.execute("SELECT COUNT(admin_id) FROM Admin WHERE admin_sign_in_date = '" + current_date + "'")
                admin_amount = my_cursor.fetchall()
                self.admin_amount.config(text=admin_amount)
                self.admin_count_amount.config(text=admin_result)
                # visitor count
                my_cursor.execute("SELECT COUNT(visitor_sign_in_date) FROM Visitors WHERE visitor_sign_in_date='" + current_date + "' AND visitor_sign_out_time is NULL")
                visitor_result = my_cursor.fetchall()
                my_cursor.execute("SELECT COUNT(visitor_id) FROM Visitors WHERE visitor_sign_in_date = '" + current_date + "'")
                visitor_amount = my_cursor.fetchall()
                self.visitor_amount.config(text=visitor_amount)
                self.visitor_count_amount.config(text=visitor_result)

                # function to destroy sign in count frame
                def inCount_destroy():
                    MsgBox = messagebox.askquestion('Exit Application', 'Are you sure you want to exit the application?',
                                                    icon='warning')
                    if MsgBox == 'yes':
                        inCount_frame.destroy()
                    else:
                        messagebox.showinfo('Return', 'Returning to the application')

                inCount_cancel_btn = Button(inCount_frame, text="X", command=inCount_destroy, bg='red', fg='black',
                                             padx=10,
                                             pady=5,
                                             borderwidth=5, font=("Arial", 16))
                inCount_cancel_btn.place(relx=0.89, rely=0.04)

            # function to count those signed out
            def out_count(self):
                outCount_frame = Frame(admin_page, width=600, height=400, bg="black")
                outCount_frame.place(relx=0.3, rely=0.2)

                self.heading = Label(outCount_frame, text="The number of people signed out:", font=("Arial", 18, "bold"),
                                     bg="black", fg="white")
                self.heading.place(relx=0.03, rely=0.04)

                self.stud_lbl = Label(outCount_frame, text="Number of Students signed in today:", bg="black", fg="white",
                                      font=("Arial", 15))
                self.stud_lbl.place(relx=0.07, rely=0.24)
                self.stud_amount = Label(outCount_frame, bg="grey", fg="white", font=("Arial", 15), width=10)
                self.stud_amount.place(relx=0.73, rely=0.24)
                self.studOut_count_lbl = Label(outCount_frame, text="Number of Students signed out:", bg="black", fg="white", font=("Arial", 15))
                self.studOut_count_lbl.place(relx=0.07, rely=0.31)
                self.studOut_count_amount = Label(outCount_frame, bg="grey", fg="white", font=("Arial", 15), width=10)
                self.studOut_count_amount.place(relx=0.73, rely=0.31)

                self.admin_lbl = Label(outCount_frame, text="Number of Admin signed in today:", bg="black", fg="white",
                                      font=("Arial", 15))
                self.admin_lbl.place(relx=0.07, rely=0.45)
                self.admin_amount = Label(outCount_frame, bg="grey", fg="white", font=("Arial", 15), width=10)
                self.admin_amount.place(relx=0.73, rely=0.45)
                self.adminOut_count_lbl = Label(outCount_frame, text="Number of Admin signed out:", bg="black", fg="white", font=("Arial", 15))
                self.adminOut_count_amount = Label(outCount_frame, bg="grey", fg="white", font=("Arial", 15), width=10)
                self.adminOut_count_lbl.place(relx=0.07, rely=0.52)
                self.adminOut_count_amount.place(relx=0.73, rely=0.52)

                self.visitor_lbl = Label(outCount_frame, text="Number of Visitors signed in today:", bg="black", fg="white",
                                       font=("Arial", 15))
                self.visitor_lbl.place(relx=0.07, rely=0.66)
                self.visitor_amount = Label(outCount_frame, bg="grey", fg="white", font=("Arial", 15), width=10)
                self.visitor_amount.place(relx=0.73, rely=0.66)
                self.visitorOut_count_lbl = Label(outCount_frame, text="Number of Visitors signed out:", bg="black", fg="white", font=("Arial", 15))
                self.visitorOut_count_lbl.place(relx=0.07, rely=0.73)
                self.visitorOut_count_amount = Label(outCount_frame, bg="grey", fg="white", font=("Arial", 15), width=10)
                self.visitorOut_count_amount.place(relx=0.73, rely=0.73)

                # student count
                # count how many students signed out
                my_cursor.execute("SELECT COUNT('stud_sign_out_time') FROM Students WHERE stud_sign_out_date='" + current_date + "'")
                studOut_result = my_cursor.fetchall()
                # count how many students signed in today
                my_cursor.execute("SELECT COUNT(stud_id) FROM Students WHERE stud_sign_in_date = '" + current_date + "'")
                stud_amount = my_cursor.fetchall()
                self.stud_amount.config(text=stud_amount)
                self.studOut_count_amount.config(text=studOut_result)

                # admin count
                my_cursor.execute(
                    "SELECT COUNT(admin_sign_out_time) FROM Admin WHERE admin_sign_out_date='" + current_date + "'")
                adminOut_result = my_cursor.fetchall()
                # count how many admin signed in today
                my_cursor.execute("SELECT COUNT(admin_id) FROM Admin WHERE admin_sign_in_date = '" + current_date + "'")
                admin_amount = my_cursor.fetchall()
                self.admin_amount.config(text=admin_amount)
                self.adminOut_count_amount.config(text=adminOut_result)

                # visitor count
                my_cursor.execute(
                    "SELECT COUNT('visitor_sign_out_time') FROM Visitors WHERE visitor_sign_out_date='" + current_date + "'")
                visitorOut_result = my_cursor.fetchall()
                # count how many visitors signed in today
                my_cursor.execute("SELECT COUNT(visitor_id) FROM Visitors WHERE visitor_sign_in_date = '" + current_date + "'")
                visitor_amount = my_cursor.fetchall()
                self.visitor_amount.config(text=visitor_amount)
                self.visitorOut_count_amount.config(text=visitorOut_result)

                # function to exit count
                def outCount_destroy():
                    MsgBox = messagebox.askquestion('Exit Application', 'Are you sure you want to exit the application?',
                                                    icon='warning')
                    if MsgBox == 'yes':
                        outCount_frame.destroy()
                    else:
                        messagebox.showinfo('Return', 'Returning to the application')

                outCount_cancel_btn = Button(outCount_frame, text="X", command=outCount_destroy, bg='red', fg='black',
                                            padx=10,
                                            pady=5,
                                            borderwidth=5, font=("Arial", 16))
                outCount_cancel_btn.place(relx=0.89, rely=0.04)


            # function for admin to sign out
            def sign_out(self):
                MsgBox = messagebox.askquestion('Exit Application', 'Are you sure you want to exit the application?',
                                                icon='warning')
                if MsgBox == 'yes':
                    admin_page.destroy()
                    import sign_out
                else:
                    messagebox.showinfo('Return', 'Returning to the application')

        admin_control = AdminAccess()
        admin_page.mainloop()


admin_logging_in = AdminLoginPage()
admin_login.mainloop()
