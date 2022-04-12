import tkinter as tk
from tkinter import *
from tkinter import ttk
import time
import random
import tkinter.messagebox as msgbox

random_API_words = "QWERTYUIOOPASDFGHJKLZXCVBNM"

def registerKey():
    global window1
    window1 = tk.Tk()
    window1.title("Create Key")
    window1.geometry("300x250")

    titleWindow1 = tk.Label(window1, text="Create Key ↓", bg="grey", width="300", height="2", font=("Century Gothic", 13)).pack()
    empty3 = tk.Label(window1, text="").pack()
    btn1 = tk.Button(window1, text="Create Key", command=createKey).pack()
    empty6 = tk.Label(window1, text="").pack()
    btnExit = tk.Button(window1, text="Close Window", command=closeWindow).pack()


def closeWindow():
    window1.destroy()


def createKey():
    x = 3
    while x != 0:
        y = 1
        while y != 0:
            API_words = random.choice(random_API_words)
            API_words1 = random.choice(random_API_words)
            API_words2 = random.choice(random_API_words)
            y -= 1
        x -= 1

    KEY_WORDS = API_words + API_words1 + API_words2

    x2 = 3
    while x2 != 0:
        y2 = 1
        while y2 != 0:
            API_numbers = random.randint(0, 9)
            API_numbers1 = random.randint(0, 9)
            API_numbers2 = random.randint(0, 9)
            y2 -= 1
        x2 -= 1

    KEY_NUMBERS = str(API_numbers) + \
        str(API_numbers1) + str(API_numbers2)
    API_KEY_RESULT = KEY_WORDS + "-" + str(KEY_NUMBERS)
    with open("apikey.txt", 'a') as file:
        file.write(API_KEY_RESULT)
        file.write("\n")
    time.sleep(1)

    writeResult = tk.Label(window1, text="SUCCESS! Your key is: " + str(API_KEY_RESULT), font=("Century Gothic", 12, "bold")).pack()

    print("\n[Console] API-KEY: " + API_KEY_RESULT)

def login():
    global VERIFY_API_KEY
    VERIFY_API_KEY = input_API_KEY.get()

    filename = open('apikey.txt', 'r')
    flag = 0
    index = 0
    for line in filename:
        index += 1
        if VERIFY_API_KEY in line:
            flag = 1
            break
    if flag == 0:

        print("Your API-KEY '" + VERIFY_API_KEY + "' was not on our database.")
        notFound()
    else:
        if len(VERIFY_API_KEY) != 7:
            print("Your API-KEY '" + VERIFY_API_KEY + "' was not on our database.")
            notFound()
        else:
            print("'" + VERIFY_API_KEY + "' API-KEY was located!")
            verifiedWindow()


def verifiedWindow():
    window2 = tk.Tk()
    window2.geometry("300x250")
    window2.title("Successfully logged on.")
    textwelcome = tk.Label(window2, text="You are a verified user! Welcome!")
    textwelcome.pack()
    closeWindowBtn = tk.Button(window2, text="Close Window", command=window2.destroy)
    closeWindowBtn.pack()

def notFound():
    msgbox.showinfo("Error Not Found", "Your " + VERIFY_API_KEY + " was not found on our database.")

def main_window():
    window = tk.Tk()
    window.geometry("300x350")
    window.title("API-KEY (maybe)")
    windowTitle = tk.Label(text="Login API-KEY ↓", bg="grey", width="300", height="2", font=("Century Gothic", 13)).pack()
    empty1 = tk.Label(text="").pack()

    global input_API_KEY

    input_API_KEY = tk.Entry(window)
    submit_API_KEY = tk.Button(window, text="Submit", command=login)
    input_API_KEY.pack()
    submit_API_KEY.pack()
    empty5 = tk.Label(text="").pack()

    windowTitle2 = tk.Label(text="Create API-KEY ↓", bg="grey", width="300", height="2", font=("Century Gothic", 13)).pack()

    empty2 = tk.Label(text="").pack()
    createKey = tk.Button(text="Create Key", height="2", width="30", command=registerKey).pack()

    window.mainloop()

main_window()