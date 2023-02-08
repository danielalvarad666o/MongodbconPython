from Cliente import cliente

class interfasC:
    
    def OptionesC(self):
     elcliente=cliente.Client()
     elcliente.actualizareljson()
     
     print()
     
     print("[----------------OPTIONES-----------------------]")   
     print("1)Insertar ")
     print("2)Modiicar ")
     print("3)Eliminar")
     print("4)Ver Clientes")
     print("5)Buscar")
     
     option=0
     try:
      option=int(input("Escoge una option: "))
     
      if option==1:
       print()
       nombre=str(input("Insertar el Nombre del Cliente: "))
       rfc=str(input("Insertar el RFC pro favor: "))
       telefono=int(input("Insertar el numero de telefono: "))
       elcliente.crearcliente(nombre,rfc,telefono)
       elcliente.append(elcliente.cliente)
       elcliente.crearjsonpersona(elcliente.lista)
      elif option==2:
       print()
       print("[---------------Propiedades 'Disponible'-------------]")
       print("nombre")
       print("rfc")
       print("telefono")
       print()
       propiedad=(input("Escoger una propiedad: "))
       buscar=(input("poner el dato a buscar: "))
       nuevovalor=(input("Nuevo valor a insertar: "))
       print(elcliente.ModificarC(elcliente.lista,propiedad,buscar,nuevovalor))
       
      
      elif option==3:    
       print()
       print("[-------------------------]")
       nombre=str(input("Poner el nombre del clinete a eliminar: "))
       elcliente.eliminarclinete(elcliente.lista,nombre)
     
      elif option==4:
        print()
        print(elcliente.lista)
     
      elif option==5:
          buscar=str(input("Inserta el nombre del cliente que deseas buscar:"))
          x=elcliente.buscar(elcliente.lista,buscar)   
          if x==False:
              print("Error el valor no se encontro")
          else:
              print(x)   
            
     except:
         return "Error de option o tipo dato "
        
            