import random
import tkinter as tk
import string 

def generate_password(length):
    characters = string.ascii_letters+string.digits + string.punctuation
    password = ''.join(random.choice(characters) for _ in range(length))
    return password

def generate_password_button_click():
    try:
        length = int(password_length_entry.get())
        if length <= 0:
            result_label.config(text= "password length should be greater than 0. ")
        else:
            password = generate_password(length)
            result_label.config(text=f"generated password: {password}")
    except ValueError:
        result_label.config(text="Invalid input. please enter a valid number for the password length. ")


#create a GUI window 
window = tk.Tk()
window.title("password generator")

#create and pack widgets
label = tk.Label(window , text="enter the desired password length: ")
label.pack(pady=10)
window.geometry("600x300")
password_length_entry = tk.Entry(window)
password_length_entry.pack()
generate_button = tk.Button(window , text="generate password", command=generate_password_button_click)
generate_button.pack(pady=10)
result_label = tk.Label(window , text="")
result_label.pack()

#start the GUI application
window.mainloop()