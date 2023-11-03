# -*- coding: utf-8 -*-
"""
Este código realiza una consulta a la dataset de BigQuery del Proyecto COIL2023
utilizando unas credenciales en JSON. El archivo JSON debe estar en la ruta
especificada en la variable 'credentials'.

La funcionalidad de este código es el de consultar TODOS los usuarios de la
tabla 'USUARIO' de la dataset 'Biblioteca' del proyecto en BigQuery 'coil2023'.
Luego imprime solo los nombres por pantalla.
"""

from google.cloud import bigquery
from google.oauth2 import service_account

# Ruta al archivo de credenciales JSON.
credentials = service_account.Credentials.from_service_account_file('../../credenciales/coil2023-6672f55c3eb6.json')

# Se instancia el cliente con las credenciales del proyecto COIL.
client = bigquery.Client(credentials=credentials, project=credentials.project_id)

# Perform a query.
QUERY = "SELECT * FROM `coil2023.Biblioteca.USUARIO` "
query_job = client.query(QUERY)  # API request
rows = query_job.result()  # Waits for query to finish

for row in rows:
    print(row.NOMBRE_USR)
