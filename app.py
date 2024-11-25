import tkinter

import random

import sqlite3

conn = sqlite3.connect('pwmanager_db.db')

cursor = conn.cursor()

cursor.execute(
    'create table IF NOT EXISTS PasswordManager (website Text, email Text, password text, id Integer primary key autoincrement )')

conn.commit()

conn.close()


def save_data():
    website = entry_website.get()

    email = entry_email.get()

    password = entry_password.get()

    conn = sqlite3.connect('pwmanager_db.db')

    cursor = conn.cursor()

    cursor.execute('INSERT INTO PasswordManager (website, email, password) VALUES (?, ?, ?)',

                   (website, email, password))

    conn.commit()

    cursor.execute("SELECT * FROM PasswordManager")

    rows = cursor.fetchall()

    for row in rows:
        print(row)

    cursor.execute("DELETE FROM PasswordManager")

    conn.close()

    print("podatocite se zacuvani")


def generate_password():
    bukvi = ["a", "b", 'c', 'd', 'e']

    brojki = ['1', '2', '3', '4']

    znaci = ["@", '#', '!']

    spoena_lista = bukvi + brojki + znaci

    random.shuffle(spoena_lista)

    lista_so_password = spoena_lista[:8]

    password = ''.join(lista_so_password)

    entry_password.insert(0, password)


screen = tkinter.Tk()

screen.title("Password Manager")

screen.geometry("500x500")

canvas = tkinter.Canvas()

img = tkinter.PhotoImage(file="logo.png")

canvas.config(height=200, width=200)

canvas.create_image(100, 100, image=img)

canvas.grid(row=0, column=1)

label_website = tkinter.Label(text="Website: ")

label_website.grid(row=1, column=0)

entry_website = tkinter.Entry(width=20)

entry_website.grid(row=1, column=1)

label_email = tkinter.Label(text="Email: ")

label_email.grid(row=2, column=0)

entry_email = tkinter.Entry(width=20)

entry_email.grid(row=2, column=1)

label_password = tkinter.Label(text="Password: ")

label_password.grid(row=3, column=0)

entry_password = tkinter.Entry(width=20)

entry_password.grid(row=3, column=1)

button_generate_pw = tkinter.Button(text="Generate Password", command=generate_password)

button_generate_pw.grid(row=3, column=2)

button_add = tkinter.Button(text="ADD", command=save_data)

button_add.grid(row=4, column=1)

screen.mainloop()