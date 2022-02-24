from time import sleep
from config import *
from win10toast import ToastNotifier
from scrape import Scrape
from server import Server
from browser import MainWindow
import sys
from PyQt5.QtWidgets import QApplication
def main():

    data = Scrape()
    
    if data.webdate != data.localdate:
        events = data.get_events()
        data.to_json(events)

        with open("used.txt", "w") as f:
            f.write("0")
        with open("lastUsed.txt" ,"w") as f:
            f.write(data.webdate)

    with open("used.txt", "r") as f:
        used = int(f.read())
    if not used:
        toast = ToastNotifier()
        toast.show_toast(name, "check the importance of the day>>>", icon_path=icon, duration=10, callback_on_click=open_web)
    else:
        open_web()
    sys.exit()
    
def open_web():
    #start_server(PORT)
    server = Server(PORT)
    server.start_server()
    
    # creating a pyQt5 application
    app = QApplication(sys.argv)

    screen_resolution = app.desktop().screenGeometry()
    w, h = screen_resolution.width(), screen_resolution.height()


    # creating a main window object
    window = MainWindow(w, h)

    # loop
    app.exec_()

    # stop the server
    server.stop_server()

    with open("used.txt", "w") as f:
        f.write("1")

if __name__ == "__main__":
    main()