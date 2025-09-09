import os
import eel
from app import main_process
eel.init("frontend")




eel.start('index.html',mode=None, host='localhost',block=True )