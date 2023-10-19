# -*- coding: utf-8 -*-
"""
Created on Sat Oct 14 19:10:32 2023

@author: Cristian, Esteban, Pepe
"""

import sqlite3


class Usuario:
    def __init__(self, id_usuario: int,
                 nombre: str, apellido: str,
                 direccion: str, email: str):
        self.id_usuario = id_usuario
        self.nombre = nombre
        self.apellido = apellido
        self.direccion = direccion
        self.email = email
    
    def __str__(self):
        usuario_completo: str = f"{self.id_usuario}" + "\t"
        usuario_completo += f"{self.nombre}" + "\t"
        usuario_completo += f"{self.apellido}" + "\t"
        usuario_completo += f"{self.direccion}" + "\t"
        usuario_completo += f"{self.email}"
        
        return usuario_completo


def control_menu():
    """
    Controla el flujo del menú principal.
    
    Se muestra el menú y luego se recibe el input del usuario para continuar
    con lo que desee. Los valores del menú son:
    1- Consulta
    2- Alta
    3- Baja
    4- Modificación
    5- Terminar

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
        if (input_usuario == 1):
            # Entra al menú de consultas.
            control_consulta()
            
        elif (input_usuario == 2):
            # Entra al menú de alta.
            control_alta_usuario()
            
        elif (input_usuario == 3):
            # Entra al menú de baja.
            control_baja_usuario()
            
        elif (input_usuario == 4):
            # Entra al menú de modificación.
            control_modificacion_usuario()
            
        elif (input_usuario == 5):
            # Termina el programa.
            repetir_menu = False
            
        else:
            # Si no se ejecutó ninguno de los if's anteriores, entonces el
            # input del usuario fue incorrecto.
            print("\nInput incorrecto.\n")
            
    return
            
def control_consulta():
    """
    Controla el flujo del menú de consulta.
    
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
        if (input_usuario == 1):
            # Mostrar todos los usuarios.
            display_tabla_consulta()
            pass
            
        elif (input_usuario == 2):
            # Buscar por id_usuario.
            print("Inserte id_usuario: ")
            id_usuario: int = int(input())
            
            usuarios: list = buscar_id_usuario(id_usuario)
            
            if (usuarios == None):
                print("No se encontro el id_usuario especificado.")
            else:
                display_tabla_consulta()
                imprimir_lista_usuarios(usuarios)
            
        elif (input_usuario == 3):
            # Buscar por nombre.
            print("Inserte nombre: ")
            nombre: str = input()
            
            usuarios: list = buscar_nombre_usuario(nombre)
            
            if (usuarios == None):
                print("No se encontro el nombre especificado.")
            else:
                display_tabla_consulta()
                imprimir_lista_usuarios(usuarios)
        
        elif (input_usuario == 4):
            # Buscar por apellido.
            print("Inserte apellido: ")
            apellido: str = input()
            
            usuarios: list = buscar_apellido_usuario(apellido)
            
            if (usuarios == None):
                print("No se encontro el apellido especificado.")
            else:
                display_tabla_consulta()
                imprimir_lista_usuarios(usuarios)
        
        elif (input_usuario == 5):
            # Buscar por email.
            print("Inserte email: ")
            email: str = input()
            
            usuarios: list = buscar_email_usuario(email)
            
            if (usuarios == None):
                print("No se encontro el email especificado.")
            else:
                display_tabla_consulta()
                imprimir_lista_usuarios(usuarios)
        
        elif (input_usuario == 6):
            # Buscar por direccion.
            print("Inserte direccion: ")
            direccion: str = input()
            
            usuarios: list = buscar_direccion_usuario(direccion)
            
            if (usuarios == None):
                print("No se encontro el direccion especificado.")
            else:
                display_tabla_consulta()
                imprimir_lista_usuarios(usuarios)
        
        elif (input_usuario == 7):
            # Vuelve al menú principal.
            repetir_menu = False
            
        else:
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

    if (alta_usuario(id_usuario, nombre, apellido, email, direccion)):
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

    if (baja_usuario(id_usuario)):
        print("Se elimino el usuario especificado.")
    else:
        print("No se pudo dar de alta el usuario.")

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

    if (modificar_usuario(id_usuario, nombre, apellido, email, direccion)):
        print("Usuario modificado.")
    else:
        print("No se pudo encontrar y modificar el usuario.")

    return

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
    print("-- Alta de un usuario para la base de datos")

def display_baja_usuario():
    print("-- Baja de un usuario en la base de datos")

def display_modificacion_usuario():
    print("-- Modificacion de un usuario en la base de datos")

def imprimir_lista_usuarios(usuarios: list):
    """
    Imprime una lista de Usuarios (objeto). Imprime cada atributo del objeto.

    Parameters
    ----------
    usuarios : list
        Lista de usuarios a imprimir.

    Returns
    -------
    None.

    """
    for usuario in usuarios:
        print(usuario)
    
