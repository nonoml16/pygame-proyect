class Map:
    def __init__(self, filename):
        self.filename = filename
        self.data = self.load_map()

    def load_map(self):
        with open(self.filename, 'r') as f:
            data = f.readlines()
        # Eliminar saltos de línea y espacios en blanco al final de cada línea
        data = [line.strip() for line in data]
        return data

    def get_tile_at(self, x, y):
        return self.data[y][x]