from django.shortcuts import render,redirect,get_object_or_404
from .models import Producto
from .forms import ContactoForm,ProductoForm
from django.contrib import messages

def home(request):
    prductos = Producto.objects.all()
    data={
        'productos':prductos
    }
    
    return render(request,'app/home.html',data)


def contacto(request):
    data={
        'form':ContactoForm
    }
    
    if request.method == 'POST':
        formulario = ContactoForm(data=request.POST)
        if formulario.is_valid():
            formulario.save()
            data["mensaje"]="contacto guardado"
        else:
            data["form"]=formulario
            data["mensaje"]="contacto no guardado"
            
        
    return render(request,'app/contacto.html',data)


def galeria(request):
    prductos = Producto.objects.all()
    
    data={
        'productos':prductos
    }
    return render(request,'app/galeria.html',data)


def agregar_producto(request):
    data={
        'form':ProductoForm
        }
    
    if request.method == 'POST':
        formulario = ProductoForm(data=request.POST, files=request.FILES)
        if formulario.is_valid():
            formulario.save()
            messages.success(request,"agregado correctamente")
            return redirect(to="listar_productos")
        else:
             data["form"]=formulario
             data["mensaje"]="producto no guardado"
            
    return render(request,'app/producto/agregar.html',data)


def listar_productos(request):
    prductos = Producto.objects.all()
    
    data={
        'productos':prductos
    }
     
    return render(request,'app/producto/listar.html',data)

def modificar_producto(request,id):
    
    producto=get_object_or_404(Producto, id=id)
    
    data={
        'form':ProductoForm(instance=producto)
    }
    if request.method == 'POST':
        formulario = ProductoForm(data=request.POST, instance=producto , files=request.FILES)
        if formulario.is_valid():
            formulario.save()
            messages.success(request,"modificado correctamente")
            return redirect(to="listar_productos")
        else:
            data["form"]=formulario
            data["mensaje"]="producto no Actualizado"
            
    return render(request,'app/producto/modificar.html',data)

def eliminar_producto(request,id):
    
    producto=get_object_or_404(Producto, id=id)
    producto.delete()    
    messages.success(request,"eliminado correctamente")    
    return redirect(to='listar_productos')

