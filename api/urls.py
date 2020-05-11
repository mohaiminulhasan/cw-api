from django.conf.urls import url

from . import views

app_name = 'api'

urlpatterns = [
    url(r'^car/data/$', views.car_data, name='car_data'),
    url(r'^bike/data/$', views.bike_data, name='bike_data'),

    url(r'^all/$', views.VehicleListView.as_view(), name='vehicles_listview'),
    url(r'^cars/$', views.CarListView.as_view(), name='car_listview'),
    url(r'^bikes/$', views.BikeListView.as_view(), name='bike_listview'),

    url(r'^brands/$', views.BrandListView.as_view(), name='brand_listview'),
    url(r'^brands/car/$', views.CarBrandListView.as_view(), name='car_brand_listview'),
    url(r'^brands/bike/$', views.BikeBrandListView.as_view(), name='bike_brand_listview'),
    url(r'^brands/(?P<brand>[\w-]+)/$', views.BrandRetrieveView.as_view(), name='brand_retrieveview'),
    url(r'^brands/(?P<brand>[\w-]+)/models/$', views.ModelListView.as_view(), name='model_listview'),
    url(r'^brands/(?P<brand>[\w-]+)/models/(?P<model>[\w-]+)/$', views.ModelRetrieveView.as_view(), name='model_retrieveview'),
    url(r'^brands/(?P<brand>[\w-]+)/models/(?P<model>[\w-]+)/variants/$', views.VariantListView.as_view(), name='variant_listview'),

    url(r'^(?P<variant>[\w-]+)/$', views.VehicleRetrieveView.as_view(), name='vehicle_retrieveview'),
    url(r'^vehicle/(?P<pk>\d+)/$', views.VehicleRetrieveWithIdView.as_view(), name='vehicle_retreive_with_id_view'),
]