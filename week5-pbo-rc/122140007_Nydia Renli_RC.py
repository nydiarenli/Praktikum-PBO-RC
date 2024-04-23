import tkinter as tk
from tkinter import ttk
from tkinter import messagebox

def get_username():
  return entry_username.get()

def get_password():
  return entry_password.get()

def msg_berhasil(username):
  messagebox.showinfo('Login Successful', f'Welcome, {username}!')

def msg_reg():
  messagebox.showinfo('Registration Successful', 'You have successfully registered')

def register():
  extra_window = tk.Toplevel()
  extra_window.title('Register')
  extra_window.geometry('300x150')

  label_username = tk.Label(extra_window, text="Username: ")
  label_password = tk.Label(extra_window, text="Password: ")
  label_username.place(x = 10, y = 10)
  label_password.place(x = 10, y = 40)

  global entry_username_reg, entry_password_reg
  entry_username_reg = tk.Entry(extra_window)
  entry_password_reg = tk.Entry(extra_window, show="*")
  entry_username_reg.place(x = 80, y = 13)
  entry_password_reg.place(x = 80, y = 43)

  button_reg = ttk.Button(extra_window, text='Register', command=msg_reg)
  button_reg.place(x = 100, y = 80)

  extra_window.mainloop()

window = tk.Tk()
window.title('Login')
window.geometry('300x150')

label_username = tk.Label(window, text="Username: ")
label_password = tk.Label(window, text="Password: ")
label_username.place(x = 10, y = 10)
label_password.place(x = 10, y = 40)

global entry_username, entry_password
entry_username = tk.Entry(window)
entry_password = tk.Entry(window, show="*")
entry_username.place(x = 80, y = 13)
entry_password.place(x = 80, y = 43)

button_login = ttk.Button(window, text='Login', command=lambda: msg_berhasil(get_username()))
button_register = ttk.Button(window, text='Register', command=register)
button_login.place(x = 100, y = 80)
button_register.place(x = 100, y = 110)

window.mainloop()
