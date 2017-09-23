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


auto = Producto('f500', 10000, 'rojo', 'ferrari')
compu = Producto('v1000', 1500 , 'negra', 'dell')
cel = Producto ('mate 8', 1900 , 'blanco', 'huawey')
auto2 = Producto ('ford', 12000 , 'plata', 'fiest')
objetos = (auto, compu, cel, auto2)

print sorted(objetos, key=lambda producto: producto.nombre)
print sorted(objetos, key=lambda producto: producto.precio)
