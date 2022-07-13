#Defino librerias a utilixar
import csv
from distutils.file_util import write_file
import datetime as dt
from tkinter.filedialog import Open

#Defino constantes y variables
filecsvdni2 = []
solicitardni = ""
identificarchequesrepetidos = []
chequesporpantalla = []

#Defino funciones

def readcsv(abrirarchivo):
    if abrirarchivo == "chequera":
        file = open("chequera.csv", "r")
        csvcheques = csv.reader(file)
        for linea in csvcheques:
            if linea != []:
                data = {"NroCheque":linea[0], "CodigoBanco":linea[1], "CodigoScurusal":linea[2], "NumeroCuentaOrigen":linea[3], "NumeroCuentaDestino":linea[4], "Valor":linea[5], "FechaOrigen":linea[6], "FechaPago":linea[7], "DNI":linea[8], "Estado":linea[9], "TIPO":linea[10]}
                filecsvdni2.append(data)
        file.close()
        print("A continuación le solicitaremos el DNI para poder realizar su consulta.")
    elif abrirarchivo != "chequera":
        print("El archivo no se encuentra")
        selectoption = input("1. Intenta nuevamente... \n2. Salir \n")
        if selectoption == "1":
            elegirarchivo()
        else:
            print("Muchas gracias por su consulta")
            exit()

def elegirarchivo():
    abrirarchivo = input("Ingrgese el nombre del archivo al que quiere ingresar: /n")
    readcsv(abrirarchivo)

def solicitudDNI():
    while True:
        try:
            solicitardni = int(input("Ingrese DNI: "))
            print("El DNI ingresado es: " + str(solicitardni))
            confirmacionDNI(solicitardni)
            break

        except ValueError:
            print("El DNI ingresado es incorrecto /n")
            print("Ingrese el DNI correctamente: ")
            solicitudDNI()
            False
            break

def confirmacionDNI(solicitardni):
    confirmar = input("Quiere continuar (s/n): ")
    if confirmar == "s" or confirmar == "n":
        if confirmar == "s":
            identificarcliente(solicitardni)
        elif confirmar == "n":
            return solicitudDNI()
        else:
            None
    else:
        print("El valor ingresado no es el correcto.")
        confirmacionDNI(solicitardni)

def identificarcliente(solicitardni):
        for elem in filecsvdni2:
            if str(solicitardni) == elem["DNI"]:
                y = elem["NroCheque"]
                identificarchequesrepetidos.append(y)
                for i in range(len(identificarchequesrepetidos)):
                    for j in range(len(identificarchequesrepetidos)):
                        if i != j:
                            if identificarchequesrepetidos[i] == identificarchequesrepetidos[j] and identificarchequesrepetidos[i] not in chequesporpantalla:
                                chequesporpantalla.append(identificarchequesrepetidos[i])
                                if len(chequesporpantalla) > 0:
                                    print("Se ha encontrado dos cheques con la misma numeración...")
                                    print("Muchas gracias por su consulta")
                                    exit()
                                else:
                                    None
                            else:
                                None
                        else:
                            None
            else:           
                None
        continuar(solicitardni)
        print("No se encontraron datos relacionados al DNI ingresado.")
        print("Muchas gracias por su consulta")
        exit()

def continuar(solicitardni):
    for elem in filecsvdni2:
        if str(solicitardni) == elem["DNI"]:
            y = elem["NroCheque"]
            identificarchequesrepetidos.append(y)
            for i in range(len(identificarchequesrepetidos)):
                for j in range(len(identificarchequesrepetidos)):
                    if i != j:
                        if identificarchequesrepetidos[i] == identificarchequesrepetidos[j] and identificarchequesrepetidos[i] not in chequesporpantalla:
                            chequesporpantalla.append(identificarchequesrepetidos[i])
                            if len(chequesporpantalla) > 0:
                                salida(solicitardni)
                                finalsaludo()
                                exit()
                            else:  
                                None
                        else:
                            None
                    else:
                        None
        else:
            None  


def BuscarPorDni(dni, tipo):
    busqueda = []
    cantidad = 0
    cheques = readFile(urlfile)
    for cheque in cheques:
        if cheque["DNI"] == dni and cheque["TIPO"] == tipo:
            cantidad += 1
            busqueda.append(cheque)

def grabarCSV(busqueda):
    file = open(dni + "_" + str(datetime) +".csv", "w")
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
        