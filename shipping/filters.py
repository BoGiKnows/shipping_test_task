from django_filters import rest_framework as filters
from .models import *


class CargoFilter(filters.FilterSet):
    capacity = filters.RangeFilter()

    class Meta:
        model = Cargo
        fields = ('capacity',)