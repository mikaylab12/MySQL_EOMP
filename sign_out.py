from tkinter import *
import mysql.connector
from tkinter import messagebox
from PIL import Image, ImageTk
from tkinter.ttk import Combobox
from datetime import datetime

sign_out_page = Tk()
sign_out_page.title("Sign Out Page")
sign_out_page.geometry("800x800")

# adding picture as background
canvas = Canvas(sign_out_page, width=900, height=2000, bg="#9fd143", borderwidth=0, highlightthickness=0)
canvas.place(relx=0, rely=0)
img_logo = ImageTk.PhotoImage(Image.open("LIFE-CHOICES-ICON-ON-GREEN.jpeg"))
canvas.create_image(390, -140, anchor=N, image=img_logo)

# combo box
group = StringVar(sign_out_page)
group_list = ['Student', 'Admin', 'Visitor']
group_selector = Combobox(sign_out_page, textvariable=group.set, font=("Arial", 13), width=19)
group_selector.set("Select One")
group_selector['values'] = group_list
group_selector['state'] = 'readonly'
group_selector.place(relx=0.35, rely=0.9)

# connecting mysql to python
lifechoices_db = mysql.connector.connect(user='lifechoices', password='8-2fermENt2020', host='127.0.0.1',
                                         database='Lifechoices_Online', auth_plugin='mysql_native_password')
my_cursor = lifechoices_db.cursor(buffered=True)


