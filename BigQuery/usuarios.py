# -*- coding: utf-8 -*-
"""
Created on Sat Oct 14 19:10:32 2023

@author: Cristian, Esteban, Pepe
"""

from google.cloud import bigquery
from google.oauth2 import service_account

def ejecutar_consulta_especifica(client: bigquery.Client, consulta: str):
    """
    Ejecuta una consulta específica a la dataset de BigQuery para el proyecto
    'coil2023', 

    Parameters
    ----------
    client : bigquery.Client
        Cliente autenticado en Google para utilizar BigQuery.
    consulta : str
        String con la consulta en SQL a realizar a la dataset de BigQuery.

    Returns
    -------
    rows : google.cloud.bigquery.table.RowIterator
        RowIterator de Google / Tabla con todos la información obtenida de la
        consulta.

    """
    # Se busca la cantidad especificada de usuarios y se obtiene su
    # información.
    query_job   = client.query(consulta)  # API request
    rows        = query_job.result()      # Waits for query to finish
    
    # Retorna las filas de la tabla obtenida en la consulta.
    return rows

def buscar_usuarios_sin_criterios(client: bigquery.Client, limite: int):
    """
    Busca una cantidad determinada de usuarios en la dataset. No utiliza
    criterios de búsqueda; simplemente devuelve los primeros usuarios que se
    encuentren en la dataset.

    Parameters
    ----------
    client : bigquery.Client
        Cliente autenticado en Google para utilizar BigQuery.
    limite : int
        Cantidad de usuarios mayor a cero (limite > 0) a consultar (límite de
        usuarios a recibir).

    Returns
    -------
    rows : google.cloud.bigquery.table.RowIterator
        RowIterator de Google / Tabla con todos la información obtenida de la
        consulta.

    """
    # Se verifican precondiciones.
    if (limite <= 0):
        raise Exception("Valor invalido: limite <= 0.")
    
    # Se genera la QUERY para el SQL de BigQuery.
    QUERY: str = ("SELECT * FROM `coil2023.Biblioteca.USUARIO` "
                  f"LIMIT {limite}")
    
    # Retorna las filas de la tabla obtenida en la consulta.
    return ejecutar_consulta_especifica(client, QUERY)

def buscar_id_usuario(client: bigquery.Client, limite: int, id_usuario: int):
    """
    Realiza una búsqueda por el ID del usuario en la dataset. Utiliza como
    criterio de búsqueda el campo ID_USUARIO.
    La búsqueda debe coincidir exactamente con el ID escrito en el parámetro.
    La cantidad de resultados obtenidos se indica con el "limite".

    Parameters
    ----------
    client : bigquery.Client
        Cliente autenticado en Google para utilizar BigQuery.
    limite : int
        Cantidad de usuarios mayor a cero (limite > 0) a consultar (límite de
        usuarios a recibir).
    id_usuario : int
        ID del usuario que se busca en la dataset. DEBE ser un número entero
        válido.

    Returns
    -------
    rows : google.cloud.bigquery.table.RowIterator
        RowIterator de Google / Tabla con todos la información obtenida de la
        consulta.

    """
    # Se verifican precondiciones.
    if (limite <= 0):
        raise Exception("Valor invalido: limite <= 0.")
    if (type(id_usuario) != int):
        raise Exception("Valor invalido: id_usuario no entero (int).")
    
    # Se genera la QUERY para el SQL de BigQuery.
    QUERY: str = ("SELECT * FROM `coil2023.Biblioteca.USUARIO` "
                  f"WHERE ID_USUARIO = {id_usuario} "
                  f"LIMIT {limite}")
    
    # Retorna las filas de la tabla obtenida en la consulta.
    return ejecutar_consulta_especifica(client, QUERY)

def buscar_nombre(client: bigquery.Client, limite: int, nombre: str):
    """
    Busca por nombre una cantidad determinada de usuarios en la dataset.
    Utiliza como criterio de búsqueda el campo NOMBRE_USR.
    La búsqueda no es por palabras que coincidan exactamente con el parámetro
    ingresado. Por ejemplo, si el nombre es "Jorge" y se buscó "Jorg", se
    encontrará a ese usuario buscado porque coinciden esos 4 caracteres (no
    no necesariamente todos).
    La cantidad de resultados obtenidos se indica con el "limite".

    Parameters
    ----------
    client : bigquery.Client
        Cliente autenticado en Google para utilizar BigQuery.
    limite : int
        Cantidad de usuarios mayor a cero (limite > 0) a consultar (límite de
        usuarios a recibir).
    nombre : str
        Nombre del usuario que se busca en la dataset.

    Returns
    -------
    rows : google.cloud.bigquery.table.RowIterator
        RowIterator de Google / Tabla con todos la información obtenida de la
        consulta.

    """
    # Se verifican precondiciones.
    if (limite <= 0):
        raise Exception("Valor invalido: limite <= 0.")
    
    # Se genera la QUERY para el SQL de BigQuery.
    QUERY: str = ("SELECT * FROM `coil2023.Biblioteca.USUARIO` "
                  f"WHERE NOMBRE_USR LIKE '%{nombre}%' "
                  f"LIMIT {limite}")
    
    # Retorna las filas de la tabla obtenida en la consulta.
    return ejecutar_consulta_especifica(client, QUERY)

