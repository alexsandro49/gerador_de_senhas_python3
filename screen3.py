import sys
import db_connection
from PyQt6.QtWidgets import QApplication, QWidget, QPushButton, QTableWidget, QTableWidgetItem

def update_table():
    global reverse

    data = db_connection.show_data()
    if reverse:
        data = data[::-1]
    if len(data) <= 12:
        data_table.setRowCount(12)
    else:
        data_table.setRowCount(len(data))

    for i in range(0, len(data)):
        data_table.setItem(i, 0, QTableWidgetItem(data[i][0]))
        data_table.setItem(i, 1, QTableWidgetItem(data[i][1]))

def delete_data():
    data = db_connection.show_data()  
    linha = data_table.currentRow()
    data_table.removeRow(linha)
    if linha >= len(data):
        return
    sobre = data[linha][1]
    db_connection.delete_data(sobre)

def reverse_state():
    global reverse

    if reverse:
        reverse = False
    else:
        reverse = True
    update_table()


app = QApplication(sys.argv)

passwords_screen = QWidget()
passwords_screen.resize(500, 500)
passwords_screen.setWindowTitle("Senhas salvas")
passwords_screen.setStyleSheet("background-color: #150050; color: #ffffff;")

btn1 = QPushButton("VOLTAR", passwords_screen)
btn1.setGeometry(20, 440, 80, 40)
btn1.setStyleSheet("background-color: #22333b; border: 2px solid #ffffff; border-radius: 5px;")

btn2 = QPushButton("INVERTER", passwords_screen)
btn2.setGeometry(305, 440, 80, 40)
btn2.setStyleSheet("background-color: #22333b; border: 2px solid #ffffff; border-radius: 5px;")

btn3 = QPushButton("DELETAR", passwords_screen)
btn3.setGeometry(400, 440, 80, 40)
btn3.setStyleSheet("background-color: #22333b; border: 2px solid #ffffff; border-radius: 5px;")

data_table = QTableWidget(passwords_screen)
data_table.setGeometry(20, 30, 460, 390)
data_table.setColumnCount(2)
data_table.setHorizontalHeaderLabels(["Senha", "Sobre"])
data_table.setColumnWidth(0, 140)
data_table.setColumnWidth(1, 320)

reverse = False
update_table()
