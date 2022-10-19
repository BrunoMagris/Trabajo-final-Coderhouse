from django.urls import URLPattern, path
from .views import *
from django.contrib.auth.views import LogoutView

urlpatterns = [
    path("restaurantes/", RestauranteList.as_view(), name='LeerResaurantes'),
    path("restaurantes/nuevo/", RestauranteCrear.as_view(), name='CrearResaurantes'),
    path("restaurantes/<int:pk>", RestauranteDetalle.as_view(), name='DetalleResaurantes'),
    path("restaurantes/editar/<int:pk>", RestauranteUpdate.as_view(), name='UpdateResaurantes'),
    path("restaurantes/borrar/<int:pk>", RestauranteBorrar.as_view(), name='BorrarResaurantes'),
    path("", inicio, name='Inicio'),
    path("registro/", registro, name='Registro'),
    path("editarUsuarios/", editarUsuario, name='editarUsuarios'),
    path("logout",LogoutView.as_view(template_name = "App1/logout.html"), name='Logout'),
    path("login/", iniciar_sesion, name='Login'),
    path("buscarRestaurantes/", busquedaRestaurantes),
    path("buscar/", buscar),
    path("home/", home, name= 'Home'),

    path("recomendaciones/", RecomendacionesList.as_view(), name='LeerRecomendaciones'),
    path("recomendaciones/nuevo/", RecomendacionesCrear.as_view(), name='CrearRecomendaciones'),
    path("recomendaciones/<int:pk>", RecomendacionesDetalle.as_view(), name='DetalleRecomendaciones'),
    path("recomendaciones/editar/<int:pk>", RecomendacionesUpdate.as_view(), name='UpdateRecomendaciones'),
    path("recomendaciones/borrar/<int:pk>", RecomendacionesBorrar.as_view(), name='BorrarRecomendaciones'),

]