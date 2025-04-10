import os
import re

def cargar_documentos(carpeta):
    documentos = {}  # Diccionario para guardar {nombre_archivo: contenido}
    
    # Recorre todos los archivos en la carpeta indicada
    for filename in os.listdir(carpeta):
        # Solo toma los archivos .txt
        if filename.endswith('.txt'): 
            # Abre el archivo en modo lectura, con codificación UTF-8
            with open(os.path.join(carpeta, filename), 'r', encoding='utf-8') as file:
                # Guarda el contenido en el diccionario
                documentos[filename] = file.read()

    return documentos  # Devuelve el diccionario con todos los textos


def tokenizar(texto, n=2):
    # Limpia el texto: pasa a minúsculas y elimina puntuación
    texto = re.sub(r'[^\w\s]', '', texto.lower())
    
    # Divide el texto en palabras
    palabras = texto.split()
    
    # Crea y retorna una lista de n-gramas como tuplas (por defecto, bi-gramas)
    return [tuple(palabras[i:i+n]) for i in range(len(palabras)-n+1)]
