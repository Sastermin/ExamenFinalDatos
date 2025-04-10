def merge_sort(arr, key=lambda x: x, reverse=False):
    # Si la lista tiene más de un elemento, se puede dividir
    if len(arr) > 1:
        mid = len(arr) // 2  # Punto medio
        left_half = arr[:mid]  # Mitad izquierda
        right_half = arr[mid:]  # Mitad derecha

        # Llamadas recursivas para ordenar cada mitad
        merge_sort(left_half, key, reverse)
        merge_sort(right_half, key, reverse)

        # Índices para recorrer las mitades y el arreglo final
        i = j = k = 0

        # Mezcla las dos mitades ordenadas
        while i < len(left_half) and j < len(right_half):
            # Compara usando la clave definida (por ejemplo, similitud) y el orden (asc o desc)
            if (key(left_half[i]) < key(right_half[j]) and not reverse) or \
               (key(left_half[i]) > key(right_half[j]) and reverse):
                arr[k] = left_half[i]  # Inserta el menor (o mayor si reverse=True)
                i += 1
            else:
                arr[k] = right_half[j]
                j += 1
            k += 1

        # Añade los elementos restantes de la mitad izquierda (si hay)
        while i < len(left_half):
            arr[k] = left_half[i]
            i += 1
            k += 1

        # Añade los elementos restantes de la mitad derecha (si hay)
        while j < len(right_half):
            arr[k] = right_half[j]
            j += 1
            k += 1

    # Devuelve la lista ordenada (útil si se llama directamente)
    return arr
