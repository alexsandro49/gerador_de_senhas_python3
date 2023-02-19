from random import randrange


def generate_password(opc1, opc2, opc3, opc4, value):
    senha = ""
    selecao = []

    if opc1:
        selecao += maiusculas
    if opc2:
        selecao += minusculas
    if opc3:
        selecao += numeros
    if opc4:
        selecao += simbolos

    if len(selecao) == 0 and value > 0:
        return
    else:
        for i in range(0, value):
            senha += selecao[randrange(len(selecao))]
        return senha


maiusculas = ["A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N", "O", "P", "Q", "R", "S", "T", "U", "V", "W", "X", "Y", "Z"]
minusculas = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z"]
numeros = ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9"]
simbolos = ['"', "'", "!", "@", "#", "$", "%", "¨", "&", "*", "(", ")", "-", "+", "£", "¢", "¬", "_", "=", "§", "\ ", "|", ",", ".", ";", "/", "~", "]", "´", "[", "<", ">", ":", "?", "^", "}", "`", "{", "°", "º", "ª"]
