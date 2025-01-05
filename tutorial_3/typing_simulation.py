import time
from sys import argv

import pyautogui
import pyperclip

if __name__ == "__main__":
    list_key = ['\t', '\n', '\r', ' ', '!', '"', '#', '$', '%', '&', "'", '(',
                ')', '*', '+', ',', '-', '.', '/', '0', '1', '2', '3', '4', '5', '6', '7',
                '8', '9', ':', ';', '<', '=', '>', '?', '@', '[', '\\', ']', '^', '_', '`',
                'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o',
                'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', '{', '|', '}', '~']

    special_list = ["[", "{", "("]
    file = open(argv.__getitem__(1))
    time.sleep(5)
    for da in file:
        data = da.replace("\n", "")
        k = 0
        s = ""
        for i in data.strip():
            if i in list_key or i.lower() in list_key:
                if i in special_list:
                    pyautogui.typewrite(i)
                    pyautogui.press("right")
                    pyautogui.press("backspace")
                else:
                    if i == '"':
                        if k == 2:
                            pyautogui.typewrite(i)
                            pyautogui.press("right")
                            pyautogui.press("backspace")
                        else:
                            pyautogui.typewrite(s + i, interval=0.01)
                        k = k + 1
                    elif i != '"':
                        if i == " ":
                            s = s + i
                        else:
                            pyautogui.typewrite(s + i)
                            s = ""
            else:
                pyperclip.copy(i)
                with pyautogui.hold("ctrl"):
                    pyautogui.press("v")
        # with pyautogui.hold("ctrl"):
        # pyautogui.press("e")
        pyautogui.press("enter")
        # with pyautogui.hold("ctrl"):
        # pyautogui.press("b")
        # pyautogui.click(0, currentMouseY)
