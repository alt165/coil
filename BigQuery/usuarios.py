# -*- coding: utf-8 -*-
"""
Created on Sat Oct 14 19:10:32 2023

@author: Cristian, Esteban, Pepe
"""

from google.cloud import bigquery
from google.oauth2 import service_account

import membresias as mem

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

def buscar_email(client: bigquery.Client, limite: int, email: str):
    """
    Busca por email una cantidad determinada de usuarios en la dataset.
    Utiliza como criterio de búsqueda el campo CORREO_E_USR.
    La búsqueda no es por palabras que coincidan exactamente con el parámetro
    ingresado. Por ejemplo, si el e-mail es "hola@email.com" y se buscó
    "hola", el resultado probablemente pueda aparecer (dependerá del límite
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
    email : str
        Correo Electrónico / E-mail del usuario que se busca en la dataset.

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
                  f"WHERE CORREO_E_USR LIKE '%{email}%' "
                  f"LIMIT {limite}")
    
    # Retorna las filas de la tabla obtenida en la consulta.
    return ejecutar_consulta_especifica(client, QUERY)

def buscar_id_membresia(client: bigquery.Client, limite: int,
                          id_membresia: int):
    """
    Realiza una búsqueda por el ID de la MEMBRESIA correspondiente a un usuario
    en la dataset. Utiliza como criterio de búsqueda el campo ID_MEMBRESIA.
    La búsqueda debe coincidir exactamente con el ID escrito en el parámetro.
    La cantidad de resultados obtenidos se indica con el "limite".

    Parameters
    ----------
    client : bigquery.Client
        Cliente autenticado en Google para utilizar BigQuery.
    limite : int
        Cantidad de usuarios mayor a cero (limite > 0) a consultar (límite de
        usuarios a recibir).
    id_membresia : int
        ID de la MEMBRESIA del usuario que se busca en la dataset. DEBE ser un
        número entero válido.

    Returns
    -------
    rows : google.cloud.bigquery.table.RowIterator
        RowIterator de Google / Tabla con todos la información obtenida de la
        consulta.

    """
    # Se verifican precondiciones.
    if (limite <= 0):
        raise Exception("Valor invalido: limite <= 0.")
    if (type(id_membresia) != int):
        raise Exception("Valor invalido: id_membresia no entero (int).")
    
    # Se genera la QUERY para el SQL de BigQuery.
    QUERY: str = ("SELECT * FROM `coil2023.Biblioteca.USUARIO` "
                  f"WHERE ID_MEMBRESIA = {id_membresia} "
                  f"LIMIT {limite}")
    
    # Retorna las filas de la tabla obtenida en la consulta.
    return ejecutar_consulta_especifica(client, QUERY)

def buscar_usuario_especifico(client: bigquery.Client,
                                 inputs_usuario: list,
                                 limite: int):
    """
    Busca un usuario específico en la dataset de BigQuery. Recibe una lista
    con los datos de los campos ID_USUARIO, NOMBRE_USR, APELLIDO_USR,
    DIRECCION_USR, CORREO_E_USR y ID_MEMBRESIA (en orden), y realiza la
    consulta a la base de datos con esta información.
    Por ejemplo, la lista de 'inputs_usuario' puede contener los siguientes
    datos: ["", "Jorge", "Perez", "", "", ""]. Así la consulta será para buscar
    exclusivamente los campos de NOMBRE_USR y APELLIDO_USR, con "Jorge" y
    "Perez" respectivamente.

    Parameters
    ----------
    inputs_usuario : list
        Lista de strings con los datos de los campos ID_USUARIO, NOMBRE_USR,
        APELLIDO_USR, DIRECCION_USR, CORREO_E_USR y ID_MEMBRESIA (en orden).
        Los campos vacíos deben ser strings vacíos: "".
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
    
    # Se genera la consulta con el sintaxis correcto en SQL para la base de
    # datos.
    consulta_SQL: str = generar_consulta(inputs_usuario, limite)
    
    return ejecutar_consulta_especifica(client, consulta_SQL)

