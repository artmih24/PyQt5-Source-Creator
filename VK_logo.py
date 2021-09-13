# auto-generated source-code file VK_logo_128.py with Pycture
# Pycture developed by
#    ____             _             _ _     ____  _  _
#   / __ \  __ _ _ __| |_ _ __ ___ (_) |__ |___ \| || |
#  / / _` |/ _` | '__| __| '_ ` _ \| | '_ \  __) | || |_
# | | (_| | (_| | |  | |_| | | | | | | | | |/ __/|__   _|
#  \ \__,_|\__,_|_|   \__|_| |_| |_|_|_| |_|_____|  |_|
#   \____/

from PyQt5 import QtGui
import base64
import os

def Get_vk_logo(image_str):
    ImageStr = base64.b64decode(image_str)
    with open("vk_logo.png", "wb") as vk_logo_text:
        vk_logo_text.write(ImageStr)
    vk_logo_text.close()
    qi = QtGui.QPixmap("vk_logo.png")
    os.remove("vk_logo.png")
    return(qi)
        
vk_logo_str = "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"