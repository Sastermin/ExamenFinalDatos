import matplotlib.pyplot as plt
import numpy as np
import os
from datetime import datetime

def generar_graficos(similitudes):
    # Convertir similitudes a porcentaje y ordenar de mayor a menor
    similitudes_ordenadas = sorted(similitudes, key=lambda x: x[2], reverse=True)
    documentos = [f"{doc1} - {doc2}" for doc1, doc2, _ in similitudes_ordenadas]
    scores = [sim * 100 for _, _, sim in similitudes_ordenadas]  # porcentaje

    # Crear una paleta de colores basada en la cantidad de documentos
    cmap = plt.get_cmap('viridis')
    colores = [cmap(i / len(documentos)) for i in range(len(documentos))]

    # Crear figura
    plt.figure(figsize=(12, 6))

    # Gráfico de barras verticales
    barras = plt.bar(documentos, scores, color=colores)

    # Etiquetas
    plt.ylabel('Nivel de Similitud (%)')
    plt.title('Similitud entre Pares de Documentos (Ordenado)')

    # Límite del eje Y
    plt.ylim(0, 100)

    # Etiquetas de porcentaje encima de cada barra
    for barra, score in zip(barras, scores):
        plt.text(barra.get_x() + barra.get_width() / 2, score + 1, f'{score:.1f}%', 
                 ha='center', va='bottom')

    # Rotar etiquetas del eje X
    plt.xticks(rotation=45, ha='right')

    # Crear el directorio si no existe
    os.makedirs('resultados/graficos', exist_ok=True)

    # Generar nombre de archivo con fecha y hora
    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
    filename = f'resultados/graficos/similitudes_{timestamp}.png'

    # Guardar y mostrar
    plt.tight_layout()
    plt.savefig(filename)
    plt.show()