def generar_consulta(datos_consulta: list, limite: int):
    """
    Genera un string para hacerle la consulta a la base de datos en SQL, en la
    tabla de "USUARIO" de la dataset de BigQuery. La misma utiliza los inputs
    de los 5 campos: ID_USUARIO, NOMBRE_USR, APELLIDO_USR, DIRECCION_USR,
    CORREO_E_USR y ID_MEMBRESIA (en orden).

    Parameters
    ----------
    datos_consulta : list
        Lista de strings con los datos de los campos ID_USUARIO, NOMBRE_USR,
        APELLIDO_USR, DIRECCION_USR, CORREO_E_USR y ID_MEMBRESIA (en orden).
        El tamaño de la lista debe concordar con la cantidad de campos en la
        tabla. C
    limite : int
        Cantidad de usuarios mayor a cero (limite > 0) a consultar (límite de
        usuarios a recibir).

    Returns
    -------
    consulta_resultado : str
        Consulta en SQL para realizar a la base de datos, formada a partir de
        lo que el usuario especificó.

    """
    # Se verifican precondiciones.
    # Se verifica que el límite de resultados sea mayor a cero.
    if (limite <= 0):
        raise Exception("Valor invalido: limite <= 0.")
    # Se verifica que el largo de la lista sea exactamente la cantidad de
    # campos de la tabla.
    if (len(datos_consulta) != 6):
        raise Exception("Valor invalido: "
                        "no coincide el tamaño de la lista de los datos para "
                        "los campos con la cantidad de campos en la tabla.")
    # Se verifica la cantidad de datos vacíos y que todos los datos sean de
    # tipo string.
    cantidad_datos_vacios: int = 0
    for dato in datos_consulta:
        if (type(dato) != str):
            raise Exception("Valor invalido: tipo ingresado no string.")
        if (dato == ""):
            cantidad_datos_vacios += 1
    if (cantidad_datos_vacios >= 6):
        raise Exception("Valor invalido: lista vacia.")
    
    
    # Nombres (en orden) de todos los campos disponibles de la tabla a
    # consultar de la base de datos.
    nombres_campos: list = ["ID_USUARIO",
                            "NOMBRE_USR",
                            "APELLIDO_USR",
                            "DIRECCION_USR",
                            "CORREO_E_USR",
                            "ID_MEMBRESIA"]
    
    # Genera una lista con los campos a agregar a la consulta en SQL. Son los
    # campos restantes, que deben ser parte de la consulta, tras analizar los
    # datos vacíos (como strings vacíos: "") en el parámetro 'datos_consulta'.
    nombres_campos_restantes: list = []
    
    # Datos de cada campo, respecto a la consulta correspondiente a cada campo.
    # Tiene los datos ingresados por el usuario que no fueron strings
    # vacíos: "".
    datos_consulta_restantes: list = []
    
    # Indice para verificar la posición en la lista.
    indice: int = 0
    
    for dato in datos_consulta:
        # Se verifica la longitud del string. Si el dato contiene algo,
        # entonces la longitud es mayor a cero y se la tiene en cuenta para
        # generar la consulta.
        if (len(dato) > 0):
            nombres_campos_restantes.append(nombres_campos[indice])
            datos_consulta_restantes.append(dato)
        else:
            cantidad_datos_vacios += 1
        indice += 1
    
    # Se genera la consulta de SQL.
    consulta_resultado: str = ("SELECT * "
                               "FROM `coil2023.Biblioteca.USUARIO` WHERE")
    # Flag que indica si debe agregarse un 'AND' en la consulta en SQL.
    agregar_and: bool = False
    
    # Se agregan los campos y sus datos a la consulta de SQL.
    for indice in range(0, len(nombres_campos_restantes)):
        if (agregar_and):
            consulta_resultado += " AND"
        else:
            agregar_and = True
        
        if (nombres_campos_restantes[indice] == nombres_campos[0]
            or nombres_campos_restantes[indice] == nombres_campos[5]):
            # Si se trata del campo ID_USUARIO o ID_MEMBRESIA, se busca
            # coincidencia exacta.
            consulta_resultado += (f" {nombres_campos_restantes[indice]} ="
                                   f" {datos_consulta_restantes[indice]}")
        else:
            # Si se trata del resto de los campos, se busca que no sea exacta
            # la coincidencia.
            consulta_resultado += (f" {nombres_campos_restantes[indice]} LIKE"
                                   f" '%{datos_consulta_restantes[indice]}%'")
    
    # Se agrega, por último, el límite de resultados esperados.
    consulta_resultado += f" LIMIT {limite}"
    
    return consulta_resultado

