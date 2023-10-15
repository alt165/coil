# -*- coding: utf-8 -*-
"""
Created on Sat Oct 14 19:10:32 2023

@author: Cristian, Esteban, Pepe
"""

import sqlite3

#con = sqlite3.connect("usuario.")
#cur = con.cursor()

"""
tiene q tener:
    consulta
    dar de alta
    dar de baja
    modificacion

"""


class Usuario:
    def __init__(self, id_usuario: int,
                 nombre: str, apellido: str,
                 direccion: str, email: str):
        self.id_usuario = id_usuario
        self.nombre = nombre
        self.apellido = apellido
        self.direccion = direccion
        self.email = email

def display_menu():
    print("Menú de la base de datos")
    print("Inserte comando:")
    print("1- Consulta")
    print("2- Alta")
    print("3- Baja")
    print("4- Modificación")
    print("5- Terminar")

def display_consulta():
    print("-- Consulta de la base de datos")
    print("Inserte comando:")
    print("1- Mostrar todos los usuarios")
    print("2- Buscar por id_usuario")
    print("3- Buscar por nombre")
    print("4- Buscar por apellido")
    print("5- Buscar por direccion")
    print("6- Buscar por email")
    print("7- Atras")

def display_alta_usuario():
    print("-- Alta de un usuario para la base de datos")

def display_baja_usuario():
    print("-- Baja de un usuario en la base de datos")

def display_modificacion_usuario():
    print("-- Modificacion de un usuario en la base de datos")
    print("Inserte el id_usuario:")
    
    id_usuario: int = int(input())
    usuario_a_modificar: Usuario = buscar_id_usuario(id_usuario)
    
    
    
def buscar_id_usuario(id_usuario: int):
    usuario_encontrado: Usuario = Usuario()
    
    conn = sqlite3.connect("usuario")
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM usuario WHERE id_usuario=?", (id_usuario,))
    datos_usuario = cursor.fetchall()
    conn.close()
    
    usuario_encontrado = Usuario()
    
    return usuario_encontrado
    
def alta_usuario(usuario: Usuario):
    """
    Da de alta/crea un usuario en la base de datos. Es la función que se
    comunica con la base de datos.

    Parameters
    ----------
    usuario : Usuario
        Objeto Usuario que contiene la información de un usuario en la base de
        datos.

    Returns
    -------
    None.

    """
    conn = sqlite3.connect("usuario")
    cursor = conn.cursor()
    cursor.execute("INSERT INTO usuario (nombre, apellido, direccion, email) VALUES (?, ?, ?, ?)", (usuario.nombre, usuario.apellido, usuario.direccion, usuario.email))
    conn.commit()
    conn.close()

def crear_usuario(nombre: str, apellido: str, direccion: str, email: str):
    """
    Crea un usuario, a partir de sus atributos (excluyendo el id_usuario):
    nombre, apellido, direccion, email.
    Se excluye el id_usuario, ya que la tabla dentro de la base de datos es
    autoincremental, por lo que no se le puede asignar arbitrariamente su ID.
    Al crear el usuario, llama la función alta_usuario con el objeto Usuario
    creado (que es la función que termina de comunicarse con la base de datos,
    para que se inserte el mismo en la base).

    Parameters
    ----------
    nombre : str
        Nombre del usuario.
    apellido : str
        Apellido del usuario.
    direccion : str
        Dirección del usuario.
    email : str
        Correo electrónico del usuario.

    Returns
    -------
    None.

    """
    usuario_nuevo: Usuario = Usuario(None, nombre, apellido, direccion, email)
    alta_usuario(usuario_nuevo)

def baja_usuario(id_usuario: int):
    """
    Da de baja/elimina un usuario en la base de datos.

    Parameters
    ----------
    id_usuario : int
        ID del usuario a eliminar en la base de datos.

    Returns
    -------
    None.

    """
    conn = sqlite3.connect("usuario")
    cursor = conn.cursor()
    cursor.execute("DELETE FROM usuario WHERE id_usuario=?", (id_usuario,))
    conn.commit()
    conn.close()

#def control_menu():
    #input_usuario = (int)input()
    
    #while 

#Prueba creacion de usuario en la base de datos
#usuario1 = Usuario("Juan", "Perez", "direccion1", "email@gmail.com")
#alta_usuario(usuario1)

#Prueba para borrar un usuario de la base de datos
#baja_usuario(1)

