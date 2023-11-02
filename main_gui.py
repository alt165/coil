# -*- coding: utf-8 -*-
"""
Created on Thu Oct 26 18:56:35 2023

@author: UNRN
"""

import flet as ft
import usuarios as usr
import membresias as mem
import membresias_usuarios as mem_usr



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
        page.scroll = "always"
        page.add(ft.Column([ft.ElevatedButton("Consultar tabla Usuarios",
                                           on_click = menu_tabla_usuarios),
                         ft.ElevatedButton("Consultar tabla Membresias",
                                           on_click = menu_tabla_membresias),
                         ft.ElevatedButton("Consultar tabla Membresias-Usuarios",
                                           on_click = menu_tabla_membresias_usuarios),
                         ft.ElevatedButton("Salir", on_click = lambda _: page.window_destroy())]))
        
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
                                   width=480,
                                   keyboard_type=ft.KeyboardType.NUMBER)
        nombre      = ft.TextField(label="Nombre")
        apellido    = ft.TextField(label="Apellido")
        email       = ft.TextField(label="E-mail")
        direccion   = ft.TextField(label="Direccion")
        
        tabla: ft.DataTable = ft.DataTable(
            columns = [],
            rows = [])
        
        # Se agregan los campos de texto para el input del usuario
        page.add(ft.Column([id_usuario,
                            ft.Row([nombre, apellido]),
                            ft.Row([email, direccion])]))
        
        # Se agregan los botoens de "Consultar" y "Volver"
        page.add(ft.Row([ft.ElevatedButton("Volver",
                                           on_click = lambda _: menu_principal()),
                         ft.ElevatedButton("Consultar usuario",
                                           on_click = lambda _: consultar_usuario(tabla,
                                                                                  id_usuario.value,
                                                                                  nombre.value,
                                                                                  apellido.value,
                                                                                  email.value,
                                                                                  direccion.value))]))
        
        # Se agrega la tabla
        page.add(tabla)
        
        page.update()
    
    def consultar_usuario(tabla: ft.DataTable,
                            id_usuario: str,
                            nombre: str,
                            apellido: str,
                            email: str,
                            direccion: str):
        
        input_usuario: list = [id_usuario,
                               nombre,
                               apellido,
                               email,
                               direccion]
        
        resultados: list = usr.buscar_usuario_especifico(input_usuario)
        
        # Se genera la tabla
        columnas: list =[
            ft.DataColumn(ft.Text("id_usuario")),
            ft.DataColumn(ft.Text("nombre")),
            ft.DataColumn(ft.Text("apellido")),
            ft.DataColumn(ft.Text("email")),
            ft.DataColumn(ft.Text("direccion"))
        ]
        
        filas: list = []
        
        for fila in resultados:
            
            filas.append(ft.DataRow(cells = [ft.DataCell(ft.Text(str(fila.id_usuario))),
                                             ft.DataCell(ft.Text(fila.nombre)),
                                             ft.DataCell(ft.Text(fila.apellido)),
                                             ft.DataCell(ft.Text(fila.email)),
                                             ft.DataCell(ft.Text(fila.direccion))]))
        
        # Se actualiza la tabla
        tabla.columns = columnas
        tabla.rows = filas
        
        page.update()
    
    def menu_tabla_membresias(e: ft.ControlEvent):
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
        
        id_membresia    = ft.TextField(label="id_membresia",
                                     keyboard_type=ft.KeyboardType.NUMBER)
        tipo        = ft.TextField(label="Tipo")
        
        tabla: ft.DataTable = ft.DataTable(
            columns = [],
            rows = [])
        
        # Se agregan los campos de texto para el input del usuario
        page.add(ft.Column([id_membresia, tipo]))
        
        # Se agregan los botoens de "Consultar" y "Volver"
        page.add(ft.Row([ft.ElevatedButton("Volver",
                                           on_click = lambda _: menu_principal()),
                         ft.ElevatedButton("Consultar membresia",
                                           on_click = lambda _: consultar_membresia(tabla,
                                                                                  id_membresia.value,
                                                                                  tipo.value))]))
        
        # Se agrega la tabla
        page.add(tabla)
        
        page.update()
    
    def consultar_membresia(tabla: ft.DataTable,
                            id_membresia: str,
                            tipo: str):
        
        input_usuario: list = [id_membresia,
                               tipo]
        
        resultados: list = mem.buscar_membresia_especifica(input_usuario)
        
        # Se genera la tabla
        columnas: list =[
            ft.DataColumn(ft.Text("id_membresia")),
            ft.DataColumn(ft.Text("tipo"))
        ]
        
        filas: list = []
        
        for fila in resultados:
            filas.append(ft.DataRow(cells = [ft.DataCell(ft.Text(str(fila.id_membresia))),
                                             ft.DataCell(ft.Text(fila.tipo))]))
        
        # Se actualiza la tabla
        tabla.columns = columnas
        tabla.rows = filas
        
        page.update()
    
    def menu_tabla_membresias_usuarios(e: ft.ControlEvent):
        """
        Dibuja el menu de tabla de membresias_usuarios. Crea cada campo de
        texto para el input de la consulta del usuario.

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
                                   keyboard_type=ft.KeyboardType.NUMBER)
        id_membresia    = ft.TextField(label="id_membresia",
                                       keyboard_type=ft.KeyboardType.NUMBER)
        vencimiento     = ft.TextField(label="Vencimiento")
        
        tabla: ft.DataTable = ft.DataTable(
            columns = [],
            rows = [])
        
        # Se agregan los campos de texto para el input del usuario
        page.add(ft.Column([ft.Row([id_usuario, id_membresia]),
                            vencimiento]))
        
        # Se agregan los botoens de "Consultar" y "Volver"
        page.add(ft.Row([ft.ElevatedButton("Volver",
                                           on_click = lambda _: menu_principal()),
                         ft.ElevatedButton("Consultar membresia-usuario",
                                           on_click = lambda _: consultar_membresia_usuario(
                                               tabla,
                                               id_usuario.value,
                                               id_membresia.value,
                                               vencimiento.value))]))
        
        # Se agrega la tabla
        page.add(tabla)
        
        page.update()
    
    def consultar_membresia_usuario(tabla: ft.DataTable,
                                       id_usuario: str,
                                       id_membresia: str,
                                       vencimiento: str):
        
        input_usuario: list = [id_usuario,
                               id_membresia,
                               vencimiento]
        
        resultados: list = mem_usr.buscar_membresia_usuario_especifico(input_usuario)
        
        # Se genera la tabla
        columnas: list =[
            ft.DataColumn(ft.Text("id_usuario")),
            ft.DataColumn(ft.Text("id_membresia")),
            ft.DataColumn(ft.Text("vencimiento"))
        ]
        
        filas: list = []
        
        for fila in resultados:
            filas.append(ft.DataRow(cells = [ft.DataCell(ft.Text(str(fila.id_usuario))),
                                             ft.DataCell(ft.Text(str(fila.id_membresia))),
                                             ft.DataCell(ft.Text(fila.vencimiento))]))
        
        # Se actualiza la tabla
        tabla.columns = columnas
        tabla.rows = filas
        
        page.update()
    
    menu_principal()

ft.app(main)
