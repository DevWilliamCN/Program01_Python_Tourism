import mysql.connector
import datetime

mydb = mysql.connector.connect(
    host="localhost",
    user="root",
    passwd="",
    database="turismo"
)

micursor = mydb.cursor()


#####################Clase turista####################

class turista:
    def _init_(self, numero_Turista,nombre_Turista, pais_Turista):
        self.numero_Turista = numero_Turista
        self.nombre_Turista = nombre_Turista
        self.pais_Turista = pais_Turista

#####################Clase Destino####################


class destino:
    def _init_(self, numero_Destino, nombre_Sitio, tipo_Destino, continente):
        self.numero_Destino = numero_Destino
        self.nombre_Sitio = nombre_Sitio
        self.tipo_Destino = tipo_Destino
        self.continente = continente


#####################Clase Viaje####################

class viaje:
    def _init_(self, numero_Viaje, numero_Turista, numero_Destino, fecha_Salida, fecha_Llegada, ciudad_Salida):
        self.numero_Viaje = numero_Viaje
        self.numero_Turista = numero_Turista
        self.numero_Destino = numero_Destino
        self.fecha_Salida = fecha_Salida
        self.fecha_Llegada = fecha_Llegada
        self.ciudad_Salida = ciudad_Salida


#####################Funciones####################

def registrar_turista(numero_Turista, nombre_Turista, pais_Turista):
    try:
        sql = "INSERT INTO Turistas (numeroTurista, nombreTurista, paisTurista) VALUES (%s, %s, %s)"
        val = (numero_Turista, nombre_Turista, pais_Turista)
        micursor.execute(sql, val)
        mydb.commit()
        print("Se ha registrado el turista con exito")
    except:
        print("Hubo un problema al registrar al turista")

def comprar_tiquete(numero_Turista, numero_Destino, fecha_Salida, ciudad_Salida):
    try:
        contiene_turista = False
        sql = "SELECT * FROM Turistas WHERE numeroTurista = %s"
        val = (numero_Turista,)
        micursor.execute(sql, val)
        result = micursor.fetchall()
        for x in result:
            if x[0] == numero_Turista:
                contiene_turista = True
        if contiene_turista == True:
            contiene_destino = False
            sql = "SELECT * FROM Destinos WHERE numeroDestino = %s"
            val = (numero_Destino,)
            micursor.execute(sql, val)
            result = micursor.fetchall()
            for x in result:
                if x[0] == numero_Destino:
                    contiene_destino = True
            if contiene_destino == True:
                costo_tiquete = 0
                sql = "SELECT continente FROM Destinos WHERE numeroDestino = %s"
                val = (numero_Destino,)
                micursor.execute(sql, val)
                result = micursor.fetchall()
                continente_destino = result[0][0]
                if continente_destino == "América":
                    costo_tiquete = 850
                elif continente_destino == "Africa":
                    costo_tiquete = 3500
                elif continente_destino == "Asia":
                    costo_tiquete = 3800
                elif continente_destino == "Europa":
                    costo_tiquete = 2750
                elif continente_destino == "Oceanía":
                    costo_tiquete = 4500
                if fecha_Salida.month == 12:
                    costo_tiquete = costo_tiquete * 1.15
                numero_Viaje = str(numero_Turista) + str(numero_Destino) + str(fecha_Salida)
                sql = "INSERT INTO Viajes (numeroViaje, numeroTurista, numeroDestino, fechaSalida, fechaLlegada, ciudadSalida) VALUES (%s, %s, %s, %s, %s, %s)"
                val = (numero_Viaje, numero_Turista, numero_Destino, fecha_Salida, fecha_Salida + datetime.timedelta(days=14), ciudad_Salida)
                micursor.execute(sql, val)
                mydb.commit()
                print("Se ha realizado la compra con éxito")
                print("Los datos de la compra son los siguientes:")
                print("Número de viaje: " + numero_Viaje)
                print("Nombre del Turista: " + nombre_Turista)
                print("Nombre del Sitio: " + nombre_Sitio)
                print("Fecha de Salida: " + str(fecha_Salida))
                print("Continente: " + continente_destino)
                print("Precio del tiquete: " + str(costo_tiquete))
                print("Ciudad de Salida: " + ciudad_Salida)
            else:
                print("La agencia no ofrece viajes a este destino")
        else:
            print("El turista no está registrado")
    except:
        print("Hubo un problema al realizar la compra")

