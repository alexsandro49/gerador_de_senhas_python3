import sys
from PyQt6.QtWidgets import QApplication, QWidget, QPushButton, QLabel, QLineEdit, QCheckBox, QSlider
from PyQt6.QtCore import Qt

app = QApplication(sys.argv)

main_screen = QWidget()
main_screen.resize(500, 500)
main_screen.setWindowTitle("Gerenciador de senhas")
main_screen.setStyleSheet("background-color: #FF101F; color: #ffffff;")

line_edit = QLineEdit("", main_screen)
line_edit.setGeometry(50, 60, 400, 50)
line_edit.setStyleSheet("background-color: #ffffff; color: #22333b; border: 2px solid #ffffff; border-radius: 5px; font-size: 18px; font-weight: bold; font-family: Arial, Verdana, sans-serif;")

checkbox1 = QCheckBox("Maiúsculas", main_screen)
checkbox1.setGeometry(50, 130, 150, 30)
checkbox1.setStyleSheet("background-color: #ffffff; color: #22333b; font-size: 12px; border: 2px solid #ffffff; border-radius: 5px; font-family: Arial, Verdana, sans-serif;")

checkbox2 = QCheckBox("Minúsculas", main_screen)
checkbox2.setGeometry(50, 180, 150, 30)
checkbox2.setStyleSheet("background-color: #ffffff; color: #22333b; font-size: 12px; border: 2px solid #ffffff; border-radius: 5px; font-family: Arial, Verdana, sans-serif;")

checkbox3 = QCheckBox("Números", main_screen)
checkbox3.setGeometry(50, 230, 150, 30)
checkbox3.setStyleSheet("background-color: #ffffff; color: #22333b; font-size: 12px; border: 2px solid #ffffff; border-radius: 5px; font-family: Arial, Verdana, sans-serif;")

checkbox4 = QCheckBox("Símbolos", main_screen)
checkbox4.setGeometry(50, 280, 150, 30)
checkbox4.setStyleSheet("background-color: #ffffff; color: #22333b; font-size: 12px; border: 2px solid #ffffff; border-radius: 5px; font-family: Arial, Verdana, sans-serif;")

slider = QSlider(main_screen)
slider.setGeometry(220, 130, 50, 180)
slider.setStyleSheet("background-color: #ffffff; color: #22333b; font-size: 12px; border: 2px solid #ffffff; border-radius: 5px; font-family: Arial, Verdana, sans-serif;")

btn1 = QPushButton("GERAR", main_screen)
btn1.setGeometry(320, 160, 100, 50)
btn1.setStyleSheet("background-color: #22333b; border: 2px solid #ffffff; border-radius: 5px;")

btn2 = QPushButton("SALVAR", main_screen)
btn2.setGeometry(320, 230, 100, 50)
btn2.setStyleSheet("background-color: #22333b; border: 2px solid #ffffff; border-radius: 5px;")

btn3 = QPushButton("SENHAS SALVAS", main_screen)
btn3.setGeometry(50, 340, 400, 50)
btn3.setStyleSheet("background-color: #22333b; border: 2px solid #ffffff; border-radius: 5px;")
