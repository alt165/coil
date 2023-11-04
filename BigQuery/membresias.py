# -*- coding: utf-8 -*-
"""
Created on Tue Oct 24 14:04:14 2023

@author: Cristian, Esteban, Pepe
"""

import sqlite3

from google.cloud import bigquery
from google.oauth2 import service_account


class Membresia:
    def __init__(self, id_membresia: int, tipo: str, vencimiento: str):
        self.id_membresia = id_membresia
        self.tipo = tipo
        self.vencimiento = vencimiento
    
    def __str__(self):
        membresia_completa: str = f"{self.id_membresia}" + "\t"
        membresia_completa += f"{self.tipo}"
        membresia_completa += f"{self.vencimiento}"
        
        return membresia_completa

def imprimir_lista_membresias(membresias: list):
    """
    Imprime una lista de Membresia (objeto). Imprime cada atributo del objeto.

    Parameters
    ----------
    membresias : list
        Lista de membresias a imprimir.

    Returns
    -------
    None.

    """
    for membresia in membresias:
        print(membresia)

def crear_membresia(id_membresia: int, tipo: str):
    """
        Crea una membresia en la base de datos. Esta función que se comunica con la
        base de datos.
        En caso de que no se pueda dar de alta, imprime un mensaje con el error
        que haya ocurrido.

        Parameters
        ----------
        id_membresia : int
            ID de la membresia (es única).
        tipo : str
            Tipo de membresia.

        Returns
        -------
        membresia_creada : bool
            Retorna True en caso de que haya podido crear la membresia en la
            base de datos. Caso contrario retorna False.
    """
    membresia_creada: bool = True

    conn = sqlite3.connect("usuario")
    cursor = conn.cursor()
    
    try:
        cursor.execute("INSERT INTO membresia (id_membresia, tipo, vencimiento) VALUES (?, ?, ?)", (id_membresia, tipo, vencimiento))
        conn.commit()
    except Exception as exc:
        membresia_creada = False
        print(f"Error al crear membresia en la base de datos: {type(exc)}")

    conn.close()
    
    return membresia_creada

def eliminar_membresia(id_membresia: int):
    """
        Elimina una membresia en la base de datos, por medio de una id_membresia
        otorgada.
        
        Parameters
        ----------
        id_membresia : int
            ID de la membresia a eliminar en la base de datos.

        Returns
        -------
        membresia_encontrada : bool
            Retorna True en caso de que haya podido encontrar la membresia. En ese
            caso, fue borrado. De lo contrario, retorna False.
    """
    membresia_encontrada: bool = True
    
    # Se busca la membresia en la base de datos y se la borra.
    cursor.execute("DELETE FROM membresia WHERE id_membresia=?", (id_membresia,))
    conn.commit()
    
    # Si no se encontró ninguna membresia, entonces no se realizaron cambios en
    # la base de datos.
    if (cursor.rowcount == 0):
        membresia_encontrada = False
    
    return membresia_encontrada

def modificar_membresia(id_membresia: int, tipo: str, vencimiento: str):
    """
        Busca y modifica una membresia dentro de la base de datos. Si la encuentra,
        la modifica. Caso contrario no realiza cambios en la base de datos.

        Parameters
        ----------
        id_membresia : int
            ID de la membresia dentro de la base de datos. Es un valor único.
        tipo : str
            Tipo de membresia.

        Returns
        -------
        membresia_encontrada : bool
            Retorna True si se encontró la membresia, por medio de su id_membresia,
            y se lo modificó. Caso contrario, retorna False porque no se encontró
            y, por ende, no se realizó ninguna modificación.
    """
    membresia_encontrada: bool = True
    
    # Se busca modificar la membresia, por medio de su id_membresia.
    cursor.execute("UPDATE  `coil2023.Biblioteca.MEMBRESIA` SET tipo=? WHERE id_membresia=?", (tipo, id_membresia))
    conn.commit()
    
    # Verifica si se encontró y modificó la membresia especificada.
    if (cursor.rowcount == 0):
        membresia_encontrada = False
    
    return membresia_encontrada


