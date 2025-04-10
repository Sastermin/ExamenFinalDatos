class HashTable:
    def __init__(self):
        # Inicializa una tabla hash vacía usando un diccionario
        self.table = {}

    def insert(self, n_gram):
        # Si el n-grama ya existe en la tabla, incrementa su contador
        if n_gram in self.table:
            self.table[n_gram] += 1
        else:
            # Si no existe, lo agrega con contador en 1
            self.table[n_gram] = 1

    def get(self, n_gram):
        # Retorna cuántas veces ha aparecido un n-grama (0 si no existe)
        return self.table.get(n_gram, 0)

    def keys(self):
        # Retorna todas las claves (n-gramas únicos) almacenadas en la tabla
        return self.table.keys()