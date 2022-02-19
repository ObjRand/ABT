import os,ctypes,json,keyboard,threading,linecache

wallpath = ''

def gset_old_wallpaper(mode):
    global wallpath
    if mode == 'set':
        os.chdir('src')
    os.chdir('gwtf')
    if mode == 'get':
        os.system('start /min run.bat')
        print('getting wallpaper...')
        time.sleep(0.5)
        wallpath = linecache.getline('wallpath.txt', 1)
    os.chdir('..')
    if mode == 'set':
        os.chdir('..')
        print('setting wallpaper...')
        time.sleep(0.5)
        print(wallpath)
        ctypes.windll.user32.SystemParametersInfoW(20,0,wallpath,3)

gset_old_wallpaper('get')

# CLS #
os.system('cls')

# GET OUT OF SRC #
os.chdir('..')

# CD #
CD = os.getcwd()

# IMAGE SHIT #
ammountofitems = 0
imageid = 0
image_list = []
curimage = ''

# BG CHOOSING FILE #
try:
    with open("backgrounds/bg.json", "r") as bgFile:
        bgData = json.loads(bgFile.read())
        bgFile.close()
except:
  print("An Error occurred... BG.JSON_INVALID_DATA")
  os.system('pause')
  quit()

# BG DATA #
bgstring = bgData['bg']

# FIND THE BGS CONFIG AND USE IT #
bgconfigpath = CD + "\\backgrounds\\bgs\\" + bgstring + "\\" + "config.json"

with open(bgconfigpath, "r") as configFile:
    configData = json.loads(configFile.read())
    configFile.close()

for i in configData['config']:
    ammountofitems = int(i['AmountOfFrames'])

# ADDING IMAGES TO LIST #
for x in range(ammountofitems):
    imageid += 1
    image_list.append(str(imageid) + ".png")

# DEFINING VARS #
curimage = ''
WALLPAPER_PATH = ''
Loop_Running = True

# APP LOOP FUNC #

def apploop():
    global Loop_Running
    
    # sussy #
    loopvar = 0

    # APP LOOP #
    while Loop_Running:

        curimage = image_list[loopvar]

        WALLPAPER_PATH = CD + "\\backgrounds\\bgs\\" + bgstring + "\\frames\\" + curimage

        loopvar += 1

        # Check if the Loop Var Is Bigger Than Amount Of Frames Minus One!
        if loopvar > ammountofitems - 1:
            loopvar -= ammountofitems

        # Checks If Loop is running to not waste time on change bg if it is.
        if Loop_Running:
            ctypes.windll.user32.SystemParametersInfoW(20,0,WALLPAPER_PATH,3)
        

# EXIT KEY DETECTION FUNC #
def ExitKeyDec():
    global Loop_Running

    while Loop_Running:
        if keyboard.is_pressed('end'):
            gset_old_wallpaper()
            Loop_Running = False
            quit()

def gset_old_wallpaper(mode):
    global wallpath
    if mode == 'get':
        os.chdir('src')
        os.chdir('gwtf')
        os.system('start /min run.bat')
        print('getting wallpaper...')
        time.sleep(2)
        wallpath = linecache.getline('wallpath.txt', 1)
        os.chdir('..')
        os.chdir('..')
        # START THREADS #           
        threading.Thread(target=apploop).start() # APP LOOP #
        threading.Thread(target=ExitKeyDec).start() # EXIT KEY DEC #
    if mode == 'set':
        ctypes.windll.user32.SystemParametersInfoW(20,0,wallpath.rstrip('\n'),3)

gset_old_wallpaper('get')

