import sys
import sqlite3
from sqlite3 import Error
import pandas as pd
import os
import numpy as np
import json



def guardar_alumno():
    try:
        with sqlite3.connect("PIA2.db") as conn:
            mi_cursor = conn.cursor()
            mi_cursor.execute("CREATE TABLE IF NOT EXISTS alumno (matricula INTEGER PRIMARY KEY, nombre TEXT NOT NULL);")
            print("Tabla creada exitosamente")
            
            valores = {"matricula":campo_matricula, "nombre":campo_nombre}
            mi_cursor.execute("INSERT INTO alumno VALUES(:matricula,:nombre)", valores)
            print("*** PROYECTO AGREGADO EXITOSAMENTE ***")
            print("")
    except Error as e:
        print (e)
    except:
        print(f"Se produjo el siguiente error: {sys.exc_info()[0]}")
    finally:
        conn.close()
#------------------------------------------------------------------------------------
def reporte_alumnos():
    try:
        with sqlite3.connect("PIA2.db") as conn:
            mi_cursor = conn.cursor()
            mi_cursor.execute("SELECT * FROM alumno")
            registros = mi_cursor.fetchall()
        
            print("Matricula\tNombre")
            print("*" * 30)
            
            
            for matricula, nombre in registros:
                print(f"{matricula}\t", end="")
                print(nombre)
    except Error as e:
        print (e)
    except:
        print(f"Se produjo el siguiente error: {sys.exc_info()[0]}")
    finally:
        conn.close()
#------------------------------------------------------------------------------------        
def guardar_materia():
    try:
        with sqlite3.connect("PIA2.db") as conn:
            mi_cursor = conn.cursor()
            mi_cursor.execute("CREATE TABLE IF NOT EXISTS materia (id_materia INTEGER PRIMARY KEY, nombre TEXT NOT NULL);")
            print("Tabla creada exitosamente")
            
            valores = {"id_materia":id_materia, "nombre":campo_nombre_materia}
            mi_cursor.execute("INSERT INTO materia VALUES(:id_materia,:nombre)", valores)
            print("*** PROYECTO AGREGADO EXITOSAMENTE ***")
            print("")
    except Error as e:
        print (e)
    except:
        print(f"Se produjo el siguiente error: {sys.exc_info()[0]}")
    finally:
        conn.close()
#---------------------------------------------------------------------------------------
def generar_calif():
    try:
        with sqlite3.connect("PIA2.db") as conn:
            global valores
            global campo_calificaciones
            mi_cursor = conn.cursor()
            mi_cursor.execute("CREATE TABLE IF NOT EXISTS calificaciones (ID_alumno   PRIMARY KEY REFERENCES alumno (matricula), ID_materia  REFERENCES materia (id_materia), ID_cal      REFERENCES Rangos_Calif (id_cal), ID_periodo  REFERENCES periodo (id_periodo) );")
            mi_cursor.execute
            print("Tabla creada exitosamente")
    except Error as e:
        print (e)
    except:
        print(f"Se produjo el siguiente error: {sys.exc_info()[0]}")
    finally:
        conn.close()

def guardar_cantidad():
    try:
        with sqlite3.connect("PIA2.db") as conn:
            mi_cursor = conn.cursor()
            mi_cursor.execute("CREATE TABLE IF NOT EXISTS Rangos_Calif (id_cal INTEGER PRIMARY KEY, cantidad INTEGER NOT NULL);")
            print("Tabla creada exitosamente")
            
            valores = {"id_cal":id_cal, "cantidad":campo_cantidad}
            mi_cursor.execute("INSERT INTO Rangos_Calif VALUES(:id_cal,:cantidad)", valores)
            print("*** PROYECTO AGREGADO EXITOSAMENTE ***")
            print("")
    except Error as e:
        print (e)
    except:
        print(f"Se produjo el siguiente error: {sys.exc_info()[0]}")
    finally:
        conn.close()

