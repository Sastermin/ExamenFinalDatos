import matplotlib.pyplot as plt
import numpy as np
import os
from datetime import datetime

def generar_graficos(similitudes):
    # Ordena la lista de similitudes de mayor a menor (basado en el valor de similitud)
    similitudes_ordenadas = sorted(similitudes, key=lambda x: x[2], reverse=True)

    # Crea una lista con etiquetas tipo "doc1 - doc2" para cada par comparado
    documentos = [f"{doc1} - {doc2}" for doc1, doc2, _ in similitudes_ordenadas]

    # Extrae los valores de similitud y los convierte a porcentaje (de 0 a 100)
    scores = [sim * 100 for _, _, sim in similitudes_ordenadas]


    # Genera una paleta de colores (gradiente) según la cantidad de pares
    cmap = plt.get_cmap('viridis')
    colores = [cmap(i / len(documentos)) for i in range(len(documentos))]

    # Crea una figura de 12x6 pulgadas
    plt.figure(figsize=(12, 6))

    # Dibuja las barras verticales con los colores definidos
    barras = plt.bar(documentos, scores, color=colores)

    # Etiqueta del eje Y
    plt.ylabel('Nivel de Similitud (%)')

    # Título del gráfico
    plt.title('Similitud entre Pares de Documentos (Ordenado)')

    # Establece el límite del eje Y de 0 a 100
    plt.ylim(0, 100)


    # Agrega el valor numérico encima de cada barra
    for barra, score in zip(barras, scores):
        plt.text(
            barra.get_x() + barra.get_width() / 2,  # posición X centrada en la barra
            score + 1,                              # ligeramente arriba del borde de la barra
            f'{score:.1f}%',                        # texto con formato 00.0%
            ha='center', va='bottom'                # alineación horizontal y vertical
        )


    # Rota las etiquetas del eje X para evitar que se encimen
    plt.xticks(rotation=45, ha='right')


    # Crea la carpeta donde se guardarán los gráficos, si no existe
    os.makedirs('resultados/graficos', exist_ok=True)

    # Genera nombre de archivo con timestamp único
    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
    filename = f'resultados/graficos/similitudes_{timestamp}.png'


    # Ajusta automáticamente los márgenes, guarda la imagen y la muestra en pantalla
    plt.tight_layout()
    plt.savefig(filename)
    plt.show()

