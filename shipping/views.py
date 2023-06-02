
from django.shortcuts import render
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import generics

from .filters import CargoFilter
from .serializers import *


class CargoCreateView(generics.CreateAPIView):
    serializer_class = CargoCreateSerializer


class CargoListView(generics.ListAPIView):
    serializer_class = CargoListSerializer
    queryset = Cargo.objects.all()
    filter_backends = (DjangoFilterBackend,)
    filterset_class = CargoFilter
    filter_fields = ('capacity',)


class CargoDetailView(generics.RetrieveAPIView):
    serializer_class = CargoDetailSerializer
    queryset = Cargo.objects.all()


class CargoUpdateView(generics.RetrieveUpdateAPIView):
    serializer_class = CargoUpdateSerializer
    queryset = Cargo.objects.all()


class CargoDeleteView(generics.RetrieveDestroyAPIView):
    serializer_class = CargoDeleteSerializer
    queryset = Cargo.objects.all()
    #
    # def get_queryset(self):
    #     return Cargo.objects.get(pk=self.kwargs['pk'])


class CarCreateView(generics.CreateAPIView):
    serializer_class = CarCreateSerializer


class CarDetailView(generics.RetrieveUpdateAPIView):
    serializer_class = CarDetailSerializer
    queryset = Car.objects.all()

