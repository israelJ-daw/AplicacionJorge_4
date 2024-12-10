from django.urls import path
from . import views

urlpatterns = [
    path("", views.index, name="index"),

    path('usuarios/<str:email>/', views.usuario_detalle, name='usuario_detalle'),  # OneToOne
    path('propiedades/', views.lista_propiedades, name='lista_propiedades'),  # ManyToMany
    path('categorias/<int:id>/', views.detalle_categoria, name='detalle_categoria'),  # QuerySet con parámetros
    path('propiedad/reservas/<int:propiedad_id>/', views.reservas_propiedad, name='reservas_propiedad'),  # Filtro ManyToOne
    path('comentarios/propiedad/<int:propiedad_id>/', views.comentarios_propiedad, name='comentarios_propiedad'),  # Reverse
    path('reservas/filtro/', views.filtrar_reservas, name='filtrar_reservas'),  # Filtros con AND y OR
    path('categorias/none/', views.categorias_sin_propiedades, name='categorias_sin_propiedades'),  # None intermedio
    path('propiedades/precios/', views.propiedad_precio_agregado, name='propiedad_precio_agregado'),  # Aggregate
    path('usuarios/recientes/', views.usuarios_recientes, name='usuarios_recientes'),# OrderBy y limit
    path('error/404/', views.error_404, name='error_404'),  # Error personalizado
    path('error/404/', views.error_404, name='error_404'),  # Error personalizado
    path('error/404/', views.error_404, name='error_404'),  # Error personalizado
    path('error/404/', views.error_404, name='error_404'),  # Error personalizado
    path('Propiedad_buscar/ ', views.Propiedad_buscar, name='Propiedad_buscar'), #Formulario para buscar una propiedad 
    
]
