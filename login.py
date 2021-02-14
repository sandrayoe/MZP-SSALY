from tkinter import *
from functools import partial

def validateLogin(username, password):
	print("username entered :", username.get())
	print("password entered :", password.get())
	return

#create window
tkWindow = Tk()  
tkWindow.geometry('250x150')  
tkWindow.title('LOGIN - SSALY') #header

#username label and text entry
usernameLabel = Label(tkWindow, text="User Name").grid(row=0, column=5)
username = StringVar()
usernameEntry = Entry(tkWindow, textvariable=username).grid(row=0, column=7)  

#password label and password entry 
passwordLabel = Label(tkWindow,text="Password").grid(row=1, column=5)  
password = StringVar()
passwordEntry = Entry(tkWindow, textvariable=password, show='*').grid(row=1, column=7)  

validateLogin = partial(validateLogin, username, password)

#login button
loginButton = Button(tkWindow, text="Login", command=validateLogin).grid(row=4, column=5)  

tkWindow.mainloop()