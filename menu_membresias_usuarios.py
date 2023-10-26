# -*- coding: utf-8 -*-
"""
Created on Tue Oct 24 14:04:14 2023

@author: Cristian, Esteban, Pepe
"""

import membresias_usuarios as mem_usr



def control_menu():
    """
    Controla el flujo del menú principal de la tabla de membresia_usuario.
    
    Se muestra el menú y luego se recibe el input del usuario para continuar
    con lo que desee. Los valores del menú son:
    1- Consulta
    2- Creacion
    3- Eliminacion
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
                # Entra al menú de creación de membresia_usuario.
                control_creacion_membresia_usuario()
                
            case 3:
                # Entra al menú de eliminacion de membresia_usuario.
                control_eliminacion_membresia_usuario()
                
            case 4:
                # Entra al menú de modificación de membresia_usuario.
                control_modificacion_membresia_usuario()
                
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
    Controla el flujo del menú de consulta de la tabla de membresia_usuario.
    
    Se muestra el menú y luego se recibe el input del usuario para continuar
    con lo que desee. Los valores del menú son:
    1- Mostrar todas los membresias
    2- Buscar por id_usuario
    3- Buscar por id_membresia
    4- Buscar por vencimiento
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
        display_consulta()
        input_usuario = int(input())
        
        # Se verifica que se haya seleccionado alguna de las opciones válidas.
        match (input_usuario):
            case 1:
                # Mostrar todas las membresia_usuario.
                membresias_usuarios: list = mem_usr.buscar_todas_membresias_usuarios()
                
                if (membresias_usuarios == None):
                    print("No se encontraron membresias.")
                else:
                    display_tabla_consulta()
                    mem_usr.imprimir_lista_membresias_usuarios(membresias_usuarios)
                
            case 2:
                # Buscar por id_usuario.
                print("Inserte id_usuario: ")
                id_usuario: int = int(input())
                
                membresias_usuarios: list = mem_usr.buscar_id_usuario(id_usuario)
                
                if (membresias_usuarios == None):
                    print("No se encontro el id_usuario especificado.")
                else:
                    display_tabla_consulta()
                    mem_usr.imprimir_lista_membresias_usuarios(membresias_usuarios)
                
            case 3:
                # Buscar por id_membresia.
                print("Inserte id_membresia: ")
                id_membresia: int = int(input())
                
                membresias_usuarios: list = mem_usr.buscar_id_membresia(id_membresia)
                
                if (membresias_usuarios == None):
                    print("No se encontro el id_membresia especificado.")
                else:
                    display_tabla_consulta()
                    mem_usr.imprimir_lista_membresias_usuarios(membresias_usuarios)
                
            case 4:
                # Buscar por vencimiento.
                print("Inserte vencimiento (DD-MM-AAAA): ")
                vencimiento: str = input()
                
                membresias_usuarios: list = mem_usr.buscar_vencimiento(vencimiento)
                
                if (membresias_usuarios == None):
                    print("No se encontro el vencimiento especificado.")
                else:
                    display_tabla_consulta()
                    mem_usr.imprimir_lista_membresias(membresias_usuarios)
            
            case 5:
                # Vuelve al menú principal.
                repetir_menu = False
                
            case _:
                # Si no se ejecutó ninguno de los if's anteriores, entonces el
                # input del usuario fue incorrecto.
                print("\nInput incorrecto.\n")
            
    return

def control_creacion_membresia_usuario():
    """
    Controla el flujo del menú de creación de membresia_usuario.

    Returns
    -------
    None.

    """
    display_creacion_membresia_usuario()
    
    print("Ingrese los datos de la nueva membresia_usuario:")
    
    # Input del usuario.
    print("id_usuario: ")
    id_usuario: int = int(input())
    
    print("id_membresia: ")
    id_membresia: int = int(input())
    
    print("vencimiento: ")
    vencimiento: str = str(input())

    if (mem_usr.crear_membresia_usuario(id_usuario, id_membresia, vencimiento)):
        print("Membresia_usuario nueva creada.")
    else:
        print("No se pudo crear la membresia_usuario.")

    return

def control_eliminacion_membresia_usuario():
    """
    Controla el flujo del menú de eliminación de una membresia_usuario.

    Returns
    -------
    None.

    """
    display_eliminacion_membresia_usuario()
    
    print("Ingrese el id_usuario que desea eliminar:")
    
    # Input del usuario.
    print("id_usuario: ")
    id_usuario: int = int(input())

    if (mem_usr.eliminar_membresia_usuario(id_usuario)):
        print("Se elimino la membresia_usuario especificado.")
    else:
        print("No se pudo eliminar la membresia_usuario.")

    return

def control_modificacion_membresia_usuario():
    """
    Controla el flujo del menú de modificación de membresia_usuario.

    Returns
    -------
    None.

    """
    display_modificacion_membresia_usuario()
    
    print("Ingrese los datos de la membresia_usuario a modificar:")
    
    # Input del usuario.
    print("id_usuario: ")
    id_usuario: int = int(input())
    
    print("id_membresia: ")
    id_membresia: int = int(input())
    
    print("vencimiento: ")
    vencimiento: str = input()

    if (mem_usr.modificar_membresia_usuario(id_usuario, id_membresia, vencimiento)):
        print("Membresia_usuario modificada.")
    else:
        print("No se pudo encontrar y modificar la membresia_usuario.")

    return

def display_menu():
    print("Menú de la tabla membresia_usuario:")
    print("Inserte comando:")
    print("1- Consulta")
    print("2- Creacion")
    print("3- Eliminacion")
    print("4- Modificación")
    print("5- Atras")

def display_tabla_consulta():
    mensaje: str = "id_usuario" + "\t"
    mensaje += "id_membresia" + "\t"
    mensaje += "vencimiento" 
    print(mensaje)
    
def display_consulta():
    print("-- Consulta de membresia_usuario's de la base de datos")
    print("Inserte comando:")
    print("1- Mostrar todos los membresias")
    print("2- Buscar por id_usuario")
    print("3- Buscar por id_membresia")
    print("4- Buscar por vencimiento")
    print("5- Atras")

def display_creacion_membresia_usuario():
    print("-- Creacion de una membresia_usuario para la base de datos")

def display_eliminacion_membresia_usuario():
    print("-- Baja de una membresia_usuario en la base de datos")

def display_modificacion_membresia_usuario():
    print("-- Modificacion de una membresia_usuario en la base de datos")

control_menu()