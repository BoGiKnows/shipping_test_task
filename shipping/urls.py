from django.urls import path
from .views import *

urlpatterns = [
    path('cargo/create/', CargoCreateView.as_view(), name='cargo_create'),
    path('cargo/list/', CargoListView.as_view(), name='cargo_list'),
    path('cargo/detail/<int:pk>/', CargoDetailView.as_view(), name='cargo_detail'),
    path('cargo/update/<int:pk>/', CargoUpdateView.as_view(), name='cargo_update'),
    path('cargo/delete/<int:pk>/', CargoDeleteView.as_view(), name='cargo_delete'),
    path('car/create/', CarCreateView.as_view(), name='car_create'),
    path('car/detail/<int:pk>/', CarDetailView.as_view(), name='car_detail'),
]