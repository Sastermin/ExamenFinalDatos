class BloomFilter:
    def __init__(self, size=1000):
        # Inicializa el filtro de Bloom con un tamaño fijo de bits (por defecto 1000)
        self.size = size
        # Crea un arreglo de bits (todos inicialmente en 0)
        self.bit_array = [0] * size

    def _hash(self, n_gram):
        # Función hash simple: convierte el n-grama a un índice dentro del rango del arreglo
        return hash(n_gram) % self.size

    def add(self, n_gram):
        # Calcula la posición del n-grama usando la función hash
        index = self._hash(n_gram)
        # Marca esa posición como 1 (lo "agrega" al filtro)
        self.bit_array[index] = 1

    def check(self, n_gram):
        # Verifica si la posición hash del n-grama está en 1
        # Si está en 1: el elemento posiblemente esté en el conjunto
        # Si está en 0: el elemento definitivamente NO está
        index = self._hash(n_gram)
        return self.bit_array[index] == 1
