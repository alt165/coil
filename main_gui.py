# -*- coding: utf-8 -*-
"""
Created on Thu Oct 26 18:56:35 2023

@author: UNRN
"""

import flet as ft

def main(page: ft.Page):
    
    def menu_principal():
        page.clean()
        page.add(ft.ElevatedButton("Usuarios", on_click=menu_usuarios))
        page.add(ft.ElevatedButton("Membresías", on_click=menu_membresia))
        page.add(ft.ElevatedButton("Membresía por usuario", on_click=menu_membresia_por_usuario))
        page.add(ft.ElevatedButton("Salir"))
        page.update()
        
    def botones_menu_principal(e):
        menu_principal()
        
    def menu_usuarios(e):
        opciones_menu = ("Consulta usuarios", menu_consulta_usuarios)
        menu_abm(e, opciones_menu)
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
        page.add(ft.ElevatedButton(opciones_menu[0], on_click=opciones_menu[1]))
        page.add(ft.ElevatedButton(f"Alta "))
        page.add(ft.ElevatedButton(f"Baja "))
        page.add(ft.ElevatedButton(f"Modificación "))
        page.add(ft.ElevatedButton("Volver", on_click = botones_menu_principal))
        page.update()
    
    menu_principal()
   
ft.app(main)