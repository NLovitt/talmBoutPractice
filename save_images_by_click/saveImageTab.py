import time
import pyautogui as pg

# Prompt user to select the Chrome window
chrome_windows = pg.getWindowsWithTitle("Google Chrome")

if not chrome_windows:
    pg.alert(text="Could not find Chrome window.", button='OK')
    exit()
elif len(chrome_windows) == 1:
    chrome_window = chrome_windows[0]
else:
    titles = [window.title for window in chrome_windows]
    choice = pg.confirm(text="Select the Chrome window to use:", buttons=titles)
    chrome_window = chrome_windows[titles.index(choice)]

# Bring the selected window to the foreground
chrome_window.activate()

# Maximize the window if needed
if chrome_window.isMaximized:
    # If the window is already maximized, restore it first
    chrome_window.restore()
chrome_window.maximize()

SAVE_PIC = r'C:\Users\naeem\Documents\_VSCODE\Personal_projects\save_images_by_click\savePic.png'
SAVE_VID = r'C:\Users\naeem\Documents\_VSCODE\Personal_projects\save_images_by_click\saveVid.png'

def save_image():
    # right click center of screen
    pg.rightClick(x=pg.size().width / 2, y=pg.size().height / 2)

    save_image_button = pg.locateOnScreen(SAVE_PIC, confidence=0.8)
    if save_image_button is not None:
        save_image_button_center = pg.center(save_image_button)
        pg.click(save_image_button_center)
        time.sleep(0.5)
    else:
        save_video_button = pg.locateOnScreen(SAVE_VID, confidence=0.8)
        if save_video_button is not None:
            save_video_button_center = pg.center(save_video_button)
            pg.click(save_video_button_center)
            time.sleep(0.5)
        else:
            pg.alert(text="Could not find 'Save image as' or 'Save video as' button.", button='OK')
            return

    time.sleep(0.5)
    # Press enter to save the file
    pg.press('enter')
    time.sleep(1)

    # Close tab
    pg.hotkey('ctrl', 'w')

# Prompt user to select the mode of operation
choice = pg.confirm(text="Press OK when ready to save images.", buttons=['1by1', 'Numbered'])
if choice == '1by1':
    while True:
        okay = pg.confirm(text='Ready?', title='Save images', buttons=['OK', 'Cancel'])
        if okay == 'Cancel':
            break
        save_image()
else:
    while True:
        num_images = pg.prompt(text='How many images to save?', title='Save images', default='1')
        if num_images is None:
            break
        for i in range(int(num_images)):
            save_image()
        flag = pg.confirm(text="Save more images?", buttons=['Yes', 'No']) == 'Yes'
        if not flag:
            break
