from django.shortcuts import render, redirect
from django.conf import settings
from django.core.mail import send_mail
from.models import Mipyme, Producto
from django.contrib import messages
from django.core.files.storage import default_storage
from django.db.models import Q

# Create your views here.
def form(request):
    return render(request, "inicio.html")

def contact(request):
    if request.method == "POST":
        asunto = request.POST["txtasunto"]
        mensaje = request.POST["txtmensaje"] + " / Email: " + request.POST["txtemail"]
        emailsrc = settings.EMAIL_HOST_USER
        emaildst = ["larroquegusnel@gmail.com"]
        send_mail(asunto, mensaje, emailsrc, emaildst, fail_silently=False)
        return render(request, "contactexito.html")
    return render(request, "inicio.html")

def list(request):
    mipymes = Mipyme.objects.prefetch_related('product')
    return render(request, 'list.html', {'mipymes': mipymes})


def visitarMipyme(request, codigo):
    mipyme = Mipyme.objects.get(codigo=codigo)
    return render(request, "visitarMipyme.html", {'Mipyme':mipyme})

def addpromo(request):
    return render(request, 'addpromo.html') 

def registrarMipyme(request):
    
    nombre = request.POST['txtnombre']
    ubicacion = request.POST['txtubicacion']
    num = request.POST['txtnum']
    provincia = request.POST['provincia']
    descripcion = request.POST['txtdesc']

    imagen = request.FILES.get('txtimg', None)

    if num == "":
        num= 0
        
    if imagen:
        mipyme = Mipyme.objects.create(nombre=nombre, ubicacion=ubicacion, descripcion=descripcion, provincia=provincia, num=num, imagen=imagen)
        file_path = default_storage.save(imagen.name, imagen)

        messages.success(request, '¡Mipyme registrada!')
        return redirect('/list')
    else:
        messages.error(request, 'Error al cargar la imagen')
        return redirect('/list')

def eliminarMipyme(request, codigo):
    mipyme = Mipyme.objects.get(codigo=codigo)
    mipyme.delete()
    messages.success(request, '!Mipyme eliminada!')
    return redirect('/list')

def buscar_productos(request):
    if request.method == "GET":
        min_precio = request.GET.get('min_precio')
        max_precio = request.GET.get('max_precio')
        nombre_producto = request.GET.get('nombre_producto')
        provincia = request.GET.get('provincia')
        mipymes = Mipyme.objects.prefetch_related('product')
        valido = 'si'
        mipymes = mipymes.filter(valido=valido)
        productos = Producto.objects.all()

        if provincia:
            mipymes = mipymes.filter(provincia=provincia)

        productos = Producto.objects.filter(mipyme__in=mipymes)

        if min_precio and max_precio:
            productos = productos.filter(precio__gte=min_precio, precio__lte=max_precio)
        if nombre_producto:
            palabras_clave = nombre_producto.split()
            q = Q(nombre__icontains=palabras_clave[0])
            for palabra in palabras_clave[1:]:
                q |= Q(nombre__icontains=palabra)
            productos = productos.filter(q)
        
            

        return render(request, 'resultado_busqueda.html', {'productos': productos})

    return render(request, 'formulario_busqueda.html')