def modificar_usuario(id_usuario: int, nombre: str, apellido: str,
                        email: str, direccion: str):
    """
    Busca y modifica un usuario dentro de la base de datos. Si lo encuentra, lo
    modifica. Caso contrario no realiza cambios en la base de datos.

    Parameters
    ----------
    id_usuario : int
        ID del usuario dentro de la base de datos. Puede ser un número
        arbitrario o DNI, etc.
    nombre : str
        Nombre del usuario.
    apellido : str
        Apellido del usuario.
    email : str
        Correo electrónico del usuario.
    direccion : str
        Dirección del usuario.

    Returns
    -------
    usuario_encontrado : bool
        Retorna True si se encontró el usuario, por medio de su id_usuario, y
        se lo modificó. Caso contrario, retorna False porque no se encontró y,
        por ende, no se realizó ninguna modificación.

    """
    usuario_encontrado: bool = True
    
    # Se busca modificar el usuario, por medio de su id_usuario.
    conn = sqlite3.connect('usuario')
    cursor = conn.cursor()
    cursor.execute("UPDATE usuario SET nombre=?, apellido=?, email=?, direccion=? WHERE id_usuario=?", (nombre, apellido, email, direccion, id_usuario))
    conn.commit()
    conn.close()
    
    # Verifica si se encontró y modificó el usuario especificado.
    if (cursor.rowcount == 0):
        usuario_encontrado = False
    
    return usuario_encontrado

def buscar_usuario(caracteristica: str, busqueda: str):
    """
    Busca a un usuario en la base de datos.

    Parameters
    ----------
    caracteristica : str
        Característica a buscar. Esto es, por ejemplo, "nombre", "apellido",
        "email", "direccion".
    busqueda : str
        Búsqueda que se desea realizar sobre la característica. Por ejemplo, si
        la característica es "nombre", la búsqueda puede ser "Juan".

    Returns
    -------
    usuario_encontrado : list
        Lista de objetos de tipo Usuario (con toda la información encontrada en
        la base de datos).

    """
    
    consulta: str = f"SELECT * FROM usuario WHERE {caracteristica}=?"
    
    # Se busca al usuario en la base de datos, y se obtiene su información.
    conn = sqlite3.connect("usuario")
    cursor = conn.cursor()
    cursor.execute(consulta, (busqueda,))
    datos_usuario = cursor.fetchall()
    conn.close()
    
    # Si el retorno de la base de datos es una lista vacía, la función no
    # retorna nada. De lo contrario retorna un objeto Usuario con los datos
    # encontrados.
    usuario_encontrado: Usuario = []
    for elem in datos_usuario:
        usuario_encontrado.append(Usuario(elem[0],
                                          elem[1],
                                          elem[2],
                                          elem[3],
                                          elem[4]))
    
    # Retorna lista vacía si no se encontró, o con objetos Usuario si sí.
    return usuario_encontrado

def buscar_nombre_usuario(nombre: str):
    """
    Busca a un usuario en la base de datos, por medio de su nombre.

    Parameters
    ----------
    nombre : str
        Nombre buscado.

    Returns
    -------
    usuario_encontrado : list
        Lista de objetos de tipo Usuario (con toda la información encontrada en
        la base de datos).

    """
    # Se busca al usuario en la base de datos, y se obtiene su información.
    return buscar_usuario("nombre", nombre)

def buscar_apellido_usuario(apellido: str):
    """
    Busca a un usuario en la base de datos, por medio de su apellido.

    Parameters
    ----------
    apellido : str
        Apellido buscado.

    Returns
    -------
    usuario_encontrado : list
        Lista de objetos de tipo Usuario (con toda la información encontrada en
        la base de datos).

    """
    # Se busca al usuario en la base de datos, y se obtiene su información.
    return buscar_usuario("apellido", apellido)

def buscar_email_usuario(email: str):
    """
    Busca a un usuario en la base de datos, por medio de su email.

    Parameters
    ----------
    email : str
        E-mail buscado.

    Returns
    -------
    usuario_encontrado : list
        Lista de objetos de tipo Usuario (con toda la información encontrada en
        la base de datos).

    """
    # Se busca al usuario en la base de datos, y se obtiene su información.
    return buscar_usuario("email", email)

def buscar_direccion_usuario(direccion: str):
    """
    Busca a un usuario en la base de datos, por medio de su direccion.

    Parameters
    ----------
    direccion : str
        Dirección buscada.

    Returns
    -------
    usuario_encontrado : list
        Lista de objetos de tipo Usuario (con toda la información encontrada en
        la base de datos).

    """
    # Se busca al usuario en la base de datos, y se obtiene su información.
    return buscar_usuario("direccion", direccion)

