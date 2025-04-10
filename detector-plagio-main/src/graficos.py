import matplotlib.pyplot as plt
import numpy as np
import os
from datetime import datetime

def generar_graficos(similitudes):
    # Ordenar de mayor a menor según la similitud
    similitudes_ordenadas = sorted(similitudes, key=lambda x: x[2], reverse=True)

    # Extraer los valores de similitud como porcentajes
    y = [sim * 100 for _, _, sim in similitudes_ordenadas]

    # Índices simples para el eje X
    x = list(range(1, len(y) + 1))

    # Crear la figura
    plt.figure(figsize=(10, 5))
    plt.plot(x, y, marker='o', linestyle='-', color='blue')

    # Añadir etiquetas
    plt.title('Similitud entre Pares de Documentos')
    plt.xlabel('Comparación N°')
    plt.ylabel('Similitud (%)')
    plt.ylim(0, 100)

    # Agregar cuadrícula para mejor legibilidad
    plt.grid(True, linestyle='--', alpha=0.5)

    # Guardar el gráfico
    os.makedirs('resultados/graficos', exist_ok=True)
    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
    filename = f'resultados/graficos/linea_similitudes_{timestamp}.png'

    # Ajustar, guardar y mostrar
    plt.tight_layout()
    plt.savefig(filename)
    plt.show()

    print(f"[✔] Gráfico de líneas guardado en: {filename}")



