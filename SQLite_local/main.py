# -*- coding: utf-8 -*-
"""
Created on Tue Oct 24 14:04:14 2023

@author: Cristian, Esteban, Pepe
"""

import menu_usuarios
import menu_membresias
import menu_membresias_usuarios

def control_main():
    """
    Controla el flujo del menú principal (desde el main).
    
    Se muestra el menú y luego se recibe el input del usuario para continuar
    con lo que desee. Los valores del menú son:
    1- Usuarios
    2- Membresias (tipos)
    3- Registros de membresias-usuarios
    4- Terminar

    Returns
    -------
    None.

    """
    
    display_main_bienvenida()

    # Input del usuario.
    input_usuario: int = -1
    
    # Flag para repetir el menú hasta que se termine el programa.
    repetir_menu: bool = True
    
    while (repetir_menu):
        display_main_menu()
        input_usuario = int(input())
        
        # Se verifica que se haya seleccionado alguna de las opciones válidas.
        match input_usuario:
            case 1:
                # Entra al menú de la tabla de Usuarios.
                menu_usuarios.control_menu()
            
            case 2:
                # Entra al menú de la tabla de Membresias.
                menu_membresias.control_menu()    
            
            case 3:
                # Entra al menú de la tabla de Membresias_usuarios.
                menu_membresias_usuarios.control_menu()
            
            case 4:
                # Termina el programa.
                repetir_menu = False
                
            case _:
                # Si no se ejecutó ninguno de los if's anteriores, entonces el
                # input del usuario fue incorrecto.
                print("\nInput incorrecto.\n")
            
    return

def display_main_bienvenida():
    print("Bienvenido al programa de consulta, modificacion,")
    print("creacion y eliminacion de usuarios y membresias para la base")
    print("de datos\n")

def display_main_menu():
    print("¿Con que tabla de la base de datos desearia conectarse?")
    print("1- Usuarios")
    print("2- Membresias (tipos)")
    print("3- Registros de membresias-usuarios")
    print("4- Terminar")

def main():
    control_main()
    print("\nFin del programa.\n")

if (__name__ == "__main__"):
    main()
