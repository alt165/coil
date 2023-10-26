# -*- coding: utf-8 -*-
"""
Created on Tue Oct 24 14:04:14 2023

@author: Cristian, Esteban, Pepe
"""

import sqlite3


class Membresia:
    def __init__(self, id_membresia: int, tipo: str):
        self.id_membresia = id_membresia
        self.tipo = tipo
    
    def __str__(self):
        membresia_completa: str = f"{self.id_membresia}" + "\t"
        membresia_completa += f"{self.tipo}"
        
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
        cursor.execute("INSERT INTO membresia (id_membresia, tipo) VALUES (?, ?)", (id_membresia, tipo))
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
    conn = sqlite3.connect("usuario")
    cursor = conn.cursor()
    cursor.execute("DELETE FROM membresia WHERE id_membresia=?", (id_membresia,))
    conn.commit()
    conn.close()
    
    # Si no se encontró ninguna membresia, entonces no se realizaron cambios en
    # la base de datos.
    if (cursor.rowcount == 0):
        membresia_encontrada = False
    
    return membresia_encontrada

def modificar_membresia(id_membresia: int, tipo: str):
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
    conn = sqlite3.connect('usuario')
    cursor = conn.cursor()
    cursor.execute("UPDATE membresia SET tipo=? WHERE id_membresia=?", (tipo, id_membresia))
    conn.commit()
    conn.close()
    
    # Verifica si se encontró y modificó la membresia especificada.
    if (cursor.rowcount == 0):
        membresia_encontrada = False
    
    return membresia_encontrada

def buscar_todas_membresias():
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
    conn = sqlite3.connect("usuario")
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM membresia")
    datos_membresia = cursor.fetchall()
    conn.close()
    
    # Si el retorno de la base de datos es una lista vacía, la función no
    # retorna nada. De lo contrario retorna una lista con objetos Membresia con
    # los datos encontrados.
    membresia_encontrada: Membresia = []
    for elem in datos_membresia:
        membresia_encontrada.append(Membresia(elem[0], elem[1]))
    
    # Retorna lista vacía si no se encontró, o con objetos Membresia si sí.
    return membresia_encontrada

def buscar_membresia(caracteristica: str, busqueda: str):
    """
    Busca una membresia en la base de datos. (tabla membresia)

    Parameters
    ----------
    caracteristica : str
        Característica a buscar. Esto es, por ejemplo, "id_membresia", "tipo".
    busqueda : str
        Búsqueda que se desea realizar sobre la característica. Por ejemplo, si
        la característica es "tipo", la búsqueda puede ser "Oro".

    Returns
    -------
    membresia_encontrado : list
        Lista de objetos de tipo Membresia (con toda la información encontrada
        en la base de datos).

    """
    
    consulta: str = f"SELECT * FROM membresia WHERE {caracteristica}=?"
    
    # Se busca la membresia en la base de datos, y se obtiene su información.
    conn = sqlite3.connect("usuario")
    cursor = conn.cursor()
    cursor.execute(consulta, (busqueda,))
    datos_membresia = cursor.fetchall()
    conn.close()
    
    # Si el retorno de la base de datos es una lista vacía, la función no
    # retorna nada. De lo contrario retorna un objeto Membresia con los datos
    # encontrados.
    membresia_encontrada: Membresia = []
    for elem in datos_membresia:
        membresia_encontrada.append(Membresia(elem[0], elem[1]))
    
    # Retorna lista vacía si no se encontró, o con objetos Membresia si sí.
    return membresia_encontrada

def buscar_id_membresia(id_membresia: int):
    """
    Busca una membresía en la base de datos, por medio de su id_membresia.

    Parameters
    ----------
    id_membresia : int
        ID buscada.

    Returns
    -------
    membresia_encontrada : list
        Lista de objetos de tipo Membresia (con toda la información encontrada
        en la base de datos).

    """
    # Se busca la membresia en la base de datos, y se obtiene su información.
    return buscar_membresia("id_membresia", id_membresia)

def buscar_tipo_membresia(tipo: str):
    """
    Busca una membresía en la base de datos, por medio de su tipo.

    Parameters
    ----------
    tipo : str
        Tipo de membresia buscada.

    Returns
    -------
    membresia_encontrada : list
        Lista de objetos de tipo Membresia (con toda la información encontrada
        en la base de datos).

    """
    # Se busca la membresia en la base de datos, y se obtiene su información.
    return buscar_membresia("tipo", tipo)


#imprimir_lista_membresias(buscar_id_membresia(33))
#crear_membresia(33, "Gold")
#imprimir_lista_membresias(buscar_id_membresia(33))
#modificar_membresia(33, "RE Gold")
#imprimir_lista_membresias(buscar_id_membresia(33))
#eliminar_membresia(33)
#imprimir_lista_membresias(buscar_id_membresia(33))
