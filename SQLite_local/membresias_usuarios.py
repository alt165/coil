# -*- coding: utf-8 -*-
"""
Created on Tue Oct 24 14:04:14 2023

@author: Cristian, Esteban, Pepe
"""

import sqlite3


class Membresia_usuario:
    def __init__(self, id_usuario: int, id_membresia: int,
                 vencimiento: str):
        self.id_usuario = id_usuario
        self.id_membresia = id_membresia
        self.vencimiento = vencimiento
    
    def __str__(self):
        membresia_usuario_completa: str = f"{self.id_usuario}" + "\t"
        membresia_usuario_completa += f"{self.id_membresia}" + "\t"
        membresia_usuario_completa += f"{self.vencimiento}"
        
        return membresia_usuario_completa

def imprimir_lista_membresias_usuarios(membresias_usuarios: list):
    """
    Imprime una lista de Membresia_usuario (objeto). Imprime cada atributo del
    objeto.

    Parameters
    ----------
    membresias_usuarios : list
        Lista de membresias_usuarios a imprimir.

    Returns
    -------
    None.

    """
    for membresia_usuario in membresias_usuarios:
        print(membresia_usuario)

def crear_membresia_usuario(id_usuario: int, id_membresia: int,
                              vencimiento: str):
    """
    Crea una membresia_usuario en la base de datos. Esta función se comunica
    con la base de datos.
    En caso de que no se pueda crear, imprime un mensaje con el error
    que haya ocurrido.

    Parameters
    ----------
    id_usuario : int
        ID del usuario.
    id_membresia : int
        ID de la membresia.
    vencimiento : str
        Fecha de vencimiento.

    Returns
    -------
    membresia_usuario_creada : bool
        Retorna True en caso de que haya podido crear la membresia_usuario en
        la base de datos. Caso contrario retorna False.

    """
    membresia_usuario_creada: bool = True

    conn = sqlite3.connect("usuario")
    cursor = conn.cursor()
    
    try:
        cursor.execute("INSERT INTO membresia_usuario (id_usuario, id_membresia, vencimiento) VALUES (?, ?, ?)", (id_usuario, id_membresia, vencimiento))
        conn.commit()
    except Exception as exc:
        membresia_usuario_creada = False
        print(f"Error al crear membresia_usuario en la base de datos: {type(exc)}")

    conn.close()
    
    return membresia_usuario_creada

def eliminar_membresia_usuario(id_usuario: int):
    """
    Elimina una membresia_usuario en la base de datos, por medio de una
    id_usuario otorgada.
    
    Parameters
    ----------
    id_usuario : int
        ID del usuario afiliado a una membresia a eliminar de la base de datos.

    Returns
    -------
    membresia_usuario_encontrada : bool
        Retorna True en caso de que haya podido encontrar la
        membresia_usuario_encontrada. En ese caso, fue borrado. De lo
        contrario, retorna False.

    """
    membresia_usuario_encontrada: bool = True
    
    # Se busca a la membresia_usuario en la base de datos y se lo borra.
    conn = sqlite3.connect("usuario")
    cursor = conn.cursor()
    cursor.execute("DELETE FROM membresia_usuario WHERE id_usuario=?", (id_usuario,))
    conn.commit()
    conn.close()
    
    # Si no se encontró ninguna membresia_usuario, entonces no se realizaron
    # cambios en la base de datos.
    if (cursor.rowcount == 0):
        membresia_usuario_encontrada = False
    
    return membresia_usuario_encontrada

def modificar_membresia_usuario(id_usuario: int, id_membresia: int,
                                   vencimiento: str):
    """
    Busca y modifica una membresia dentro de la base de datos. Si la encuentra,
    la modifica. Caso contrario no realiza cambios en la base de datos.

    Parameters
    ----------
    id_usuario : int
        ID del usuario dentro de la base de datos.
    id_membresia : int
        ID de la membresia dentro de la base de datos.
    vencimiento : str
        Fecha de vencimiento de la membresia.

    Returns
    -------
    membresia_usuario_encontrada : bool
        Retorna True si se encontró la membresia_usuario, por medio de su
        id_usuario, y se lo modificó. Caso contrario, retorna False porque no
        se encontró y, por ende, no se realizó ninguna modificación.

    """
    membresia_usuario_encontrada: bool = True
    
    # Se busca modificar la membresia_usuario, por medio de su id_usuario.
    conn = sqlite3.connect('usuario')
    cursor = conn.cursor()
    cursor.execute("UPDATE membresia_usuario SET id_membresia=?, vencimiento=? WHERE id_usuario=?", (id_membresia, vencimiento, id_usuario))
    conn.commit()
    conn.close()
    
    # Verifica si se encontró y modificó la membresia_usuario especificado.
    if (cursor.rowcount == 0):
        membresia_usuario_encontrada = False
    
    return membresia_usuario_encontrada

def buscar_todas_membresias_usuarios():
    """
    Busca a todas las membresia_usuario en la base de datos.

    Returns
    -------
    membresia_usuario_encontrada : list
        Lista de objetos de tipo Membresia_usuario (con toda la información
        encontrada en la base de datos).

    """
    # Se busca a todas las membresias_usuarios en la base de datos, y se
    # obtiene su información.
    conn = sqlite3.connect("usuario")
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM membresia_usuario")
    datos_membresia = cursor.fetchall()
    conn.close()
    
    # Si el retorno de la base de datos es una lista vacía, la función no
    # retorna nada. De lo contrario retorna una lista con objetos
    # Membresia_usuario con los datos encontrados.
    membresia_usuario_encontrada: Membresia_usuario = []
    for elem in datos_membresia:
        membresia_usuario_encontrada.append(Membresia_usuario(elem[0],
                                                              elem[1],
                                                              elem[2]))
    
    # Retorna lista vacía si no se encontró, o con objetos Usuario si sí.
    return membresia_usuario_encontrada

