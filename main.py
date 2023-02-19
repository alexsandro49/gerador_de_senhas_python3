import sys
import screen1, screen2, screen3, generate_password, db_connection
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

def slider_value():
    value = screen1.slider.value()
    screen1.label2.setText(str(value))

def password_label():
    screen2.update_label(password)
    screen2.save_screen.show()

def save_password():
    db_connection.save_data(password, screen2.line_edit.text())
    screen3.update_table()
    screen2.save_screen.close()

def show_passwords():
    screen3.passwords_screen.show()
    screen1.main_screen.close()

def close_passwords():
    screen1.main_screen.show()
    screen3.passwords_screen.close()

app = QApplication(sys.argv)
password = ""

screen1.main_screen.show()
screen1.btn1.clicked.connect(check_boxes)
screen1.slider.valueChanged.connect(slider_value)
screen1.btn2.clicked.connect(password_label)
screen1.btn3.clicked.connect(show_passwords)

screen2.btn.clicked.connect(save_password)

screen3.btn1.clicked.connect(close_passwords)
screen3.btn2.clicked.connect(screen3.reverse_state)
screen3.btn3.clicked.connect(screen3.delete_data)

app.exec()