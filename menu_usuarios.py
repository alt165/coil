# -*- coding: utf-8 -*-
"""
Created on Tue Oct 24 14:04:14 2023

@author: Cristian, Esteban, Pepe
"""

import usuarios as usr


def control_menu():
    """
    Controla el flujo del menú principal de la tabla de Usuarios.
    
    Se muestra el menú y luego se recibe el input del usuario para continuar
    con lo que desee. Los valores del menú son:
    1- Consulta
    2- Alta
    3- Baja
    4- Modificación
    5- Atras

    Returns
    -------
    None.

    """
    
    # Input del usuario.
    input_usuario: int = -1
    
    # Flag para repetir el menú hasta que se termine el programa.
    repetir_menu: bool = True
    
    # Se repite el menú hasta que ingrese el valor que termina el programa.
    while (repetir_menu):
        display_menu()
        input_usuario = int(input())
        
        # Se verifica que se haya seleccionado alguna de las opciones válidas.
        match (input_usuario):
            case 1:
                # Entra al menú de consultas.
                control_consulta()
                
            case 2:
                # Entra al menú de alta.
                control_alta_usuario()
                
            case 3:
                # Entra al menú de baja.
                control_baja_usuario()
                
            case 4:
                # Entra al menú de modificación.
                control_modificacion_usuario()
                
            case 5:
                # Termina el programa actual.
                repetir_menu = False
                
            case _:
                # Si no se ejecutó ninguno de los if's anteriores, entonces el
                # input del usuario fue incorrecto.
                print("\nInput incorrecto.\n")
            
    return
            
def control_consulta():
    """
    Controla el flujo del menú de consulta de la tabla de usuarios.
    
    Se muestra el menú y luego se recibe el input del usuario para continuar
    con lo que desee. Los valores del menú son:
    1- Mostrar todos los usuarios
    2- Buscar por id_usuario
    3- Buscar por nombre
    4- Buscar por apellido
    5- Buscar por email
    6- Buscar por direccion
    7- Atras

    Returns
    -------
    None.

    """
    
    # Input del usuario.
    input_usuario: int = -1
    
    # Flag para repetir el menú hasta que se termine el programa.
    repetir_menu: bool = True
    
    # Se repite el menú hasta que ingrese el valor que termina el programa.
    while (repetir_menu):
        display_consulta()
        input_usuario = int(input())
        
        # Se verifica que se haya seleccionado alguna de las opciones válidas.
        match (input_usuario):
            case 1:
                # Mostrar todos los usuarios.
                usuarios: list = usr.buscar_todos_usuarios()
                
                if (usuarios == None):
                    print("No se encontraron usuarios.")
                else:
                    display_tabla_consulta()
                    usr.imprimir_lista_usuarios(usuarios)
                
            case 2:
                # Buscar por id_usuario.
                print("Inserte id_usuario: ")
                id_usuario: int = int(input())
                
                usuarios: list = usr.buscar_id_usuario(id_usuario)
                
                if (usuarios == None):
                    print("No se encontro el id_usuario especificado.")
                else:
                    display_tabla_consulta()
                    usr.imprimir_lista_usuarios(usuarios)
                
            case 3:
                # Buscar por nombre.
                print("Inserte nombre: ")
                nombre: str = input()
                
                usuarios: list = usr.buscar_nombre_usuario(nombre)
                
                if (usuarios == None):
                    print("No se encontro el nombre especificado.")
                else:
                    display_tabla_consulta()
                    usr.imprimir_lista_usuarios(usuarios)
            
            case 4:
                # Buscar por apellido.
                print("Inserte apellido: ")
                apellido: str = input()
                
                usuarios: list = usr.buscar_apellido_usuario(apellido)
                
                if (usuarios == None):
                    print("No se encontro el apellido especificado.")
                else:
                    display_tabla_consulta()
                    usr.imprimir_lista_usuarios(usuarios)
            
            case 5:
                # Buscar por email.
                print("Inserte email: ")
                email: str = input()
                
                usuarios: list = usr.buscar_email_usuario(email)
                
                if (usuarios == None):
                    print("No se encontro el email especificado.")
                else:
                    display_tabla_consulta()
                    usr.imprimir_lista_usuarios(usuarios)
            
            case 6:
                # Buscar por direccion.
                print("Inserte direccion: ")
                direccion: str = input()
                
                usuarios: list = usr.buscar_direccion_usuario(direccion)
                
                if (usuarios == None):
                    print("No se encontro el direccion especificado.")
                else:
                    display_tabla_consulta()
                    usr.imprimir_lista_usuarios(usuarios)
            
            case 7:
                # Vuelve al menú principal.
                repetir_menu = False
                
            case _:
                # Si no se ejecutó ninguno de los if's anteriores, entonces el
                # input del usuario fue incorrecto.
                print("\nInput incorrecto.\n")
            
    return

