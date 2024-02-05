
import pyautogui #pyautogui is used to control mouse and keyboard inputs in python.
import time

#Colorising the ternimal 
RED = '\033[31m'
RESET = '\033[0m'
GREEN = '\033[32m'

def Spam():
    message = input("What message you want to spam?\nLeave empty to use clipboard.\n=> ")

    #number of repeats
    while True:
        repeats = input("How many times do you want to spam?\n=> ")

        if not (repeats.isnumeric()):
            print(RED + "The number of repeats you have entered should contain only numbers. Please enter again." + RESET)
        else:
            break

    repeats = int(repeats)

    #delays in milliseconds
    while True:
        delay = input("How many milliseconds you want between each spam?\n=> ")

        if not (delay.isnumeric()):
            print(RED + "The time you have entered should contain only numbers. Please enter again." + RESET)
        else:
            break

    delay = int(delay)

    # giving user a warning to be ready one more time
    IsLoaded = input("Press enter when you are ready to spam.\n=> ")
    print("You have 10 seconds before spamming is started! Good Luck!")
    time.sleep(10)


    for i in range(0, repeats):
        if message != "":
            # paste the message
            pyautogui.write(message)
            # and press enter
            pyautogui.hotkey("enter")
        else:
            # press control + v to paste from clipboard
            pyautogui.hotkey('ctrl', 'v')
            # and then press enter
            pyautogui.hotkey("enter")

        time.sleep(delay/1000)

    print(GREEN + "Spam Done!\n")
    print("Made By Spoiled Unknown.")
    input("Press any key to close the program.\n=> " + RESET)

        

#handling the inputs for starting the session
while True:
    print(GREEN + "Welcome back! How do you wanna irritate your pc or friends (if any left...)" + RESET)
    user_session = input("Choose between 'spam' or exit\n=> ")

    if user_session.lower() == "spam":
        Spam()
    elif user_session.lower() == "quit" or user_session.lower() == "exit":
        break
    else:
        print(RED + "Invalid option. Please choose 'spam' or 'quit'/'exit'." + RESET)