import json, os
from colorama import Fore, Back, Style

# GET OUT OF SRC #
os.chdir('..')

# DATA CLEAR VAR #
Default_bgData = {}
Default_bgData['bg'] = ''

def Bg_input():
    Bg = input('->' + Fore.RED)
    print(Style.RESET_ALL, end="")
    return Bg

def ABT_print():
    print(Fore.BLUE + '''ANIMATED BACKGROUND TOOL''')
    print(Style.RESET_ALL)

def error(Bg):
    os.system('cls')

    ABT_print()

    print('Bg'+ Fore.RED + ' "' + Bg + '" ' + Style.RESET_ALL + 'Is Not In The Backgrounds Folder (Error 404: BG NOT FOUND)')
    print('')

    os.system('pause')
    main()

def bgset(Bg):
    os.system('cls')

    ABT_print()

    bgData = {}
    bgData['bg'] = Bg

    with open('backgrounds/bg.json','w') as file:
        json.dump(bgData,file)
        file.close()

    print('Background'+ Fore.GREEN + ' "' + Bg + '" ' + Style.RESET_ALL + 'has been selected!')
    print('')

    os.system('pause')
    askforbg()

def askforbg():
    # ASK FOR BG #
    os.system('cls')

    ABT_print()

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
    Bg = Bg_input() 

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

