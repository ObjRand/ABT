import json, os

# GET OUT OF SRC #
os.chdir('..')

# DATA CLEAR VAR #
Default_bgData = {}
Default_bgData['bg'] = ''

def error(Bg):
    os.system('cls')
    print('Bg "' + Bg + '" Is Not In The Backgrounds Folder (Error 404: BG NOT FOUND)')
    print('')

    os.system('pause')
    main()

def bgset(Bg):
    # 

    os.system('cls')

    bgData = {}
    bgData['bg'] = Bg

    with open('backgrounds/bg.json','w') as file:
        json.dump(bgData,file)
        file.close()

    print('Background "'+ Bg + '" has been selected!')
    print('')

    os.system('pause')
    askforbg()

def askforbg():
    # ASK FOR BG #
    os.system('cls')

    print("What Background Would You Like To Use?")

    cd = os.getcwd()

    itemsindir = os.listdir(cd + "\\backgrounds\\bgs")

    listlength = len(itemsindir)

    # PARSE AND PRINT LIST #
    for i in range(listlength):
        print('')
        print('"' + itemsindir[i] + '"')

    # INPUT BG #
    print('')
    Bg = input('>')

    if Bg == '!exit':
        quit()
    # CHECK FOR ERROR #
    for i in range(listlength):
        if Bg == itemsindir[i]:
            bgset(Bg)
    error(Bg)

def main():
    # CLEAR JSON #
    with open('backgrounds/bg.json','w') as file:
        json.dump(Default_bgData,file)
        file.close()

    # RESTART FUNC #
    askforbg()
    

# RUN APPS CODE #
askforbg()

