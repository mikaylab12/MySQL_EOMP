from tkinter import *
from tkinter import ttk
import mysql.connector
from tkinter import messagebox
admin_page = Tk()
admin_page.title("Admin")
admin_page.config(bg="green")
admin_page.geometry("800x900")

# declaring text variables
name = StringVar()
person_id = IntVar()
surname = StringVar()
password = IntVar()
contact = IntVar()

# combo box
group = StringVar(admin_page)
group_list = ['Student', 'Admin', 'Visitor']
group_selector = ttk.Combobox(admin_page, textvariable=group.set, font=("Arial", 13), width=19)
group_selector.set("Select One")
group_selector['values'] = group_list
group_selector['state'] = 'readonly'
group_selector.place(relx=0.1, rely=0.15)

# connecting mysql to python
lifechoices_db = mysql.connector.connect(user='lifechoices', password='8-2fermENt2020', host='127.0.0.1',
                                         database='Lifechoices_Online', auth_plugin='mysql_native_password')
my_cursor = lifechoices_db.cursor()

frame1 = Frame(admin_page, bg="grey", highlightbackground="white", highlightthickness=5, width=400, height=300)
frame1.place(relx=0.1, rely=0.2)


class Admin(object):
    def __init__(self):
        self.heading = Label(admin_page, text="Admin Page", font=("Arial", 26, "bold"), bg="green")
        self.heading.place(x=210, y=10)

        search_btn = Button(admin_page, text="Search", command=self.group_treeview, pady=10, padx=15, borderwidth=5)
        search_btn.place(relx=0.2, rely=0.15)

        # treeview
        self.treeview_table = ttk.Treeview(frame1, columns=(1, 2, 3), show="headings")
        self.treeview_table.pack()
        self.treeview_table.heading(1, text="ID Number")
        self.treeview_table.heading(2, text="Name")
        self.treeview_table.heading(3, text="Surname")

        delete_entries = Button(admin_page, text="Delete", bg="white", fg="black", command=self.delete)
        delete_entries.place(relx=0.3, rely=0.8)

        # # students treeview
        # stud_heading = Label(admin_page, bg="grey", fg="white", font=("Arial", 20, "bold"), text="Students:")
        # stud_heading.place(relx=0.1, rely=0.16)
        # frame1 = Frame(admin_page, bg="grey", highlightbackground="white", highlightthickness=5, width=400, height=300)
        # frame1.place(relx=0.1, rely=0.2)
        #
        # stud_treeview_table = ttk.Treeview(frame1, columns=(1, 2, 3), show="headings")
        # stud_treeview_table.pack()
        #
        # stud_treeview_table.heading(1, text="ID Number")
        # stud_treeview_table.heading(2, text="Name")
        # stud_treeview_table.heading(3, text="Surname")
        # # stud_treeview_table.heading(4, text="Group")
        #
        # lifechoices_db = mysql.connector.connect(user='lifechoices', password='8-2fermENt2020', host='127.0.0.1',
        #                                          database='Lifechoices_Online', auth_plugin='mysql_native_password')
        # my_cursor = lifechoices_db.cursor()
        #
        # sql = "SELECT stud_id, stud_name, stud_surname FROM Students"
        # my_cursor.execute(sql)
        #
        # stud_rows = my_cursor.fetchall()
        # total = my_cursor.rowcount
        #
        # for i in stud_rows:
        #     stud_treeview_table.insert("", 'end', values=i)
        #
        # # visitors treeview
        # visitor_heading = Label(admin_page, bg="grey", fg="white", font=("Arial", 20, "bold"), text="Vistors:")
        # visitor_heading.place(relx=0.1, rely=0.5)
        # frame2 = Frame(admin_page, bg="grey", highlightbackground="white", highlightthickness=5, width=400, height=300)
        # frame2.place(relx=0.1, rely=0.54)
        #
        # visitor_treeview_table = ttk.Treeview(frame2, columns=(1, 2, 3), show="headings")
        # visitor_treeview_table .pack()
        #
        # visitor_treeview_table .heading(1, text="ID Number")
        # visitor_treeview_table .heading(2, text="Name")
        # visitor_treeview_table .heading(3, text="Surname")
        # # visitor_treeview_table .heading(4, text="Group")
        #
        # lifechoices_db = mysql.connector.connect(user='lifechoices', password='8-2fermENt2020', host='127.0.0.1',
        #                                          database='Lifechoices_Online', auth_plugin='mysql_native_password')
        # my_cursor = lifechoices_db.cursor()
        #
        # sql2 = "SELECT visitor_id, visitor_name, visitor_surname FROM Visitors"
        # my_cursor.execute(sql2)
        #
        # visitor_rows = my_cursor.fetchall()
        # total = my_cursor.rowcount

        # for i in visitor_rows:
        #     stud_treeview_table.insert("", 'end', values=i)

    def group_treeview(self):
        if group_selector.get() == 'Student':
            lifechoices_db = mysql.connector.connect(user='lifechoices', password='8-2fermENt2020', host='127.0.0.1',
                                                     database='Lifechoices_Online', auth_plugin='mysql_native_password')
            my_cursor = lifechoices_db.cursor()

            sql = "SELECT stud_id, stud_name, stud_surname FROM Students"
            my_cursor.execute(sql)

            rows = my_cursor.fetchall()
            total = my_cursor.rowcount

            for i in rows:
                self.treeview_table.insert("", 'end', values=i)
        elif group_selector.get() == 'Admin':
            lifechoices_db = mysql.connector.connect(user='lifechoices', password='8-2fermENt2020', host='127.0.0.1',
                                                     database='Lifechoices_Online', auth_plugin='mysql_native_password')
            my_cursor = lifechoices_db.cursor()

            sql = "SELECT admin_id, admin_name, admin_surname FROM Admin"
            my_cursor.execute(sql)

            rows = my_cursor.fetchall()
            total = my_cursor.rowcount

            for i in rows:
                self.treeview_table.insert("", 'end', values=i)
        elif group_selector.get() == 'Visitor':
            lifechoices_db = mysql.connector.connect(user='lifechoices', password='8-2fermENt2020', host='127.0.0.1',
                                                     database='Lifechoices_Online', auth_plugin='mysql_native_password')
            my_cursor = lifechoices_db.cursor()

            sql = "SELECT visitor_id, visitor_name, visitor_surname FROM Visitors"
            my_cursor.execute(sql)

            rows = my_cursor.fetchall()
            total = my_cursor.rowcount

            for i in rows:
                self.treeview_table.insert("", 'end', values=i)

    def delete(self):
        selected_item = self.treeview_table.selection()[0]
        uid = self.treeview_table.item(selected_item)['values'][0]
        remove = "DELETE FROM Students WHERE id_number = %s"
        selected_data = (uid,)
        my_cursor.execute(remove, selected_data)
        lifechoices_db.commit()
        self.treeview_table.delete(selected_item)
        messagebox.showinfo("Success", "Student Data Removed")

    # def insert(self):
    #     pass
    # def insert_data(self):
    #     self.frame = Frame(admin_page, width=400, height=320, bg="black")
    #     self.frame.place(x=100, y=150)
    #     l1 = Label(self.frame, text="name", width=8)
    #     e1 = Entry(self.frame, textvariable=name, width=25)
    #     l1.place(x=50, y=30)
    #     e1.place(x=170, y=30)
    #
    #     l2 = Label(self.frame, text="ID number", width=8)
    #     e2 = Entry(self.frame, textvariable=person_id, width=25)
    #     l2.place(x=50, y=70)
    #     e2.place(x=170, y=70)
    #
    #     l3 = Label(self.frame, text="Surname", width=8)
    #     l3.place(x=50, y=110)
    #     e3 = Entry(self.frame, textvariable=surname, width=25)
    #     e3.place(x=170, y=110)
    #
    #     l4 = Label(self.frame, text="Phone number", width=11)
    #     l4.place(x=50, y=150)
    #     e4 = Entry(self.frame, textvariable=contact, width=25)
    #     e4.place(x=170, y=150)
    #     e4.delete(0, END)
    #
    #     l5 = Label(self.frame, text="Password", width=8)
    #     l5.place(x=50, y=190)
    #     e5 = Entry(self.frame, textvariable=password, width=25)
    #     e5.place(x=170, y=190)
    #
    #     submit_btn = Button(self.frame, text="submit", command=self.add_data)
    #     submit_btn.configure(bg='white', fg='black')
    #     submit_btn.place(x=100, y=280)
    #     cancel_btn = Button(self.frame, text="cancel", command=self.frame.destroy)
    #     cancel_btn.configure(bg='white', fg='black')
    #     cancel_btn.place(x=240, y=280)
    # def add_data(self):
    #     frame = Frame(administrator, width=400, height=320, bg="black")
    #     frame.place(x=100, y=150)
    #

    def add_data(self):
        # nonlocal e1, e2, e3, e4, e5
        student_name = name.get()
        id_number = person_id.get()
        s_name = surname.get()
        p_word = password.get()
        phone_number = contact.get()
        my_cursor.execute(
            'INSERT INTO student(id_number, student_name, student_password, student_surname, phone_number) '
            'VALUES (%s, %s, %s, %s, %s)', (id_number, student_name, p_word, s_name, phone_number))
        lifechoices_db.commit()
        self.treeview_table.insert('', 'end', text='', values=(id_number, student_name, p_word, s_name, phone_number))
        messagebox.showinfo("Success", "Student Registered")
        # e1.delete(0, END)
        # e2.delete(0, END)
        # e3.delete(0, END)
        # e4.delete(0, END)
        # e5.delete(0, END)
        frame1.destroy()

        def insert_data():
            self.frame = Frame(admin_page, width=400, height=320, bg="black")
            self.frame.place(x=100, y=150)
            l1 = Label(self.frame, text="name", width=8)
            e1 = Entry(self.frame, textvariable=name, width=25)
            l1.place(x=50, y=30)
            e1.place(x=170, y=30)

            l2 = Label(self.frame, text="ID number", width=8)
            e2 = Entry(self.frame, textvariable=person_id, width=25)
            l2.place(x=50, y=70)
            e2.place(x=170, y=70)

            l3 = Label(self.frame, text="Surname", width=8)
            l3.place(x=50, y=110)
            e3 = Entry(self.frame, textvariable=surname, width=25)
            e3.place(x=170, y=110)

            l4 = Label(self.frame, text="Phone number", width=11)
            l4.place(x=50, y=150)
            e4 = Entry(self.frame, textvariable=contact, width=25)
            e4.place(x=170, y=150)
            e4.delete(0, END)

            l5 = Label(self.frame, text="Password", width=8)
            l5.place(x=50, y=190)
            e5 = Entry(self.frame, textvariable=password, width=25)
            e5.place(x=170, y=190)

        insert_entries = Button(admin_page, text="Insert", bg="white", fg="black", command=insert_data)
        insert_entries.place(relx=0.7, rely=0.8)

        submit_btn = Button(frame1, text="submit", command=self.add_data)
        submit_btn.configure(bg='white', fg='black')
        submit_btn.place(x=100, y=280)
    # cancel_btn = Button(frame1, text="cancel", command=self.destroy)
    # cancel_btn.configure(bg='white', fg='black')
    # cancel_btn.place(x=240, y=280)


    def destroy(self):
        frame1.destroy()
        # button
        cancel_btn = Button(frame1, text="cancel", command=self.destroy)
        cancel_btn.configure(bg='white', fg='black')
        cancel_btn.place(x=240, y=280)

    def selected_data(self):
        cur_item = self.focus()
        value = self.item(cur_item, "values")
        frame = Frame(admin_page, width=400, height=320, bg="black")
        frame.place(x=100, y=150)
        self.name_lbl = Label(frame, text="name", width=8)
        self.name_lbl.place(x=50, y=30)
        self.name_ent = Entry(frame, textvariable=name, width=25)
        self.name_ent.place(x=170, y=30)

        self.id_lbl = Label(frame, text="ID number", width=8)
        self.id_lbl.place(x=50, y=70)
        self.id_ent = Entry(frame, textvariable=person_id, width=25)
        self.id_ent.place(x=170, y=70)

        self.surname_lbl = Label(frame, text="Surname", width=8)
        self.surname_lbl.place(x=50, y=110)
        self.surname_ent = Entry(frame, textvariable=surname, width=25)
        self.surname_ent.place(x=170, y=110)

        l4 = Label(frame, text="Phone number", width=11)
        l4.place(x=50, y=150)
        e4 = Entry(frame, textvariable=contact, width=25)
        e4.place(x=170, y=150)
        e4.delete(0, END)

        l5 = Label(frame, text="Password", width=8)
        l5.place(x=50, y=190)
        e5 = Entry(frame, textvariable=password, width=25)
        e5.place(x=170, y=190)

        self.id_ent.insert(0, value[0])
        self.name_ent.insert(0, value[1])
        self.surname_ent.insert(0, value[2])
        e4.insert(0, value[3])
        e5.insert(0, value[4])
        def update_data():
            # nonlocal self.name_ent, self.id_ent, self.surname_ent, e4, e5, cur_item, value
            student_name = name.get()
            id_number = person_id.get()
            s_name = surname.get()
            p_word = password.get()
            phone_number = contact.get()
            self.treeview_table.item(cur_item, value=(value[0], id_number, student_name, s_name, contact, p_word))
            my_cursor.execute("UPDATE Students SET stud_id=%s, stud_name=%s, stud_surname=%s, stud_contact=%s, "
                              "student_password=%s", (student_name, id_number, s_name, p_word, phone_number, value[0]))
            lifechoices_db.commit()
            messagebox.showinfo("Success", "Students Updated")
            self.name_ent.delete(0, END)
            self.id_ent.delete(0, END)
            self.surname_ent.delete(0, END)
            e4.delete(0, END)
            e5.delete(0, END)
            frame1.destroy()

        submit_btn = Button(frame1, text="submit", command=update_data)
        submit_btn.configure(bg='white', fg='black')
        submit_btn.place(x=100, y=280)
        cancel_btn = Button(frame1, text="cancel", command=frame1.destroy)
        cancel_btn.configure(bg='white', fg='black')
        cancel_btn.place(x=240, y=280)


# delete_entries = Button(administrator, text="delete", bg="white", fg="black", command=lambda: destroy(table))
# delete_entries.place(x=50, y=450)
# insert_entries = Button(administrator, text="insert", bg="white", fg="black", command=lambda: add_data(table))
# insert_entries.place(x=150, y=450)
        update_entries = Button(admin_page, text="Update", bg="white", fg="black", command=self.selected_data)
        update_entries.place(x=250, y=450)


admin_control = Admin()
admin_page.mainloop()
