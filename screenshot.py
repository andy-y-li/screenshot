import sys
import time
import pyautogui
import pygetwindow as gw
from pywinauto import Application


def setMinimizeWindow(window_title):
    try:
        app = Application().connect(title=window_title)
        target_window = app.window(title=window_title)
        target_window.minimize()
    except Exception as e:
        print('Error:', e)


def setActivateWindow(window_title):
    try:
        app = Application().connect(title=window_title)
        target_window = app.window(title=window_title)
        target_window.set_focus()
        time.sleep(1)
    except Exception as e:
        print('Error:', e)


def get_screenShot(target_title, png_file):
    all_titles = gw.getAllTitles()
    for title in all_titles:
        print(title)

    target_windows = gw.getWindowsWithTitle(target_title)
    if target_windows:
        target_window = target_windows[0]
        for window in target_windows:
            if 'Command Prompt' not in window.title:
                target_window = window
                break
        print('Found window:', target_window.title)
        setActivateWindow(target_window.title)
        left, top, width, height = target_window.left, target_window.top, target_window.width, target_window.height
        screenshot = pyautogui.screenshot(region=(left, top, width, height))
        screenshot.save(png_file)
        setMinimizeWindow(target_window.title)
        print('Save the screen file: %s' % png_file)
    else:
        print('Not found the window: %s' % target_title)
    return 'png_file:\\' + png_file


if __name__ == '__main__':
    if len(sys.argv) < 2:
        print('Usage %s target_title images_filepath' % sys.argv[0])
        exit(1)
    target_title = sys.argv[1]
    png_file = sys.argv[2]
    get_screenShot(target_title, png_file)
