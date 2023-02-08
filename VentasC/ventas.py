from Lista import lista


import datetime

class Venta(lista.Lista):
    
    def __init__(self):
        super().__init__()
       
        
              
    def check(self,cliente,producto):
     validarC=super().elmpatyjson('cliente')
     validarP=super().elmpatyjson('producto')
     validarNC=False
     validarNP=False
     if validarC==True & validarP==True:   
      
      listacliente=super().datosdeljson1('cliente')
      
      listaproducto=super().datosdeljson1('producto')
      current_date = datetime.date.today()
      
      for ObjetoC in listacliente:
          if ObjetoC.get('nombre')==cliente:
              validarNC=True
              cliente=ObjetoC
              
      for Objetop in listaproducto:
          if Objetop.get('nombre')==producto:
              variableTP=Objetop
              validarNP=True
              
      if validarNP==True & validarNC==True:
          self.laventa={"Cliente":cliente,"Producto":[variableTP],"fecha":format(current_date)}
          self.lista.append(self.laventa)
          
          super().guardar(self.lista,'venta')
          return "Venta exitosa"
      else:
        return "404"       
    
    def modificar(self, lista, propiedad, buscarelvalor, nuevovalor):
       x=super().modificar(lista, propiedad, buscarelvalor, nuevovalor)
       super().guardar(lista,"venta") 
       return x
   
     
    def eliminarVenta(self,lista,elcaracter):
       x=super().eliminarV(lista,elcaracter)
       if x==True:
         y= "se elimino correctamente"
       else:
         y= "no se elimino el objeto"
       super().guardar(lista,"venta")  
       return y
   
    def verventas(self):
     return super().datosdeljson1("venta")
    
    def actualizarventas(self):
     auxiliar=super().elmpatyjson('venta')
     if auxiliar == True:  
          for objetoss in super().datosdeljson1('venta'):
                   self.lista.append(objetoss)
     else:
        print("Se ha creado el Json")
        
        
        
    def agregaProducto(self,nombredelcliente,nombredelproducto):
        contador=0
        listaproducto=super().datosdeljson1('producto')
        for ObjetoP in listaproducto:
            if  ObjetoP.get("nombre")==nombredelproducto:
                auxiliar=ObjetoP
        for ObjetoC in self.lista:
            
            if ObjetoC['Cliente'].get('nombre')==nombredelcliente:
               ObjetoC['Producto'].append(auxiliar)
               super().guardar(self.lista,"venta") 
               print("se inserto correctamente ")
            else:
                contador=contador+1
        
    def verVentasentabla(self):
      listaV=list()
      cliente=""
      for Objeto in self.lista:
          total=0
          cliente=Objeto["Cliente"]
          listaV=Objeto["Producto"]
          print()
          print()
          print("------------------------------------------------------------TABLA-------------------------","---"*10)  
          print("-----------------------------------El cliente-------------------------------- \n")
          print('nombre: ',cliente["nombre"],"\t" ,"rfc: ", cliente["rfc"],"\t"+ ' telefono: ' ,cliente["telefono"]) 
          print ("---------------------Productos------------------------")
          for ObjetoP in listaV:  
            total += ObjetoP["precio"]
            print("Codigo: ",(ObjetoP["codigo"]),"|| \t Nombre del producto: ",(ObjetoP["nombre"]),"|| \t Description: ",(ObjetoP["description"]),"|| \t Precio: ",(ObjetoP["precio"]))
            
            print("-----------------------------------------------------------------------------------------------")
          print("TOTAL: ",total)
          print()
        
          
             
            
            
        
        
                 
                
    
             
            
                 
                 
                 
        