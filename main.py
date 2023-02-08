from Menu import Menus
from InterfasCliente import InterfasClientess
from interfaceProducto import interfaceP
from interfasV import interfaceVentas

intefacec=InterfasClientess.interfasC()
lainterfaceproducto=interfaceP.interfaceP()
elmenu=Menus.interfasMenu()
interfaceV=interfaceVentas.InterfacedelasVentas()
option=0
while option!=5:
 option=elmenu.MostrarMenu()
 

 if option==1:
     intefacec.OptionesC()  
 elif option==2:
     lainterfaceproducto.OptionesP()
 elif option==3:
     interfaceV.InicioV()
    
 
     
 