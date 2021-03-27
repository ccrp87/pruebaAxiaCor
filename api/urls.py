from django.urls import path, include
from rest_framework import routers
from api.views.tarjeta import TarjetaAPIView,FranquiciaViewSet
from api.views.usuario import UsuarioAPIView


urlpatterns = [
    # path('',include(router.urls)),
    path('tarjeta/',TarjetaAPIView.as_view()),
    path('tarjeta/<str:uuid>',TarjetaAPIView.as_view()),
    path('tarjeta/asociar_tarjeta/',TarjetaAPIView.asociar_tarjeta_usuario),
    path('usuario/',UsuarioAPIView.as_view()),
    path('usuario/<str:uuid>',UsuarioAPIView.as_view()),
    path('usuario/<str:token>/verify',UsuarioAPIView.verify_user)

    ]