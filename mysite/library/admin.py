from django.contrib import admin
from .models import CarModel, Car, Service, Order, Order_line

class OrderLineInline(admin.TabularInline):
    model =Order_line

class OrderAdmin(admin.ModelAdmin):
    inlines = [OrderLineInline]
    list_display = ('car', 'due_date')

class CarAdmin(admin.ModelAdmin):
    list_display = ('owner', 'car_model', 'licence_plate', 'vin_code')
    list_filter = ('owner', 'car_model')
    search_fields = ('licence_plate', 'vin_code')

class ServiceAdmin(admin.ModelAdmin):
    list_display = ('name', 'price')

admin.site.register(Service)
admin.site.register(CarModel)
admin.site.register(Car, CarAdmin)
admin.site.register(Order, OrderAdmin)
admin.site.register(Order_line)

