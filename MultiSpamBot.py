
import pyautogui #pyautogui is used to control mouse and keyboard inputs in python.
import time

message = input("What message you want to spam?\nLeave empty to use clipboard.\n")
repeats = int(input("How many times do you want to spam?\n"))
delay = int(input("How many milliseconds you want between each spam?\n"))
IsLoaded = input("Press enter when you are ready to spam.\n")

# giving user a warning to be ready one more time
print("You have 10 seconds before spamming is started! Good Luck!")

time.sleep(10)


for i in range(0, repeats):
    if message != "":
        # paste the message
        pyautogui.typewrite(message)
        # and press enter
        pyautogui.press("enter")
    else:
        # press control + v to paste from clipboard
        pyautogui.hotkey('ctrl', 'v')
        # and then press enter
        pyautogui.press("enter")

    time.sleep(delay/1000)

print("Spam Done!\n")
print("Made By Spoiled Unknown.")
input("Press any key to close the program.")
        