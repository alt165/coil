# -*- coding: utf-8 -*-
"""
Created on Thu Oct 26 18:56:35 2023

@author: UNRN
"""

import flet as ft
import usuarios_v2 as usr
import membresias_v2 as mem

from google.cloud import bigquery
from google.oauth2 import service_account

# Ruta al archivo de credenciales JSON.
credentials = service_account.Credentials.from_service_account_file('coil2023-6672f55c3eb6.json')

# Se instancia el cliente con las credenciales del proyecto COIL.
cliente = bigquery.Client(credentials=credentials, project=credentials.project_id)

def main(page: ft.Page):
    def menu_principal():
        """
            Dibuja el menu principal. Crea los botones para consultar cada tabla
            de la base de datos.

            Returns
            -------
            None.
        """
        page.clean()
        page.title = "Menu Usuarios|Membresias"

        page.window_width = 400
        page.window_min_width = 400
        page.window_max_width = 500
        page.window_center()

        page.scroll = "always"
        page.add(ft.Column([ft.ElevatedButton("Consultar tabla Usuarios",
                                           on_click = menu_tabla_usuarios),
                         ft.ElevatedButton("Consultar tabla Membresias",
                                           on_click = menu_membresias),
                         ft.ElevatedButton("Salir", on_click = lambda _: page.window_destroy()),
                         ]))
        
        page.update()

    def menu_tabla_usuarios(e: ft.ControlEvent):
        """
            Dibuja el menu de tabla de usuarios. Crea cada campo de texto para el
            input de la consulta del usuario.

            Parameters
            ----------
            e : ft.ControlEvent
                Control Event de flet.

            Returns
            -------
            None.
        """
        page.clean()
        
        id_usuario  = ft.TextField(label="id_usuario",
                                   width=610,
                                   keyboard_type=ft.KeyboardType.NUMBER)
        nombre      = ft.TextField(label="Nombre")
        apellido    = ft.TextField(label="Apellido")
        email       = ft.TextField(label="E-mail")
        direccion   = ft.TextField(label="Direccion")
        membresia   = ft.TextField(label="Membresias",
                                   width=610,
                                   keyboard_type=ft.KeyboardType.NUMBER)
        
        tabla: ft.DataTable = ft.DataTable(
            columns = [],
            rows = [])
        
        # Se agregan los campos de texto para el input del usuario
        page.add(ft.Column([ft.Row([id_usuario]),
                            ft.Row([nombre, apellido]),
                            ft.Row([email, direccion]),
                            ft.Row([membresia])
                            ]))
        
        # Se agregan los botoens de "Consultar" y "Volver"
        page.add(ft.Row([ft.ElevatedButton("Volver",
                                           on_click = lambda _: menu_principal()),
                         ft.ElevatedButton("Consultar usuario",
                                           on_click = lambda _: consultar_usuario(tabla,
                                                                                  id_usuario.value,
                                                                                  nombre.value,
                                                                                  apellido.value,
                                                                                  email.value,
                                                                                  direccion.value,
                                                                                  membresia.value
                                                                                  ))]))
        page.add(ft.Row([ft.ElevatedButton("Consultar todos los Usuarios",
                                           on_click = lambda _: consultar_todos_usuarios(tabla))]))
        
        # Se agrega la tabla
        page.add(tabla)
        
        page.update()
    
    def consultar_usuario(cliente: bigquery.Client, tabla: ft.DataTable, id_usuario: int, nombre: str, apellido: str, email: str, direccion: str, membresia: int):
        
        input_usuario: list = [id_usuario,
                               nombre,
                               apellido,
                               email,
                               direccion,
                               membresia]
        
        resultados: list = usr.buscar_usuario_especifico(input_usuario)
        
        # Se genera la tabla
        columnas: list =[
            ft.DataColumn(ft.Text("id_usuario")),
            ft.DataColumn(ft.Text("nombre")),
            ft.DataColumn(ft.Text("apellido")),
            ft.DataColumn(ft.Text("direccion")),
            ft.DataColumn(ft.Text("email")),
            ft.DataColumn(ft.Text("membresia"))
        ]
        
        filas: list = []
        
        for fila in resultados:
            filas.append(ft.DataRow(cells = [ft.DataCell(ft.Text(str(fila.id_usuario))),
                                             ft.DataCell(ft.Text(fila.nombre)),
                                             ft.DataCell(ft.Text(fila.apellido)),
                                             ft.DataCell(ft.Text(fila.email)),
                                             ft.DataCell(ft.Text(fila.direccion)),
                                             ft.DataCell(ft.Text(str(fila.membresia))),
                                             ]))
        
        # Se actualiza la tabla
        tabla.columns = columnas
        tabla.rows = filas
        
        page.update()
    


    
    def menu_membresias(e: ft.ControlEvent):
        page.clean()
        page.title = "Menu de Membresias"

        page.add(ft.Column([ft.ElevatedButton("Consultar membresias", on_click = menu_membresias_consultar),
                         ft.ElevatedButton("Crear membresias", on_click = menu_membresias_agregar),
                         ft.ElevatedButton("Modificar membresias existentes", on_click = menu_membresias_modificar),
                         ft.ElevatedButton("Eliminar membresia", on_click = menu_membresias_eliminar),
                         ft.ElevatedButton("Volver", on_click = lambda _: menu_principal())
            ]))

    def menu_membresias_agregar(e: ft.ControlEvent):
        page.clean()
        page.window_width = 455
        page.title = "Crear membresia"
        page.add(ft.Text("Crear Membresia:"))
        
        id_membresia    = ft.TextField(label="id_membresia", width=410, keyboard_type=ft.KeyboardType.NUMBER)
        tipo            = ft.TextField(label="Tipo", width=410)
        vencimiento     = ft.TextField(label="Vencimiento", width=410)

        tabla: ft.DataTable = ft.DataTable(
            columns = [],
            rows = [])

        # Se agregan los campos de texto para el input del usuario
        page.add(ft.Column([id_membresia, tipo, vencimiento]))
        
        resultado = ft.Text("[resultado de la operación]")

        # Se agregan los botoens de "Consultar" y "Volver"
        page.add(ft.Row([ft.ElevatedButton("Crear membresia",width=410 , on_click = lambda _: agregar_membresia(cliente, tabla, 
                                                                                    resultado,
                                                                                    id_membresia.value,
                                                                                    tipo.value,
                                                                                    vencimiento.value)),
                        ]))
        page.add(ft.Row([resultado]))
        page.add(ft.Row([ft.ElevatedButton("Volver", on_click = menu_membresias)]))
        
        # Se agrega la tabla
        page.add(tabla)
        
        consultar_todas_membresias(cliente, tabla)

        page.update()

    def menu_membresias_eliminar(e: ft.ControlEvent):
        page.clean()
        page.window_width = 455
        page.title = "Eliminar membresia"
        page.add(ft.Text("Eliminar Membresia:"))

        id_membresia    = ft.TextField(label="id_membresia", width=410, keyboard_type=ft.KeyboardType.NUMBER)
        
        tabla: ft.DataTable = ft.DataTable(
            columns = [],
            rows = [])
        
        # Se agregan los campos de texto para el input del usuario
        page.add(ft.Column([id_membresia]))
        
        resultado = ft.Text("[resultado de la operación]")

        # Se agregan los botoens de "Consultar" y "Volver"
        page.add(ft.Row([ft.ElevatedButton("Eliminar membresia", width=410, on_click = lambda _: eliminar_membresia(cliente, tabla,
                                                                                        resultado,
                                                                                        id_membresia.value)),
                        resultado
                        ]))

        page.add(ft.Row([ft.ElevatedButton("Volver", on_click = menu_membresias)]))
        
        # Se agrega la tabla
        page.add(tabla)
        
        consultar_todas_membresias(cliente, tabla)

        page.update()

    def menu_membresias_modificar(e: ft.ControlEvent):
        page.clean()
        page.window_width = 455
        page.title = "Modificar membresia"
        page.add(ft.Text("Modificar Membresia:"))

        id_membresia    = ft.TextField(label="id_membresia", width=410, keyboard_type=ft.KeyboardType.NUMBER)
        tipo            = ft.TextField(label="Tipo", width=410)
        vencimiento     = ft.TextField(label="Vencimiento", width=410)
        
        tabla: ft.DataTable = ft.DataTable(
            columns = [],
            rows = [])
        
        # Se agregan los campos de texto para el input del usuario
        page.add(ft.Column([id_membresia, tipo, vencimiento]))
        
        resultado = ft.Text("[resultado de la operación]")

        # Se agregan los botoens de "Consultar" y "Volver"
        page.add(ft.Row([ft.ElevatedButton("Modificar membresia", width=410, on_click = lambda _: modificar_membresia(cliente, tabla,
                                                                                    resultado,
                                                                                    id_membresia.value,
                                                                                    tipo.value,
                                                                                    vencimiento.value)),
                         resultado
                        ]))

        page.add(ft.Row([ft.ElevatedButton("Volver", on_click = menu_membresias)]))
        
        # Se agrega la tabla
        page.add(tabla)
        
        page.update()

    def menu_membresias_consultar(e: ft.ControlEvent):
        """
            Dibuja el menu de tabla de membresias. Crea cada campo de texto para el
            input de la consulta del usuario.

            Parameters
            ----------
            e : ft.ControlEvent
                Control Event de flet.

            Returns
            -------
            None.
        """
        page.clean()
        page.window_width = 455
        page.title = "Consultar membresia"
        page.add(ft.Text("Consultar Membresia:"))

        id_membresia    = ft.TextField(label="id_membresia", width=410, keyboard_type=ft.KeyboardType.NUMBER)
        tipo            = ft.TextField(label="Tipo", width=410)
        vencimiento     = ft.TextField(label="Vencimiento", width=410)
        
        tabla: ft.DataTable = ft.DataTable(
            columns = [],
            rows = [])
        
        # Se agregan los campos de texto para el input del usuario
        page.add(ft.Column([id_membresia, tipo, vencimiento]))
        
        # Se agregan los botoens de "Consultar" y "Volver"
        page.add(ft.Row([ft.ElevatedButton("Consultar membresia", width=205, on_click = lambda _: consultar_membresia(cliente, tabla,
                                                                                  id_membresia.value,
                                                                                  tipo.value,
                                                                                  vencimiento.value)),
                         ft.ElevatedButton("Consultar todas las membresia", width=205, on_click = lambda _: consultar_todas_membresias(cliente, tabla)),
                        ]))

        page.add(ft.Row([ft.ElevatedButton("Volver", on_click = menu_membresias)]))
        
        # Se agrega la tabla
        page.add(tabla)
        
        page.update()


    def agregar_membresia(cliente: bigquery.Client, tabla: ft.DataTable, respuesta: ft.Text, id_membresia: str, tipo: str, vencimiento: str):
        input_usuario: list = [id_membresia,
                               tipo,
                               vencimiento]
        
        #resultados: bool
        #mensaje: str
        resultados, mensaje = mem.crear_membresia(cliente, input_usuario)

        if resultados:
            respuesta.value = f"[Se ha agregado correctamente la nueva membresia]"
        else:
            respuesta.value = f"[{mensaje}]"

        consultar_todas_membresias(cliente, tabla)

        page.update()

    def eliminar_membresia(cliente: bigquery.Client, tabla: ft.DataTable, respuesta: ft.Text, id_membresia: str):
        #resultados: bool
        #mensaje: str
        resultados, mensaje = mem.eliminar_membresia(cliente, id_membresia)
        
        if resultados:
            respuesta.value = f"[Se ha eliminado correctamente la membresia solicitada]"
        else:
            respuesta.value = f"[{mensaje}]"

        consultar_todas_membresias(cliente, tabla)

        page.update()

    def modificar_membresia(cliente: bigquery.Client, tabla: ft.DataTable, respuesta: ft.Text, id_membresia: str, tipo: str, vencimiento: str):
        input_usuario: list = [id_membresia,
                               tipo,
                               vencimiento]
        
        #resultados: bool
        #mensaje: str
        resultados, mensaje = mem.modificar_membresia(cliente, input_usuario)
        
        if resultados:
            respuesta.value = f"[Se ha modificado correctamente la membresia solicitada]"
        else:
            respuesta.value = f"[{mensaje}]"

        consultar_todas_membresias(cliente, tabla)

        page.update()
    
    def consultar_membresia(cliente: bigquery.Client, tabla: ft.DataTable, id_membresia: str, tipo: str, vencimiento: str):
        
        input_usuario: list = [id_membresia,
                               tipo,
                               vencimiento]
        
        # Se genera la tabla
        columnas: list =[
            ft.DataColumn(ft.Text("id_membresia")),
            ft.DataColumn(ft.Text("tipo")),
            ft.DataColumn(ft.Text("vencimiento"))
        ]
        
        try:
            resultados: list = mem.buscar_membresia_especifica(cliente, input_usuario)

            filas: list = []
        
            for fila in resultados:
                filas.append(ft.DataRow(cells = [ft.DataCell(ft.Text(str(fila.ID_MEMBRESIA))),
                                                 ft.DataCell(ft.Text(fila.TIPO_MEMBRESIA)),
                                                 ft.DataCell(ft.Text(fila.FECHA_VENCIM_MEMBRE))
                                                 ]))
            
            # Se actualiza la tabla
            tabla.columns = columnas
            tabla.rows = filas
            
            page.update()
        except Exception as exc:
            print("falla la fecha... reparación postergada")
            tabla.columns = columnas
            tabla.rows = ""
            page.update()

    def consultar_todas_membresias(cliente: bigquery.Client, tabla: ft.DataTable):
        
        resultados: list = mem.buscar_todas_membresias(cliente)
        
        # Se genera la tabla
        columnas: list =[
            ft.DataColumn(ft.Text("id_membresia")),
            ft.DataColumn(ft.Text("tipo")),
            ft.DataColumn(ft.Text("vencimiento"))
        ]
        
        filas: list = []
        
        for fila in resultados:
            filas.append(ft.DataRow(cells = [ft.DataCell(ft.Text(str(fila.ID_MEMBRESIA))),
                                             ft.DataCell(ft.Text(fila.TIPO_MEMBRESIA)),
                                             ft.DataCell(ft.Text(fila.FECHA_VENCIM_MEMBRE))
                                             ]))
        
        # Se actualiza la tabla
        tabla.columns = columnas
        tabla.rows = filas
        
        page.update()
    
    menu_principal()

ft.app(main)
