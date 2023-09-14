import pyautogui as pag
import time

#clangd, c++ testmate, c++ helper, cmake, cmake tools


def extensionInstaller(extensionName):
    install_button = pag.locateCenterOnScreen("install.png", confidence=0.7)
    extension_button = pag.locateCenterOnScreen(extensionName + ".png", confidence=0.7)
    
    try:
        if extension_button is not None and install_button is not None:
            ext_x, ext_y = extension_button
            install_x, install_y = install_button
            install_relative_x = install_x - ext_x
            install_relative_y = install_y - ext_y
            pag.click(ext_x + install_relative_x, ext_y + install_relative_y)
        else:
            print("Image not found for: " + extensionName)
    except Exception as e:
        return f"An error has occurred: {e}"
        
    
# Open VS Code
pag.hotkey("ctrl", "alt", "t")
time.sleep(2)
pag.typewrite("code .")
pag.hotkey("enter")
time.sleep(2)

pag.hotkey("ctrl", "shift", "x")
time.sleep(3)

# Installing Clangd
pag.typewrite("clangd")
time.sleep(5)
extensionInstaller("clangd")
time.sleep(5)

# Installing C++ Test Mate
pag.hotkey("ctrl", "shift", "x")
time.sleep(1)
pag.hotkey("ctrl", "backspace")
time.sleep(1)
pag.typewrite("c++ testmate")
time.sleep(3)
extensionInstaller("cppTestMate")
time.sleep(5)

# Installing Cmake
pag.hotkey("ctrl", "shift", "x")
time.sleep(1)
pag.hotkey("ctrl", "backspace")
pag.hotkey("ctrl", "backspace")
pag.hotkey("ctrl", "backspace")
time.sleep(1)
pag.typewrite("cmake")
time.sleep(3)
extensionInstaller("cmake")
time.sleep(5)

# Installing Cmake Tools
pag.hotkey("ctrl", "shift", "x")
time.sleep(1)
pag.hotkey("ctrl", "backspace")
time.sleep(1)
pag.typewrite("cmake tools")
time.sleep(3)
extensionInstaller("cmakeTools")
time.sleep(5)

# Installing C++ Helper
pag.hotkey("ctrl", "shift", "x")
time.sleep(1)
pag.hotkey("ctrl", "backspace")
pag.hotkey("ctrl", "backspace")
time.sleep(1)
pag.typewrite("c++ helper")
time.sleep(3)
extensionInstaller("cppHelper")