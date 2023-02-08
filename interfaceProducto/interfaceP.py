from Producto import producto
from Mongoclass import mongo
uri = "mongodb+srv://root:2tCVgy$_DEa!ZYB@5b.y2llyqd.mongodb.net/test"

class interfaceP:
  
    def OptionesP(self):
     elproducto=producto.Producto()
     validacion=elproducto.actualizareljson()
     client = mongo.MongoDBClient(uri)
     conecc=client.connect()
     if conecc: 
      if validacion!=True:
         client.get_documents("Python","Productos",elproducto.lista)
         elproducto.crearjsondeproducto(elproducto.lista)
         
         
     
     
     print()
     print("[----------------OPTIONES-----------------------]")   
     print("1)Insertar ")
     print("2)Modiicar ")
     print("3)Eliminar")
     print("4)Ver Productos")
     print("5)Buscar")
     
     option=0
     
     
     try:
      option=int(input("Escoge una option: "))
     
      if option==1:
          
       print()
       codigo=int(input("El codigo del producto: "))
       nombre=str(input("Ingresa el nombre del producto: "))
       description=str(input("Ingresa la description del produto: "))
       precio=float(input("Ingresa el precio del producto: "))
       elproducto.crearproducto(codigo,nombre,description,precio)
       elproducto.append(elproducto.elproducto)
       elproducto.crearjsondeproducto(elproducto.lista)
       client.update_all_documents("Python","Productos",elproducto.lista)
       
       
       
       
      elif option ==2:
       print()
       print("[---------------Propiedades 'Disponible'-------------]")
       print("codigo")
       print("nombre")
       print("description")
       print()
       propiedad=str(input("Escoger una propiedad: "))
       buscar=str(input("poner el dato a buscar: "))
       nuevovalor=str(input("Nuevo valor a insertar: "))
       elproducto.modificar2(elproducto.lista,propiedad,buscar,nuevovalor)
       client.update_all_documents("Python","Productos",elproducto.lista)
       
      elif option==3:
          
       print()
       print("[-------------------------]")
       nombre=str(input("Poner el nombre del clinete a eliminar: "))
       elproducto.eliminarclinete(elproducto.lista,nombre)
       client.update_all_documents("Python","Productos",elproducto.lista)
       
      elif option==4:
        client.update_all_documents("Python","Productos",elproducto.lista)
        elproducto.mostrarP(elproducto.lista)
        
      elif option==5:
          
          buscar=str(input("Inserta el nombre del producto que deseas buscar:"))
          x=elproducto.buscar(elproducto.lista,buscar)   
          if x==False:
              print("Error el valor no se encontro")
          else:
              print(x)  
     except:
         return "Error de option o tipo dato "
     
     
      