# coding=utf-8
from __future__ import unicode_literals
from django.conf import settings
from django.db import models
from django.contrib.auth.models import User
from django.core.validators import MaxValueValidator


# Create your models here.
class ProviderCatalog(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL)
    name = models.CharField("nombre", max_length=40)
    RFC = models.CharField(max_length=13, blank=True, null=True)
    registry_date = models.DateTimeField("fecha registro", auto_now=True)
    facture_name = models.CharField("Nombre facturación", max_length=40, blank=True, null=True)
    email = models.EmailField("email", blank=True, null=True)
    web = models.CharField("Pagina web", max_length=200, blank=True, null=True)
    telephone = models.CharField("Teléfono", blank=True, null=True, max_length=30)

    class Meta(object):
        verbose_name_plural = 'Catalogo de proveedores'

    def __str__(self):
        return self.name


class PaymentCatalog(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL)
    payment_type = models.CharField("forma de pago", max_length=30)
    description = models.CharField("descripcion", max_length=80)

    class Meta(object):
        verbose_name_plural = 'Forma de pagos'

    def __str__(self):
        return self.payment_type


class ProducerCatalog(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL)
    producer = models.CharField("productor", max_length=40, blank=True, null=True)
    country = models.CharField("país", max_length=40)

    class Meta(object):
        verbose_name_plural = 'Catalogo de productores'

    def __str__(self):
        return self.producer


class ProductCatalog(models.Model):
    MALE = 'M'
    FEMALE = 'F'
    SEX_CHOICE = (
        (MALE, 'Hombre'),
        (FEMALE, 'Mujer')
    )

    user = models.ForeignKey(settings.AUTH_USER_MODEL)
    slug = models.SlugField()  # etiqueta para url amigables
    product_name = models.CharField("nombre del producto", max_length=80)
    patent = models.CharField("marca", max_length=80, null=True, blank=True)  # Marca
    series = models.CharField("serie", max_length=20, null=True, blank=True)
    origin = models.CharField("origen", max_length=20, null=True, blank=True)  # origen
    net = models.DecimalField("contenido", max_digits=6, decimal_places=2)  # contenido neto
    measure = models.DecimalField("medida", max_digits=6, decimal_places=2)  # medida
    barcode = models.IntegerField("código de barras", validators=[MaxValueValidator(999999999999999), ], blank=True,
                                  null=True
                                  )
    producer = models.ForeignKey(ProducerCatalog)
    provider = models.ForeignKey(ProviderCatalog)

    class Meta(object):
        verbose_name_plural = 'Catalogo de productos'

    def __str__(self):
        return '%s %s' % (self.product_name, self.patent)


class Store(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL)
    name = models.CharField("nombre", max_length=40)
    description = models.CharField("descripción", max_length=120, blank=True, null=True)

    class Meta(object):
        verbose_name_plural = 'Almacén'

    def __str__(self):
        return self.name


class Inventory(models.Model):
    store = models.ForeignKey(Store)
    product = models.ForeignKey(ProductCatalog)
    quantity = models.DecimalField("cantidad", max_digits=6, decimal_places=2)
    entry = models.DecimalField("entradas", max_digits=6, decimal_places=2)
    date_entry = models.DateTimeField("Fecha de entrada", auto_now=True)
    user = models.OneToOneField(User)
    out = models.DecimalField("salidas", max_digits=6, decimal_places=2)
    entry_price = models.DecimalField("precio entrada", max_digits=6, decimal_places=2)
    out_price = models.DecimalField("precio salida", max_digits=6, decimal_places=2)
    percent_desc = models.IntegerField("porcentaje oferta", validators=[MaxValueValidator(99), ])

    class Meta(object):
        verbose_name_plural = 'Inventario'

    def __str__(self):
        return self.store


class EntryOrder(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL)
    provider = models.ForeignKey(ProviderCatalog)
    payment = models.ForeignKey(PaymentCatalog)
    store = models.ForeignKey(Store)
    order_ref = models.CharField("referencia", max_length=20)
    date_order = models.DateTimeField("fecha", auto_now=True)
    total_price = models.DecimalField("precio total", max_digits=6, decimal_places=2)
    entry_date = models.DateTimeField("fecha entrega")
    payment_order = models.BooleanField("pagado", default=False)
    entry = models.BooleanField("entregado", default=False)

    class Meta(object):
        verbose_name_plural = 'Pedido'

    def __str__(self):
        return self.id


class EntryOrderDetail(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL)
    order_ref = models.ForeignKey(EntryOrder)
    product = models.ForeignKey(ProductCatalog)
    quantity_order = models.DecimalField("cantidad ordenada", max_digits=6, decimal_places=2)
    piece_price = models.DecimalField("precio unidad", max_digits=6, decimal_places=2)

    class Meta(object):
        verbose_name_plural = 'Detalle de Pedido'

    def __str__(self):
        return self.order_ref


class OutOrder(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL)
    order_ref = models.CharField("referencia", max_length=20)
    client = models.CharField("cliente", max_length=30)
    payment = models.OneToOneField(PaymentCatalog)
    store = models.OneToOneField(Store)
    date_order = models.DateTimeField("fecha orden", auto_now=True)
    total_price = models.DecimalField("precio total", max_digits=6, decimal_places=2)
    entry_date = models.DateTimeField("fecha venta")
    payment_order = models.BooleanField("pagado", default=False)
    entry = models.BooleanField("entregado", default=False)
    description = models.CharField("descripción", max_length=80)

    class Meta(object):
        verbose_name_plural = 'Salida de producto'

    def __str__(self):
        return self.id


class OutOrderDetail(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL)
    order_ref = models.ForeignKey(OutOrder)
    product = models.OneToOneField(ProductCatalog)
    quantity_order = models.DecimalField("cantidad vendidas", max_digits=6, decimal_places=2)
    piece_price = models.DecimalField("precio unidad", max_digits=6, decimal_places=2)

    class Meta(object):
        verbose_name_plural = 'Detalle de salida de producto'

    def __str__(self):
        return self.order_ref


class Sales(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL)
    cash = models.CharField("caja", max_length=40)
    date_sale = models.DateTimeField("fecha venta", auto_now=True)
    total = models.DecimalField("total", max_digits=6, decimal_places=2)
    payment = models.ForeignKey(PaymentCatalog)

    class Meta(object):
        verbose_name_plural = 'Ventas'

    def __str__(self):
        return self.id


class SalesDetail(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL)
    sale = models.ForeignKey(Sales)
    quantity = models.DecimalField("cantidad", max_digits=6, decimal_places=2)
    amount = models.DecimalField("precio", max_digits=6, decimal_places=2)
    product = models.ForeignKey(ProductCatalog)

    class Meta(object):
        verbose_name_plural = 'Detalle de venta'

    def __str__(self):
        return self.sale
