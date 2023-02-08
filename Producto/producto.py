from Lista import lista
class Producto(lista.Lista):
    def __init__(self):
        super().__init__()
    
    def crearproducto(self,codigo=0,nombre="",description="",precio=float): 
     self.codigo=codigo
     self.nombre=nombre
     self.descripcion=description
     self.precio=precio
     self.elproducto={"codigo":self.codigo,"nombre":self.nombre,"description":self.descripcion,"precio":self.precio}
    
    def crearjsondeproducto(self,diccionario):  
     super().guardar(diccionario,"producto")
     
     
    def actualizareljson(self): 
     auxiliar=super().elmpatyjson('producto')
     if auxiliar == True:  
         for objetoss in super().datosdeljson1('producto'):
                  self.lista.append(objetoss)
         return True
     else:
       return "Se ha creado el Json"
     
     
    def modificar2(self,lista,propiedad,nombre,nuevovalor):
      x=super().modificar(lista,propiedad,nombre,nuevovalor)
      super().guardar(lista,"producto")
      return x
   
    def eliminarclinete(self,lista,elcaracter):
       x=super().eliminar(lista,elcaracter)
       if x==True:
         y= "se elimino correctamente"
       else:
         y= "no se elimino el objeto"
       super().guardar(lista,"producto")  
       return y
     
    def mostrarP(self,listadep):
      numero=len(listadep)
      print("-------------------------TABLA--------------------------------------------------------------------------------------")
      for ObjetoP in listadep:
        print("--------------------------------Producto--------------------------------------")
        print("|| Codigo: ",format(ObjetoP["codigo"])+"\t ||Nombre: "+format(ObjetoP["nombre"])+"\t ||Description: "+format(ObjetoP["description"])+"\t ||Precio: $"+format(ObjetoP["precio"]))
        print()
      print("TOTAL DE PRODUCTOS: ",numero)
      print()
    
       
   