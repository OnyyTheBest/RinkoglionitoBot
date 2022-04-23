import tkinter as tk
import tkinter
from tkinter import *
import tkinter.messagebox as tkMessageBox
from tkinter import filedialog, ttk
import os
import requests
import json

savepath = '/'.join(os.getcwd().split('/')[:3])

gui = tk.Tk()

gui.title('RinkoConfigurer')
gui.iconphoto(False, tk.PhotoImage(file=f'{savepath}\icons8-telegramma-app-150.png'))
gui.geometry("1024x720")
Label(gui, text="RinkoConfigurer, This little program makes it easy to create your own Rinkoglionito, use your real data because no one will fuck with it ;)", font=('Helvetica', 10, 'bold')).pack()
Label(gui, text="Put your token here!", font=15).pack()
token = Text(width=100, height=1)
token.pack()



def helloCallBack():
   tkMessageBox.showinfo("ERROR", "specifies the bot's token")

def tokerr():
   tkMessageBox.showinfo("ERROR", "The specified token is invalid!")

def take_input():
    INPUT = token.get("1.0", "end-1c")
    if(INPUT == "Put your token here"):
        helloCallBack()
    elif INPUT == "":
        helloCallBack()
    else:
        req = requests.get(f"https://api.telegram.org/bot{INPUT}/getMe")
        if req.status_code == 200:
            B["state"] = DISABLED
            print(INPUT)
            more_lines = f"Token = '{INPUT}'"
            with open('config.txt', 'a') as f:
                f.writelines(more_lines+"\n")
                f.close()
        else:
            tokerr()
        return
B = ttk.Button(gui, text ="Confirm TOKEN:",command=lambda:take_input())
B.pack()
Label(gui, text="Put here Owner ChatID", font=('Helvetica', 18, 'bold')).pack()
chatid = Text(width=100, height=1)
chatid.pack()

def take_cid():
    INPUT = chatid.get("1.0", "end-1c")
    if(INPUT == "Put OWNER ChatID"):
        tkMessageBox.showinfo("ERROR", "Please enter the ChatID of the owner!")
    elif INPUT == "":
        tkMessageBox.showinfo("ERROR", "Please enter the ChatID of the owner!")
    else:
        print(INPUT)
        more_lines = f"Chatid = '{INPUT}'"
        with open('config.txt', 'a') as f:
            f.writelines(more_lines+"\n")
            f.close()

        
        CID["state"] = DISABLED
        return
CID = ttk.Button(gui, text="Confirm ChatID:",command=lambda:take_cid())
CID.pack()
Label(gui, text="Select a download folder...", font=('Helvetica', 18, 'bold')).pack()


def select_file():
    filename = filedialog.askdirectory(
        title='Select music download directory...')
    more_lines = f"directory = '{filename}'"
    with open('config.txt', 'a') as f:
            f.writelines(more_lines+"\n")
            f.close()
    Label(gui, text=filename, font=13).pack()
    open_button["state"] = DISABLED


open_button = ttk.Button(gui, text='select dir', command=select_file)
open_button.pack(expand=False)
Label(gui, text="Directory currently selected:", font=40).pack()


def Req():
    ciao = 'pip install -r requirments.txt'
    os.system(ciao)
    Label(gui, text="Done!", font=('Helvetica', 18, 'bold')).pack()
reqbutton = ttk.Button(gui, text='Install requirments', command=Req)
reqbutton.pack(side=tk.BOTTOM)



gui.mainloop()
