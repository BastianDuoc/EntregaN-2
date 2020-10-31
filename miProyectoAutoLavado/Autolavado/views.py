from django.shortcuts import render
from .models import autoGaleria , autoInicio , MisionVision , Insumos

# utilizar la tabla usuario
from django.contrib.auth.models import User

# importar las librerias de validaciones
from django.contrib.auth import authenticate, logout, login as login_autent

# decorado
from django.contrib.auth.decorators import login_required,permission_required



# Create your views here.
def inicio(request):
    autosIni = autoInicio.objects.all()
    return render(request,'core/inicio.html',{'lista_AutosIni':autosIni})

def galeria(request):
    autosGal = autoGaleria.objects.all()
    return render(request,'core/Galeria.html',{'lista_AutosGal':autosGal})

@login_required(login_url='/login/')
def logout_vista(request):
    logout(request)
    autosIni = autoInicio.objects.all()
    return render(request,'core/inicio.html',{'lista_AutosIni':autosIni})

def login(request):
    if request.POST:
        usuario  = request.POST.get("nombreUS")
        password = request.POST.get("contraseña")
        us = authenticate(request, username=usuario, password=password)
        if us is not None and us.is_active:
            login_autent(request, us)
            autosIni = autoInicio.objects.all()
            return render(request,'core/inicio.html',{'user':us, 'lista_AutosIni':autosIni})
        else:
            return render(request,'core/Login.html', {'msg': 'Usuario o Contraseña incorrectos'})
    return render(request,'core/Login.html')

def misionvision(request):
    MisVis = MisionVision.objects.all()
    return render(request,'core/MisionVision.html',{'MisionVisionL':MisVis})
    
def registro(request):
    if request.POST:
        nombre    = request.POST.get("nombre")
        apellido  = request.POST.get("apellido")
        email     = request.POST.get("correo")
        usuario   = request.POST.get("nombreUS")
        password  = request.POST.get("contraseña")
        password2 = request.POST.get("rcontraseña")

        if password != password2:
            return render(request,'core/Registro.html',{'msg': 'La contraseña no coincide'})

        try:
            u = User.objects.get(email=email)
            return render(request,'core/Registro.html',{'msg': 'Este correo ya esta registrado'})
        except:
                try:
                    u = User.objects.get(username=usuario)
                    return render(request,'core/Registro.html',{'msg': 'Usuario Existente'})
                except:

                    u = User()
                    u.username   = usuario
                    u.first_name = nombre
                    u.last_name  = apellido
                    u.email      = email
                    u.set_password(password)
                    u.save()

                    us = authenticate(request, username=usuario, password=password)
                    login_autent(request, us)
                    autosIni = autoInicio.objects.all()
                    return render(request,'core/inicio.html',{'lista_AutosIni':autosIni})
    return render(request,'core/Registro.html')

@login_required(login_url='/login/')
@permission_required('Autolavado.add_insumos')
def registroinsumo(request):
    if request.POST:
        nombre = request.POST.get("NombreInsumo")
        precio = request.POST.get("PrecioInsumo")
        descripcion = request.POST.get("DescripcionInsumo")
        stock = request.POST.get("CantidadInsumo")

        insumo = Insumos( 
            nombre=nombre,
            precio=precio,
            descripcion=descripcion,
            stock=stock
        )
        insumo.save()
        return render(request,'core/RegistroInsumos.html',{'msg':'insumo grabado'})
    return render(request,'core/RegistroInsumos.html')


@login_required(login_url='/login/')
@permission_required('Autolavado.change_insumos')
@permission_required('Autolavado.view_insumos')
def modificar_insumos(request):
    if request.POST:
        nombre = request.POST.get("NombreInsumo")
        precio = request.POST.get("PrecioInsumo")
        descripcion = request.POST.get("DescripcionInsumo")
        stock = request.POST.get("CantidadInsumo")

        try:
            insumo = Insumos.objects.get(nombre=nombre)
            insumo.precio = precio
            insumo.descripcion = descripcion
            insumo.stock = stock
            insumo.save()
            msg='insumo actualizado con exito'
        except :
             msg='no se pudo Modificar el insumo'
    insumos = Insumos.objects.all()
    return render(request,'core/Admin_Insumos.html',{'insumos':insumos,'msg':msg})




@login_required(login_url='/login/')
@permission_required('Autolavado.view_insumos')
def modificarinsumo(request,id):
    try:
        insumo = Insumos.objects.get(nombre=id)
        return render(request,'core/Mod_Insumos.html',{'insumo':insumo})
    except:
        msg = "inusmo no encontrado en la base de datos"
    insumos = Insumos.objects.all()
    return render(request,'core/Admin_Insumos.html',{'insumos':insumos,'msg':msg})


def ubicacion(request):
    return render(request,'core/Ubicacion.html')
    
@login_required(login_url='/login/')
@permission_required('Autolavado.view_insumos')
def admin_insumos(request):
    insumos = Insumos.objects.all()
    return render(request,'core/Admin_Insumos.html',{'insumos':insumos})

@login_required(login_url='/login/')
@permission_required('Autolavado.delete_insumos')
def eliminar(request,id):
    try:

        insumo = Insumos.objects.get(nombre=id)
        insumo.delete()
        msg = "insumo eliminado"

    except:
        msg = "el insumo no se a podido eliminar"
    insumos = Insumos.objects.all()
    return render(request,'core/Admin_Insumos.html',{'insumos':insumos,'msg':msg})

