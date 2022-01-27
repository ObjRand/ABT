import cv2, os, json
from colorama import Fore, Style, init

init(convert=True)

"""

{
    "config":[
        {
            "AmountOfFrames":"5"
        }
    ]
}

"""

file = input("Video/Gif File Directory: ")
bg_name = input("Backgrounds Name: ")
print("")

if os.path.exists(file):
    cam = cv2.VideoCapture(file)
else:
    print(f"{Fore.RED}Error: Couldn't find ('video.mp4') file")
    os.system('pause')
    quit()
  
if not os.path.exists(bg_name):
    # ENTER BG #
    os.chdir('..')
    os.chdir('..')
    os.chdir('backgrounds')
    os.chdir('bgs')

    os.makedirs(bg_name)
    os.chdir(bg_name)
    os.makedirs('frames')
else:
    print(f'{Fore.RED}Error: Output folder already exists')
    os.system('pause')
    quit()
  
currentframe = 1
  
while True:
      
    ret,frame = cam.read()
  
    if ret:
        name = './frames/' + str(currentframe) + '.png'
        print(name.replace('./frames/', ''), 'Created')
  
        cv2.imwrite(name, frame)
        currentframe += 1
    else:
        dictionary = ' {"config":\
[ { "AmountOfFrames": "' + str(currentframe) + '"} ] } '


        json_data = json.loads(dictionary)
        json_formatted_str = json.dumps(json_data, indent=4, sort_keys=True)

        with open('config.json', 'w') as f:
            f.write(json_formatted_str)
        print(f'{Fore.GREEN}!!! DONE !!!')
        os.system('pause')
        break
  
cam.release()
cv2.destroyAllWindows()

quit()