import sys
from PyQt6.QtWidgets import QApplication, QWidget, QPushButton, QLabel, QLineEdit, QCheckBox, QSlider
from PyQt6.QtCore import Qt

app = QApplication(sys.argv)

main_screen = QWidget()
main_screen.resize(500, 500)
main_screen.setWindowTitle("Gerenciador de senhas")
main_screen.setStyleSheet("background-color: #FF101F; color: #ffffff;")

label1 = QLineEdit("", main_screen)
label1.setGeometry(50, 60, 400, 50)
label1.setStyleSheet("background-color: #ffffff; color: #22333b; border: 2px solid #ffffff; border-radius: 5px; font-size: 18px; font-weight: bold; font-family: Arial, Verdana, sans-serif;")

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
slider.setGeometry(250, 130, 50, 180)
slider.setRange(0, 50)
slider.setStyleSheet("background-color: #ffffff; color: #22333b; font-size: 12px; border: 2px solid #ffffff; border-radius: 5px; font-family: Arial, Verdana, sans-serif;")

label2 = QLabel("0", main_screen)
label2.setGeometry(350, 130, 100, 40)
label2.setStyleSheet("background-color: #22333b; border: 2px solid #ffffff; border-radius: 5px; font-size: 15px;")

btn1 = QPushButton("GERAR", main_screen)
btn1.setGeometry(350, 200, 100, 40)
btn1.setStyleSheet("background-color: #22333b; border: 2px solid #ffffff; border-radius: 5px;")

btn2 = QPushButton("SALVAR", main_screen)
btn2.setGeometry(350, 270, 100, 40)
btn2.setStyleSheet("background-color: #22333b; border: 2px solid #ffffff; border-radius: 5px;")

btn3 = QPushButton("SENHAS SALVAS", main_screen)
btn3.setGeometry(50, 340, 400, 40)
btn3.setStyleSheet("background-color: #22333b; border: 2px solid #ffffff; border-radius: 5px;")