class SignOut(object):
    def __init__(self):
        self.sign_out_btn = Button(sign_out_page, text="Sign Out", borderwidth=5, padx=15, pady=10,
                                   font=("Arial", 25),
                                   bg="black", fg="white", command=self.sign_out_user)
        self.sign_out_btn.place(relx=0.7, rely=0.8)
        # heading
        self.heading = Label(sign_out_page, text="Please sign out when you are ready to:", fg="black", bg="#a2cc41",
                             font=("Arial", 25, "bold"))
        self.heading.place(relx=0.09, rely=0.04)
        # instruction heading
        self.instruction_heading = Label(sign_out_page, text="Please enter your details:", fg="black",
                                         bg="#a2cc41", font=("Arial", 21, "bold"))
        self.instruction_heading.place(relx=0.1, rely=0.68)
        self.combobox_label = Label(sign_out_page, text="Group:", fg="white", bg="#a2cc41", font=("Arial", 17,
                                                                                                  "bold"))
        self.combobox_label.place(relx=0.1, rely=0.9)

        # labels and entries
        self.id_label = Label(sign_out_page, text="ID number:", fg="white", bg="#a2cc41", font=("Arial", 17,
                                                                                                "bold"))
        self.id_label.place(relx=0.1, rely=0.76)
        self.id_entry = Entry(sign_out_page, font=("Arial", 14))
        self.id_entry.place(relx=0.35, rely=0.76)

        self.password_label = Label(sign_out_page, text="Password:", fg="white", bg="#a2cc41", font=("Arial", 17,
                                                                                                    "bold"))
        self.password_label.place(relx=0.1, rely=0.83)
        self.password_entry = Entry(sign_out_page, font=("Arial", 14), show='*')
        self.password_entry.place(relx=0.35, rely=0.83)

    # signing out function
    def sign_out_user(self):
        if group_selector.get() == "Select One":
            messagebox.showerror("Entry Error", "Please select your group.")
        elif self.id_entry.get() == "":
            messagebox.showerror("Entry Error", "Please enter your ID number.")
        elif self.password_entry.get() == "":
            messagebox.showerror("Entry Error", "Please enter your password.")
        try:
            if group_selector.get() == 'Student':
                my_cursor.execute('SELECT * FROM Students WHERE stud_id = "' + self.id_entry.get() + '"')
                results = my_cursor.fetchall()
                if results == []:
                    messagebox.showerror("Login Unsuccessful",
                                         "Please select the correct group, and/or enter the correct ID number.\nIf the issue persists, please see reception!")
                elif str(self.id_entry.get()) == results[0][0] and str(self.password_entry.get()) == results[0][6]:
                    self.sign_out()
                elif str(self.id_entry.get()) == results[0][0] and str(self.password_entry.get()) != results[0][6]:
                    messagebox.showerror("Error", "Password is incorrect")
                    self.password_entry.delete(0, END)
            elif group_selector.get() == 'Admin':
                my_cursor.execute('SELECT * FROM Admin WHERE admin_id = "' + self.id_entry.get() + '"')
                results = my_cursor.fetchall()
                if results == []:
                    messagebox.showerror("Login Unsuccessful",
                                         "Please select the correct group, and/or enter the correct ID number.\n\nIf the issue persists, please see reception!")
                elif str(self.id_entry.get()) == results[0][0] and str(self.password_entry.get()) == results[0][6]:
                    self.sign_out()
                elif str(self.id_entry.get()) == results[0][0] and str(self.password_entry.get()) != results[0][6]:
                    messagebox.showerror("Error", "Password is incorrect")
                    self.password_entry.delete(0, END)
            elif group_selector.get() == 'Visitor':
                my_cursor.execute('SELECT * FROM Visitors WHERE visitor_id = "' + self.id_entry.get() + '"')
                results = my_cursor.fetchall()
                if results == []:
                    messagebox.showerror("Login Unsuccessful",
                                         "Please select the correct group, and/or enter the correct ID number.\n\nIf the issue persists, please see reception!")
                elif str(self.id_entry.get()) == results[0][0] and str(self.password_entry.get()) == results[0][6]:
                    self.sign_out()
                elif str(self.id_entry.get()) == results[0][0] and str(self.password_entry.get()) != results[0][6]:
                    messagebox.showerror("Error", "Password is incorrect")
                    self.password_entry.delete(0, END)
        except TypeError:
            pass

    # function to execute sign out date and sign out time
    def sign_out(self):
        if group_selector.get() == 'Student':
            so_date = datetime.now().date().strftime('%Y-%m-%d')
            so_time = datetime.now().time().strftime('%H:%M:%S')
            date_signoutsql = "UPDATE Students SET stud_sign_out_date=%s WHERE stud_id='" \
                              + self.id_entry.get() + "' AND stud_password='" + self.password_entry.get() + "'"
            date_signoutval = [so_date]
            time_signoutsql = "UPDATE Students SET stud_sign_out_time=%s WHERE stud_id='" \
                         + self.id_entry.get() + "' AND stud_password='" + self.password_entry.get() + "'"
            time_signoutval = [so_time]
            my_cursor.execute(date_signoutsql, date_signoutval)
            my_cursor.execute(time_signoutsql, time_signoutval)
            lifechoices_db.commit()
            messagebox.showinfo('Sign Out successful', 'Enjoy the rest of your day!')
            sign_out_page.destroy()
            import main
        elif group_selector.get() == 'Admin':
            so_date = datetime.now().date().strftime('%Y-%m-%d')
            so_time = datetime.now().time().strftime('%H:%M:%S')
            date_signoutsql = "UPDATE Admin SET admin_sign_out_date=%s WHERE admin_id='" \
                              + self.id_entry.get() + "' AND admin_password='" + self.password_entry.get() + "'"
            date_signoutval = [so_date]
            time_signoutsql = "UPDATE Admin SET admin_sign_out_time=%s WHERE admin_id='" \
                         + self.id_entry.get() + "' AND admin_password='" + self.password_entry.get() + "'"
            time_signoutval = [so_time]
            my_cursor.execute(date_signoutsql, date_signoutval)
            my_cursor.execute(time_signoutsql, time_signoutval)
            lifechoices_db.commit()
            messagebox.showinfo('Sign Out successful', 'Enjoy the rest of your day!')
            sign_out_page.destroy()
            import main
        elif group_selector.get() == 'Visitor':
            so_date = datetime.now().date().strftime('%Y-%m-%d')
            so_time = datetime.now().time().strftime('%H:%M:%S')
            date_signoutsql = "UPDATE Visitors SET visitor_sign_out_date=%s WHERE visitor_id='" \
                              + self.id_entry.get() + "' AND visitor_password='" + self.password_entry.get() + "'"
            date_signoutval = [so_date]
            time_signoutsql = "UPDATE Visitors SET visitor_sign_out_time=%s WHERE visitor_id='" \
                              + self.id_entry.get() + "' AND visitor_password='" + self.password_entry.get() + "'"
            time_signoutval = [so_time]
            my_cursor.execute(date_signoutsql, date_signoutval)
            my_cursor.execute(time_signoutsql, time_signoutval)
            lifechoices_db.commit()
            messagebox.showinfo('Sign Out successful', 'Enjoy the rest of your day!')
            sign_out_page.destroy()
            import main


signOut = SignOut()
sign_out_page.mainloop()