def buscar_consulta_especifica(consulta: str, parametros: tuple):
    # Se busca a todos los usuarios que coincidan con la consulta dada por el
    # string, que especifica los campos específicos buscados.
    conn = sqlite3.connect("usuario")
    cursor = conn.cursor()
    cursor.execute(consulta, parametros)
    datos_membresia_usuario = cursor.fetchall()
    conn.close()
    
    # Se retorna una lista con objetos Membresia_usuario's que contienen la
    # información de cada Membresia_usuario que coincide con la búsqueda.
    membresia_usuario_encontrada: list = []
    for elem in datos_membresia_usuario:
        membresia_usuario_encontrada.append(Membresia_usuario(elem[0],
                                                              elem[1],
                                                              elem[2]))
    
    return membresia_usuario_encontrada

def buscar_membresia_usuario_especifico(inputs_usuario: list):
    """
    Busca una membresia_usuario específico en la base de datos. Recibe una
    lista con los datos de id_usuario, id_membresia y vencimiento (en orden), y
    realiza la consulta a la base de datos con esta información.

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
    la tabla de "membresia_usuario". La misma utiliza los inputs de los 3
    campos:
    id_usuario, id_membresia, vencimiento.

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
    campos: list = ["id_usuario",
                    "id_membresia",
                    "vencimiento"]
    
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
    
    consulta_resultado: str = "SELECT * FROM membresia_usuario WHERE"
    agregar_and: bool = False
    
    for j in consulta:
        if (agregar_and):
            consulta_resultado += " AND"
        
        consulta_resultado += f" {j} = ?"
        
        agregar_and = True
    
    return consulta_resultado, parametros

def buscar_membresia_usuario(caracteristica: str, busqueda: str):
    """
    Busca una membresia_usuario en la base de datos. (tabla membresia_usuario)

    Parameters
    ----------
    caracteristica : str
        Característica a buscar. Esto es, por ejemplo, "id_membresia", "tipo".
    busqueda : str
        Búsqueda que se desea realizar sobre la característica. Por ejemplo, si
        la característica es "tipo", la búsqueda puede ser "Oro".

    Returns
    -------
    membresia_usuario_encontrada : list
        Lista de objetos de tipo Membresia_usuario (con toda la información
        encontrada en la base de datos).

    """
    
    consulta: str = f"SELECT * FROM membresia_usuario WHERE {caracteristica}=?"
    
    # Se busca la membresia_usuario en la base de datos, y se obtiene su
    # información.
    conn = sqlite3.connect("usuario")
    cursor = conn.cursor()
    cursor.execute(consulta, (busqueda,))
    datos_membresia_usuario = cursor.fetchall()
    conn.close()
    
    # Si el retorno de la base de datos es una lista vacía, la función no
    # retorna nada. De lo contrario retorna un objeto Membresia_usuario con los
    # datos encontrados.
    membresia_usuario_encontrada: list = []
    for elem in datos_membresia_usuario:
        membresia_usuario_encontrada.append(Membresia_usuario(elem[0],
                                                              elem[1],
                                                              elem[2]))
    
    # Retorna lista vacía si no se encontró, o con objetos Mebresia_usuario si
    # sí.
    return membresia_usuario_encontrada

def buscar_id_membresia(id_membresia: int):
    """
    Busca una membresia_usuario en la base de datos, por medio de su
    id_membresia.

    Parameters
    ----------
    id_membresia : int
        ID buscada.

    Returns
    -------
    membresia_usuario_encontrada : list
        Lista de objetos de tipo Membresia_usuario (con toda la información
        encontrada en la base de datos).

    """
    # Se busca la membresia_usuario en la base de datos, y se obtiene su
    # información.
    return buscar_membresia_usuario("id_membresia", id_membresia)

def buscar_id_usuario(id_usuario: int):
    """
    Busca una membresia_usuario en la base de datos, por medio de su
    id_membresia. (tabla membresia_usuario)

    Parameters
    ----------
    id_usuario : int
        ID buscada.

    Returns
    -------
    membresia_usuario_encontrada : list
        Lista de objetos de tipo Membresia_usuario (con toda la información
        encontrada en la base de datos).

    """
    # Se busca la membresia_usuario en la base de datos, y se obtiene su
    # información.
    return buscar_membresia_usuario("id_usuario", id_usuario)

def buscar_vencimiento(vencimiento: str):
    """
    Busca una membresia_usuario en la base de datos, por medio de su
    vencimiento. (tabla membresia_usuario)

    Parameters
    ----------
    vencimiento : str
        Fecha de vencimiento.

    Returns
    -------
    membresia_usuario_encontrada : list
        Lista de objetos de tipo Membresia_usuario (con toda la información
        encontrada en la base de datos).

    """
    # Se busca la membresia_usuario en la base de datos, y se obtiene su
    # información.
    return buscar_membresia_usuario("vencimiento", vencimiento)




