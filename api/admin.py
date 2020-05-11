from django.contrib import admin

from .models import *

admin.site.register(Category)
admin.site.register(Brand)
admin.site.register(Model)
admin.site.register(Variant)
admin.site.register(CountryOfAssembly)
admin.site.register(VehicleType)
admin.site.register(DriveOption)
admin.site.register(Fuel)
admin.site.register(FrontSuspension)
admin.site.register(RearSuspension)
admin.site.register(Vehicle)