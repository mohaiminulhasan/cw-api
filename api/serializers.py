from rest_framework import serializers

from .models import Vehicle, Brand, Model, Variant, Category

class VehicleSerializer(serializers.ModelSerializer):
    category = serializers.StringRelatedField()
    variant = serializers.StringRelatedField()
    country_of_assembly = serializers.StringRelatedField()
    dealer = serializers.StringRelatedField()
    slug = serializers.SlugRelatedField(slug_field='variant', read_only=True)
    vehicle_type = serializers.StringRelatedField()

    class Meta:
        model = Vehicle
        fields = ('__all__')


class BrandSerializer(serializers.ModelSerializer):
    class Meta:
        model = Brand
        fields = ('name', 'slug')


class ModelSerializer(serializers.ModelSerializer):
    class Meta:
        model = Model
        fields = ('name', 'slug')


class VariantSerializer(serializers.ModelSerializer):
    class Meta:
        model = Variant
        fields = ('name', 'slug')