def buscar_apellido(client: bigquery.Client, limite: int, apellido: str):
    """
    Busca por apellido una cantidad determinada de usuarios en la dataset.
    Utiliza como criterio de búsqueda el campo APELLIDO_USR.
    La búsqueda no es por palabras que coincidan exactamente con el parámetro
    ingresado. Por ejemplo, si el apellido es "Vargas" y se buscó "Varg", el
    resultado probablemente pueda aparecer (dependerá del límite de resultados
    que se quiera obtener, no de la coincidencia exacta de TODOS los caracteres
    del parámetro).
    La cantidad de resultados obtenidos se indica con el "limite".

    Parameters
    ----------
    client : bigquery.Client
        Cliente autenticado en Google para utilizar BigQuery.
    limite : int
        Cantidad de usuarios mayor a cero (limite > 0) a consultar (límite de
        usuarios a recibir).
    apellido : str
        Apellido del usuario que se busca en la dataset.

    Returns
    -------
    rows : google.cloud.bigquery.table.RowIterator
        RowIterator de Google / Tabla con todos la información obtenida de la
        consulta.

    """
    # Se verifican precondiciones.
    if (limite <= 0):
        raise Exception("Valor invalido: limite <= 0.")
    
    # Se genera la QUERY para el SQL de BigQuery.
    QUERY: str = ("SELECT * FROM `coil2023.Biblioteca.USUARIO` "
                  f"WHERE APELLIDO_USR LIKE '%{apellido}%' "
                  f"LIMIT {limite}")
    
    # Retorna las filas de la tabla obtenida en la consulta.
    return ejecutar_consulta_especifica(client, QUERY)

def buscar_direccion(client: bigquery.Client, limite: int, direccion: str):
    """
    Busca por dirección una cantidad determinada de usuarios en la dataset.
    Utiliza como criterio de búsqueda el campo DIRECCION_USR.
    La búsqueda no es por palabras que coincidan exactamente con el parámetro
    ingresado. Por ejemplo, si la dirección es "Avenida Illinois" y se buscó
    "Avenida", el resultado probablemente pueda aparecer (dependerá del límite
    de resultados que se quiera obtener, no de la coincidencia exacta de TODOS
    los caracteres del parámetro).
    La cantidad de resultados obtenidos se indica con el "limite".

    Parameters
    ----------
    client : bigquery.Client
        Cliente autenticado en Google para utilizar BigQuery.
    limite : int
        Cantidad de usuarios mayor a cero (limite > 0) a consultar (límite de
        usuarios a recibir).
    direccion : str
        Dirección del usuario que se busca en la dataset.

    Returns
    -------
    rows : google.cloud.bigquery.table.RowIterator
        RowIterator de Google / Tabla con todos la información obtenida de la
        consulta.

    """
    # Se verifican precondiciones.
    if (limite <= 0):
        raise Exception("Valor invalido: limite <= 0.")
    
    # Se genera la QUERY para el SQL de BigQuery.
    QUERY: str = ("SELECT * FROM `coil2023.Biblioteca.USUARIO` "
                  f"WHERE DIRECCION_USR LIKE '%{direccion}%' "
                  f"LIMIT {limite}")
    
    # Retorna las filas de la tabla obtenida en la consulta.
    return ejecutar_consulta_especifica(client, QUERY)

"""
# Ruta al archivo de credenciales JSON.
credentials = service_account.Credentials.from_service_account_file('../credenciales/coil2023-6672f55c3eb6.json')

# Se instancia el cliente con las credenciales del proyecto COIL.
client = bigquery.Client(credentials=credentials, project=credentials.project_id)

rows = buscar_id_usuario(client, limite = 3, id_usuario = 4215687)

for row in rows:
    print(f"{row.ID_USUARIO}\t{row.NOMBRE_USR}\t{row.APELLIDO_USR}")
"""