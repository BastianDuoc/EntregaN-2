
from django.contrib import admin
from django.urls import path , include
from .views import inicio,galeria,login,misionvision,registro,registroinsumo,ubicacion,logout_vista,admin_insumos,eliminar,modificarinsumo,modificar_insumos

urlpatterns = [
    path('',inicio, name='Inicio'), 
    path('galeria/', galeria, name='Galeria'), 
    path('login/', login, name='Login'),
    path('misionvision/', misionvision, name='MisionVision'),
    path('registro/', registro, name='Registro'),
    path('registroinsumo/', registroinsumo, name='RegistroInsumos'),
    path('ubicacion/', ubicacion, name='Ubicacion'),
    path('logout_vista', logout_vista, name='Logout'),
    path('admin_insumos/', admin_insumos, name='Admin_Insumos'),
    path('eliminar/<id>/', eliminar, name='ELIMINAR'),
    path('modificar_insumo/<id>/', modificarinsumo, name='MODIFICAR_V'),
    path('modificar/', modificar_insumos, name='MODIFICAR'),
]
