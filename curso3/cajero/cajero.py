#  Para este proyecto, deberás programar una caja registradora para una almacén. 
#  El sistema debe poder escanear un producto (el cajero puede tipear el código del producto), 
# y agregarlo a la lista de productos comprados para ese cliente. 
#  Además debe mostrar el subtotal. 
#  El cajero cuando lo desee puede finalizar la compra y el sistema deberá aplicar los descuentos 
# correspondientes a los productos. 
#  Luego, el cajero indica con cuánto paga el cliente y el sistema debe mostrar el cambio que debe 
# devolver al cliente.
import unittest
from os import system, name


class Producto(object):
   def __init__(self, codigo, nombre, precio):
      self.codigo = codigo
      self.nombre = nombre
      self.precio = precio

   def __repr__(self):
      return "{}: {} \t${}".format(self.codigo, self.nombre, self.precio)

   def __mul__(self, cantidad):
      return self.precio * cantidad



class Compra(object):
   def __init__(self, producto, cantidad):
      self.producto = producto
      self.cantidad = cantidad
      self.subtotal = producto * cantidad

   def __repr__(self):
      return "{} unidad/es de {}".format(self.cantidad, self.producto.nombre)



class Carrito(object):
   def __init__(self, codigo):
      self.codigo = codigo
      self.compras = []
      self.total = 0
      self.pago = 0
      self.vuelto = 0
      self.tieneDescuento = False
      self.descontado = 0

   def agregarProducto(self, producto, cantidad):
      self.compras.append(Compra(producto, cantidad))
      self.calcTotal()
   
   def calcTotal(self):
      total = 0
      cantProds = 0
      for x in self.compras:
         total += x.subtotal
         cantProds += x.cantidad
      
      if cantProds >= 10 or total > 1000:
         self.total = total * 0.9
         self.tieneDescuento = True
         self.descontado = total * 0.1
      else:
         self.total = total

   def setPago(self, pago):
      self.pago = pago
      self.calcVuelto()

   def calcVuelto(self):
      self.vuelto = self.pago - self.total

   def mostrarCompras(self):
      for x in self.compras:
         print(x)

   def mostrarTotal(self):
      return "El Total es: \t${}".format(self.total)

   def mostrarVuelto(self):
      return "El Vuelto es: \t${}".format(self.vuelto)



### FUNCION CLEARSCREEN
def clear(): 
   if name == 'nt': 
      _ = system('cls') 
   else: 
      _ = system('clear') 



class CajaRegistradora(object):
   def __init__(self):
      self.productos = [
            Producto(0, "Agua", 65),
            Producto(1, "Snack", 120),
            Producto(2, "Chocolate", 80)
         ]
      self.contador = 0
      self.carritos = []

   def aumentarContador(self):
      self.contador += 1

   def mostrarProductos(self):
      for x in self.productos:
         print(x)

   def ingresarProducto(self, carrito):
      producto = int(input("\nIngrese el codigo del producto(0 al 2):   "))
      cantidad = int(input("Ingrese la cantidad deseada:   "))
      carrito.agregarProducto(self.productos[producto], cantidad)
      return carrito

   def verificarDescuento(self, carrito):
      if carrito.tieneDescuento:
         print("{}\nSe ha aplicado el descuento del 10% (${})".format(carrito.mostrarTotal(), carrito.descontado))
      else:
         print(carrito.mostrarTotal())

   def comprar(self):
      carrito = Carrito(self.contador)
      self.aumentarContador()

      comprar = True
      print("Con la compra de mas de $1000 o 10 productos tenes un 10% de descuento\n")

      while comprar:
         self.mostrarProductos()
         carrito = self.ingresarProducto(carrito)
         clear()
         carrito.mostrarCompras()
         print(carrito.mostrarTotal())

         comprar = int(input("\nDesea agregar mas productos?:\n0: No\n1: Si\n: "))
         clear()

      self.verificarDescuento(carrito)
      carrito.setPago(int(input("\nIngrese el monto con el que abonara: ")))

      print(carrito.mostrarVuelto())
      self.carritos.append(carrito)
   
   def main(self):
      print("Bienvenide al carrito de compra!\n")
      actividad = True
      while actividad:
         self.comprar()
         actividad = int(input("\nNueva compra?:\n0: No\n1: Si\n: "))
         clear()



class Tester(unittest.TestCase):
   def setUp(self):
      self.productos = [
         Producto(0, "Agua", 65),
         Producto(1, "Snack", 120),
         Producto(2, "Chocolate", 80)
      ]
      self.compras = [
         Compra(self.productos[0], 2),
         Compra(self.productos[1], 1),
         Compra(self.productos[2], 5)
      ]
      self.carrito = Carrito(1)


   # Test producto
   def testProd0(self):
      self.assertEqual(0, self.productos[0].codigo)
      self.assertEqual("Agua", self.productos[0].nombre)
      self.assertEqual(65, self.productos[0].precio)

   def testProd1(self):
      self.assertEqual(1, self.productos[1].codigo)
      self.assertEqual("Snack", self.productos[1].nombre)
      self.assertEqual(120, self.productos[1].precio)

   def testProd2(self):
      self.assertEqual(2, self.productos[2].codigo)
      self.assertEqual("Chocolate", self.productos[2].nombre)
      self.assertEqual(80, self.productos[2].precio)


   # Test multiplicar producto
   def testMulProds0(self):
      self.assertEqual(650, self.productos[0]*10)
   
   def testMulProds1(self):
      self.assertEqual(960, self.productos[1]*8)

   def testMulProds2(self):
      self.assertEqual(240, self.productos[2]*3)


   # Test  de compras
   def testCompra0(self):
      self.assertEqual(0, self.compras[0].producto.codigo)
      self.assertEqual(2, self.compras[0].cantidad)
      
   def testCompra1(self):
      self.assertEqual(1, self.compras[1].producto.codigo)
      self.assertEqual(1, self.compras[1].cantidad)

   def testCompra2(self):
      self.assertEqual(2, self.compras[2].producto.codigo)
      self.assertEqual(5, self.compras[2].cantidad)


   # Test de calculo de subtotal
   def testTubtotal0(self):
      self.assertEqual(130, self.compras[0].subtotal)

   def testTubtotal1(self):
      self.assertEqual(120, self.compras[1].subtotal)
   
   def testTubtotal2(self):
      self.assertEqual(400, self.compras[2].subtotal)


   # Test de carrito
   def testAgregarProd0(self):
      self.carrito.agregarProducto(self.productos[0], 2)
      self.assertEqual(130, self.carrito.total)

   def testAgregarProd1(self):
      self.carrito.agregarProducto(self.productos[1], 8)
      self.assertEqual(960, self.carrito.total)

   def testAgregarProd2(self):
      self.carrito.agregarProducto(self.productos[1], 8)
      self.carrito.agregarProducto(self.productos[0], 2)
      self.assertEqual(981.0, self.carrito.total)

   def testVuelto(self):
      self.carrito.agregarProducto(self.productos[1], 8)
      self.carrito.agregarProducto(self.productos[0], 2)
      self.carrito.setPago(1100)
      self.assertEqual(119.0, self.carrito.vuelto)


# unittest.main()
caja = CajaRegistradora()
caja.main()