import sys
import screen1
from PyQt6.QtWidgets import QApplication


app = QApplication(sys.argv)

screen1.main_screen.show()
app.exec()