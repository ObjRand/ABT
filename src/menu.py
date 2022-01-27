import sys,os
from colorama import Fore, Back, Style

fastmode = True
path = ''

def option_input():
    option = input('->' + Fore.RED)
    print(Style.RESET_ALL, end="")
    return option

def ABT_print():
    print(Fore.BLUE + '''ANIMATED BACKGROUND TOOL''')
    print(Style.RESET_ALL)

def playbg():

    if fastmode:
        os.system('main-fast.py')
    else:
        os.system('main-normal.py')
        
    main() 

def changebg():
    os.system('cls')

    os.system('set_bg.py')

    main()

def png_bg_maker():
    os.system('cls')

    print(Fore.RED + "TEST: THIS IS NOT DONE YET PLEASE WAIT!")
    print(Style.RESET_ALL, end="")

    print('')

    os.system('pause')
    main()

def VIDTOBG():
    os.system('cls')

    os.chdir('video_parser')

    os.system('video_parser.py')

    main()

    
def BGMAKER():
    os.system('cls')
    ABT_print()

    print('How Do You Wanna Make A Bg?')
    print('''
1) Manually Selected Pngs.
2) Videos and Gifs To Bg.
    ''')

    option = option_input()

    if option == '1':
        png_bg_maker()
    elif option == '2':
        VIDTOBG()
    elif option == '!exit':
        main()
    else:
        error()
    

def settings(fastmode):
    os.system('cls')

    ABT_print()

    print(Fore.RED + """SETTINGS:""")
    print(Style.RESET_ALL, end="")

    print("""- Fast Mode (On By Default): """ + str(fastmode) + """
""")

    option = option_input()

    if option == '!t fast_mode':
        os.system('cls')

        print('Toggle Fast Mode (T/F)')

        option = option_input()

        if option == 'T':
            fastmode = True
            settings(fastmode)
        elif option == 'F':
            fastmode = False
            settings(fastmode)
        else:
            error()
    if option == '!exit':
        main()
    else:
        error()

def error():
    os.system('cls')
    print(Fore.RED + 'NOT AN OPTION!')
    print(Style.RESET_ALL, end="")
    print('')

    os.system('pause')
    main()


def main():
    os.system('cls')

    ABT_print()

    print('''What Would You Like To Do?''')

    print('''    
1) Play Current BG 
2) Change Current BG 
3) Background Maker
4) Settings
5) Exit
    ''')

    option = option_input()

    if option == '1':
        playbg()
    elif option == '2':
        changebg()
    elif option == '3':
        BGMAKER()
    elif option == '4':
        settings(fastmode)
    elif option == '5':
        sys.exit()
    else:
        error()

main()
