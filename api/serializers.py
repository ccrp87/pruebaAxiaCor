from rest_framework import serializers
from api.models import Franquicia,Tarjeta,Usuario

class TarjetaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Tarjeta
        fields = ('__all__')
        
class FranquiciaSerialier(serializers.ModelSerializer):
    class Meta:
        model = Franquicia
        fields = ('__all__')

class UsuarioSerializer(serializers.ModelSerializer):
    class Meta:
        model = Usuario
        fields = ('__all__')