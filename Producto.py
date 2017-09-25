class Producto:
    def __init__(self, nombre, precio, color, marca):
        self.nombre = nombre
        self.precio = precio
        self.color = color
        self.marca = marca

    def __repr__(self):
        return '{}: {} {} {} {}'.format(self.__class__.__name__,
                                  self.nombre,
                                  self.precio,
                                  self.color,
                                  self.marca
                                  )
