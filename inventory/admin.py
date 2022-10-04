from django.contrib import admin
from inventory.models import Equipment, UserEquipment

@admin.register(Equipment)
class EquipmentAdmin(admin.ModelAdmin):
    list_display = ('reference', 'brand', 'processor', 'memory', 'disk', "type")
    

@admin.register(UserEquipment)
class EquipmentAdmin(admin.ModelAdmin):
    list_display = ('user', 'equipment', 'date_assignment', 'date_delivery')
    list_filter = ('date_assignment', 'user__username')