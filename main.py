#! python3
# main.py
# In charge of moving the mouse and executing keyboard commands.
import pyautogui, sys, time

pyautogui.FAILSAFE= True # STOP THE PROGRAM FROM FUCKING MY DAY UP
print('Please move the window to your second display, or at least out of the way.')
input('Press any key to continue.')
print('Please make sure that your book is on the main display.')

# print('Please move mouse to first corner.')
# input('Press any key to continue')

# print('Move mouse to the bottom right of page..')
# input('Press any key to continue')

# print('Now move your mouse to the next button.')
# input('Press any key to continue')

# print('Move your mouse to Word')
# input('Press any key to continue')

print('Okay. Get ready. You have 10 seconds to open word and chrome.')
input('Press any key to start the screenshot utility.')
counter = 0
try:
    while True:
        #TODO get print.
        # First action, win key s
        pyautogui.moveTo(197, 178, duration=.2) # move to upper right corner of page
        pyautogui.hotkey('win', 'shift', 's') # opens up snip and sketch
        time.sleep(.1)
        pyautogui.dragTo(748, 1007, button='left', duration=.1) #moves to bottom right
        pyautogui.moveTo(1795, 716) #clicks on word
        time.sleep(.5)
        pyautogui.click()
        pyautogui.hotkey('ctrl', 'v') #pastes into word

        pyautogui.click(x=924, y=548) #move to and click next button
        # print('On sleep event')
        time.sleep(.3)
except KeyboardInterrupt:
    print('You hit CTRL+C you fuckin-')