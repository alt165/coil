# -*- coding: utf-8 -*-
"""
Created on Thu Nov  9 18:32:56 2023

@author: Cristian
"""

import flet as ft

from google.cloud import bigquery
from google.oauth2 import service_account

import usuarios as usr
import membresias as mem


class TablaUsuario:
    def __init__ (self, client: bigquery.Client):
        """
        Constructor del menú de la Tabla de Usuarios.

        Parameters
        ----------
        client : bigquery.Client
            Cliente autenticado en Google para utilizar BigQuery.

        Returns
        -------
        None.

        """
        # Se inicializa el cliente autenticado en Google, para hacer la
        # conexión con BigQuery.
        self.client = client
        
        # Se inicializa una tabla con los nombres de los campos de la tabla.
        self.columnas: list = [
            ft.DataColumn(ft.Text("ID_USUARIO"   )),
            ft.DataColumn(ft.Text("NOMBRE_USR"   )),
            ft.DataColumn(ft.Text("APELLIDO_USR" )),
            ft.DataColumn(ft.Text("DIRECCION_USR")),
            ft.DataColumn(ft.Text("CORREO_E_USR" )),
            ft.DataColumn(ft.Text("ID_MEMBRESIA" ))
        ]
        self.filas: list = []
        
        # Se inicializan los campos de texto, a los que mas tarde se les
        # asignarán los valores deseados por el usuario.
        self.id_usuario     = None
        self.nombre         = None
        self.apellido       = None
        self.direccion      = None
        self.email          = None
        self.id_membresia   = None
        self.limite         = None
        
        # Se guardan en atributos las funcionalidades del programa.
        self.consultar_todos_usuarios   = None
        self.consultar_usuario          = None
        self.modificar_usuario          = None
        self.crear_usuario              = None
        self.eliminar_usuario           = None
        
    def gui_usuarios(self):
        def consultar_todos_usuarios():
            # Se verifica que haya al menos una cantidad de usuarios a mostrar.
            limite = 50
            try:
                limite = int(self.limite.value)
            except Exception:
                limite = 50
            if (limite <= 0):
                limite = 50
            
            # Se hace la consulta a la base de datos.
            resultados = usr.buscar_usuarios_sin_criterios(
                client = self.client, limite = limite
            )
            
            filas: list = []
            
            for fila in resultados:
                filas.append(
                    ft.DataRow(
                        cells = [
                            ft.DataCell(ft.Text(str(fila.ID_USUARIO))),
                            ft.DataCell(ft.Text(fila.NOMBRE_USR)),
                            ft.DataCell(ft.Text(fila.APELLIDO_USR)),
                            ft.DataCell(ft.Text(fila.DIRECCION_USR)),
                            ft.DataCell(ft.Text(fila.CORREO_E_USR)),
                            ft.DataCell(ft.Text(fila.ID_MEMBRESIA)),
                        ]
                    )
                )
            
            # Se actualizan las filas.
            self.filas = filas
            
            # Se actualiza la tabla.
            tabla           = ft.DataTable(
                columns = self.columnas,
                rows    = self.filas
            )
            contenedor_tabla = ft.Container(tabla, alignment=ft.alignment.center)
            
            # Se actualiza el contenedor para que muestre el menú nuevo.
            estructura = ft.Column([
                contenedor_header,
                contenedor_menu,
                contenedor_tabla
            ])
            contenedor.content = ft.Container(
                estructura,
                alignment=ft.alignment.center
            )
            contenedor.update()
        
        def consultar_usuario():
            # Se verifica que haya al menos una cantidad de usuarios a mostrar.
            limite = 50
            try:
                limite = int(self.limite.value)
            except Exception:
                limite = 50
            if (limite <= 0):
                limite = 50
            
            # Se hace la consulta a la base de datos.
            resultados = usr.buscar_usuario_especifico(
                client = self.client,
                inputs_usuario = [
                    str(self.id_usuario.value),
                    str(self.nombre.value),
                    str(self.apellido.value),
                    str(self.direccion.value),
                    str(self.email.value),
                    str(self.id_membresia.value),
                ],
                limite = limite
            )
            
            filas: list = []
            
            # Se crean las filas en base a los resultados de la base de datos.
            for fila in resultados:
                filas.append(
                    ft.DataRow(
                        cells = [
                            ft.DataCell(ft.Text(str(fila.ID_USUARIO))),
                            ft.DataCell(ft.Text(fila.NOMBRE_USR)),
                            ft.DataCell(ft.Text(fila.APELLIDO_USR)),
                            ft.DataCell(ft.Text(fila.DIRECCION_USR)),
                            ft.DataCell(ft.Text(fila.CORREO_E_USR)),
                            ft.DataCell(ft.Text(fila.ID_MEMBRESIA)),
                        ]
                    )
                )
            
            # Se actualizan las filas.
            self.filas = filas
            
            # Se actualiza la tabla.
            tabla           = ft.DataTable(
                columns = self.columnas,
                rows    = self.filas
            )
            contenedor_tabla = ft.Container(tabla, alignment=ft.alignment.center)
            
            # Se actualiza el contenedor para que muestre el menú nuevo.
            estructura = ft.Column([
                contenedor_header,
                contenedor_menu,
                contenedor_tabla
            ])
            contenedor.content = ft.Container(
                estructura,
                alignment=ft.alignment.center
            )
            contenedor.update()
        
        def modificar_usuario():
            # Se hace la consulta a la base de datos.
            resultados = usr.modificar_usuario_especifico(
                client = self.client,
                inputs_usuario = [
                    str(self.id_usuario.value),
                    str(self.nombre.value),
                    str(self.apellido.value),
                    str(self.direccion.value),
                    str(self.email.value),
                    str(self.id_membresia.value),
                ]
            )
            
            filas: list = []
            
            # Se crean las filas en base a los resultados de la base de datos.
            for fila in resultados:
                filas.append(
                    ft.DataRow(
                        cells = [
                            ft.DataCell(ft.Text(str(fila.ID_USUARIO))),
                            ft.DataCell(ft.Text(fila.NOMBRE_USR)),
                            ft.DataCell(ft.Text(fila.APELLIDO_USR)),
                            ft.DataCell(ft.Text(fila.DIRECCION_USR)),
                            ft.DataCell(ft.Text(fila.CORREO_E_USR)),
                            ft.DataCell(ft.Text(fila.ID_MEMBRESIA)),
                        ]
                    )
                )
            
            # Se actualizan las filas.
            self.filas = filas
            
            # Se actualiza la tabla.
            tabla           = ft.DataTable(
                columns = self.columnas,
                rows    = self.filas
            )
            contenedor_tabla = ft.Container(tabla, alignment=ft.alignment.center)
            
            # Se actualiza el contenedor para que muestre el menú nuevo.
            estructura = ft.Column([
                contenedor_header,
                contenedor_menu,
                contenedor_tabla
            ])
            contenedor.content = ft.Container(
                estructura,
                alignment=ft.alignment.center
            )
            contenedor.update()
        
        def crear_usuario():
            # Se hace la consulta a la base de datos.
            resultados = usr.crear_usuario(
                client = self.client,
                ID_USUARIO = str(self.id_usuario.value),
                NOMBRE_USR = str(self.nombre.value),
                APELLIDO_USR = str(self.apellido.value),
                DIRECCION_USR = str(self.direccion.value),
                CORREO_E_USR = str(self.email.value),
                ID_MEMBRESIA = str(self.id_membresia.value)
            )
            
            filas: list = []
            
            # Se crean las filas en base a los resultados de la base de datos.
            for fila in resultados:
                filas.append(
                    ft.DataRow(
                        cells = [
                            ft.DataCell(ft.Text(str(fila.ID_USUARIO))),
                            ft.DataCell(ft.Text(fila.NOMBRE_USR)),
                            ft.DataCell(ft.Text(fila.APELLIDO_USR)),
                            ft.DataCell(ft.Text(fila.DIRECCION_USR)),
                            ft.DataCell(ft.Text(fila.CORREO_E_USR)),
                            ft.DataCell(ft.Text(fila.ID_MEMBRESIA)),
                        ]
                    )
                )
            
            # Se actualizan las filas.
            self.filas = filas
            
            # Se actualiza la tabla.
            tabla           = ft.DataTable(
                columns = self.columnas,
                rows    = self.filas
            )
            contenedor_tabla = ft.Container(tabla, alignment=ft.alignment.center)
            
            # Se actualiza el contenedor para que muestre el menú nuevo.
            estructura = ft.Column([
                contenedor_header,
                contenedor_menu,
                contenedor_tabla
            ])
            contenedor.content = ft.Container(
                estructura,
                alignment=ft.alignment.center
            )
            contenedor.update()
        
        def eliminar_usuario():
            # Se hace la consulta a la base de datos.
            resultados = usr.eliminar_usuario(
                client = self.client,
                ID_USUARIO = str(self.id_usuario.value)
            )
            
            filas: list = []
            
            # Se crean las filas en base a los resultados de la base de datos.
            for fila in resultados:
                filas.append(
                    ft.DataRow(
                        cells = [
                            ft.DataCell(ft.Text(str(fila.ID_USUARIO))),
                            ft.DataCell(ft.Text(fila.NOMBRE_USR)),
                            ft.DataCell(ft.Text(fila.APELLIDO_USR)),
                            ft.DataCell(ft.Text(fila.DIRECCION_USR)),
                            ft.DataCell(ft.Text(fila.CORREO_E_USR)),
                            ft.DataCell(ft.Text(fila.ID_MEMBRESIA)),
                        ]
                    )
                )
            
            # Se actualizan las filas.
            self.filas = filas
            
            # Se actualiza la tabla.
            tabla           = ft.DataTable(
                columns = self.columnas,
                rows    = self.filas
            )
            contenedor_tabla = ft.Container(tabla, alignment=ft.alignment.center)
            
            # Se actualiza el contenedor para que muestre el menú nuevo.
            estructura = ft.Column([
                contenedor_header,
                contenedor_menu,
                contenedor_tabla
            ])
            contenedor.content = ft.Container(
                estructura,
                alignment=ft.alignment.center
            )
            contenedor.update()
        
        def actualizar_menu():
            """
            Actualiza el menú según la opción elegida en el Dropdown.

            Returns
            -------
            None.

            """
            if (btn_opciones.value == "Consultas"):
                titulo_menu.value = " - Menu Consultas"
                contenedor_menu = self.gui_contenedor_consultas()
            elif (btn_opciones.value == "Modificacion"):
                titulo_menu.value = " - Menu Modificacion"
                contenedor_menu = self.gui_contenedor_modificacion()
            elif (btn_opciones.value == "Alta"):
                titulo_menu.value = " - Menu Alta"
                contenedor_menu = self.gui_contenedor_alta()
            elif (btn_opciones.value == "Baja"):
                titulo_menu.value = " - Menu Baja"
                contenedor_menu = self.gui_contenedor_baja()
            
            # Se actualiza el contenedor para que muestre el menú nuevo.
            estructura = ft.Column([
                contenedor_header,
                contenedor_menu,
                contenedor_tabla
            ])
            contenedor.content = ft.Container(
                estructura,
                alignment=ft.alignment.center
            )
            contenedor.update()
        
        # Se definen los "punteros a funciones" que contienen las
        # funcionalidades de consultas.
        self.consultar_todos_usuarios   = consultar_todos_usuarios
        self.consultar_usuario          = consultar_usuario
        self.modificar_usuario          = modificar_usuario
        self.crear_usuario              = crear_usuario
        self.eliminar_usuario           = eliminar_usuario
        
        # Se agrega la parte del título.
        titulo_tabla    = ft.Text("Tabla Usuarios", weight=ft.FontWeight.BOLD)
        titulo_menu     = ft.Text(" - Menu Consultas", width = 150)
        
        # Se crea el dropdown (lista) para seleccionar el menú (consulta,
        # modificacion, ...).
        btn_opciones    = ft.Dropdown(
            options=[
                ft.dropdown.Option("Consultas"),
                ft.dropdown.Option("Modificacion"),
                ft.dropdown.Option("Alta"),
                ft.dropdown.Option("Baja")
            ],
            on_change = lambda _: actualizar_menu()
        )
        # Se establece el valor por defecto.
        btn_opciones.value = "Consultas"
        
        # Se inicializan los objetos 
        header          = ft.Row([titulo_tabla, titulo_menu, btn_opciones])
        contenedor_header = ft.Container(header, alignment=ft.alignment.center)
        
        # Se inicializa por defecto el menu de las consultas.
        contenedor_menu = self.gui_contenedor_consultas()

        # Se crea la tabla con los valores del objeto. (Se debe actualizar
        # luego con otra función para mostrar cambios)
        tabla           = ft.DataTable(
            columns = self.columnas,
            rows    = self.filas
        )
        contenedor_tabla = ft.Container(tabla, alignment=ft.alignment.center)
        
        # Se los mete en una columna para estructurarlos antes de meterlos
        # dentro del container.
        estructura      = ft.Column([
            contenedor_header,
            contenedor_menu,
            contenedor_tabla
        ])
        
        # Se genera el contenedor final a retornar.
        contenedor = ft.Container(
            ft.Container(estructura),
            alignment=ft.alignment.center
        )
        
        return contenedor
    
    def gui_contenedor_consultas(self):
        # Se instancia cada campo de texto que el usuario debe llenar.
        id_usuario      = ft.TextField(label="ID del Usuario",
                                       width=610,
                                       keyboard_type=ft.KeyboardType.NUMBER)
        nombre          = ft.TextField(label="Nombre")
        apellido        = ft.TextField(label="Apellido")
        direccion       = ft.TextField(label="Direccion")
        email           = ft.TextField(label="E-mail")
        id_membresia    = ft.TextField(label="ID Membresia",
                                       width=610,
                                       keyboard_type=ft.KeyboardType.NUMBER)
        limite          = ft.TextField(label="Cantidad de resultados a mostrar")
        
        # Se asignan los campos de texto a los atributos del objeto.
        self.id_usuario     = id_usuario
        self.nombre         = nombre
        self.apellido       = apellido
        self.direccion      = direccion
        self.email          = email
        self.id_membresia   = id_membresia
        self.limite         = limite
        
        # Se crea la tabla correspondiente a la estructura que debe tener
        # la tabla de los campos de texto.
        fila_campos_1   = ft.Row([id_usuario        ])
        fila_campos_2   = ft.Row([nombre, apellido  ])
        fila_campos_3   = ft.Row([direccion, email  ])
        fila_campos_4   = ft.Row([id_membresia      ])
        fila_campos_5   = ft.Row([limite            ])
        campos_de_texto = ft.Column([
            fila_campos_1,
            fila_campos_2,
            fila_campos_3,
            fila_campos_4,
            fila_campos_5
        ])
        
        # Se agregan los botones de consultas.
        btn_todos       = ft.ElevatedButton("Consultar todos los usuarios",
                                            on_click = lambda _: self.consultar_todos_usuarios())
        btn_consultar   = ft.ElevatedButton("Consultar usuario",
                                            on_click = lambda _: self.consultar_usuario())
        
        # Se estructuran los botones.
        botones         = ft.Row([btn_todos, btn_consultar])
        
        # Se agrega una línea de división horizontal.
        division        = ft.Divider()
        
        # Se hace la estructura final para meterlo adentro del contenedor
        # final.
        estructura      = ft.Column([
            campos_de_texto,
            botones,
            division
        ])
        
        # Se crea el contenedor que contenga los campos de texto.
        contenedor_menu = ft.Container(estructura)
        
        return contenedor_menu
        
    def gui_contenedor_modificacion(self):
        # Se instancia cada campo de texto que el usuario debe llenar.
        id_usuario      = ft.TextField(label="ID del Usuario",
                                       width=610,
                                       keyboard_type=ft.KeyboardType.NUMBER)
        nombre          = ft.TextField(label="Nombre")
        apellido        = ft.TextField(label="Apellido")
        direccion       = ft.TextField(label="Direccion")
        email           = ft.TextField(label="E-mail")
        id_membresia    = ft.TextField(label="ID Membresia",
                                       width=610,
                                       keyboard_type=ft.KeyboardType.NUMBER)
        
        # Se asignan los campos de texto a los atributos del objeto.
        self.id_usuario     = id_usuario
        self.nombre         = nombre
        self.apellido       = apellido
        self.direccion      = direccion
        self.email          = email
        self.id_membresia   = id_membresia
        
        # Se crea la tabla correspondiente a la estructura que debe tener
        # la tabla de los campos de texto.
        fila_campos_1   = ft.Row([id_usuario        ])
        fila_campos_2   = ft.Row([nombre, apellido  ])
        fila_campos_3   = ft.Row([direccion, email  ])
        fila_campos_4   = ft.Row([id_membresia      ])
        campos_de_texto = ft.Column([
            fila_campos_1,
            fila_campos_2,
            fila_campos_3,
            fila_campos_4
        ])
        
        # Se agregan los botones de consultas.
        btn_modificar   = ft.ElevatedButton("Modificar usuario",
                                            on_click = lambda _: self.modificar_usuario())
        
        # Se estructuran los botones.
        botones         = ft.Row([btn_modificar])
        
        # Se agrega una línea de división horizontal.
        division        = ft.Divider()
        
        # Se hace la estructura final para meterlo adentro del contenedor
        # final.
        estructura      = ft.Column([
            campos_de_texto,
            botones,
            division
        ])
        
        # Se crea el contenedor que contenga los campos de texto.
        contenedor_menu = ft.Container(estructura)
        
        return contenedor_menu
    
    def gui_contenedor_alta(self):
        # Se instancia cada campo de texto que el usuario debe llenar.
        id_usuario      = ft.TextField(label="ID del Usuario",
                                       width=610,
                                       keyboard_type=ft.KeyboardType.NUMBER)
        nombre          = ft.TextField(label="Nombre")
        apellido        = ft.TextField(label="Apellido")
        direccion       = ft.TextField(label="Direccion")
        email           = ft.TextField(label="E-mail")
        id_membresia    = ft.TextField(label="ID Membresia",
                                       width=610,
                                       keyboard_type=ft.KeyboardType.NUMBER)
        
        # Se asignan los campos de texto a los atributos del objeto.
        self.id_usuario     = id_usuario
        self.nombre         = nombre
        self.apellido       = apellido
        self.direccion      = direccion
        self.email          = email
        self.id_membresia   = id_membresia
        
        # Se crea la tabla correspondiente a la estructura que debe tener
        # la tabla de los campos de texto.
        fila_campos_1   = ft.Row([id_usuario        ])
        fila_campos_2   = ft.Row([nombre, apellido  ])
        fila_campos_3   = ft.Row([direccion, email  ])
        fila_campos_4   = ft.Row([id_membresia      ])
        campos_de_texto = ft.Column([
            fila_campos_1,
            fila_campos_2,
            fila_campos_3,
            fila_campos_4
        ])
        
        # Se agregan los botones de consultas.
        btn_crear       = ft.ElevatedButton("Crear usuario",
                                            on_click = lambda _: self.crear_usuario())
        
        # Se estructuran los botones.
        botones         = ft.Row([btn_crear])
        
        # Se agrega una línea de división horizontal.
        division        = ft.Divider()
        
        # Se hace la estructura final para meterlo adentro del contenedor
        # final.
        estructura      = ft.Column([
            campos_de_texto,
            botones,
            division
        ])
        
        # Se crea el contenedor que contenga los campos de texto.
        contenedor_menu = ft.Container(estructura)
        
        return contenedor_menu
    
    def gui_contenedor_baja(self):
        # Se instancia cada campo de texto que el usuario debe llenar.
        id_usuario      = ft.TextField(label="ID del Usuario",
                                       width=610,
                                       keyboard_type=ft.KeyboardType.NUMBER)
        
        # Se asignan los campos de texto a los atributos del objeto.
        self.id_usuario     = id_usuario
        
        # Se crea la tabla correspondiente a la estructura que debe tener
        # la tabla de los campos de texto.
        fila_campos_1   = ft.Row([id_usuario])
        campos_de_texto = ft.Column([
            fila_campos_1
        ])
        
        # Se agregan los botones de consultas.
        btn_eliminar    = ft.ElevatedButton("Eliminar usuario",
                                            on_click = lambda _: self.eliminar_usuario())
        
        # Se estructuran los botones.
        botones         = ft.Row([btn_eliminar])
        
        # Se agrega una línea de división horizontal.
        division        = ft.Divider()
        
        # Se hace la estructura final para meterlo adentro del contenedor
        # final.
        estructura      = ft.Column([
            campos_de_texto,
            botones,
            division
        ])
        
        # Se crea el contenedor que contenga los campos de texto.
        contenedor_menu = ft.Container(estructura)
        
        return contenedor_menu

"""
def main(page):
    # Ruta al archivo de credenciales JSON
    credentials = service_account.Credentials.from_service_account_file('../credenciales/coil2023-6672f55c3eb6.json')

    # Se instancia el cliente con las credenciales del proyecto COIL.
    client = bigquery.Client(credentials=credentials, project=credentials.project_id)
    
    tablita = TablaUsuario(client)
    page.scroll = "always"
    page.add(tablita.gui_usuarios())
        
        
ft.app(target=main)
        
"""
