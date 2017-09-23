import Producto

prod = []
prodnom = []

auto = Producto()
auto.nombre = "f500"
auto.precio = 10000000
auto.color = "rojo"
auto.marca = "ferrari"

compu = Producto()
compu.nombre = "v1000"
compu.precio = 15000
compu.color = "negra"
compu.marca = "dell"

cel = Producto()
cel.nombre = "mate 8"
cel.precio = 8000
cel.color = "blanco"
cel.marca = "huawei"

def compara( x, y ) :

    if self.Name < other.Name :
      rst = -1
    elif self.Name > other.Name :
      rst = 1
    else :
      rst = 0

    return rst

prod = [auto, compu, cel]
prodnom = prod.sort( compara )

print prodnom


