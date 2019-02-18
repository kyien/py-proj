from tkinter import *
import mysql.connector
  
def register_ui():
        global r
        r=Tk() #instantiation
        r.geometry('300x400')
        r.title('REGISTER')
        global first_name
        global last_name
        global user_email
        global password
        global fname_entry
        global lname_entry
        global email_entry
        global pass_entry

        first_name=StringVar()
        last_name=StringVar()
        user_email=StringVar()
        password=StringVar()

        #email entry
        fname_label=Label(r,text="FirstName:",).place(x=20,y=50)
        fname_entry=Entry(r,textvariable=first_name)
        fname_entry.place(x=100,y=50)

        #email entry
        lname_label=Label(r,text="LastName:",).place(x=20,y=85)
        lname_entry=Entry(r,textvariable=last_name)
        lname_entry.place(x=100,y=85)
    
        #email ent
        email_label=Label(r,text="Email:",).place(x=20,y=120)
        email_entry=Entry(r,textvariable=user_email)
        email_entry.place(x=100,y=120)

        #password entry
        password_label=Label(r,text="Password:",).place(x=20,y=155)
        pass_entry=Entry(r,textvariable=password)
        pass_entry.place(x=100,y=155)

        #button
        register_user_btn=Button(r,text="REGISTER",command=register_to_db).place(x=180,y=190)

        r.mainloop()

def register_user():
	first_name_dt=first_name.get()
	last_name_dt=last_name.get()
	email_dt=user_email.get()
	password_dt=password.get()

	user_creds=[first_name_dt,last_name_dt,email_dt,password_dt]

	dm=open('users.txt','w+')

	for i in user_creds:
		dm.write(i + "\n")

	dm.close()

	#fname_entry.delete(0,END)
	#lname_entry.delete(0,END)
	#email_entry.delete(0,END)
	#password_entry.delete(0,END)
def register_to_db():
	first_name_dt=first_name.get()
	last_name_dt=last_name.get()
	email_dt=user_email.get()
	password_dt=password.get()

	try:
		db=mysql.connector.connect(host='localhost',database='pyson',user='root',password='kyien')

		db_cursor=db.cursor()
		sql_text=""" INSERT INTO `users`(`first_name`, `last_name`, `email`, `password`) VALUES (%s,%s,%s,%s)"""
		sql_values=(first_name_dt,last_name_dt,email_dt,password_dt)
		db_cursor.execute(sql_text,sql_values)
		db.commit()
	except mysql.connector.Error as e:
		print(e)
		db.rollback()
		db.close()

#re=Register()
register_ui()


