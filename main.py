import os 
import eel


def start():
    eel.init("www")

  


    os.system('start msedge.exe --app="http://localhost:8000/index.html"')
    eel.start('index.html',mode=None,host='localhost',block=True)