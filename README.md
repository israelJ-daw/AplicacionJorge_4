 templates tags:
 1 for/endfor  en todos    
 2 block/endblock en todos
 3 include  en todos
 4 empty en categorias_sin_propiedades.html
 5 {% static  'img/imagen.jpeg'  %} en principal


 

operadores:

1  {% if comentario.anonimo == True %} en plantilla_comentarios_propiedad.html

2  {% if propiedad.direccion => "Subject add media. Discussion person people however day couple. Cold type begin." %} en plantilla_detalle_categoria.html

3  {% if propiedad.precio_por_noche < 100 %} en plantilla_lista_propiedades.html

4  {% if usuario.fecha_registro|date:"Y" > "2023" %} en usuario_detalle.html

5  {% if propiedad.max_usuarios <=2 %}





10 template filtrer:

1 |capfirst en plantilla_categorias_sin_propiedades.html

2 |date:"d-m-Y" en todas las fechas

3  cut:" "  en pantilla_filtrar_reservas.html

4  time:"H:i" en plantilla_usuario_detalle.html

5 linenumbers en plantilla_lista_propiedades

6 |title en plantilla_detalle_categorias.html

7  timesince en plantilla_comentarios_propiedad.html

8 upper en plantilla_detalle_categoria.html

9 | lower en plantilla_detalle_categoria.html

10 | default:"No hay nada" en plantilla_comentario_propiedad.html