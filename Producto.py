class Producto:
    def __init__(self, nombre, precio, color, marca):
        self.nombre = nombre
        self.precio = precio
        self.color = color
        self.marca = marca

    def por_nombre(self, objetos):
        return sorted(objetos, key=lambda producto: producto.nombre)

    def por_precio(self, objetos):
        return sorted(objetos, key=lambda producto: producto.precio)

    def opcional(self, objetos, tipo):
        if(tipo == "nombre"):
            return sorted(objetos, key=lambda producto: producto.nombre)
        else:
            return sorted(objetos, key=lambda producto: producto.precio)

    def __repr__(self):
        return '{}: {} {} {} {}'.format(self.__class__.__name__,
                                  self.nombre,
                                  self.precio,
                                  self.color,
                                  self.marca
                                  )
