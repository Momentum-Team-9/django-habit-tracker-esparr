from django.shortcuts import render
from rest_framework import serializers, viewsets
from core.models import Habit

# Create your views here.


class HabitViewSet(viewsets.ModelViewSet):
    queryset = Habit.objects.all()
    serializer_class = HabitSerializer