def validar_ID_USUARIO(client: bigquery.Client, ID_USUARIO: str):
    """
    Valida un ID_USUARIO dada. Verifica que la ID sea un número entero entre 1
    y 8 dígitos.
    En caso de ingresar un 'client' para hacer la conexión con la base de datos
    de BigQuery, se realiza una consulta para verificar si existe ya el ID en
    cuestión. Caso afirmativo retorna True. Caso contrario, False.
    Si se ingresa un 'client' None, entonces el retorno siempre será False
    (porque no hace la conexión con la base de datos).

    Parameters
    ----------
    client : bigquery.Client
        Cliente autenticado en Google para utilizar BigQuery. Puede ser None y,
        en este caso, el retorno será siempre False porque no se verifica si
        la ID existe ya en la base de datos.
    ID_USUARIO : str
        ID a validar. Debe ser un número entero de entre 1 y 8 dígitos.

    Raises
    ------
    Exception
        Se lanza la excepción cuando la longitud es invalida o mayor a 8.
        También cuando el ID no es un número entero.

    Returns
    -------
    existe_ID : bool
        Se retorna False o True en caso de que exista o no el ID en cuestión.
        En caso de que el 'client' ingresado sea None, el retorno será siempre
        False porque no se conecta con la base de datos.

    """
    existe_ID: bool = False
    
    # Se verifica la longitud del ID.
    if (len(str(ID_USUARIO)) <= 0):
        raise Exception("Valor invalido: longitud del ID_USUARIO no valida.")
    if (len(str(ID_USUARIO)) > 8):
        raise Exception("Valor invalido: longitud del ID_USUARIO mayor a 8.")
    
    # Se verifica que sea un número entero.
    try:
        int(ID_USUARIO) # Si falla el casteo, no es un número entero.
    except:
        raise Exception("Valor invalido:"
                        "se esperaba un numero entero para ID_USUARIO.")
    
    # Si ingresó el cliente de BigQuery, entonces realiza la búsqueda para ver
    # si existe algún usuario con ese ID.
    if (client != None):
        consulta_ID = buscar_id_usuario(client, 1, int(ID_USUARIO))
        if (consulta_ID.total_rows == 0):
            existe_ID = False
        else:
            existe_ID = True
    
    return existe_ID

def validar_ID_MEMBRESIA(client: bigquery.Client, ID_MEMBRESIA: str):
    """
    Valida un ID_MEMBRESIA dada. Verifica que la ID sea un número entero entre
    1 y 10 dígitos.
    En caso de ingresar un 'client' para hacer la conexión con la base de datos
    de BigQuery, se realiza una consulta para verificar si existe ya el ID en
    cuestión. Caso afirmativo retorna True. Caso contrario, False.
    Si se ingresa un 'client' None, entonces el retorno siempre será False
    (porque no hace la conexión con la base de datos).
    (Utiliza el módulo "membresias.py")

    Parameters
    ----------
    client : bigquery.Client
        Cliente autenticado en Google para utilizar BigQuery. Puede ser None y,
        en este caso, el retorno será siempre False porque no se verifica si
        la ID existe ya en la base de datos.
    ID_MEMBRESIA : str
        ID a validar. Debe ser un número entero de entre 1 y 10 dígitos.

    Raises
    ------
    Exception
        Se lanza la excepción cuando la longitud es invalida o mayor a 10.
        También cuando el ID no es un número entero.

    Returns
    -------
    existe_ID : bool
        Se retorna False o True en caso de que exista o no el ID en cuestión.
        En caso de que el 'client' ingresado sea None, el retorno será siempre
        False porque no se conecta con la base de datos.

    """
    return mem.validar_ID_MEMBRESIA(client, ID_MEMBRESIA)

def validar_NOMBRE_USR(NOMBRE_USR: str):
    # Se verifica la longitud del NOMBRE_USR.
    if (len(str(NOMBRE_USR)) <= 0):
        raise Exception("Valor invalido: longitud de NOMBRE_USR no valida.")
    if (len(str(NOMBRE_USR)) > 40):
        raise Exception("Valor invalido: longitud de NOMBRE_USR mayor a 40.")

def validar_APELLIDO_USR(APELLIDO_USR: str):
    # Se verifica la longitud del APELLIDO_USR.
    if (len(str(APELLIDO_USR)) <= 0):
        raise Exception("Valor invalido: longitud de APELLIDO_USR no valida.")
    if (len(str(APELLIDO_USR)) > 40):
        raise Exception("Valor invalido: longitud de APELLIDO_USR mayor a 40.")

def validar_DIRECCION_USR(DIRECCION_USR: str):
    # Se verifica la longitud del DIRECCION_USR.
    if (len(str(DIRECCION_USR)) <= 0):
        raise Exception("Valor invalido: longitud de DIRECCION_USR no valida.")
    if (len(str(DIRECCION_USR)) > 40):
        raise Exception("Valor invalido: longitud de DIRECCION_USR mayor a 40.")
    

