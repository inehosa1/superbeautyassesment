from inventory.views import ListEquipments
from django.urls import path

urlpatterns = [
    path('', ListEquipments.as_view()),
]
