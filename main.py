# Mikayla Beelders' End Of Module Project
from tkinter import *
import mysql.connector
from tkinter import messagebox
from PIL import Image, ImageTk
from tkinter.ttk import Combobox
from datetime import datetime

login_screen = Tk()
login_screen.geometry("800x900")
login_screen.config(bg="#3556e8")
login_screen.title("Login Page")


def admin_page(event):
    import admin
    login_screen.destroy()


login_screen.bind("<Control-a>", admin_page)

# adding image
canvas = Canvas(login_screen, width=620, height=300, bg="#3c5be6", borderwidth=0, highlightthickness=0)
canvas.place(relx=0.1, rely=0.1)
img_logo = ImageTk.PhotoImage(Image.open("lifechoices-2.jpg"))
canvas.create_image(310, -15, anchor=N, image=img_logo)

# combo box
group = StringVar(login_screen)
group_list = ['Student', 'Admin', 'Visitor']
group_selector = Combobox(login_screen, textvariable=group.set, font=("Arial", 13), width=19)
group_selector.set("Select One")
group_selector['values'] = group_list
group_selector['state'] = 'readonly'
group_selector.place(relx=0.35, rely=0.65)

#connecting mysql to python
lifechoices_db = mysql.connector.connect(user='lifechoices', password='8-2fermENt2020', host='127.0.0.1',
                                         database='Lifechoices_Online', auth_plugin='mysql_native_password')
my_cursor = lifechoices_db.cursor()

# for exact date and time
current_date = datetime.now().date().strftime("%Y-%m-%d")
current_time = datetime.now().time().strftime("%H:%M:%S")

