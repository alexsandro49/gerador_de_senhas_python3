import sys
import screen1
import generate_password
from PyQt6.QtWidgets import QApplication


def check_boxes():
    global password
    opc1 = screen1.checkbox1.isChecked()
    opc2 = screen1.checkbox2.isChecked()
    opc3 = screen1.checkbox3.isChecked()
    opc4 = screen1.checkbox4.isChecked()
    value = screen1.slider.value()
    screen1.label2.setText(str(value))
    password = generate_password.generate_password(opc1, opc2, opc3, opc4, value)
    screen1.label1.setText(password)

def slider():
    value = screen1.slider.value()
    screen1.label2.setText(str(value))


app = QApplication(sys.argv)
password = ""

screen1.main_screen.show()
screen1.btn1.clicked.connect(check_boxes)
screen1.slider.valueChanged.connect(slider)
app.exec()