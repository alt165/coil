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

def buscar_consulta_especifica(consulta: str, parametros: tuple):
    # Se busca a todos los usuarios que coincidan con la consulta dada por el
    # string, que especifica los campos específicos buscados.
    conn = sqlite3.connect("usuario")
    cursor = conn.cursor()
    cursor.execute(consulta, parametros)
    datos_membresia = cursor.fetchall()
    conn.close()
    
    # Se retorna una lista con objetos Membresia's que contienen la información
    # de cada Membresia que coincide con la búsqueda.
    membresia_encontrada: list = []
    for elem in datos_membresia:
        membresia_encontrada.append(Membresia(elem[0],
                                              elem[1]))
    
    return membresia_encontrada

def buscar_membresia_especifica(inputs_usuario: list):
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
    
    # Genera una tupla con:
    # - 1: la consulta en SQL a la base de datos (según el input del usuario)
    # - 2: la tupla con los datos para la consulta a la base de datos, según
    #      ese mismo input del usuario.
    consulta_SQL = generar_consulta(inputs_usuario)
    
    return buscar_consulta_especifica(consulta_SQL[0], consulta_SQL[1])

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
    campos: list = ["id_membresia",
                    "tipo"]
    
    # Genera una lista con los campos a agregar a la consulta en SQL.
    consulta: list = []
    
    # Datos de cada campo, respecto a la consulta correspondiente a cada campo.
    # Tiene los datos ingresados por el usuario.
    parametros: list = []
    
    # Indice para verificar la posición en la lista.
    indice: int = 0
    
    for i in consultas:
        if (len(i) > 0):
            consulta.append(campos[indice])
            parametros.append(i)
        indice += 1
        
    # Se castea de list a tuple.
    parametros = tuple(parametros)
    
    consulta_resultado: str = "SELECT * FROM membresia WHERE"
    agregar_and: bool = False
    
    for j in consulta:
        if (agregar_and):
            consulta_resultado += " AND"
        
        consulta_resultado += f" {j} = ?"
        
        agregar_and = True
    
    return consulta_resultado, parametros

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