def informacion_ventas():
    try:
        sql = "SELECT * FROM Viajes"
        micursor.execute(sql)
        result = micursor.fetchall()
        for x in result:
            numero_Turista = x[1]
            numero_Destino = x[2]
            fecha_Salida = x[3]
            sql = "SELECT nombreTurista FROM Turistas WHERE numeroTurista = %s"
            val = (numero_Turista,)
            micursor.execute(sql, val)
            result = micursor.fetchall()
            nombre_Turista = result[0][0]
            sql = "SELECT nombreSitio, continente FROM Destinos WHERE numeroDestino = %s"
            val = (numero_Destino,)
            micursor.execute(sql, val)
            result = micursor.fetchall()
            nombre_Sitio = result[0][0]
            continente = result[0][1]
            print("Número de viaje: " + x[0])
            print("Nombre del Turista: " + nombre_Turista)
            print("Nombre del Sitio: " + nombre_Sitio)
            print("Fecha de Salida: " + str(fecha_Salida))
            print("Continente: " + continente)
            print()
    except:
        print("Hubo un problema al obtener la información")

def monto_total_recaudado():
    try:
        sql = "SELECT * FROM Viajes"
        micursor.execute(sql)
        result = micursor.fetchall()
        monto_total = 0
        for x in result:
            numero_Destino = x[2]
            fecha_Salida = x[3]
            sql = "SELECT continente FROM Destinos WHERE numeroDestino = %s"
            val = (numero_Destino,)
            micursor.execute(sql, val)
            result = micursor.fetchall()
            continente_destino = str(result[0][0])
            print(continente_destino)
            if continente_destino == "América":
                costo_tiquete = 850
            elif continente_destino == "Àfrica":
                costo_tiquete = 3500
            elif continente_destino == "Asia":
                costo_tiquete = 3800
            elif continente_destino == "Europa":
                costo_tiquete = 2750
            elif continente_destino == "Oceania":
                costo_tiquete = 4500
            if fecha_Salida.month == 12:
                costo_tiquete = costo_tiquete * 1.15
            monto_total = monto_total + costo_tiquete
        print("El monto total recaudado hasta el momento es: " + str(monto_total))
    except:
        print("Hubo un problema al obtener el monto total recaudado")

def cantidad_turistas_continente(continente):
    try:
        sql = "SELECT * FROM Viajes"
        micursor.execute(sql)
        result = micursor.fetchall()
        contador = 0
        for x in result:
            numero_Destino = x[2]
            sql = "SELECT continente FROM Destinos WHERE numeroDestino = %s"
            val = (numero_Destino,)
            micursor.execute(sql, val)
            result = micursor.fetchall()
            continente_destino = result[0][0]
            if continente_destino == continente:
                contador += 1
        print("La cantidad de turistas que han comprado tíquetes para países que se encuentran en el continente " + continente + " es de: " + str(contador))
    except:
        print("Hubo un problema al obtener la cantidad de turistas")

#####################Programa Principal####################

numero_Turista = int(input("Ingrese el número de turista: "))
sql = "SELECT * FROM Turistas WHERE numeroTurista = %s"
val = (numero_Turista,)
micursor.execute(sql, val)
result = micursor.fetchall()
if len(result) == 0:
    nombre_Turista = input("Ingrese el nombre del turista: ")
    pais_Turista = input("Ingrese el país del turista: ")
    registrar_turista(numero_Turista, nombre_Turista, pais_Turista)
numero_Destino = int(input("Ingrese el número de destino: "))
sql = "SELECT * FROM Destinos WHERE numeroDestino = %s"
val = (numero_Destino,)
micursor.execute(sql, val)
result = micursor.fetchall()
if len(result) == 0:
    print("La agencia no ofrece viajes a este destino")
else:
    nombre_Sitio = result[0][1]
    fecha_Salida = datetime.datetime.strptime(input("Ingrese la fecha de salida (dd/mm/aaaa): "), "%d/%m/%Y")
    ciudad_Salida = input("Ingrese la ciudad de salida: ")
    comprar_tiquete(numero_Turista, numero_Destino, fecha_Salida, ciudad_Salida)

print("Información de Ventas: ")
informacion_ventas()

print("Monto Total Recaudado: ")
monto_total_recaudado()

continente = input("Ingrese el nombre del continente: ")
print("Cantidad de Turistas en " + continente + ": ")
cantidad_turistas_continente(continente)