def guardar_periodo():
    try:
        with sqlite3.connect("PIA2.db") as conn:
            mi_cursor = conn.cursor()
            mi_cursor.execute("CREATE TABLE IF NOT EXISTS periodo (id_periodo INTEGER PRIMARY KEY, año INTEGER NOT NULL, mes TEXT NOT NULL);")
            print("Tabla creada exitosamente")
            
            valores = {"id_periodo":id_periodo, "año":campo_año, "mes":campo_mes}
            mi_cursor.execute("INSERT INTO periodo VALUES(:id_periodo,:año,:mes)", valores)
            print("*** PROYECTO AGREGADO EXITOSAMENTE ***")
            print("")
    except Error as e:
        print (e)
    except:
        print(f"Se produjo el siguiente error: {sys.exc_info()[0]}")
    finally:
        conn.close()


#-----------------------------------------------------------------------------------------
def desplegar_menu_principal():
    print("**********************")
    print("*** MENÚ PARA EXPORTAR A SQLITE ***")
    print("**********************")
    print("\n1) Agregar alumno.")
    print("2) Consultar Alumnos.")
    print("3) Agregar materia.")
    print("4) Agregar rangos de calificaciones.")
    print("5) Agregar periodo escolar.")
    print("6) Tercera forma Normal")
    print("7) Regresar al menu")
    
def baseDeDatos():
#Código principal_SQL
        ciclo_principal = True

        while ciclo_principal:
            continuar = True
            desplegar_menu_principal()
            opcion = int(input("\n Indique su elección: "))
            
            if opcion == 1:#Agregar
                while continuar:
                    print("")
                    print("*****************************************************************************************")
                    print("* Proporcione los datos del proyecto a AGREGAR, capture la clave 0 (cero) para terminar *")
                    print("*****************************************************************************************")
                    global campo_matricula
                    campo_matricula = int(input("Matricula del alumno agregar: "))
                    if campo_matricula == 0:
                        continuar = False
                    else:
                        global campo_nombre
                        campo_nombre = input("Nombre del alumno a agregar: ")
                        guardar_alumno()
            
            if opcion == 2:#Mostrar Alumnos
                reporte_alumnos()
            
            if opcion == 3:#Agregar
                while continuar:
                    print("")
                    print("*****************************************************************************************")
                    print("* Proporcione los datos del proyecto a AGREGAR, capture la clave 0 (cero) para terminar *")
                    print("*****************************************************************************************")
                    global id_materia
                    id_materia = int(input("ID de la materia a agregar: "))
                    if id_materia == 0:
                        continuar = False
                    else:
                        global campo_nombre_materia
                        campo_nombre_materia = input("Nombre de la materia a agregar: ")
                        guardar_materia()
            
            if opcion == 4:#Agrega rangos de calificaciones
                while continuar:
                    print("")
                    print("******************************************************************************************************************************")
                    print("* Proporcione los rangos de las calificaciones a AGREGAR, se recomienda del 1 al 10, capture la clave 0 (cero) para terminar *")
                    print("******************************************************************************************************************************")
                    global id_cal
                    id_cal = int(input("ID de la calificacion: "))
                    if id_cal == 0:
                        continuar = False
                    else:
                        global campo_cantidad
                        campo_cantidad = input("Cantidad de la calificacion: ")
                        guardar_cantidad()
            
            if opcion == 5:#Agregar periodos
                while continuar:
                    print("")
                    print("*******************************************************************************")
                    print("* Proporcione los periodos a AGREGAR, capture la clave 0 (cero) para terminar *")
                    print("*******************************************************************************")
                    global id_periodo
                    id_periodo = int(input("ID del periodo: "))
                    if id_periodo == 0:
                        continuar = False
                    else:
                        global campo_año
                        campo_año = input("Año del periodo: ")
                        global campo_mes
                        campo_mes = input("Mes del periodo: ")
                        guardar_periodo()
            
            if opcion == 6:#3NF
                generar_calif()

            elif opcion == 7:#Salir
                ciclo_principal = False
            else:
                print(f"Lo siento, la opción *{opcion}* no es una opción válida")
                print("")



#-----------------------------------------------------------------------------------------
nombres_alumnos = []

asignatura_progra = []
asignatura_basedatos = []
asignatura_conta = []
asignatura_estadistica = []
asignatura_macro = []

Separador = ("-" * 80) + "\n"


