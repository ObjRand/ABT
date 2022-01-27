from tkinter import *
import os, json, webbrowser

os.chdir("..")

ws = Tk()
ws.title('BG Anim')
ws.wm_iconbitmap('src/logo.ico')
ws.geometry('507x300')
ws.resizable(False, False)
frame_shown = '1'

canvas = Canvas(
    ws,
    width = 500, 
    height = 500
)
canvas.pack()

itemsindir = os.listdir(os.getcwd() + "\\backgrounds\\bgs")
listlength = len(itemsindir)
x = -1

print(listlength)

def refresh():
    os.chdir("src")
    os.system("start /min refresh.bat")
    quit()


for i in range(listlength):
    x += 1
    print(itemsindir[x])

bg_insert = PhotoImage(file='backgrounds\\bgs\\' + itemsindir[x] + '\\frames\\' + frame_shown + '.png')
bg_insert = bg_insert.zoom(1, 1)
bg_insert = bg_insert.subsample(4, 4)


def update():
    global itemsindir, listlength, x, bg_insert, frame_shown, i

    frame_shown = '1'

    print("asd")

    if x == -2:
        x = listlength - 2

    if x >= listlength:
        x += 1
    else:
        x -= 1
    
    bg_insert = PhotoImage(file='backgrounds\\bgs\\' + itemsindir[x] + '\\frames\\' + frame_shown + '.png')
    bg_insert = bg_insert.zoom(1, 1)
    bg_insert = bg_insert.subsample(4, 4)
    canvas.itemconfigure(bgs_text, text="Backgrounds: " + itemsindir[x])
    print(x)

    canvas.create_image(
        10,
        25, 
        anchor=NW, 
        image=bg_insert
    )

def set_background():
    global itemsindir

    os.system('taskkill /F /IM conhost.exe') # 13024
    os.system('taskkill /F /IM python.exe')

    bgData = {}
    bgData['bg'] = itemsindir[x]

    with open('backgrounds/bg.json','w') as file:
        json.dump(bgData,file)
        file.close()

    os.chdir("src")
    os.system("start run_min.bat")
    os.chdir("..")

def next_frame():
    global itemsindir, listlength, x, bg_insert, frame_shown

    bgconfigpath = 'backgrounds\\bgs\\' + itemsindir[x] + '\\config.json'

    with open(bgconfigpath, "r") as configFile:
        configData = json.loads(configFile.read())
        configFile.close()

    for i in configData['config']:
        ammountofitems = str(i['AmountOfFrames'])
        print(ammountofitems)
        print(frame_shown)

    if frame_shown == ammountofitems:
        frame_shown = '1'
    else:
        frame_shown = int(frame_shown)
        frame_shown += 1
        frame_shown = str(frame_shown)


    bg_insert = PhotoImage(file='backgrounds\\bgs\\' + itemsindir[x] + '\\frames\\' + frame_shown + '.png')
    bg_insert = bg_insert.zoom(1, 1)
    bg_insert = bg_insert.subsample(4, 4)
    canvas.itemconfigure(bgs_text, text="Backgrounds: " + itemsindir[x])

    canvas.create_image(
        10,
        25, 
        anchor=NW, 
        image=bg_insert
    )

def open_credits():
    os.chdir("src")
    os.system("start credits.py")
    os.chdir("..")

def video_parser():
    os.chdir("src")
    os.chdir("video_parser")
    os.system("start Video_Parser.bat")
    os.chdir("..")
    os.chdir("..")

canvas.create_image(
    10,
    25, 
    anchor=NW, 
    image=bg_insert
)

bgs_text = canvas.create_text((50,10),text="Background: " + itemsindir[x], fill='black', font=('Helvetica 9'))
page_text = canvas.create_text((50,230),text="Change Page: ", fill='black', font=('Helvetica 9'))
info = canvas.create_text((370,70),text="What Is AnimBG?\nAnimBG is a software that lets\nyou have animated desktop backgrounds. \n", fill='black', font=('Helvetica 9'))

link1 = Label(ws, text="README: https://github.com/Yeeterboi4/ABT", fg="blue", cursor="hand2", font=('Helvetica 9 underline'))
link1.place(x=255,y=100)
link1.bind("<Button-1>", lambda e: os.system("start https://github.com/Yeeterboi4/ABT/blob/main/README.md"))

link2 = Label(ws, text="SRC: https://github.com/Yeeterboi4/ABT", fg="blue", cursor="hand2", font=('Helvetica 9 underline'))
link2.place(x=255,y=120)
link2.bind("<Button-1>", lambda e: os.system("start https://github.com/Yeeterboi4/ABT"))

btn = Button(ws, text = 'Next Page -->', bd = '1', command = update, font=('Helvetica 9'))
btn2 = Button(ws, text = 'Next Frame -->', bd = '1', command = next_frame, font=('Helvetica 9'))
btn3 = Button(ws, text = 'Select Background', bd = '2', command = set_background, font=('Helvetica 9'))
btn4 = Button(ws, text = 'Make Background', bd = '2', command = video_parser, font=('Helvetica 9'))
btn5 = Button(ws, text = 'Refresh Backgrounds', bd = '2', command = refresh, font=('Helvetica 9'))
btn6 = Button(ws, text = 'Credits', bd = '2', command = open_credits, font=('Helvetica 9'))
btn.place(x=100, y=220)
btn2.place(x=100, y=250)
btn3.place(x=200, y=220)
btn4.place(x=200, y=250)
btn5.place(x=330, y=250)
btn6.place(x=330, y=220)

ws.mainloop()