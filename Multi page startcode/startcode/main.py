from PyQt6.QtWidgets import *
from page1 import Page1
from page2 import Page2

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Multi-page app")
        self.setGeometry(100, 100, 260, 200)

        #QStackedWidget aanmaken en instellen als centrale widget van QMainWindow
        self.stacked_widget = QStackedWidget()
        self.setCentralWidget(self.stacked_widget)

        #Pagina's initialiseren
        self.page1 = Page1(self)
        self.page2 = Page2(self)

        #Pagina's toevoegen aan QStackedWidget
        self.stacked_widget.addWidget(self.page1)
        self.stacked_widget.addWidget(self.page2)

    def show_page(self, page):
        self.stacked_widget.setCurrentWidget(page)

#applicatie aanmaken en starten
app = QApplication([])
window = MainWindow()
window.show()
app.exec()