def calcular_similitud(hash_table_a, hash_table_b, compared_pairs):
    # Crea una tupla única para representar el par de documentos
    doc_pair = (id(hash_table_a), id(hash_table_b))
    reverse_doc_pair = (id(hash_table_b), id(hash_table_a))

    # Verifica si ya se compararon antes en cualquier orden
    if doc_pair in compared_pairs or reverse_doc_pair in compared_pairs:
        return None  # Evita comparación duplicada

    # Registra que este par ha sido comparado
    compared_pairs.add(doc_pair)

    # Inicializa contadores
    intersection = 0  # n-gramas que están en ambos documentos
    union = len(hash_table_a.keys()) + len(hash_table_b.keys())  # suma total de claves únicas (sin considerar repetidos)

    # Recorre todos los n-gramas del primer documento
    for key in hash_table_a.keys():
        # Si también existen en el segundo documento, se cuentan como intersección
        if hash_table_b.get(key) > 0:
            intersection += 1

    # La unión real se calcula restando los elementos que están en ambos (ya contados dos veces)
    union -= intersection

    # Calcula y retorna la similitud de Jaccard
    return intersection / union if union > 0 else 0




