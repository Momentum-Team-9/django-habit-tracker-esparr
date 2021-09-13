from api.serializers import HabitSerializer
from django.shortcuts import render
from rest_framework import serializers, viewsets
from rest_framework.generics import CreateAPIView
from rest_framework.decorators import action
from rest_framework.response import Response
from rest_framework.exceptions import PermissionDenied
from core.models import DailyRecord, Habit, User
from .serializers import HabitSerializer, UserSerializer, DailyRecordSerializer

# Create your views here.


class HabitViewSet(viewsets.ModelViewSet):
    queryset = Habit.objects.all()
    serializer_class = HabitSerializer

    # def get_serializer_class(self):
    #     if self.action in ["list", "records"]:
    #         return HabitSerializer
    #     return super().get_serializer_class()

    # @action(detail=False, methods=["get", "post"])
    # def records(self, request):
    #     daily_records = self.get_queryset()
    #     serializer = self.get_serializer(daily_records, many=True)
    #     return Response(serializer.data)


class DailyRecordViewSet(viewsets.ModelViewSet):
    queryset = DailyRecord.objects.all()
    serializer_class = DailyRecordSerializer


class RecordCreateViewSet(CreateAPIView):
    queryset = DailyRecord.objects.all()
    serializer_class = DailyRecordSerializer

    def perform_create(self, serializer):
        habit = Habit.objects.get(pk=self.kwargs.get('habit_pk'))
        if self.request.user is not habit.user:
            raise PermissionDenied()
        serializer.save(habit=habit)


class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer
