import sys,os

fastmode = True
path = ''

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
    print("")

def VIDTOBG():
    os.system('cls')

    os.chdir('video_parser')

    os.system('video_parser.py')

    main()

    

def BGMAKER():
    os.system('cls')
    print('''ANIMATED BACKGROUND TOOL
        ''')

    print('How Do You Wanna Make A Bg?')
    print('''
1) Manually Selected Pngs.
2) Videos and Gifs To Bg.
    ''')

    option = input('->')

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
    print("""SETTINGS:

- Fast Mode (On By Default): """ + str(fastmode) + """
""")
    option = input('->')

    if option == '!t fast_mode':
        os.system('cls')

        print('Toggle Fast Mode (T/F)')

        option = input('->')

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
    print('NOT AN OPTION!')
    print('')

    os.system('pause')
    main()


def main():
    os.system('cls')
    print('''ANIMATED BACKGROUND TOOL

What Would You Like To Do?''')

    print('''    
1) Play Current BG 
2) Change Current BG 
3) Background Maker
4) Settings
5) Exit
    ''')

    option = input('->')

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
