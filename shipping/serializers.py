import random
import string
from geopy import distance

from rest_framework import serializers
from .models import *


class CargoCreateSerializer(serializers.ModelSerializer):
    delivery_loc = serializers.IntegerField(label='delivery location ZIP')
    pick_up_loc = serializers.IntegerField(label='pick up location ZIP')

    class Meta:
        model = Cargo
        fields = ('pick_up_loc', 'delivery_loc', 'capacity', 'description')

    def create(self, validated_data):
        delivery_loc = Location.objects.get(zip=validated_data['delivery_loc'])
        pick_up_loc = Location.objects.get(zip=validated_data['pick_up_loc'])
        Cargo.objects.create(
            pick_up_loc=pick_up_loc,
            delivery_loc=delivery_loc,
            capacity=int(validated_data['capacity']),
            description=validated_data['description']
        )
        return validated_data


class CargoListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Cargo
        fields = '__all__'

    def to_representation(self, instance):
        ret = super().to_representation(instance)
        instance_loc = (instance.pick_up_loc.lat, instance.pick_up_loc.lon)  # lat, lon
        cars = Car.objects.all().select_related('location')
        count = 0
        for car in cars:
            car_loc = (car.location.lat, car.location.lon)
            dist = distance.distance(instance_loc, car_loc).miles
            if dist <= 450:
                count += 1
        ret['cars_near'] = count
        return ret


class CargoDetailSerializer(serializers.ModelSerializer):
    car_list = serializers.SerializerMethodField()

    class Meta:
        model = Cargo
        fields = '__all__'

    def get_car_list(self, obj):
        obj_loc = obj.pick_up_loc.lat, obj.pick_up_loc.lon
        cars = Car.objects.all().select_related('location')
        car_near = []
        for car in cars:
            car_loc = (car.location.lat, car.location.lon)
            dist = distance.distance(obj_loc, car_loc).miles
            car_near.append({car.plate: dist})
        return car_near


class CargoUpdateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Cargo
        fields = ('capacity', 'description')


class CargoDeleteSerializer(serializers.ModelSerializer):
    class Meta:
        model = Cargo
        fields = ('id',)


class CarCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Car
        fields = ('capacity',)

    def create(self, validated_data):
        capacity = validated_data['capacity']
        plate_number = 1000 if not Car.objects.last() else int(Car.objects.last().plate[:-1]) + 1
        plate_letter = random.choice(string.ascii_uppercase)
        plate = str(plate_number) + plate_letter
        rand_loc_id = random.randint(1, Location.objects.last().pk)
        location = Location.objects.get(pk=rand_loc_id)
        car = Car.objects.create(plate=plate, location=location, capacity=capacity)
        return car


class LocationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Location
        fields = "__all__"


class CarDetailSerializer(serializers.ModelSerializer):
    location = serializers.IntegerField(label='location ZIP', source='location.zip')

    class Meta:
        model = Car
        fields = '__all__'

    def update(self, instance, validated_data):
        instance.location = Location.objects.get(zip=validated_data['location']['zip']) if validated_data[
            'location'] else instance.location
        instance.plate = validated_data.get('plate', instance.plate)
        instance.capacity = validated_data.get('capacity', instance.capacity)
        instance.save()
        return instance
