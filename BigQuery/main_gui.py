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
        page.scroll = "always"
        page.add(ft.Column([ft.ElevatedButton("Consultar tabla Usuarios",
                                           on_click = menu_tabla_usuarios),
                         ft.ElevatedButton("Consultar tabla Membresias",
                                           on_click = menu_tabla_membresias),
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
    
    def consultar_usuario(tabla: ft.DataTable, id_usuario: int, nombre: str, apellido: str, email: str, direccion: str, membresia: int):
        
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
                                             ft.DataCell(ft.Text(fila.membresia)),
                                             ]))
        
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
        
        id_membresia    = ft.TextField(label="id_membresia", keyboard_type=ft.KeyboardType.NUMBER)
        tipo            = ft.TextField(label="Tipo")
        vencimiento     = ft.TextField(label="Vencimiento")
        
        tabla: ft.DataTable = ft.DataTable(
            columns = [],
            rows = [])
        
        # Se agregan los campos de texto para el input del usuario
        page.add(ft.Column([id_membresia, tipo, vencimiento]))
        
        # Se agregan los botoens de "Consultar" y "Volver"
        page.add(ft.Row([ft.ElevatedButton("Volver", on_click = lambda _: menu_principal()),
                         ft.ElevatedButton("Consultar membresia", on_click = lambda _: consultar_membresia(cliente, tabla,
                                                                                  id_membresia.value,
                                                                                  tipo.value,
                                                                                  vencimiento.value)),
                         ft.ElevatedButton("Consultar todas las membresia", on_click = lambda _: consultar_todas_membresias(cliente, tabla))
                        ]))
        
        # Se agrega la tabla
        page.add(tabla)
        
        page.update()
    
    def consultar_membresia(cliente: bigquery.Client, tabla: ft.DataTable, id_membresia: str, tipo: str, vencimiento: str):
        
        input_usuario: list = [id_membresia,
                               tipo,
                               vencimiento]
        
        resultados: list = mem.buscar_membresia_especifica(cliente, input_usuario)
        
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