def buscar_todas_membresias(cliente: bigquery.Client):
    """
        Busca a todas las membresias en la base de datos.

        Returns
        -------
        membresia_encontrada : list
            Lista de objetos de tipo Membresia (con toda la información encontrada
            en la base de datos).
    """
    # Se busca a todas las membresias en la base de datos, y se obtiene su
    # información.

    query_job = client.query("SELECT * FROM `coil2023.Biblioteca.MEMBRESIA`")  # API request
    datos_membresia = query_job.result()

    # Si el retorno de la base de datos es una lista vacía, la función no
    # retorna nada. De lo contrario retorna una lista con objetos Membresia con
    # los datos encontrados.
    membresia_encontrada: Membresia = []
    for elem in datos_membresia:
        membresia_encontrada.append(Membresia(elem[0], elem[1], elem[2]))
    
    # Retorna lista vacía si no se encontró, o con objetos Membresia si sí.
    return membresia_encontrada
#bien :^)

def buscar_membresia_especifica(client: bigquery.Client, inputs_usuario: list):
    """
        Busca una membresia específico en la base de datos. Recibe una lista con
        los datos de id_membresia y tipo (en orden), y realiza la consulta a la
        base de datos con esta información.

        Parameters
        ----------
        inputs_usuario : list
            Lista de strings con los datos de: id_membresia y tipo (en orden).

        Returns
        -------
        resultado : list
            Lista con objetos Membresia's que contienen la información encontrada
            de la consulta realizada a la base de datos.
    """
    
    consulta_SQL = generar_consulta(inputs_usuario)
    
    return buscar_consulta_especifica(client, consulta_SQL)
#bien :^)

def buscar_consulta_especifica(client: bigquery.Client, consulta: str):
    # Se busca a todos los usuarios que coincidan con la consulta dada por el
    # string, que especifica los campos específicos buscados.

    query_job = client.query(consulta)  # API request
    datos_membresia = query_job.result()  # Waits for query to finish

    # Se retorna una lista con objetos Membresia's que contienen la información
    # de cada Membresia que coincide con la búsqueda.
    membresia_encontrada: list = []
    for elem in datos_membresia:
        membresia_encontrada.append(Membresia(elem[0], elem[1], elem[2]))
    
    return membresia_encontrada
#bien :^)

def generar_consulta(consultas: list):
    """
        Genera un string para hacerle la consulta a la base de datos en SQL, en
        la tabla de "membresias". La misma utiliza los inputs de los 2 campos:
        id_membresia, tipo.

        Parameters
        ----------
        consultas : list
            DESCRIPTION.

        Returns
        -------
        consulta_resultado : TYPE
            DESCRIPTION.
        parametros : TYPE
            DESCRIPTION.
    """
    # Nombres (en orden) de los campos de la base de datos.
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

    cant_inputs_vacios = 0
    
    for i in consultas:
        if (len(i) > 0):
            consulta.append(campos[indice])
            parametros.append(i)
        else:
            cant_inputs_vacios += 1
        indice += 1
        
    if cant_inputs_vacios == len(consultas):
        return consultas

    consulta_resultado: str = "SELECT * FROM `coil2023.Biblioteca.MEMBRESIA` WHERE"
    agregar_and: bool = False
    
    for j in range(0, len(consulta)):
        if (agregar_and):
            consulta_resultado += " AND"
        
        consulta_resultado += f" {consulta[j]} = '{parametros[j]}'"
        
        agregar_and = True
    
    return consulta_resultado
#bien :^)

# Ruta al archivo de credenciales JSON.
credentials = service_account.Credentials.from_service_account_file('coil2023-6672f55c3eb6.json')

# Se instancia el cliente con las credenciales del proyecto COIL.
client = bigquery.Client(credentials=credentials, project=credentials.project_id)


test = buscar_todas_membresias(client)

print(test)