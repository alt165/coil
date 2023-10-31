# -*- coding: utf-8 -*-
"""
Created on Thu Oct 26 18:56:35 2023

@author: UNRN
"""

import flet as ft
import usuarios


def main(page: ft.Page):
    
    def menu_principal():
        page.clean()
        page.event_handlers.setdefault
        page.add(ft.ElevatedButton("Usuarios", on_click=menu_usuarios))
        page.add(ft.ElevatedButton("Membresías", on_click=menu_membresia))
        page.add(ft.ElevatedButton("Membresía por usuario", on_click=menu_membresia_por_usuario))
        page.add(ft.ElevatedButton("Salir", on_click= page.window_destroy))
        page.update()
    


    def botones_menu_principal(e):
        menu_principal()
        
    def menu_usuarios(e):
        page.clean()
        page.add(ft.ElevatedButton("Consulta usuario", on_click=consulta_usuario))
        page.add(ft.ElevatedButton("Alta usuario", on_click=alta_usuario))
        page.add(ft.ElevatedButton("Baja usuario", on_click=baja_usuario))
        page.add(ft.ElevatedButton(f"Modificación usuario", on_click=modificacion_usuario))
        page.add(ft.ElevatedButton("Volver", on_click = botones_menu_principal))
        page.update()

    def consulta_usuario(e):
        def buscar_usuario(e): 
            resultado = usuarios.buscar_apellido_usuario(apellido.value)
            
            for element in resultado:
                print(element)

            


        page.clean()
       
        nombre = ft.TextField(label="Nombre")
        apellido = ft.TextField(label="Apellido")
        id = ft.TextField(label="id", keyboard_type=ft.KeyboardType.NUMBER)
        page.add(nombre,apellido,id)
        page.add(ft.ElevatedButton("Buscar", on_click=buscar_usuario))
        page.add(ft.ElevatedButton("Volver", on_click=menu_usuarios))
        page.update()
        
        

    def alta_usuario(e):
        pass
    def baja_usuario(e):
        pass
    def modificacion_usuario(e):
        pass
    def menu_consulta_usuarios(e):
        page.clean()
        page.add(ft.Text("GANAMO"))
        page.update()
    def menu_membresia(e):
        tipo_menu = "membresía"
        menu_abm(e, mensaje=tipo_menu)
        
    def menu_membresia_por_usuario(e):
        tipo_menu = "membresía por usuario"
        menu_abm(e, mensaje=tipo_menu)
        
    
    def menu_abm(e, opciones_menu):
        page.clean()
        page.add(ft.ElevatedButton("Consulta " + opciones_menu[0], on_click=opciones_menu[1]))
        page.add(ft.ElevatedButton(f"Alta "))
        page.add(ft.ElevatedButton(f"Baja "))
        page.add(ft.ElevatedButton(f"Modificación "))
        page.add(ft.ElevatedButton("Volver", on_click = botones_menu_principal))
        page.update()
    
    menu_principal()
   
ft.app(main)