from django import forms
from .models import Usuario, Perfil, Categoria, ServicioExtra, Propiedad, Reserva, Comentario, Pago

class UsuarioForm(forms.ModelForm):
    class Meta:
        model = Usuario
        fields = ['nombre', 'email', 'telefono']  # No incluimos `id` ni `fecha_registro` porque se generan automáticamente.
        widgets = {
            'nombre': forms.TextInput(attrs={'class': 'form-control'}),
            'email': forms.EmailInput(attrs={'class': 'form-control'}),
            'telefono': forms.TextInput(attrs={'class': 'form-control'}),
        }

class PerfilForm(forms.ModelForm):
    class Meta:
        model = Perfil
        fields = ['genero', 'edad', 'ubicacion', 'biografia']
        widgets = {
            'genero': forms.TextInput(attrs={'class': 'form-control'}),
            'edad': forms.NumberInput(attrs={'class': 'form-control'}),
            'ubicacion': forms.Textarea(attrs={'class': 'form-control'}),
            'biografia': forms.Textarea(attrs={'class': 'form-control'}),
        }

class CategoriaForm(forms.ModelForm):
    class Meta:
        model = Categoria
        fields = ['nombre', 'descripcion', 'premiun', 'principal']
        widgets = {
            'nombre': forms.TextInput(attrs={'class': 'form-control'}),
            'descripcion': forms.Textarea(attrs={'class': 'form-control'}),
        }

class ServicioExtraForm(forms.ModelForm):
    class Meta:
        model = ServicioExtra
        fields = ['nombre', 'descripcion', 'precio', 'disponible']
        widgets = {
            'nombre': forms.TextInput(attrs={'class': 'form-control'}),
            'descripcion': forms.Textarea(attrs={'class': 'form-control'}),
            'precio': forms.NumberInput(attrs={'class': 'form-control'}),
        }

class PropiedadForm(forms.ModelForm):
    class Meta:
        model = Propiedad
        fields = ['titulo', 'direccion', 'precio_por_noche', 'max_usuarios', 'usuario', 'categoria', 'servicios_extra']
        widgets = {
            'titulo': forms.TextInput(attrs={'class': 'form-control', 'readonly': 'readonly'}),
            'direccion': forms.TextInput(attrs={'class': 'form-control'}),
            'precio_por_noche': forms.NumberInput(attrs={'class': 'form-control'}),
            'max_usuarios': forms.NumberInput(attrs={'class': 'form-control'}),
            'usuario': forms.Select(attrs={'class': 'form-control'}),
            'categoria': forms.CheckboxSelectMultiple(),
            'servicios_extra': forms.CheckboxSelectMultiple(),
        }

class ReservaForm(forms.ModelForm):
    class Meta:
        model = Reserva
        fields = ['fecha_inicio', 'fecha_fin', 'total', 'estado', 'pago', 'perfil']
        widgets = {
            'fecha_inicio': forms.DateInput(attrs={'class': 'form-control', 'type': 'date'}),
            'fecha_fin': forms.DateInput(attrs={'class': 'form-control', 'type': 'datetime-local'}),
            'total': forms.NumberInput(attrs={'class': 'form-control'}),
            'estado': forms.TextInput(attrs={'class': 'form-control'}),
            'pago': forms.Select(attrs={'class': 'form-control'}),
            'perfil': forms.Select(attrs={'class': 'form-control'}),
        }

class ComentarioForm(forms.ModelForm):
    class Meta:
        model = Comentario
        fields = ['contenido', 'valoracion', 'anonimo', 'propiedad']
        widgets = {
            'contenido': forms.Textarea(attrs={'class': 'form-control'}),
            'valoracion': forms.NumberInput(attrs={'class': 'form-control'}),
            'anonimo': forms.CheckboxInput(attrs={'class': 'form-check-input'}),
            'propiedad': forms.Select(attrs={'class': 'form-control'}),
        }

class PagoForm(forms.ModelForm):
    class Meta:
        model = Pago
        fields = ['total', 'metodo_pago', 'cod_transaccion']
        widgets = {
            'total': forms.NumberInput(attrs={'class': 'form-control'}),
            'metodo_pago': forms.TextInput(attrs={'class': 'form-control'}),
            'cod_transaccion': forms.TextInput(attrs={'class': 'form-control'}),
        }
