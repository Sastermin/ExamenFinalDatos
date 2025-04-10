import csv
import os
from datetime import datetime

def exportar_similitudes_a_csv(similitudes, carpeta='resultados/csv'):
    # Crea la carpeta 'resultados/csv' si no existe
    os.makedirs(carpeta, exist_ok=True)

    # Genera un nombre de archivo con la fecha y hora actual (formato: AAAAMMDD_HHMMSS)
    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
    nombre_archivo = f"{carpeta}/similitudes_{timestamp}.csv"

    # Abre (o crea) el archivo CSV en modo escritura con codificación UTF-8
    with open(nombre_archivo, mode='w', newline='', encoding='utf-8') as archivo_csv:
        writer = csv.writer(archivo_csv)
        
        # Escribe la fila de encabezados
        writer.writerow(['Documento 1', 'Documento 2', 'Similitud (%)'])

        # Escribe cada fila de resultados: nombres de documentos y su similitud en porcentaje con 2 decimales
        for doc1, doc2, sim in similitudes:
            writer.writerow([doc1, doc2, f"{sim:.2f}"])

    # Mensaje en consola indicando que la exportación fue exitosa
    print(f"[✔] Similitudes exportadas a: {nombre_archivo}")

