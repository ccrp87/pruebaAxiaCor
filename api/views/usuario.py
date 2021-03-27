from django.shortcuts import render
from rest_framework import viewsets
from api.models import Usuario, Tarjeta
from api.serializers import UsuarioSerializer, TarjetaSerializer
from rest_framework import status
from rest_framework.response import Response
import re, uuid
from rest_framework.views import APIView
from django.core.mail import send_mail
from rest_framework.decorators import api_view


class UsuarioAPIView(APIView):
    def post(self,request):
        serializer = UsuarioSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        usuario = serializer.create(serializer.validated_data)
        if usuario:
            host = 'http://localhost/api/usuario/'+ str(usuario.token_verificacion+'/verify')
            mensaje = "Registro exitoso, para activar la cuenta de usuario debe hacer click en el siguiente enlace: <a href='"+host+"'>Click</a>"
            send_mail('Registro exitoso','','info@3itc.co', [usuario.correo], fail_silently=False,html_message=mensaje)
            return Response({'uuid':usuario.token_verificacion,'fecha_creacion':usuario.fecha_creacion}, status=status.HTTP_201_CREATED)
        else:
            return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)
    def get(self,request):
        pass

    @api_view(http_method_names=['GET'])    
    def verify_user(request,token):
        
        try:
            usuario = Usuario.objects.get(token_verificacion=token)
            usuario.vericado = True
            usuario.token_verificacion = uuid.uuid4
            usuario.save()
            return Response({'mensaje':'Usuario activado correctamente'},status=status.HTTP_202_ACCEPTED)
        except Usuario.DoesNotExist:
            return Response({'mensaje':'el usuario no existe'},status=status.HTTP_400_BAD_REQUEST)
            
        


 