def buscar_id_usuario(id_usuario: int):
    """
    Busca a un usuario en la base de datos, por medio de su id_usuario.

    Parameters
    ----------
    id_usuario : int
        DESCRIPTION.

    Returns
    -------
    usuario_encontrado : list
        Retorna None si no se encontró. Caso contrario, un objeto de tipo
        Usuario, con toda la información obtenida de la base de datos.

    """
    # Se busca al usuario en la base de datos, y se obtiene su información.
    conn = sqlite3.connect("usuario")
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM usuario WHERE id_usuario=?", (id_usuario,))
    datos_usuario = cursor.fetchall()
    conn.close()
    
    # Si el retorno de la base de datos es una lista vacía, la función no
    # retorna nada. De lo contrario retorna un objeto Usuario con los datos
    # encontrados.
    usuario_encontrado: list = []
    if (len(datos_usuario) != 0):
        usuario_encontrado.append(Usuario(datos_usuario[0][0],
                                     datos_usuario[0][1],
                                     datos_usuario[0][2],
                                     datos_usuario[0][3],
                                     datos_usuario[0][4]))
    
    # Retorna lista vacía si no se encontró, o con objetos Usuario si sí.
    return usuario_encontrado

def alta_usuario(id_usuario: int, nombre: str, apellido: str,
                   email: str, direccion: str):
    """
    Da de alta/crea un usuario en la base de datos. Esta función que se
    comunica con la base de datos.
    En caso de que no se pueda dar de alta, imprime un mensaje con el error
    que haya ocurrido.

    Parameters
    ----------
    id_usuario : int
        ID del usuario dentro de la base de datos. Puede ser un número
        arbitrario o DNI, etc.
    nombre : str
        Nombre del usuario.
    apellido : str
        Apellido del usuario.
    email : str
        Correo electrónico del usuario.
    direccion : str
        Dirección del usuario.

    Returns
    -------
    usuario_creado : bool
        Retorna True en caso de que haya podido dar de alta al usuario en la
        base de datos. Caso contrario retorna False.

    """
    usuario_creado: bool = True

    conn = sqlite3.connect("usuario")
    cursor = conn.cursor()
    
    try:
        cursor.execute("INSERT INTO usuario (id_usuario, nombre, apellido, email, direccion) VALUES (?, ?, ?, ?, ?)", (id_usuario, nombre, apellido, email, direccion))
        conn.commit()
    except Exception as exc:
        usuario_creado = False
        print(f"Error al crear usuario en la base de datos: {type(exc)}")

    conn.close()
    
    return usuario_creado

def baja_usuario(id_usuario: int):
    """
    Da de baja/elimina un usuario en la base de datos, por medio de un
    id_usuario otorgado.
    
    Parameters
    ----------
    id_usuario : int
        ID del usuario a eliminar en la base de datos.

    Returns
    -------
    usuario_encontrado : bool
        Retorna True en caso de que haya podido encontrar al usuario. En ese
        caso, fue borrado. De lo contrario, retorna False.

    """
    usuario_encontrado: bool = True
    
    # Se busca al usuario en la base de datos y se lo borra.
    conn = sqlite3.connect("usuario")
    cursor = conn.cursor()
    cursor.execute("DELETE FROM usuario WHERE id_usuario=?", (id_usuario,))
    conn.commit()
    conn.close()
    
    # Si no se encontró ningún usuario, entonces no se realizaron cambios en la
    # base de datos.
    if (cursor.rowcount == 0):
        usuario_encontrado = False
    
    return usuario_encontrado

def main():
    control_menu()
    print("\nFin del programa.\n")

main()

#Prueba creacion de usuario en la base de datos
#usuario1 = Usuario("Juan", "Perez", "direccion1", "email@gmail.com")
#usuario2 = (18422, "Esteban", "Capuccino", "direccion1", "email@gmail.com")
#alta_usuario(usuario1)
#alta_usuario(usuario2[0], usuario2[1], usuario2[2], usuario2[3], usuario2[4])

#Prueba para borrar un usuario de la base de datos
#baja_usuario(1)

#Prueba de busqueda de un id_usuario
#busqueda = buscar_id_usuario(16472)
#print(busqueda)
#print(type(busqueda))

#Prueba para modificar a un usuario
#modificar_usuario(3, "Esteban", "Capo", "@mail", "bari")

# Prueba para buscar usuarios
"""
print("nombre existente")
for x in buscar_nombre_usuario("Esteban"):
    print(x)
print("nombre no existente")
for x in buscar_nombre_usuario("asdasd"):
    print(x)
print("apellido existente")
for x in buscar_apellido_usuario("Capuccino"):
    print(x)
print("apellido no existente")
for x in buscar_apellido_usuario("qwrwe"):
    print(x)
print("email existente")
for x in buscar_email_usuario("email@gmail.com"):
    print(x)
print("email no existente")
for x in buscar_email_usuario("ggaga"):
    print(x)
print("direccion existente")
for x in buscar_direccion_usuario("direccion1"):
    print(x)
print("direccion no existente")
for x in buscar_direccion_usuario("asdasg"):
    print(x)
"""




