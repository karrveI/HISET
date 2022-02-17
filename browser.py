# importing required libraries
from PyQt5.QtCore import *
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtWebEngineWidgets import *
from PyQt5.QtPrintSupport import *
from config import name, PORT, icon


# creating main window class
class MainWindow(QMainWindow):

	# constructor
	def __init__(self, screenW, screenH, *args, **kwargs):
		super(MainWindow, self).__init__(*args, **kwargs)
		self.setWindowTitle(name)
		# creating a QWebEngineView
		self.browser = QWebEngineView()

		self.w = 450
		self.h = 500
		self.x = screenW - self.w - 20 #margin
		self.y = screenH - self.h - 50 #margin

		#set size of the window
		self.browser.setMinimumSize(QSize(self.w, self.h))

		#set position of the window
		self.setGeometry(QRect(self.x, self.y, self.w, self.h))

		#set the icon
		self.setWindowIcon(QIcon(icon))

		# setting default browser url as the url of the website
		self.browser.setUrl(QUrl(f"http://localhost:{PORT}/web/index.html"))

		# set this browser as central widget or main window
		self.setCentralWidget(self.browser)

		# showing all the components
		self.show()