def control_alta_usuario():
    """
    Controla el flujo del menú de alta de usuario.

    Returns
    -------
    None.

    """
    display_alta_usuario()
    
    print("Ingrese los datos del nuevo usuario:")
    
    # Input del usuario.
    print("id_usuario: ")
    id_usuario: int = int(input())
    
    print("nombre: ")
    nombre: str = input()
    
    print("apellido: ")
    apellido: str = input()
    
    print("email: ")
    email: str = input()
    
    print("direccion: ")
    direccion: str = input()

    if (usr.alta_usuario(id_usuario, nombre, apellido, email, direccion)):
        print("Usuario nuevo creado.")
    else:
        print("No se pudo dar de alta el usuario.")

    return

def control_baja_usuario():
    """
    Controla el flujo del menú de baja de usuario.

    Returns
    -------
    None.

    """
    display_baja_usuario()
    
    print("Ingrese el id_usuario que desea dar de baja:")
    
    # Input del usuario.
    print("id_usuario: ")
    id_usuario: int = int(input())

    if (usr.baja_usuario(id_usuario)):
        print("Se elimino el usuario especificado.")
    else:
        print("No se pudo eliminar el usuario.")

    return

def control_modificacion_usuario():
    """
    Controla el flujo del menú de modificación de usuario.

    Returns
    -------
    None.

    """
    display_modificacion_usuario()
    
    print("Ingrese los datos del usuario a modificar:")
    
    # Input del usuario.
    print("id_usuario: ")
    id_usuario: int = int(input())
    
    print("nombre: ")
    nombre: str = input()
    
    print("apellido: ")
    apellido: str = input()
    
    print("email: ")
    email: str = input()
    
    print("direccion: ")
    direccion: str = input()

    if (usr.modificar_usuario(id_usuario, nombre, apellido, email, direccion)):
        print("Usuario modificado.")
    else:
        print("No se pudo encontrar y modificar el usuario.")

    return

def display_menu():
    print("Menú de la tabla Usuarios:")
    print("Inserte comando:")
    print("1- Consulta")
    print("2- Alta")
    print("3- Baja")
    print("4- Modificación")
    print("5- Atras")

def display_consulta():
    print("-- Consulta de Usuarios de la base de datos")
    print("Inserte comando:")
    print("1- Mostrar todos los usuarios")
    print("2- Buscar por id_usuario")
    print("3- Buscar por nombre")
    print("4- Buscar por apellido")
    print("5- Buscar por email")
    print("6- Buscar por direccion")
    print("7- Atras")

def display_tabla_consulta():
    mensaje: str = "id_usuario" + "\t"
    mensaje += "nombre" + "\t"
    mensaje += "apellido" + "\t"
    mensaje += "email" + "\t"
    mensaje += "direccion"
    print(mensaje)

def display_alta_usuario():
    print("-- Alta de un Usuario para la base de datos")

def display_baja_usuario():
    print("-- Baja de un Usuario en la base de datos")

def display_modificacion_usuario():
    print("-- Modificacion de un Usuario en la base de datos")
