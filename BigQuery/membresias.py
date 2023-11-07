# -*- coding: utf-8 -*-
"""
Created on Tue Oct 24 14:04:14 2023

@author: Cristian, Esteban, Pepe
"""

import datetime

from google.cloud import bigquery
from google.oauth2 import service_account

def validar_creacion_membresia(inputs_usuario: list):
    """
        Valida que los datos ingresados sean válidos para crear una membresía.

        Parameters
        ----------
        inputs_usuario: list
            Es una lista que contiene cada uno de los inputs del usuario.
            Para membresía son: (los nombres son solo para mejor comprensión de la lista)
                id: int
                tipo: str
                vencimiento: date


        Returns
        -------
        validado : boolean
            Devuelve si son válidos todos los elementos de la lista
    """
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
    """
        Crea una membresía en la base de datos de BigQuery.

        Parameters
        ----------
        cliente : google.cloud.bigquery.Client
            Cliente de BigQuery para realizar la operación.
            
        inputs_usuario : list
            Lista que contiene los datos de la membresía a crear. Debe tener la siguiente estructura:
            [ID_MEMBRESIA, TIPO_MEMBRESIA, FECHA_VENCIM_MEMBRE]

        Returns
        -------
        bool
            True si la membresía se crea con éxito, False en caso contrario.
    """
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
    """
        Elimina una membresía de la base de datos de BigQuery.

        Parameters
        ----------
        id_membresia : int
            El ID de la membresía que se va a eliminar.

        Returns
        -------
        bool
            True si la membresía se elimina con éxito, False en caso contrario.
    """
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
    """
        Modifica una membresía en la base de datos de BigQuery.

        Parameters
        ----------
        id_membresia : int
            El ID de la membresía que se va a modificar.
        tipo : str
            El nuevo tipo de membresía.
        vencimiento : str
            La nueva fecha de vencimiento de la membresía en formato de cadena.

        Returns
        -------
        bool
            True si la membresía se modifica con éxito, False en caso contrario.
    """
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
    """
        Busca todas las membresías en la base de datos de BigQuery.

        Parameters
        ----------
        cliente : google.cloud.bigquery.Client
            Cliente de BigQuery para realizar la operación.

        Returns
        -------
        google.cloud.bigquery.table.RowIterator
            Resultado de la consulta que contiene todas las membresías.
    """
    query_job = client.query("SELECT * FROM `coil2023.Biblioteca.MEMBRESIA`")
    datos_membresia = query_job.result()
    
    return datos_membresia
#bien :^)

def buscar_membresia_especifica(client: bigquery.Client, inputs_usuario: list):
    """
        Busca membresías en la base de datos de BigQuery con criterios específicos.

        Parameters
        ----------
        client : google.cloud.bigquery.Client
            Cliente de BigQuery para realizar la operación.
            
        inputs_usuario : list
            Lista que contiene los criterios de búsqueda.

        Returns
        -------
        google.cloud.bigquery.table.RowIterator
            Resultado de la consulta que contiene las membresías que coinciden con los criterios.
    """
    consulta_SQL = generar_consulta(inputs_usuario)
    
    return buscar_consulta_especifica(client, consulta_SQL)
#bien :^)

def buscar_consulta_especifica(client: bigquery.Client, consulta: str):
    """
        Busca en la base de datos de BigQuery utilizando una consulta SQL personalizada.

        Parameters
        ----------
        client : google.cloud.bigquery.Client
            Cliente de BigQuery para realizar la operación.
            
        consulta : str
            Consulta SQL personalizada para buscar datos en la base de datos.

        Returns
        -------
        google.cloud.bigquery.table.RowIterator
            Resultado de la consulta que contiene los datos que coinciden con la consulta especificada.
    """
    query_job = client.query(consulta)
    datos_membresia = query_job.result() 
    
    return datos_membresia
#bien :^)

def generar_consulta(consultas: list):
    """
        Genera una consulta SQL para buscar membresías en la base de datos de BigQuery.

        Parameters
        ----------
        consultas : list
            Lista que contiene los criterios de búsqueda.

        Returns
        -------
        str
            Consulta SQL generada para buscar membresías en la base de datos.
    """
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
