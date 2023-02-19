import sqlite3
import screen1
import screen2

def save_data(password, about):
    banco = sqlite3.connect('database.db')
    cursor = banco.cursor()
    try:
        if len(password) > 0:
            cursor.execute(f"INSERT INTO passwords VALUES('{password}', '{about}');")
            banco.commit()
            banco.close()   

            #screen2.update_table() 
            print("Banco modificado com sucesso!")
    except sqlite3.Error as erro:
        print(f"Houve um erro: {erro}")

def show_data():
    banco = sqlite3.connect('database.db')
    cursor = banco.cursor()
    cursor.execute("SELECT * FROM passwords")  
    return cursor.fetchall()

def delete_data(data):
    banco = sqlite3.connect('database.db')
    cursor = banco.cursor()
    try:
        cursor.execute(f"DELETE FROM passwords WHERE about = '{data}'")
        banco.commit()
        banco.close()
        print("Banco modificado com sucesso!")
    except sqlite3.Error as erro:
        print(f"Houve um erro: {erro}")
