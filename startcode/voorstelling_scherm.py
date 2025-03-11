from PyQt6.QtWidgets import *
from PyQt6.QtCore import *
from voorstelling import Voorstelling

class VoorstellingScherm(QWidget):
    
    def __init__(self, voorstelling):
        super().__init__()
        self.voorstelling = voorstelling

        # Instellingen voor het venster
        self.setWindowTitle(f"Voorstelling {voorstelling.get_naam()}")
        self.setGeometry(100, 100, 350, 200)

        # Layout en widgets toevoegen
        layout = QGridLayout()

        layout.addWidget(QLabel("Aantal plaatsen vrij:"), 0, 0) #in GridLayout op rij 0, kolom 0
        self.plaatsen_label = QLabel(str(voorstelling.get_aantal_plaatsen()))
        layout.addWidget(self.plaatsen_label, 0, 1) #in GridLayout op rij 0, kolom 1 

        layout.addWidget(QLabel("Aantal plaatsen verkocht:"), 1, 0)
        self.verkocht_label = QLabel(str(voorstelling.get_aantal_verkocht()))
        layout.addWidget(self.verkocht_label, 1, 1) 

        self.verkoop_knop = QPushButton("Verkoop kaartje")  
        layout.addWidget(self.verkoop_knop,2,0)

        self.setLayout(layout)
        

app = QApplication([])
voorstelling = Voorstelling("Magic Circus", 10)
window = VoorstellingScherm(voorstelling)

window.show()
app.exec()