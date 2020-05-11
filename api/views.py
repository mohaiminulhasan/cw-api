import os, csv
from django.shortcuts import render
from django.http import HttpResponse
from django.conf import settings
from django.utils.text import slugify

from rest_framework.generics import ListAPIView, RetrieveAPIView
from rest_framework.filters import SearchFilter

from .serializers import VehicleSerializer, BrandSerializer, ModelSerializer, VariantSerializer

from .models import Category, VehicleType, Brand, Model, \
         Variant, CountryOfAssembly, DriveOption, Fuel, Vehicle, Dealer, \
         FrontSuspension, RearSuspension

def car_data(request):
    with open(os.path.join(settings.BASE_DIR, 'cars.csv')) as f:
        reader = csv.reader(f)
        category, created = Category.objects.get_or_create(
            slug = 'car', defaults = { 'name': 'Car' }
        )
        for row in reader:
            vehicle_type, created = VehicleType.objects.get_or_create(
                slug = slugify(row[1]), defaults = { 'name': row[1] }
            )

            brand, created = Brand.objects.get_or_create(
                slug = "{0}-{1}".format(category.slug, slugify(row[2])), defaults = { 'name': row[2], 'category': category }
            )

            model, created = Model.objects.get_or_create(
                slug = "{0}-{1}".format(brand.slug, slugify(row[3])), defaults = { 'name': row[3], 'brand': brand }
            )
            
            variant, created = Variant.objects.get_or_create(
                slug = "{0}-{1}".format(model.slug, slugify(row[4])), defaults = { 'name': row[4], 'model': model }
            )

            country_of_assembly, created = CountryOfAssembly.objects.get_or_create(
                slug = slugify(row[5]), defaults = { 'name': row[5] }
            )

            fuel_consumption = [row[6] if row[6] != '' else None][0]
            displacement = [row[7] if row[7] != '' else None][0]
            power = [row[8] if row[8] != '' else None][0]
            length = [row[9] if row[9] != '' else None][0]
            width = [row[10] if row[10] != '' else None][0]
            height = [row[11] if row[11] != '' else None][0]
            ground_clearance = [row[12] if row[12] != '' else None][0]
            seats = [row[13] if row[13] != '' else None][0]
            price = [row[14] if row[14] != '' else None][0]

            drive_option, created = DriveOption.objects.get_or_create(
                slug = slugify(row[15]), defaults = { 'name': row[15] }
            )

            fuel, created = Fuel.objects.get_or_create(
                slug = slugify(row[16]), defaults = { 'name': row[16] }
            )

            dealer, created = Dealer.objects.get_or_create(
                slug = slugify(row[17]), defaults = { 'name': row[17] }
            )

            vehicle = Vehicle.objects.create(
                category            = category,
                vehicle_type        = vehicle_type,
                brand               = brand,
                model               = model,
                variant             = variant,
                country_of_assembly = country_of_assembly,
                fuel_consumption    = fuel_consumption,
                displacement        = displacement,
                power               = power,
                length              = length,
                width               = width,
                height              = height,
                ground_clearance    = ground_clearance,
                seats               = seats,
                price               = price,
                drive_option        = drive_option,
                fuel                = fuel,
                dealer              = dealer
            )

    return HttpResponse('Car data loaded!')


