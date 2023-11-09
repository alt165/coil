# -*- coding: utf-8 -*-
"""
Created on Tue Oct 24 14:04:14 2023

@author: Cristian, Esteban, Pepe
"""

import datetime

from google.cloud import bigquery
from google.oauth2 import service_account


def validar_creacion_membresia(cliente: bigquery.Client, inputs_usuario: list):
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
        raise Exception("Demasiados Inputs")
    if validar_ID_MEMBRESIA(cliente, inputs_usuario[0]):
        raise Exception("Membresia existente")
    if len(str(inputs_usuario[1])) > 20:
        raise Exception("TIPO incorrecto")
    #se verifica que se haya pasado algo parecido a un DATE
    if not validar_fecha(inputs_usuario[2]):
        raise Exception("VENCIMIENTO incorrecto, no es una fecha")
    if str(inputs_usuario[2]) < str(datetime.datetime.now()):
        raise Exception("VENCIMIENTO incorrecto, no es una fecha valida")
    validado = True
    return validado

def validar_ID_MEMBRESIA(cliente: bigquery.Client, ID_MEMBRESIA: int):
    existe_ID: bool = False

    # Se verifica que la longitud del ID.
    if (len(str(ID_MEMBRESIA)) <= 0):
        raise Exception("ID invalido, longitud del ID_MEMBRESIA no es valida.")
    if (len(str(ID_MEMBRESIA)) > 10):
        raise Exception("ID invalido, longitud del ID_MEMBRESIA debe de ser menor de 10 caracteres.")
    
    # Se verifica que sea un número entero.
    try:
        int(ID_MEMBRESIA) # Si falla el casteo, no es un número entero.
    except:
        raise Exception("ID invalido, se esperaba un numero entero para ID_MEMBRESIA.")
    
    # Si ingresó el cliente de BigQuery, entonces realiza la búsqueda para ver
    # si existe algún usuario con ese ID.
    if (cliente != None):
        consulta_ID = buscar_membresia_especifica(cliente, [str(ID_MEMBRESIA), "", ""])
        if (consulta_ID.total_rows != 0):
            existe_ID = True
    return existe_ID

def validar_fecha(fecha_str):
    partes = fecha_str.split('-')  # Suponiendo un formato YYYY-MM-DD

    if len(partes) != 3:
        return False

    try:
        año, mes, dia = map(int, partes)
        datetime.date(año, mes, dia)
        return True
    except Exception as exc:
        return False


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
        if validar_creacion_membresia(cliente, inputs_usuario):
            consulta = f"INSERT INTO `coil2023.Biblioteca.MEMBRESIA` (ID_MEMBRESIA, TIPO_MEMBRESIA, FECHA_VENCIM_MEMBRE) VALUES ({inputs_usuario[0]}, \"{inputs_usuario[1]}\", '{inputs_usuario[2]}')"
            query_job = cliente.query(consulta)
            datos_membresia = query_job.result()
            print("Creación exitosa")
            return True, ""
        else:
            return False, ""
    except Exception as exc:
        print(f"{exc}")
        return False, f"Error al crear membresia en la base de datos: {exc}"

def eliminar_membresia(cliente: bigquery.Client, id_membresia: int):
    """
        Elimina una membresía de la base de datos de BigQuery.

        Parameters
        ----------
        cliente : google.cloud.bigquery.Client
            Cliente de BigQuery para realizar la operación.

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
        query_job = cliente.query(consulta)
        datos_membresia = query_job.result()
        print("Eliminación exitosa")
        return True, ""
        #else:
        #    return False
    except Exception as exc:
        print(f"Error al borrar membresia en la base de datos: {exc}")
        return False, f"{exc}"

def modificar_membresia(cliente: bigquery.Client, inputs_usuario: list):
    """
        Modifica una membresía en la base de datos de BigQuery.

        Parameters
        ----------
        cliente : google.cloud.bigquery.Client
            Cliente de BigQuery para realizar la operación.

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
        id_membresia = inputs_usuario[0]
        if id_membresia == "":
            return False, "Se requiere un ID para aplicar una modificación"
        
        elemento_a_modificar = buscar_membresia_especifica(cliente, inputs_usuario)
        if len(elemento_a_modificar) != 1:
            return False, "No existe esa membresia"

        tipo = inputs_usuario[1]

        vencimiento = inputs_usuario[2]
        if vencimiento == "":
                vencimiento = elemento_a_modificar.FECHA_VENCIM_MEMBRE
        
        if validar_creación_membresia([id_membresia, tipo, vencimiento]):
            consulta = f"UPDATE `coil2023.Biblioteca.MEMBRESIA` SET TIPO_MEMBRESIA='{tipo}', FECHA_VENCIM_MEMBRE='{vencimiento}' WHERE ID_MEMBRESIA = {id_membresia}"
            query_job = cliente.query(consulta)
            datos_membresia = query_job.result()
            print("Modificación exitosa")
            return True, ""
        else:
            return False, ""
    except Exception as exc:
        print(f"Error al modificar membresia en la base de datos: {exc}")
        return False, f"{exc}"

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
    query_job = cliente.query("SELECT * FROM `coil2023.Biblioteca.MEMBRESIA`")
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

    if  inputs_usuario[2] != "" and not validar_fecha(inputs_usuario[2]):
        raise Exception("fecha erronea al momento de buscarla")

    consulta_SQL = generar_consulta(inputs_usuario)
    resultado = buscar_consulta_especifica(client, consulta_SQL)
    
    return resultado
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

    consulta_resultado: str = "SELECT * FROM `coil2023.Biblioteca.MEMBRESIA` WHERE"

    mas_de_un_campo = False

    for j in range(0, len(consulta)):
        if mas_de_un_campo:
            consulta_resultado += " AND "
        if consulta[j] == campos[0]:
            consulta_resultado += f" {consulta[j]} = {parametros[j]}"
        elif consulta[j] == campos[1]:
            consulta_resultado += f" {consulta[j]} LIKE '%{parametros[j]}%'"
        else:
            consulta_resultado += f" {consulta[j]} = '{parametros[j]}'"
        mas_de_un_campo = True
    #print(consulta_resultado)
    return consulta_resultado
#bien :^)