class Login(object):
    def __init__(self):
        # heading
        self.heading = Label(login_screen, text="Welcome To:", fg="white", bg="#3556e8",
                             font=("Arial", 25, "bold"))
        self.heading.place(relx=0.37, rely=0.04)
        # instruction heading
        self.instruction_heading = Label(login_screen, text="Please enter your login details:", fg="#7bfa05",
                                         bg="#3556e8", font=("Arial", 21, "bold"))
        self.instruction_heading.place(relx=0.1, rely=0.45)
        self.combobox_label = Label(login_screen, text="Group:", fg="white", bg="#3556e8", font=("Arial", 15,
                                                                                                 "bold"))
        self.combobox_label.place(relx=0.1, rely=0.65)

        # labels and entries
        self.id_label = Label(login_screen, text="ID number:", fg="white", bg="#3556e8", font=("Arial", 15,
                                                                                               "bold"))
        self.id_label.place(relx=0.1, rely=0.515)
        self.id_entry = Entry(login_screen, font=("Arial", 14))
        self.id_entry.place(relx=0.35, rely=0.515)

        self.password_label = Label(login_screen, text="Password:", fg="white", bg="#3556e8", font=("Arial", 15,
                                                                                                    "bold"))
        self.password_label.place(relx=0.1, rely=0.58)
        self.password_entry = Entry(login_screen, font=("Arial", 14), show='*')
        self.password_entry.place(relx=0.35, rely=0.58)
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
        if group_selector.get() == "Select One":
            messagebox.showinfo("Entry Error", "Please select your group.")
        elif self.id_entry.get() == "":
            messagebox.showinfo("Entry Error", "Please enter your ID number.")
        elif self.password_entry.get() == "":
            messagebox.showinfo("Entry Error", "Please enter your password.")
        # if self.id_entry == "" or self.password_entry == "":
        #     messagebox.showinfo("Entry Error", "Please enter your details.")
        else:
            try:
                if group_selector.get() == "Student":
                    my_cursor.execute('SELECT * FROM Students')
                    for i in my_cursor:
                        # if i.type == group_selector.MOUSEBUTTONDOWN:
                            # if self.id_entry.get() == i[0] and self.password_entry.get() == i[6]:
                            #     messagebox.showinfo("Congratulations", "Successful login")
                            #     break
                        if self.id_entry.get() == i[0] and self.password_entry.get() == i[6]:
                            # my_cursor.execute('UPDATE Students SET stud_sign_in_date= "' + current_date + '"' \
                            #                   ' WHERE id ="' + self.id_entry.get() + '"')
                            messagebox.showinfo("Congratulations", "Successful login")
                            self.password_entry.delete(0, END)
                        elif self.id_entry.get() != i[0] and self.password_entry.get() == i[6]:
                            messagebox.showerror("Error", "ID number is incorrect")
                            self.id_entry.delete(0, END)
                        # elif self.id_entry.get() != i[0] or self.password_entry.get() != i[6]:
                        #     messagebox.showerror("Error", "ID number and/or password is incorrect")
                        else:
                            if self.id_entry.get() == i[0] and self.password_entry.get() != i[6]:
                                messagebox.showerror("Error", "Password is incorrect")
                elif group_selector.get() == "Admin":
                    xy = my_cursor.execute('SELECT * FROM Admin')
                    for i in my_cursor:
                        # if self.id_entry.get() == i[0] and self.password_entry.get() == i[6]:
                        #     messagebox.showinfo("Congratulations", "Successful login")
                        #     break
                        if self.id_entry.get() == i[0] and self.password_entry.get() != i[6]:
                            messagebox.showerror("Error", "Password is incorrect")
                            self.password_entry.delete(0, END)
                        elif self.id_entry.get() != i[0] and self.password_entry.get() == i[6]:
                            messagebox.showerror("Error", "ID number is incorrect")
                            self.id_entry.delete(0, END)
                        elif self.id_entry.get() != i[0] or self.password_entry.get() != i[6]:
                            messagebox.showerror("Error", "ID number and/or password is incorrect")
                        else:
                            if self.id_entry.get() == i[0] and self.password_entry.get() == i[6]:
                                messagebox.showinfo("Congratulations", "Successful login")
                elif group_selector.get() == "Visitor":
                    xy = my_cursor.execute('SELECT * FROM Visitors')
                    for i in my_cursor:
                        # if self.id_entry.get() == i[0] and self.password_entry.get() == i[6]:
                        #     messagebox.showinfo("Congratulations", "Successful login")
                        #     break
                        if self.id_entry.get() == i[0] and self.password_entry.get() != i[6]:
                            messagebox.showerror("Error", "Password is incorrect")
                            self.password_entry.delete(0, END)
                        elif self.id_entry.get() != i[0] and self.password_entry.get() == i[6]:
                            messagebox.showerror("Error", "ID number is incorrect")
                            self.id_entry.delete(0, END)
                        elif self.id_entry.get() != i[0] or self.password_entry.get() != i[6]:
                            messagebox.showerror("Error", "ID number and/or password is incorrect")
                        else:
                            if self.id_entry.get() == i[0] and self.password_entry.get() == i[6]:
                                messagebox.showinfo("Congratulations", "Successful login")
            except AttributeError:
                pass
            group_selector.bind("<<ComboboxSelected>>", self.login)

            # elif xy == []:
            #     messagebox.showinfo("User Error", "user odes not exist, please register")

        # def comb1_selected():
        #     date = StringVar()
        #     global comb2
        #     comb2 = Combobox(login_screen, textvariable=date)
        #     comb2.pack()
        #     comb2.config(state=DISABLED)
        #
        #     if (self.option_selector.current() != -1):
        #         print('current: ' + str(self.option_selector.current()))  # current: 0
        #         print('get: ' + self.option_selector.get())  # get: Jan
        #
        #         comb2.config(state='normal')
        #         if self.option_selector.get() == 'Student':
        #             comb2.config(values=('J'))
        # self.option_selector.bind("<<ComboboxSelected>>", login)

        # lifechoices_db = mysql.connector.connect(user='lifechoices', password='8-2fermENt2020', host='127.0.0.1',
        #                                          database='Lifechoices_Online', auth_plugin='mysql_native_password')
        # my_cursor = lifechoices_db.cursor()
        # xy = my_cursor.execute('SELECT * FROM login')
        # if self.id_entry == "":
        #     messagebox.showinfo("Entry Error", "Please enter your ID number.")
        # if self.password_entry == "":
        #     messagebox.showinfo("Entry Error", "Please enter your password.")
        # else:
        #     for i in my_cursor:
        #         if self.id_entry.get() == i[0] and self.password_entry.get() == i[1]:
        #             messagebox.showinfo("Successful", "Login Successful!\nEnjoy your day.")
        #             login_screen.destroy()
        #             # import menu_page
        #             break
        #     for i in my_cursor:
        #         if self.id_entry.get() != i[0] and self.password_entry.get() != i[1]:
        #             messagebox.showinfo("Error", "Access denied!\nPlease visit reception.")
        #             self.id_entry.delete(0, END)
        #             self.password_entry.delete(0, END)

    # group_selector.bind("<<ComboboxSelected>>", login)

    def registering(self):
        messagebox.showinfo("New User", "You will be redirected to enter your credentials!")
        login_screen.destroy()
        import registration

    def clear(self):
        self.id_entry.delete(0, END)
        self.password_entry.delete(0, END)
        group_selector.set("Select One")


logging_in = Login()
login_screen.mainloop()
