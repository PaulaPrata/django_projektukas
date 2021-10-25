from django.db import models
from django.urls import reverse

class Service(models.Model):
    name = models.CharField(verbose_name='service', max_length=200)
    price = models.FloatField(verbose_name='price')

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Service'
        verbose_name_plural = 'Services'

class CarModel(models.Model):
    manufacturer = models.CharField(verbose_name='Manufacturer', max_length=200)
    model = models.CharField(verbose_name='Model', max_length=200)

    def __str__(self):
        return f"{self.manufacturer} {self.model}"

    class Meta:
        verbose_name = 'Car Model'
        verbose_name_plural = 'Car Models'


class Car(models.Model):
    owner = models.CharField(verbose_name="Owner", null=True, max_length=200)
    car_model = models.ForeignKey('CarModel', verbose_name="Model", on_delete=models.SET_NULL, null=True)
    licence_plate = models.CharField(verbose_name='Licence plate', max_length=200)
    vin_code = models.CharField(verbose_name='VIN code', max_length=200)

    def __str__(self):
        return f"{self.owner} {self.car_model}{self.licence_plate}{self.vin_code}"
    class Meta:
        verbose_name = 'Car'
        verbose_name_plural = 'Cars'

class Order(models.Model):
    due_date = models.DateTimeField(verbose_name='Due Date', null=True, blank=True)
    car = models.ForeignKey('Car', verbose_name='Car', on_delete=models.SET_NULL, null=True)


    def __str__(self):
        return f"{self.due_date} {self.car}"

    class Meta:
        verbose_name = 'Order'
        verbose_name_plural = 'Orders'


class Order_line(models.Model):
    order_id = models.ForeignKey("Order", verbose_name='order_id',on_delete=models.SET_NULL, null=True, related_name='lines')
    service = models.ForeignKey('Service', verbose_name='Service', on_delete=models.SET_NULL, null=True)
    quantity = models.IntegerField( verbose_name='quantity', null=True)

    def __str__(self):
        return f"{self.order_id} {self.service}{self.quantity}"
    class Meta:
        verbose_name = 'Order Line'
        verbose_name_plural = 'Order Lines'
