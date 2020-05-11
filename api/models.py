import os
from django.db import models
from django.utils.text import slugify
from django.utils.deconstruct import deconstructible
from .storage import OverwriteStorage

from utils.models import Timestamp, NameMixin


class Category(NameMixin):
    pass

class Brand(NameMixin):
    category = models.ForeignKey(Category, on_delete=models.CASCADE)

class Model(Timestamp):
    brand = models.ForeignKey(Brand, on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    slug = models.SlugField(max_length=100)
    
    def __str__(self):
        return "{brand} {model}".format(
            brand=self.brand,
            model=self.name
        )
    
    class Meta:
        unique_together = ('brand', 'slug')

class Variant(NameMixin):
    model = models.ForeignKey(Model, on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    slug = models.SlugField(max_length=100)
    
    def __str__(self):
        return "{model} {variant}".format(
            model=self.model,
            variant=self.name
        )
    
    # def save(self, *args, **kwargs):
    #     self.slug = "{model}-{variant}".format(model=self.model.id, variant=slugify(self.name))
    #     super().save(*args, **kwargs)
    
    class Meta:
        unique_together = ('model', 'slug')

class CountryOfAssembly(NameMixin):
    pass

class VehicleType(NameMixin):
    pass

class Dealer(NameMixin):
    pass

@deconstructible
class UploadToPathAndRename(object):

    def __init__(self, path):
        self.sub_path = path

    def __call__(self, instance, filename):
        ext = filename.split('.')[-1]
        # get filename
        if instance.variant.slug:
            filename = '{}.{}'.format(instance.variant.slug, ext)
        # else:
        #     # set filename as random string
        #     filename = '{}.{}'.format(uuid4().hex, ext)
        # return the whole path to the file
        return os.path.join(self.sub_path, filename)

class VehicleBase(Timestamp):
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    vehicle_type = models.ForeignKey(VehicleType, on_delete=models.CASCADE)
    brand = models.ForeignKey(Brand, on_delete=models.CASCADE)
    model = models.ForeignKey(Model, on_delete=models.CASCADE)
    variant = models.ForeignKey(Variant, on_delete=models.CASCADE)
    country_of_assembly = models.ForeignKey(CountryOfAssembly, on_delete=models.CASCADE, blank=True, null=True)
    fuel_consumption = models.FloatField(blank=True, null=True)
    displacement = models.FloatField(blank=True, null=True)
    power = models.FloatField(blank=True, null=True)
    length = models.FloatField(blank=True, null=True)
    width = models.FloatField(blank=True, null=True)
    height = models.FloatField(blank=True, null=True)
    ground_clearance = models.FloatField(blank=True, null=True)
    price = models.FloatField(blank=True, null=True)
    dealer = models.ForeignKey(Dealer, on_delete=models.CASCADE, blank=True, null=True)
    image = models.ImageField(upload_to=UploadToPathAndRename('vehicles/'), default='vehicle_default.png', storage=OverwriteStorage())

    class Meta:
        abstract = True


class DriveOption(NameMixin):
    pass

class Fuel(NameMixin):
    pass

class Car(models.Model):
    seats = models.PositiveIntegerField(blank=True, null=True)
    drive_option = models.ForeignKey(DriveOption, on_delete=models.CASCADE, blank=True, null=True)
    fuel = models.ForeignKey(Fuel, on_delete=models.CASCADE, blank=True, null=True)

    class Meta:
        abstract = True

class FrontSuspension(NameMixin):
    pass

class RearSuspension(NameMixin):
    pass

class Bike(models.Model):
    torque = models.FloatField(blank=True, null=True)
    front_suspension = models.ForeignKey(FrontSuspension, on_delete=models.CASCADE, blank=True, null=True)
    rear_suspension = models.ForeignKey(RearSuspension, on_delete=models.CASCADE, blank=True, null=True)
    front_tyre_size = models.CharField(max_length=100, blank=True, null=True)
    rear_tyre_size = models.CharField(max_length=100, blank=True, null=True)
    front_brake = models.CharField(max_length=100, blank=True, null=True)
    rear_brake = models.CharField(max_length=100, blank=True, null=True)

    class Meta:
        abstract = True


class Vehicle(VehicleBase, Car, Bike):
    pass

    class Meta:
        unique_together = ('category', 'variant')
    
    def __str__(self):
        return "{vehicle_type} : {brand} {model} {variant}".format(
            vehicle_type=self.vehicle_type,
            brand=self.brand,
            model=self.model,
            variant=self.variant
        )
