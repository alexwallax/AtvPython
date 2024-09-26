from receitas.models import Receitas
from rest_framework import serializers

class ReceitasSerializers(serializers.ModelSerializer):
    class Meta:
        model = Receitas
        fields = '__all__' 
 

    
