# -*- coding: utf-8 -*-
"""
Created on Tue Oct 24 14:04:14 2023

@author: Cristian, Esteban, Pepe
"""

import membresias as mem


def control_menu():
    """
    Controla el flujo del menú principal de la tabla de Membresias.
    
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
                # Entra al menú de creación de membresia.
                control_creacion_membresia()
                
            case 3:
                # Entra al menú de eliminacion de membresia.
                control_eliminacion_membresia()
                
            case 4:
                # Entra al menú de modificación de membresia.
                control_modificacion_membresia()
                
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
    Controla el flujo del menú de consulta de la tabla de membresias.
    
    Se muestra el menú y luego se recibe el input del usuario para continuar
    con lo que desee. Los valores del menú son:
    1- Mostrar todas los membresias
    2- Buscar por id_membresia
    3- Buscar por tipo
    4- Atras

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
                # Mostrar todas las membresias.
                membresias: list = mem.buscar_todas_membresias()
                
                if (membresias == None):
                    print("No se encontraron membresias.")
                else:
                    display_tabla_consulta()
                    mem.imprimir_lista_membresias(membresias)
                
            case 2:
                # Buscar por id_membresia.
                print("Inserte id_membresia: ")
                id_membresia: int = int(input())
                
                membresias: list = mem.buscar_id_membresia(id_membresia)
                
                if (membresias == None):
                    print("No se encontro el id_membresia especificado.")
                else:
                    display_tabla_consulta()
                    mem.imprimir_lista_membresias(membresias)
                
            case 3:
                # Buscar por tipo.
                print("Inserte tipo de membresia: ")
                tipo: str = input()
                
                membresias: list = mem.buscar_tipo_membresia(tipo)
                
                if (membresias == None):
                    print("No se encontro el tipo especificado.")
                else:
                    display_tabla_consulta()
                    mem.imprimir_lista_membresias(membresias)
            
            case 4:
                # Vuelve al menú principal.
                repetir_menu = False
                
            case _:
                # Si no se ejecutó ninguno de los if's anteriores, entonces el
                # input del usuario fue incorrecto.
                print("\nInput incorrecto.\n")
            
    return

def control_creacion_membresia():
    """
    Controla el flujo del menú de creación de membresia.

    Returns
    -------
    None.

    """
    display_creacion_membresia()
    
    print("Ingrese los datos de la nueva membresia:")
    
    # Input del usuario.
    print("id_membresia: ")
    id_membresia: int = int(input())
    
    print("tipo: ")
    tipo: str = input()

    if (mem.crear_membresia(id_membresia, tipo)):
        print("Membresia nueva creada.")
    else:
        print("No se pudo crear la membresia.")

    return

def control_eliminacion_membresia():
    """
    Controla el flujo del menú de eliminación de membresias.

    Returns
    -------
    None.

    """
    display_eliminacion_membresia()
    
    print("Ingrese el id_membresia que desea eliminar:")
    
    # Input del usuario.
    print("id_membresia: ")
    id_membresia: int = int(input())

    if (mem.eliminar_membresia(id_membresia)):
        print("Se elimino la membresia especificado.")
    else:
        print("No se pudo eliminar la membresia.")

    return

def control_modificacion_membresia():
    """
    Controla el flujo del menú de modificación de membresia.

    Returns
    -------
    None.

    """
    display_modificacion_membresia()
    
    print("Ingrese los datos de la membresia a modificar:")
    
    # Input del usuario.
    print("id_membresia: ")
    id_membresia: int = int(input())
    
    print("tipo: ")
    tipo: str = input()

    if (mem.modificar_membresia(id_membresia, tipo)):
        print("Membresia modificada.")
    else:
        print("No se pudo encontrar y modificar la membresia.")

    return

def display_menu():
    print("Menú de la tabla Membresias:")
    print("Inserte comando:")
    print("1- Consulta")
    print("2- Creacion")
    print("3- Eliminacion")
    print("4- Modificación")
    print("5- Atras")

def display_tabla_consulta():
    mensaje: str = "id_membresia" + "\t"
    mensaje += "tipo" 
    print(mensaje)
    
def display_consulta():
    print("-- Consulta de Membresias de la base de datos")
    print("Inserte comando:")
    print("1- Mostrar todos los membresias")
    print("2- Buscar por id_membresia")
    print("3- Buscar por tipo")
    print("4- Atras")

def display_creacion_membresia():
    print("-- Creacion de una Membresia para la base de datos")

def display_eliminacion_membresia():
    print("-- Baja de una Membresia en la base de datos")

def display_modificacion_membresia():
    print("-- Modificacion de una Membresia en la base de datos")
