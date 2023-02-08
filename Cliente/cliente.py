from Lista import lista
class Client(lista.Lista):
    
    def __init__(self):
        super().__init__()
        
        
    
    def crearcliente(self,nombre="",rfc="",telefono=0):
        self.nombre=nombre
        self.rfc=rfc
        self.telefono=telefono
        self.cliente={'nombre':self.nombre,'rfc':self.rfc,'telefono':self.telefono}
        
    def crearjsonpersona(self,diccionario):
      super().guardar(diccionario,"cliente")

        
    def actualizareljson(self): 
     auxiliar=super().elmpatyjson('cliente')
     if auxiliar == True:  
         for objetoss in super().datosdeljson1('cliente'):
                  self.lista.append(objetoss)
     else:
       print("Se ha creado el Json")
       
  
    def eliminarclinete(self,lista,elcaracter):
       x=super().eliminar(lista,elcaracter)
       if x==True:
         y= "se elimino correctamente"
       else:
         y= "no se elimino el objeto"
       super().guardar(lista,"cliente")  
       return y
     
    def ModificarC(self,lista,propiedad,buscar,nuevovalor):
      x=super().modificar(lista,propiedad,buscar,nuevovalor)
      super().guardar(lista,"cliente") 
      return x
      
        
        