from django.shortcuts import render, get_object_or_404
from django.db.models import Q, Avg

from .models import *

# Create your views here.

def index(request):
    return render(request, "index.html")



# Obtiene detalles de un usuario por su email.
def usuario_detalle(request, email):
    usuario = get_object_or_404(Usuario.objects.select_related('perfil'), email=email)
    return render(request, 'usuario_detalle.html', {'usuario': usuario})


# Muestra todas las propiedades con sus categorías y servicios extra.
def lista_propiedades(request):
    propiedades = Propiedad.objects.prefetch_related('categoria', 'servicios_extra')
    return render(request, 'lista_propiedades.html', {'propiedades': propiedades})


# Detalle de una categoría específica.
def detalle_categoria(request, id):
    categoria = Categoria.objects.prefetch_related('propiedades').get(id=id)
    return render(request, 'detalle_categoria.html', {'categoria': categoria})


# Lista las reservas asociadas a una propiedad específica.
def reservas_propiedad(request, propiedad_id):
    reservas = Reserva.objects.filter(propiedad_id=propiedad_id).select_related('perfil', 'pago')
    return render(request, 'reservas_propiedad.html', {'reservas': reservas})


# Muestra los comentarios de una propiedad.
def comentarios_propiedad(request, propiedad_id):
    propiedad = Propiedad.objects.prefetch_related('comentarios').get(id=propiedad_id)
    return render(request, 'comentarios_propiedad.html', {'propiedad': propiedad})


# Filtra reservas por estado y rango de fechas.
def filtrar_reservas(request):
    reservas = Reserva.objects.filter(
        Q(estado="Whole war mother.") & Q(total__gte=0.446948437705188) | Q(estado="Event cover none.")
    )
    return render(request, 'filtrar_reservas.html', {'reservas': reservas})



# Categorías sin propiedades asignadas.
def categorias_sin_propiedades(request):
    categorias = Categoria.objects.filter(propiedades=None)
    return render(request, 'categorias_sin_propiedades.html', {'categorias': categorias})


# Calcula el precio promedio de las propiedades.
def propiedad_precio_agregado(request):
    precio_promedio = Propiedad.objects.aggregate(Avg('precio_por_noche'))
    return render(request, 'propiedad_precio_agregado.html', {'precio_promedio': precio_promedio})

#esta view no me sale y no encuentro el error 

def usuarios_recientes(request):
    # Obtener los 10 usuarios más recientes ordenados por fecha_registro
    usuarios = Usuario.objects.order_by('-fecha_registro')[:10]
    # Pasar los usuarios a la plantilla
    return render(request, 'usuarios_recientes.html', {'usuarios': usuarios})


# Muestra una página personalizada de error 404.
def error_404(request, exception=None):
    return render(request, 'errores/error_404.html', None, None, 400)


# Muestra una página personalizada de error 400.
def error_400(request, exception=None):
    return render(request, 'errores/error_400.html', None, None, 400)


# Muestra una página personalizada de error 403.
def error_403(request, exception=None):
    return render(request, 'errores/error_403.html', None, None, 400)


# Muestra una página personalizada de error 500.
def error_500(request, exception=None):
    return render(request, 'errores/error_500.html', None, None, 400)


#Formularios-------------------------------------


#Formulario para buscar el nombre de una propiedad

def Propiedad_buscar(request):
    
    return render(request, 'Formularios/Propiedad_buscar.html')