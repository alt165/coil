# -*- coding: utf-8 -*-
"""
Created on Tue Oct 24 14:04:14 2023

@author: Cristian, Esteban, Pepe
"""

import datetime

from google.cloud import bigquery
from google.oauth2 import service_account

def validar_creacion_membresia(inputs_usuario: list):
    validado = False
    if len(inputs_usuario) > 3:
        raise Exception("ERROR al crear membresia: Demasiados Inputs")
    if len(str(inputs_usuario[0])) > 10:
        raise Exception("ERROR al crear membresia: ID incorrecto")
    if len(str(inputs_usuario[1])) > 20:
        raise Exception("ERROR al crear membresia: TIPO incorrecto")
    if str(inputs_usuario[2]) < str(datetime.datetime.now()):
        raise Exception("ERROR al crear membresia: VENCIMIENTO incorrecto")
    validado = True
    return validado

def crear_membresia(cliente: bigquery.Client, inputs_usuario: list):
    try:
        if validar_creacion_membresia(inputs_usuario):
            consulta = f"INSERT INTO `coil2023.Biblioteca.MEMBRESIA` (ID_MEMBRESIA, TIPO_MEMBRESIA, FECHA_VENCIM_MEMBRE) VALUES ({inputs_usuario[0]}, \"{inputs_usuario[1]}\", '{inputs_usuario[2]}')"
            query_job = client.query(consulta)
            datos_membresia = query_job.result()
            print("Creación exitosa")
            return True
        else:
            return False
    except Exception as exc:
        print(f"Error al crear membresia en la base de datos: {exc}")


def eliminar_membresia(id_membresia: int):
    try:
        #if validar_destruccion_membresia(inputs_usuario):
        consulta = f"DELETE FROM `coil2023.Biblioteca.MEMBRESIA` WHERE ID_MEMBRESIA = {id_membresia}"
        query_job = client.query(consulta)
        datos_membresia = query_job.result()
        print("Eliminación exitosa")
        return True
        #else:
        #    return False
    except Exception as exc:
        print(f"Error al borrar membresia en la base de datos: {exc}")

def modificar_membresia(id_membresia, tipo, vencimiento):
    try:
        inputs_usuario = [id_membresia, tipo, vencimiento]
        if validar_creacion_membresia(inputs_usuario):
            consulta = f"UPDATE `coil2023.Biblioteca.MEMBRESIA` SET TIPO_MEMBRESIA='{tipo}', FECHA_VENCIM_MEMBRE='{vencimiento}' WHERE ID_MEMBRESIA = {id_membresia}"
            query_job = client.query(consulta)
            datos_membresia = query_job.result()
            print("Modificación exitosa")
            return True
        else:
            return False
    except Exception as exc:
        print(f"Error al modificar membresia en la base de datos: {exc}")

def buscar_todas_membresias(cliente: bigquery.Client):
    query_job = client.query("SELECT * FROM `coil2023.Biblioteca.MEMBRESIA`")
    datos_membresia = query_job.result()
    
    return datos_membresia
#bien :^)

def buscar_membresia_especifica(client: bigquery.Client, inputs_usuario: list):
    consulta_SQL = generar_consulta(inputs_usuario)
    
    return buscar_consulta_especifica(client, consulta_SQL)
#bien :^)

def buscar_consulta_especifica(client: bigquery.Client, consulta: str):
    query_job = client.query(consulta)
    datos_membresia = query_job.result() 
    
    return datos_membresia
#bien :^)

def generar_consulta(consultas: list):
    campos: list = ["ID_MEMBRESIA",
                    "TIPO_MEMBRESIA",
                    "FECHA_VENCIM_MEMBRE"]
    
    # Genera una lista con los campos a agregar a la consulta en SQL.
    consulta: list = []
    
    # Datos de cada campo, respecto a la consulta correspondiente a cada campo.
    # Tiene los datos ingresados por el usuario.
    parametros: list = []
    
    # Indice para verificar la posición en la lista.
    indice: int = 0
    cant_inputs_vacios: int = 0
    
    for i in consultas:
        if (len(str(i)) > 0):
            consulta.append(campos[indice])
            parametros.append(i)
        else:
            cant_inputs_vacios += 1
        indice += 1
        
    if cant_inputs_vacios == len(consultas):
        return ""

    consulta_resultado: str = "SELECT * FROM `coil2023.Biblioteca.MEMBRESIA` WHERE"

    mas_de_un_campo = False

    for j in range(0, len(consulta)):
        if mas_de_un_campo:
            consulta_resultado += " AND "
        if consulta[j] == campos[0]:
            consulta_resultado += f" {consulta[j]} LIKE %{parametros[j]}%"
        elif consulta[j] == campos[1]:
            consulta_resultado += f" {consulta[j]} LIKE '%{parametros[j]}%'"
        else:
            consulta_resultado += f" {consulta[j]} = '{parametros[j]}'"
        mas_de_un_campo = True

    return consulta_resultado
#bien :^)


# Ruta al archivo de credenciales JSON.
credentials = service_account.Credentials.from_service_account_file('coil2023-6672f55c3eb6.json')

# Se instancia el cliente con las credenciales del proyecto COIL.
client = bigquery.Client(credentials=credentials, project=credentials.project_id)


#test = buscar_membresia_especifica(client, ["", "", "2023-05-05"])

#print(test)
#"2023-12-12"
fecha = datetime.date(2023,12,20)
#creado_nuevo = crear_membresia(client, [1234567890, "Testeador2", fecha])

fecha2 = datetime.date(2023,12,1)
#modificado = modificar_membresia(1234567890,"Super Tester",fecha2)

borrado = eliminar_membresia(1234567890)


#print(creado_nuevo)
#print(modificado)
print(borrado)
test2 = buscar_todas_membresias(client)

for i in test2:
    print(f"{i}")
