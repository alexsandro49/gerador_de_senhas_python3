import sys
from PyQt6.QtWidgets import QApplication, QWidget, QPushButton, QLabel, QLineEdit


def update_label(text_label):
    global text_label1

    text_label1 = text_label

    label2 = QLabel(text_label1, save_screen)
    label2.setGeometry(20, 70, 260, 50)
    label2.setStyleSheet("background-color: #ffffff; color: #22333b; border: 2px solid #ffffff; border-radius: 5px; font-size: 18px; font-weight: bold; font-family: Arial, Verdana, sans-serif;")


app = QApplication(sys.argv)
text_label1 = ""

save_screen = QWidget()
save_screen.resize(300, 300)
save_screen.setWindowTitle("Salvar senha")
save_screen.setStyleSheet("background-color: #150050; color: #22333b;")

label1 = QLabel("Senha:", save_screen)
label1.setGeometry(20, 30, 260, 20)
label1.setStyleSheet("background-color: None; color: #ffffff; border: None; font-size: 22px; font-weight: bold; font-family: Arial, Verdana, sans-serif;")

label2 = QLabel("Sobre:", save_screen)
label2.setGeometry(20, 140, 260, 20)
label2.setStyleSheet("background-color: None; color: #ffffff; border: None; font-size: 22px; font-weight: bold; font-family: Arial, Verdana, sans-serif;")

line_edit = QLineEdit(save_screen)
line_edit.setGeometry(20, 180, 260, 50)
line_edit.setStyleSheet("background-color: #ffffff; color: #22333b; border: 2px solid #ffffff; border-radius: 5px; font-size: 18px; font-weight: bold; font-family: Arial, Verdana, sans-serif;")

btn = QPushButton("SALVAR", save_screen)
btn.setGeometry(100, 250, 100, 30)
btn.setStyleSheet("background-color: #22333b; color: white; border: 2px solid #ffffff; border-radius: 5px;")

update_label(text_label1)
