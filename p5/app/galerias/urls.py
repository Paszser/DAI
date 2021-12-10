from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('test_template', views.test_template, name="test_template"),
    path('loginPage', views.loginPage, name="loginPage"),
    path('registerPage', views.registerPage, name="registerPage"),
    path('logoutUser', views.logoutUser, name="logoutUser"),
    path('listarGalerias', views.listarGalerias, name="listarGalerias"),
    path('anadirGaleria', views.anadirGaleria, name="anadirGaleria"),
    path('procesarAnadir', views.procesarAnadir, name="procesarAnadir"),
    path('galeriaEdit/<id_galeria>', views.edit, name="galeriaEdit"),
    path('actualizarGaleria/<id_galeria>', views.actualizarGaleria, name="actualizarGaleria"),
    path('eliminarGaleria/<id_galeria>', views.delete, name="eliminarGaleria"),
    path('listarCuadros', views.listarCuadros, name="listarCuadros"),
    path('anadirCuadro', views.anadirCuadro, name="anadirCuadro"),
    path('procesarAnadirCuadro', views.procesarAnadirCuadro, name="procesarAnadirCuadro"),
    path('cuadroEdit/<int:id_cuadro>', views.editCuadro, name="cuadroEdit"),
    path('actualizarCuadro/<int:id_cuadro>', views.actualizarCuadro, name="actualizarCuadro"),
    path('eliminarCuadro/<int:id_cuadro>', views.deleteCuadro, name="eliminarCuadro"),
]