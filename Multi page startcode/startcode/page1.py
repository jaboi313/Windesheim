from PyQt6.QtWidgets import *
from PyQt6.QtCore import *

class Page1(QWidget):
    def __init__(self, main_window):
        super().__init__()
        self.main_window = main_window 
        layout = QVBoxLayout()

        label = QLabel("Dit is pagina 1")
        label.setAlignment(Qt.AlignmentFlag.AlignCenter)
        layout.addWidget(label)

        button = QPushButton("Volgende stap")
        button.clicked.connect(self.next_page) 
        layout.addWidget(button)

        self.setLayout(layout)

    def next_page(self):
        self.main_window.show_page(self.main_window.page2)


