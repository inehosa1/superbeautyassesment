from rest_framework import  serializers
from inventory.models import Equipment

# Serializers define the API representation.
class EquipmentSerializer(serializers.ModelSerializer):
    """
    Seralizador para equipos 
    """
    
    class Meta:
        model = Equipment
        fields = "__all__"