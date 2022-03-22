
import pyautogui # import pyautogui to spam in more dynamic ways
import time # import time for sleeping or waiting for some seconds

# message store the message that is to be spammed if left empty then it will
# use ctrl + v to paste last copied thing
message = input("What message you want to spam?\nLeave empty to use clipboard.\n")
# repeats stores the amount for repeating the loop
repeats = int(input("How many times do you want to spam?\n"))
# delay store the amount of millisecond to loop the code
delay = int(input("How many milliseconds you want between each spam?\n"))
# isLoaded is pretty useless but it gives time to open the software in which you want to spam for exaple: discord, whatsapp
IsLoaded = input("Press enter when you are ready to spam.\n")

# giving user a warning to be ready one more time
print("You have 10 seconds before spamming is started! Good Luck!")

# stopiing the code for 10 seconds
time.sleep(10)

# looping the program for repeats amount
for i in range(0, repeats):
    # if message is not empty then simply
    if message != "":
        # paste the message
        pyautogui.typewrite(message)
        # and press enter
        pyautogui.press("enter")
    # if not then
    else:
        # press control + v to paste from clipboard
        pyautogui.typewrite('ctrl', 'v')
        # and then press enter
        pyautogui.press("enter")

    # stop the loop for delay given at top portion of program
    time.sleep(delay/1000)

# after everything is executed and program is ready to be closed
print("done\n")
print("Made By MrUnKnOwNOP")
input("Press any key to close the program.")
        