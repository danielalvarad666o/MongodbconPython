from VentasC import ventas

class InterfacedelasVentas:
    def InicioV(self):
     laventa=ventas.Venta()
     laventa.actualizarventas()
     print("[----------------OPTIONES-----------------------]")   
     print("1)Craer Venta ")
     print("2)Eliminar")
     print("3)Agregar un Producto ala Venta")
     print("4)Ver Ventas")
     
     option=0
     try:
         option=int(input("Escoge una option: "))
         if option==1:
          elclinete=str(input("Inserta el nombre del cliente: "))
          elproducto=str(input("Inserta el nombre del producto: "))  
          laventa.check(elclinete,elproducto)
         elif option==2:
            print()
            print("[-------------------------]")
            nombre=str(input("Poner el nombre del clinete a eliminar: "))
            laventa.eliminarVenta(laventa.lista,nombre)
         elif option==4:
             #print(laventa.lista)
             laventa.verVentasentabla()
         elif option==3:
            elclinete=str(input("Inserta el nombre del cliente: "))
            elproducto=str(input("Inserta el nombre del producto: "))  
            laventa.agregaProducto(elclinete,elproducto)
             
             
     except:
         return "Error 404"