def reporte_materias_estudiantes():
    alumnos_asignaturas= {nombres_alumnos[0]:[asignatura_progra[0], asignatura_basedatos[0], asignatura_conta[0], asignatura_estadistica[0],
    asignatura_macro[0]], nombres_alumnos[1]:[asignatura_progra[1], asignatura_basedatos[1], asignatura_conta[1], asignatura_estadistica[1],
    asignatura_macro[1]], nombres_alumnos[2]:[asignatura_progra[2], asignatura_basedatos[2], asignatura_conta[2], asignatura_estadistica[2],
    asignatura_macro[2]], nombres_alumnos[3]:[asignatura_progra[3], asignatura_basedatos[3], asignatura_conta[3], asignatura_estadistica[3],
    asignatura_macro[3]], nombres_alumnos[4]:[asignatura_progra[4], asignatura_basedatos[4], asignatura_conta[4], asignatura_estadistica[4],
    asignatura_macro[4]], nombres_alumnos[5]:[asignatura_progra[5], asignatura_basedatos[5], asignatura_conta[5], asignatura_estadistica[5],
    asignatura_macro[5]], nombres_alumnos[6]:[asignatura_progra[6], asignatura_basedatos[6], asignatura_conta[6], asignatura_estadistica[6],
    asignatura_macro[6]], nombres_alumnos[7]:[asignatura_progra[7], asignatura_basedatos[7], asignatura_conta[7], asignatura_estadistica[7],
    asignatura_macro[7]], nombres_alumnos[8]:[asignatura_progra[8], asignatura_basedatos[8], asignatura_conta[8], asignatura_estadistica[8],
    asignatura_macro[8]], nombres_alumnos[9]:[asignatura_progra[9], asignatura_basedatos[9], asignatura_conta[9], asignatura_estadistica[9],
    asignatura_macro[9]], nombres_alumnos[10]:[asignatura_progra[10], asignatura_basedatos[10], asignatura_conta[10], asignatura_estadistica[10],
    asignatura_macro[10]], nombres_alumnos[11]:[asignatura_progra[11], asignatura_basedatos[11], asignatura_conta[11], asignatura_estadistica[11],
    asignatura_macro[11]], nombres_alumnos[12]:[asignatura_progra[12], asignatura_basedatos[12], asignatura_conta[12], asignatura_estadistica[12],
    asignatura_macro[12]], nombres_alumnos[13]:[asignatura_progra[13], asignatura_basedatos[13], asignatura_conta[13], asignatura_estadistica[13],
    asignatura_macro[13]], nombres_alumnos[14]:[asignatura_progra[14], asignatura_basedatos[14], asignatura_conta[14], asignatura_estadistica[14],
    asignatura_macro[14]], nombres_alumnos[15]:[asignatura_progra[15], asignatura_basedatos[15], asignatura_conta[15], asignatura_estadistica[15],
    asignatura_macro[15]], nombres_alumnos[16]:[asignatura_progra[16], asignatura_basedatos[16], asignatura_conta[16], asignatura_estadistica[16],
    asignatura_macro[16]], nombres_alumnos[17]:[asignatura_progra[17], asignatura_basedatos[17], asignatura_conta[17], asignatura_estadistica[17],
    asignatura_macro[17]], nombres_alumnos[18]:[asignatura_progra[18], asignatura_basedatos[18], asignatura_conta[18], asignatura_estadistica[18],
    asignatura_macro[18]], nombres_alumnos[19]:[asignatura_progra[19], asignatura_basedatos[19], asignatura_conta[19], asignatura_estadistica[19],
    asignatura_macro[19]], nombres_alumnos[20]:[asignatura_progra[20], asignatura_basedatos[20], asignatura_conta[20], asignatura_estadistica[20],
    asignatura_macro[20]], nombres_alumnos[21]:[asignatura_progra[21], asignatura_basedatos[21], asignatura_conta[21], asignatura_estadistica[21],
    asignatura_macro[21]], nombres_alumnos[22]:[asignatura_progra[22], asignatura_basedatos[22], asignatura_conta[22], asignatura_estadistica[22],
    asignatura_macro[22]], nombres_alumnos[23]:[asignatura_progra[23], asignatura_basedatos[23], asignatura_conta[23], asignatura_estadistica[23],
    asignatura_macro[23]], nombres_alumnos[24]:[asignatura_progra[24], asignatura_basedatos[24], asignatura_conta[24], asignatura_estadistica[24],
    asignatura_macro[24]], nombres_alumnos[25]:[asignatura_progra[25], asignatura_basedatos[25], asignatura_conta[25], asignatura_estadistica[25],
    asignatura_macro[25]], nombres_alumnos[26]:[asignatura_progra[26], asignatura_basedatos[26], asignatura_conta[26], asignatura_estadistica[26],
    asignatura_macro[26]], nombres_alumnos[27]:[asignatura_progra[27], asignatura_basedatos[27], asignatura_conta[27], asignatura_estadistica[27],
    asignatura_macro[27]], nombres_alumnos[28]:[asignatura_progra[28], asignatura_basedatos[28], asignatura_conta[28], asignatura_estadistica[28],
    asignatura_macro[28]], nombres_alumnos[29]:[asignatura_progra[29], asignatura_basedatos[29], asignatura_conta[29], asignatura_estadistica[29],
    asignatura_macro[29]]}
    frame_totales = pd.DataFrame(alumnos_asignaturas)
    frame_totales.index=["Progra", "Base", "Conta ", "Estadística ", "Macro"]
    estadisticos_descriptivos_estudiantes= frame_totales.T.describe()
    opciones=0
    while opciones != 5:
        print(Separador)
        print("----- Reporte Estadistico Descriptivo por materia y por estudiante -----")
        print("[1] Mostrar reporte estadístico descriptivo por materia")
        print("[2] Mostrar reporte estadístico descriptivo por estudiante")
        print("[3] Exportar reporte estadístico descriptivo por materia")
        print("[4] Exportar reporte estadístico descriptivo por estudiante")
        print("[5] Regresar al menú principal")
        i= input("Selecciona una opción del menú: ")
        if i =="1":
            print("Reporte Estadístico Descriptivo por materia")
            print(estadisticos_descriptivos_estudiantes)
        elif i =="2":
            
            for est in alumnos_asignaturas:
                print("\nReporte Estadistico Descriptivo por estudiante:")
                print(" ")
                print("Alumno:",est)
                reportes_calf = frame_totales[est].describe()
                print(reportes_calf)
                reporte_estudiante= frame_totales.describe()
        elif i =="3":
            print("Exportar reporte por materia a txt")
            estadisticos_descriptivos_estudiantes.to_csv(r'C:\Users\TortillaCaliente\Desktop\reporte_materia.txt')
        elif i =="4":
            print("Exportar reporte por estudiante a txt")
            reporte_estudiante.to_csv(r'C:\Users\TortillaCaliente\Desktop\reporte_estudiante.txt')
        elif i =="5":
            opciones= 5
        else:
            print("Selecciona una opción del menú: ")


