from tkinter import *
class Register:

    def __init__(self):
        self.register_win()

    def register_win(self):
        global register_screen
        register_screen = Tk()
        register_screen.title("Register")
        register_screen.geometry("300x250")
    
        global username
        global password
        global username_entry
        global password_entry
        username = StringVar()
        password = StringVar()
    
        Label(register_screen, text="Please enter details below", bg="blue").pack()
        Label(register_screen, text="").pack()
        username_lable = Label(register_screen, text="Username * ")
        username_lable.pack()
        username_entry = Entry(register_screen, textvariable=username)
        username_entry.pack()
        password_lable = Label(register_screen, text="Password * ")
        password_lable.pack()
        password_entry = Entry(register_screen, textvariable=password, show='*')
        password_entry.pack()
        Label(register_screen, text="").pack()
        Button(register_screen, text="Register", width=10, height=1, bg="blue", command = self.register_user).pack()

        register_screen.mainloop()

    def register_user(self):
    
        username_info = username.get()
        password_info = password.get()
        
        # print(username_info)
        file = open('usernames.txt', "w")
        file.write(username_info + "\n")
        file.write(password_info)
        file.close()
    
        username_entry.delete(0, END)
        password_entry.delete(0, END)
    
        Label(register_screen, text="Registration Success", fg="green", font=("calibri", 11)).pack()

re=Register()
# re.register_win


 