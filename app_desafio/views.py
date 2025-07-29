from django.shortcuts import render



## ACÁ CREO LA LISTA CON LOS EMPLEADOS Y SE PUEDE MODIFICAR EN CUALQUIER MOMENTO
## EL CAMBIO SE VE REFLEJADA EN LA PÁGINA CUANDO SE ACTUALIZA
empleados = [
    "Carlos Ramírez",
    "Lucía Fernández",
    "Miguel Torres",
    "Ana González",
    "Javier Soto",
    "Mariana Paredes",
    "Andrés Herrera",
    "Sofía Medina",
    "Diego Vargas",
    "Valentina Ríos"
]


## DEFINO LA FUNCION MOSTRAR_NOMBRES QUE LE ENVÍA EL CONTEXTO CON LA LISTA DE EMPLEADOS AL TEMPLATE DE EMPLEADOS.HTML
def mostrar_nombres(request):
    return render(request, "empleados.html", {"empleados":empleados}) 

