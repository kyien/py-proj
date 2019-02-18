from tkinter import *
#from register import *

class Login:
    def __init__(self):
        self.login_ui()

    def login_ui(self):
        l=Tk()
        l.geometry('300x300')
        l.title('LOGIN')

        l_email=StringVar()
        l_password=StringVar()

        #email entry
        email_label=Label(l,text="Email:",).place(x=20,y=50)
        email_entry=Entry(l,textvariable=l_email).place(x=100,y=50)

        #password entry
        password_label=Label(l,text="Password:",).place(x=20,y=95)
        pass_entry=Entry(l,textvariable=l_password).place(x=100,y=95)

        #buttons
        login_btn=Button(l,text="LOGIN").place(x=50,y=160)
        register_btn=Button(l,text="REGISTER",command=register_ui).place(x=180,y=160)

        l.mainloop()

m=Login()
    
