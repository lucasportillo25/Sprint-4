#Defino librerias a utilixar
import csv
from distutils.file_util import write_file
import datatime as dt

#Defino constantes y variables
amigos = []

#Defino funciones
def readFile():
    file = open("phonebook.csv", "r")
    csvfile = csv.reader(file)
    for row in csvfile:
        if row in csvfile:
            if row != []:
                data = {"nombre":row[0], "Apellido":row[1], "Teléfono": row[2], "Cumpleaños": row[3]}
                #amigos.append(data)
    file.close()
    return cheques

def grabarAmigos():
    nombre = input("Ingrese nombre: ")
    apellido = input("Ingrese apellido: ")
    telefono = input("Ingrese telefono: ")
    cumpleaños = input("Ingrese cumpleaños: ")
    data = {"Nombre":nombre, "Apellido":apellido, "Telefono": telefono, "Cumpleaños": cumpleaños}
    amigos.append(data)
    writeFile(amigos)

def printAmigos(amigos):
    for amigo in amigos:
        csvfile.writerow(amigo['Nombre'], amigo ['Apellido'],amigo['Telefono'], amigo['Cumpleaños'] )
    file.close()

def BuscarPorDni(dni, tipo):
    busqueda = []
    cantidad = 0
    cheques = readFile(urlfile)
    for cheque in cheques:
        if cheque["DNI"] == dni and cheque["TIPO"] == tipo:
            cantidad += 1
            busqueda.append(cheque)

def grabarCSV(dni, busqueda):
    file = open(dni + "_" + str(datatime) +".csv", "w")
    csvfile = csv.writer(file)
    for row in busqueda:
        csvfile.writerow([row["NumeroCuentaOrigen"], row["Valor"], row["FechaOrigen"], row["FechaPago"]])
    file.close()
    print("Se grabo el archivo CSV")  

#Defino el método principal
if __name__ == "__main__":
    while runtime:
        print(opciones)
        op = input()
        if op == "1":
            urlfile = input("Ingrese el nombre del archivo que contiene los cheques: \n")
            dni = input("Ingrese el DNI del usuario a consultar: \n")
            tipo = input("Seleccione el tipo de cheque a buscar EMITIDO o DEPOSITADO: \n")
            salida = input("Elija si desea recibir la salida por PANTALLA o CSV: \n")
            try:
                resultado = BuscarPorDni(dni, tipo)
                if salida == "PANTALLA":
                    print(resultado)
                elif salida == "CSV":
                    grabarCSV(resultado)
            except:
                print("Ingreso un dato erroneo")
            continue
        else:
            runtime = False