def bike_data(request):
    with open(os.path.join(settings.BASE_DIR, 'bikes.csv')) as f:
        reader = csv.reader(f)
        category, created = Category.objects.get_or_create(
            slug = 'bike', defaults = { 'name': 'Bike' }
        )
        for row in reader:
            vehicle_type, created = VehicleType.objects.get_or_create(
                slug = slugify(row[1]), defaults = { 'name': row[1] }
            )

            brand, created = Brand.objects.get_or_create(
                slug = "{0}-{1}".format(category.slug, slugify(row[2])), defaults = { 'name': row[2], 'category': category }
            )

            model, created = Model.objects.get_or_create(
                slug = "{0}-{1}".format(brand.slug, slugify(row[3])), defaults = { 'name': row[3], 'brand': brand }
            )
            
            variant, created = Variant.objects.get_or_create(
                slug = "{0}-{1}".format(model.slug, slugify(row[4])), defaults = { 'name': row[4], 'model': model }
            )

            fuel_consumption = [row[5] if row[5] != '' else None][0]
            displacement = [row[6] if row[6] != '' else None][0]
            power = [row[7] if row[7] != '' else None][0]
            torque = [row[8] if row[8] != '' else None][0]
            length = [row[9] if row[9] != '' else None][0]
            width = [row[10] if row[10] != '' else None][0]
            height = [row[11] if row[11] != '' else None][0]
            ground_clearance = [row[12] if row[12] != '' else None][0]
            price = [row[13].replace(',', '') if row[13] != '' else None][0]

            front_suspension, created = FrontSuspension.objects.get_or_create(
                slug = slugify(row[14]), defaults = { 'name': row[14] }
            )

            rear_suspension, created = RearSuspension.objects.get_or_create(
                slug = slugify(row[15]), defaults = { 'name': row[15] }
            )

            front_tyre_size = [row[16] if row[16] != '' else None][0]
            rear_tyre_size = [row[17] if row[17] != '' else None][0]
            front_brake = [row[18] if row[18] != '' else None][0]
            rear_brake = [row[19] if row[19] != '' else None][0]

            dealer, created = Dealer.objects.get_or_create(
                slug = slugify(row[20]), defaults = { 'name': row[20] }
            )

            vehicle = Vehicle.objects.create(
                category            = category,
                vehicle_type        = vehicle_type,
                brand               = brand,
                model               = model,
                variant             = variant,
                fuel_consumption    = fuel_consumption,
                displacement        = displacement,
                power               = power,
                torque              = torque,
                length              = length,
                width               = width,
                height              = height,
                ground_clearance    = ground_clearance,
                price               = price,
                front_suspension    = front_suspension,
                rear_suspension     = rear_suspension,
                front_tyre_size     = front_tyre_size,
                rear_tyre_size      = rear_tyre_size,
                front_brake         = front_brake,
                rear_brake          = rear_brake,
                dealer              = dealer
            )

    return HttpResponse('Bike data loaded!')


class VehicleListView(ListAPIView):
    serializer_class = VehicleSerializer
    filter_backends = (SearchFilter,)
    search_fields = ('brand__name', 'model__name', 'variant__name')

    def get_queryset(self):
        if not self.request.query_params.get('search'):
            return Vehicle.objects.none()
        return Vehicle.objects.all()


class CarListView(ListAPIView):
    serializer_class = VehicleSerializer
    filter_backends = (SearchFilter,)
    search_fields = ('brand__name', 'model__name', 'variant__name')

    def get_queryset(self):
        if not self.request.query_params.get('search'):
            return Vehicle.objects.none()
        return Vehicle.objects.filter(category__slug='car')


class BikeListView(ListAPIView):
    serializer_class = VehicleSerializer
    filter_backends = (SearchFilter,)
    search_fields = ('brand__name', 'model__name', 'variant__name')

    def get_queryset(self):
        if not self.request.query_params.get('search'):
            return Vehicle.objects.none()
        return Vehicle.objects.filter(category__slug='bike')


class VehicleRetrieveView(RetrieveAPIView):
    queryset = Vehicle.objects.all()
    serializer_class = VehicleSerializer
    lookup_field = 'variant__slug'
    lookup_url_kwarg = 'variant'


class VehicleRetrieveWithIdView(RetrieveAPIView):
    queryset = Vehicle.objects.all()
    serializer_class = VehicleSerializer


class BrandListView(ListAPIView):
    queryset = Brand.objects.all()
    serializer_class = BrandSerializer


class CarBrandListView(ListAPIView):
    queryset = Brand.objects.filter(category__slug='car')
    serializer_class = BrandSerializer


class BikeBrandListView(ListAPIView):
    queryset = Brand.objects.filter(category__slug='bike')
    serializer_class = BrandSerializer


class BrandRetrieveView(RetrieveAPIView):
    queryset = Brand.objects.all()
    serializer_class = BrandSerializer
    lookup_field = 'slug'
    lookup_url_kwarg = 'brand'


class ModelListView(ListAPIView):
    serializer_class = ModelSerializer

    def get_queryset(self):
        return Model.objects.filter(brand__slug=self.kwargs['brand'])


class ModelRetrieveView(RetrieveAPIView):
    serializer_class = ModelSerializer
    lookup_field = 'slug'
    lookup_url_kwarg = 'model'

    def get_queryset(self):
        return Model.objects.filter(brand__slug=self.kwargs['brand'])


class VariantListView(ListAPIView):
    serializer_class = VariantSerializer

    def get_queryset(self):
        return Variant.objects.filter(model__slug=self.kwargs['model'])