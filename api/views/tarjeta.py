from django.shortcuts import render
from rest_framework import viewsets
from api.models import Franquicia, Tarjeta, Usuario
from api.serializers import FranquiciaSerialier, TarjetaSerializer
from rest_framework import status
from rest_framework.response import Response
import re, uuid, rsa
from datetime import date
from rest_framework.views import APIView
from rest_framework.decorators import api_view
from cryptography.fernet import Fernet

class TarjetaAPIView(APIView):
    queryset = Tarjeta.objects.all()
    serializer_class = TarjetaSerializer
    fields = ('__all__')

    def delete(self, request, uuid, format=None):
        try:
            Tarjeta.objects.get(uuid=uuid).delete()
            return Response({'mensaje':'tarjeta eliminada'}, status=status.HTTP_200_OK)
        except Tarjeta.DoesNotExist:
            return Response({'mensaje':'La tarjeta no existe'}, status=status.HTTP_404_NOT_FOUND)

    def get(self, request, uuid, format=None):
        tarjeta = Tarjeta.objects.get(uuid=uuid)
        seralizer = TarjetaSerializer(tarjeta,many=False)
        return Response(seralizer.data)

    def post(self, request, *args, **kwargs):
        data = request.data
        if self.luhn_checksum(data['numero']):
      
            franquicia = self.get_franquicia(data['numero'])
            if franquicia:
                tarjeta = Tarjeta(franquiciaid=franquicia,token=uuid.uuid4,uuid=uuid.uuid4(),fecha_creacion=None,fecha_vencimiento=data['fecha_vencimiento'])
                tarjeta.save()
             
                primeros6numeros = data['numero'][:6]
                ultimos4numeros = data['numero'][-4:]
                return Response({'franquicia':franquicia.nombre,'ultimos4numeros':ultimos4numeros,'primeros6numeros':primeros6numeros,'fecha_vencimineto':data['fecha_vencimiento'],'uuid':tarjeta.uuid,'fecha_creacion':tarjeta.fecha_creacion}, status=status.HTTP_201_CREATED)

            else:
                return Response({'mensaje':'Franquicia inválida'}, status=status.HTTP_404_NOT_FOUND)
        else:
            return Response({'mensaje':'Número de tarjeta invalido'}, status=status.HTTP_404_NOT_FOUND)

    @api_view(http_method_names=['POST'])    
    def asociar_tarjeta_usuario(request):
        data = request.data

        try:
            usuario = Usuario.objects.get(id=data['usuarioid'])
            try:
                tarjeta = Tarjeta.objects.get(uuid=data['tarjetauuid'])
                message = usuario.uuid.hex + "#" +tarjeta.uuid.hex
                key = Fernet.generate_key()
                fernet = Fernet(key)
                encMessage = fernet.encrypt(message.encode())
                tarjeta.token = encMessage
                tarjeta.usuarioid = usuario
                tarjeta.token_fecha_creacion = date.today()
                tarjeta.save()
                return Response({'token':tarjeta.token,'fecha_creacion':tarjeta.token_fecha_creacion})

            except Tarjeta.DoesNotExist:
                return Response({"mensaje":"tarjeta invalida"})
        except Usuario.DoesNotExist:
            return Response({"mensaje":"usuario invalido"},status=status.HTTP_404_NOT_FOUND)
            

      
        
    def get_franquicia(self, numero):
       for franquicia in Franquicia.objects.all():
            if re.match(franquicia.expression,numero):
                return franquicia

    def luhn_checksum(self, card_number):
        def digits_of(n):
            return [int(d) for d in str(n)]
        digits = digits_of(card_number)
        odd_digits = digits[-1::-2]
        even_digits = digits[-2::-2]
        checksum = 0
        checksum += sum(odd_digits)
        for d in even_digits:
            checksum += sum(digits_of(d*2))
        if(checksum % 10 == 0):
            return True
        else:
            return False    





class FranquiciaViewSet(viewsets.ModelViewSet):
    queryset = Franquicia.objects.all()
    serializer_class = FranquiciaSerialier
    fields = ('__all__')