def validar_CORREO_E_USR(CORREO_E_USR: str):
    # Se verifica la longitud del CORREO_E_USR.
    if (len(str(CORREO_E_USR)) <= 0):
        raise Exception("Valor invalido: longitud de CORREO_E_USR no valida.")
    if (len(str(CORREO_E_USR)) > 40):
        raise Exception("Valor invalido: longitud de CORREO_E_USR mayor a 40.")
    
    # Se verifica, de manera simple, que el correo posea un solo '@' y al
    # menos un punto
    if not (CORREO_E_USR.count('@') == 1 and CORREO_E_USR.count('.') >= 1):
        raise Exception("Valor invalido: CORREO_E_USR no posee al menos "
                        "un '@' y un punto.")

def crear_usuario(client: bigquery.Client,
                    ID_USUARIO: str,
                    NOMBRE_USR: str, APELLIDO_USR: str,
                    DIRECCION_USR: str, CORREO_E_USR: str,
                    ID_MEMBRESIA: str):
    # Se validan los datos ingresados en los parámetros.
    if validar_ID_USUARIO(client, ID_USUARIO):
        # Si ya existe un ID_USUARIO idéntico, se lanza excepción.
        raise Exception("Error: ya existe un usuario con ese ID_USUARIO.")
    if not validar_ID_MEMBRESIA(client, ID_MEMBRESIA):
        # Si no existe un ID_MEMBRESIA idéntico, se lanza excepción.
        raise Exception("Error: no existe una membresia con ese ID_MEMBRESIA.")
    validar_NOMBRE_USR(NOMBRE_USR)
    validar_APELLIDO_USR(APELLIDO_USR)
    validar_DIRECCION_USR(DIRECCION_USR)
    validar_CORREO_E_USR(CORREO_E_USR)

    QUERY: str = (f"INSERT INTO `coil2023.Biblioteca.USUARIO` "
                  "(ID_USUARIO, NOMBRE_USR, APELLIDO_USR, DIRECCION_USR, "
                  "CORREO_E_USR, ID_MEMBRESIA) VALUES "
                  f"({ID_USUARIO}, '{NOMBRE_USR}', '{APELLIDO_USR}', "
                  f"'{DIRECCION_USR}', '{CORREO_E_USR}', {ID_MEMBRESIA})")
    
    return ejecutar_consulta_especifica(client, QUERY)

def modificar_usuario(client: bigquery.Client,
                        ID_USUARIO: str,
                        NOMBRE_USR: str, APELLIDO_USR: str,
                        DIRECCION_USR: str, CORREO_E_USR: str,
                        ID_MEMBRESIA: str):
    # Se validan los datos ingresados en los parámetros.
    if not validar_ID_USUARIO(client, ID_USUARIO):
        # Si no existe un ID_USUARIO idéntico, se lanza excepción.
        raise Exception("Error: no existe un usuario con ese ID_USUARIO.")
    if not validar_ID_MEMBRESIA(client, ID_MEMBRESIA):
        # Si no existe un ID_MEMBRESIA idéntico, se lanza excepción.
        raise Exception("Error: no existe una membresia con ese ID_MEMBRESIA.")
    validar_NOMBRE_USR(NOMBRE_USR)
    validar_APELLIDO_USR(APELLIDO_USR)
    validar_DIRECCION_USR(DIRECCION_USR)
    validar_CORREO_E_USR(CORREO_E_USR)
    
    # Se genera la QUERY en SQL para modificar al usuario, según su ID_USUARIO.
    QUERY: str = ("UPDATE `coil2023.Biblioteca.USUARIO` SET "
                  f"NOMBRE_USR='{NOMBRE_USR}', "
                  f"APELLIDO_USR='{APELLIDO_USR}', "
                  f"DIRECCION_USR='{DIRECCION_USR}', "
                  f"CORREO_E_USR='{CORREO_E_USR}', "
                  f"ID_MEMBRESIA={ID_MEMBRESIA} "
                  f"WHERE ID_USUARIO = {ID_USUARIO}")
    
    return ejecutar_consulta_especifica(client, QUERY)

def eliminar_usuario(client: bigquery.Client, ID_USUARIO: str):
    # Se validan los datos ingresados en los parámetros.
    existe_usuario: bool = validar_ID_USUARIO(client, ID_USUARIO)
    
    # Se genera la QUERY en SQL para modificar al usuario, según su ID_USUARIO.
    QUERY: str = ("DELETE FROM `coil2023.Biblioteca.USUARIO` WHERE "
                  f"ID_USUARIO = {ID_USUARIO}")
    
    ejecutar_consulta_especifica(client, QUERY)
    
    return existe_usuario
