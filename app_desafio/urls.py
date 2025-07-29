from django.urls import path
from .views import mostrar_nombres


## DEFINO LA URL EN DONDE SE MOSTRARÁN LOS NOMBRES DE LOS EMPLEADOS Y LA FUNCCION QUE SE EJECUTARÁ
## EN ESTE CASO ES "" PORQUE SERÁ NECESARIO AÑADIR NADA ADICIONAL A LA URL
urlpatterns = [
    path("",mostrar_nombres,name="mostrar_nombres")
]