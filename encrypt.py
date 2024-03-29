from tkinter import *
from tkinter import messagebox
from cryptography.fernet import Fernet

# Generate a key for encryption and decryption
key = Fernet.generate_key()
cipher_suite = Fernet(key)

def encrypt():
    password = code.get()

    if password == "1216":
        message = text1.get(1.0, END).encode()
        encrypted_message = cipher_suite.encrypt(message)

        screen1 = Toplevel(screen)
        screen1.title("encryption")
        screen1.geometry("400x200")
        screen1.configure(bg="#ed3974")

        Label(screen1, text="ENCRYPT", font="arial", fg="white", bg="#ed3833").place(x=10,y=0)
        text2 = Text(screen1, font="Rpbote 10", bg="white", relief=GROOVE, wrap=WORD, bd=0)
        text2.place(x=10,y=40,width=380,height=150)

        text2.insert(END, encrypted_message.decode())
    elif password == "":
        messagebox.showerror("encryption", "Enter Password")
    else:
        messagebox.showerror("encryption", "Incorrect Password")

def decrypt():
    password = code.get()

    if password == "1234":
        encrypted_message = text1.get(1.0, END).encode()
        decrypted_message = cipher_suite.decrypt(encrypted_message)

        screen2 = Toplevel(screen)
        screen2.title("decryption")
        screen2.geometry("400x200")
        screen2.configure(bg="#00bd56")

        Label(screen2, text="DECRYPT", font="arial", fg="white", bg="#00bd56").place(x=10, y=0)
        text2 = Text(screen2, font="Rpbote 10", bg="white", relief=GROOVE, wrap=WORD, bd=0)
        text2.place(x=10, y=40, width=380, height=150)

        text2.insert(END, decrypted_message.decode())
    elif password == "":
        messagebox.showerror("decryption", "Enter Password")
    else:
        messagebox.showerror("decryption", "Incorrect Password")

def main_screen():
    global screen
    global code
    global text1

    screen = Tk()
    screen.geometry("375x398")
    screen.title("PctApp")
    image_icon=PhotoImage(file="H-2.png")
    screen.iconphoto(False,image_icon)
    screen.title("PctApp")

 

    Label(text="Enter text for encryption and decryption",
          fg="black", font=("calbri", 13)).place(x=10, y=10)
    text1 = Text(font="Roboto 20", bg="white", relief=GROOVE, wrap=WORD, bd=0)
    text1.place(x=10, y=50, width=355, height=100)
    Label(text="Enter secret key for encryption and decryption", fg="black", font=("calbri", 13)).place(x=10, y=170)

    code = StringVar()
    Entry(textvariable=code, width=19, bd=0, font=("arial", 25), show="*").place(x=10, y=200)

    Button(text="ENCRYPT", height='2', width=23, bg="#ed3833", fg="white", bd=0, command=encrypt).place(x=10, y=250)
    Button(text="DECRYPT", height="2", width=23, bg="#00bd56", fg="white", bd=0, command=decrypt).place(x=200, y=250)
    Button(text="RESET", height="2", width="50", bg="#1089ff", fg="white", bd=0, command=lambda: text1.delete(1.0, END)).place(x=10, y=300)

    screen.mainloop()

main_screen()
