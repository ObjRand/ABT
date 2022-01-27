from tkinter import *
import os, json, webbrowser

os.chdir("..")

ws = Tk()
ws.title('BG Anim (credits)')
ws.wm_iconbitmap('src/logo.ico')
ws.geometry('230x200')
ws.resizable(False, False)
frame_shown = '1'

canvas = Canvas(
    ws,
    width = 500, 
    height = 500
)
canvas.pack()

info = canvas.create_text((80,70),text="Credits: \nOriginal made by ", fill='black', font=('Helvetica 11'))
link1 = Label(ws, text="Yeeterboi4", fg="blue", cursor="hand2", font=('Helvetica 11 underline'))
link1.place(x=135,y=67)
link1.bind("<Button-1>", lambda e: os.system("start https://github.com/Yeeterboi4/ABT"))

info2 = canvas.create_text((110,98),text="GUI version made by me :)", fill='black', font=('Helvetica 11'))


ws.mainloop()