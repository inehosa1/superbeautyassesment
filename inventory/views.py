from rest_framework.views import APIView
from rest_framework.response import Response
from inventory.models import Equipment
from django.forms.models import model_to_dict
from inventory.serializer import EquipmentSerializer

class ListEquipments(APIView):
    """
    Vista para consultar la lista de los equipos
    """    
    
    def get(self, request):
        """
        Retorna la lista de equipos
        """         
        queryset = Equipment.objects.all()
        serializer = EquipmentSerializer(queryset, many=True)
        return Response(serializer.data)