import sys
import screen1
from PyQt6.QtWidgets import QApplication


app = QApplication(sys.argv)

def check_boxes():
    opc1 = screen1.checkbox1.isChecked()
    opc2 = screen1.checkbox2.isChecked()
    opc3 = screen1.checkbox3.isChecked()
    opc4 = screen1.checkbox4.isChecked()
    opc5 = screen1.slider.value()
    screen1.label2.setText(str(opc5))
    screen1.label1.setText(f"{opc1}, {opc2}, {opc3}, {opc4}, {opc5}")

def slider():
    opc5 = screen1.slider.value()
    screen1.label2.setText(str(opc5))

screen1.main_screen.show()
screen1.btn1.clicked.connect(check_boxes)
screen1.slider.valueChanged.connect(slider)
app.exec()