def menu():
    OpcionMenu = 0
    salir = 10
    
    while OpcionMenu != salir:
        print("---MENU--- Seleccione la opcion deseada: \n [1] Ingresar Alumnos \n [2] Ingresar Calificaciones de Estructuras de datos y su procesamiento \n [3] Ingresar Calificaciones de Programación de bases de datos \n [4] Ingresar Calificaciones de Contabilidad Administrativa \n [5] Ingresar Calificaciones de Estadística descriptiva \n [6] Ingresar Calificaciones de Macroeconomía \n [7] Mostrar todas las calificaciones del alumnado \n [8] Asignaturas con el desempeño más bajo \n [9] Alumnos que reprobaron dos o más asignaturas \n [10] Exportar a disco el listado de las Calif. de estudiantes en formato CSV \n [11] Exportar a disco el listado de las Calif. de estudiantes en formato JSON \n [12] Reporte Estadistico Descriptivo por materia y por estudiante \n [13] SQLite \n [14] Cerrar programa ")
        opcion = input()
        
        if opcion == "1":
            print (" ---- Has seleccionado ingresar los nombres de 30 alumnos ---- ")
            for nombres in range(30):
                nombres_alumnos.append(input("Nombres de los Alumnos iniciando por su apellido paterno: " ))
                print(nombres_alumnos)
                os.system('cls')
        
        if opcion == "2":
            for calif_progra in range(30):
                asignatura_progra.append(int(input("Dime la calificación de la asignatura Estructuras de datos y su procesamiento: ")))
                print(asignatura_progra)
                os.system('cls')
        
        if opcion == "3":
            for calif_basedatos in range(30):
                asignatura_basedatos.append(int(input("Dime la calificación de la asignatura Programación de bases de datos: ")))
                print(asignatura_basedatos)
                os.system('cls')
    
        if opcion == "4":
            for calif_conta in range(30):
                asignatura_conta.append(int(input("Dime la calificación de la asignatura Contabilidad Administrativa: ")))
                print(asignatura_conta)
                os.system('cls')

        if opcion == "5":
            for calif_estadistica in range(30):
                asignatura_estadistica.append(int(input("Dime la calificación de la asignatura Estadística descriptiva: ")))
                print(asignatura_estadistica)
                os.system('cls')

        if opcion == "6":
            for calif_macro in range(30):
                asignatura_macro.append(int(input("Dime la calificación de la asignatura Macroeconomía: ")))
                print(asignatura_macro)
                os.system('cls')
        
        if opcion == "7":
            alumnos_asignaturas= {nombres_alumnos[0]:[asignatura_progra[0], asignatura_basedatos[0], asignatura_conta[0], asignatura_estadistica[0],
asignatura_macro[0]], nombres_alumnos[1]:[asignatura_progra[1], asignatura_basedatos[1], asignatura_conta[1], asignatura_estadistica[1],
asignatura_macro[1]], nombres_alumnos[2]:[asignatura_progra[2], asignatura_basedatos[2], asignatura_conta[2], asignatura_estadistica[2],
asignatura_macro[2]], nombres_alumnos[3]:[asignatura_progra[3], asignatura_basedatos[3], asignatura_conta[3], asignatura_estadistica[3],
asignatura_macro[3]], nombres_alumnos[4]:[asignatura_progra[4], asignatura_basedatos[4], asignatura_conta[4], asignatura_estadistica[4],
asignatura_macro[4]], nombres_alumnos[5]:[asignatura_progra[5], asignatura_basedatos[5], asignatura_conta[5], asignatura_estadistica[5],
asignatura_macro[5]], nombres_alumnos[6]:[asignatura_progra[6], asignatura_basedatos[6], asignatura_conta[6], asignatura_estadistica[6],
asignatura_macro[6]], nombres_alumnos[7]:[asignatura_progra[7], asignatura_basedatos[7], asignatura_conta[7], asignatura_estadistica[7],
asignatura_macro[7]], nombres_alumnos[8]:[asignatura_progra[8], asignatura_basedatos[8], asignatura_conta[8], asignatura_estadistica[8],
asignatura_macro[8]], nombres_alumnos[9]:[asignatura_progra[9], asignatura_basedatos[9], asignatura_conta[9], asignatura_estadistica[9],
asignatura_macro[9]], nombres_alumnos[10]:[asignatura_progra[10], asignatura_basedatos[10], asignatura_conta[10], asignatura_estadistica[10],
asignatura_macro[10]], nombres_alumnos[11]:[asignatura_progra[11], asignatura_basedatos[11], asignatura_conta[11], asignatura_estadistica[11],
asignatura_macro[11]], nombres_alumnos[12]:[asignatura_progra[12], asignatura_basedatos[12], asignatura_conta[12], asignatura_estadistica[12],
asignatura_macro[12]], nombres_alumnos[13]:[asignatura_progra[13], asignatura_basedatos[13], asignatura_conta[13], asignatura_estadistica[13],
asignatura_macro[13]], nombres_alumnos[14]:[asignatura_progra[14], asignatura_basedatos[14], asignatura_conta[14], asignatura_estadistica[14],
asignatura_macro[14]], nombres_alumnos[15]:[asignatura_progra[15], asignatura_basedatos[15], asignatura_conta[15], asignatura_estadistica[15],
asignatura_macro[15]], nombres_alumnos[16]:[asignatura_progra[16], asignatura_basedatos[16], asignatura_conta[16], asignatura_estadistica[16],
asignatura_macro[16]], nombres_alumnos[17]:[asignatura_progra[17], asignatura_basedatos[17], asignatura_conta[17], asignatura_estadistica[17],
asignatura_macro[17]], nombres_alumnos[18]:[asignatura_progra[18], asignatura_basedatos[18], asignatura_conta[18], asignatura_estadistica[18],
asignatura_macro[18]], nombres_alumnos[19]:[asignatura_progra[19], asignatura_basedatos[19], asignatura_conta[19], asignatura_estadistica[19],
asignatura_macro[19]], nombres_alumnos[20]:[asignatura_progra[20], asignatura_basedatos[20], asignatura_conta[20], asignatura_estadistica[20],
asignatura_macro[20]], nombres_alumnos[21]:[asignatura_progra[21], asignatura_basedatos[21], asignatura_conta[21], asignatura_estadistica[21],
asignatura_macro[21]], nombres_alumnos[22]:[asignatura_progra[22], asignatura_basedatos[22], asignatura_conta[22], asignatura_estadistica[22],
asignatura_macro[22]], nombres_alumnos[23]:[asignatura_progra[23], asignatura_basedatos[23], asignatura_conta[23], asignatura_estadistica[23],
asignatura_macro[23]], nombres_alumnos[24]:[asignatura_progra[24], asignatura_basedatos[24], asignatura_conta[24], asignatura_estadistica[24],
asignatura_macro[24]], nombres_alumnos[25]:[asignatura_progra[25], asignatura_basedatos[25], asignatura_conta[25], asignatura_estadistica[25],
asignatura_macro[25]], nombres_alumnos[26]:[asignatura_progra[26], asignatura_basedatos[26], asignatura_conta[26], asignatura_estadistica[26],
asignatura_macro[26]], nombres_alumnos[27]:[asignatura_progra[27], asignatura_basedatos[27], asignatura_conta[27], asignatura_estadistica[27],
asignatura_macro[27]], nombres_alumnos[28]:[asignatura_progra[28], asignatura_basedatos[28], asignatura_conta[28], asignatura_estadistica[28],
asignatura_macro[28]], nombres_alumnos[29]:[asignatura_progra[29], asignatura_basedatos[29], asignatura_conta[29], asignatura_estadistica[29],
asignatura_macro[29]]}
            
            frame_totales = pd.DataFrame(alumnos_asignaturas)
            frame_totales.index=["Progra", "Base", "Conta ", "Estadística ", "Macro"]
            print(Separador)
            print(frame_totales.T)
            os.system('cls')
            
 
        if opcion == "8":
            print(Separador)
            print("Estas son las asignaturas con sus estadísticos descriptivos:")
            frame_totales = pd.DataFrame(alumnos_asignaturas)
            frame_totales.index=["Progra", "Base", "Conta ", "Estadística ", "Macro"]
            estadisticos_descriptivos = frame_totales.T.describe()
            print(estadisticos_descriptivos)
            
            print(Separador)
            print("Estos son los promedios finales de las asignaturas:")
            promedio_asignaturas= frame_totales.T.mean()
            print(promedio_asignaturas)
            
            print(Separador)
            print("Este fue el promedio más bajo de las asignaturas:")
            promedio_bajo= promedio_asignaturas.min()
            print(promedio_bajo)
            os.system('cls')
            
        if opcion == "9":
            print(Separador)
            print("Estos son los alumnos que no acreditaron:")
            reprobados=frame_totales[frame_totales <= 69]
            print(reprobados.T)
            os.system('cls')
        
        if opcion == "10":
            print(Separador)
            print("Se ha exportado a disco el listado de las calificaciones obtenidas por los estudiantes en formato CSV, favor de verificar su escritorio.")
            frame_totales.T.to_csv(r'C:\Users\TortillaCaliente\Desktop\export_dataframe.csv')
            print(Separador)
            
        if opcion == "11":
            print(Separador)
            print("Se ha exportado a disco el listado de las calificaciones obtenidas por los estudiantes en formato JSON, favor de verificar su escritorio.")
            frame_totales.T.to_json(r'C:\Users\TortillaCaliente\Desktop\export_dataframe.json')
            print(Separador)
            
        if opcion =="12":
            reporte_materias_estudiantes()
                       
        if opcion =="13":
            baseDeDatos()

              
        if opcion =="14":
            print("Se ha cerrado el programa...")
            os.system('cls')
            break
 
     
menu()




