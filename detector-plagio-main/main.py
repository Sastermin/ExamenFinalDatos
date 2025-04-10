import os
from src.preprocesamiento import cargar_documentos, tokenizar
from src.hash_table import HashTable
from src.bloom_filter import BloomFilter
from src.similitud import calcular_similitud
from src.sorting import merge_sort
from src.graficos import generar_graficos

def main():
    # Obtener ruta absoluta al directorio donde se encuentra este script
    ruta_actual = os.path.dirname(os.path.abspath(__file__))

    # Construir la ruta de la carpeta que contiene los documentos
    ruta_documentos = os.path.join(ruta_actual, 'documentos')

    # Paso 1: Cargar los Documentos desde la carpeta "documentos/"
    documentos = cargar_documentos(ruta_documentos)
    
    # Paso 2: Preprocesamiento del Texto
    # Para cada documento, aplicar limpieza y tokenización en n-gramas (bi-gramas por defecto)
    n_gramas = {doc: tokenizar(texto) for doc, texto in documentos.items()}
    
    # Paso 3: Crear una Tabla Hash y un Filtro de Bloom para cada documento
    hash_tables = {doc: HashTable() for doc in n_gramas}
    bloom_filters = {doc: BloomFilter() for doc in n_gramas}
    
    # Insertar cada n-grama en su respectiva tabla hash y filtro de Bloom
    for doc, n_gram in n_gramas.items():
        for n in n_gram:
            hash_tables[doc].insert(n)
            bloom_filters[doc].add(n)
    
    # Paso 4: Comparar Documentos y Calcular Similitud de Jaccard
    similitudes = []                  # Lista para almacenar tuplas (doc1, doc2, similitud)
    compared_pairs = set()           # Conjunto para evitar comparar pares repetidos
    documentos_list = list(n_gramas.keys())

    # Comparar cada par único de documentos
    for i in range(len(documentos_list)):
        for j in range(i + 1, len(documentos_list)):
            doc1 = documentos_list[i]
            doc2 = documentos_list[j]
            sim = calcular_similitud(hash_tables[doc1], hash_tables[doc2], compared_pairs)
            if sim is not None:
                similitudes.append((doc1, doc2, sim))

    # Paso 5: Ordenar los Resultados de Similitud de mayor a menor usando Merge Sort
    similitudes_ordenadas = merge_sort(similitudes, key=lambda x: x[2], reverse=True)
    
    # Paso 6: Mostrar los N pares de documentos más similares (ej. top 5)
    N = 5
    for doc1, doc2, sim in similitudes_ordenadas[:N]:
        print(f"Similitud entre {doc1} y {doc2}: {sim:.2f}")
    
    # Paso 7: Visualización gráfica de los resultados
    generar_graficos(similitudes_ordenadas)

# Punto de entrada del programa
if __name__ == "_main_":
    main()