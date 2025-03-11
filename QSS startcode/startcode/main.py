from PyQt6.QtWidgets import *
from PyQt6.QtCore import *

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Takenlijst")
        self.setGeometry(100, 100, 500, 350)

        # Hoofdwidget instellen
        self.central_widget = QWidget()
        self.setCentralWidget(self.central_widget)

        # Layouts aanmaken
        main_layout = QVBoxLayout() #hoofd layout
        input_layout = QHBoxLayout() #layout om LineEdit en add_button naast elkaar te krijgen

        # Widgets voor input_layout aanmaken en toevoegen
        self.task_input = QLineEdit()
        self.task_input.setPlaceholderText("Voer een nieuwe taak in...")
        self.add_button = QPushButton("Toevoegen")

        input_layout.addWidget(self.task_input)
        input_layout.addWidget(self.add_button)        
        
        # Widgets voor main_layout aanmaken en toevoegen
        self.task_list = QListWidget()
        self.remove_button = QPushButton("Verwijderen")  

        main_layout.addWidget(self.task_list)
        main_layout.addLayout(input_layout)
        main_layout.addWidget(self.remove_button)

        self.central_widget.setLayout(main_layout) #main lay-out toevoegen aan centrale widget

        # Signalen van knoppen verbinden
        self.add_button.clicked.connect(self.add_task)
        self.remove_button.clicked.connect(self.remove_task)

    def add_task(self):
        task = self.task_input.text()
        self.task_list.addItem(task)
        self.task_input.clear()

    def remove_task(self):
        for item in self.task_list.selectedItems():
            self.task_list.takeItem(self.task_list.row(item))


app = QApplication([])

with open("style.css", "r") as file:
    app.setStyleSheet(file.read()) #style sheet toevoegen

window = MainWindow()
window.show()
app.exec()