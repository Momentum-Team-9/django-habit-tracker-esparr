from core.models import Habit, DailyRecord, User
from rest_framework import serializers


class DailyRecordSerializer(serializers.ModelSerializer):

    class Meta:
        model = DailyRecord
        fields = ("date", "note",)


class HabitSerializer(serializers.ModelSerializer):
    daily_records = DailyRecordSerializer(many=True, read_only=False)

    class Meta:
        model = Habit
        fields = (
            "pk",
            "title",
            "goal",
            "created_at",
            "daily_records",
        )


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['url', 'username', 'email', 'is_staff']


# class RecordSerializer(serializers.ModelSerializer):
#     habit = HabitSerializer(read_only=)

#     class Meta:
#         model = DailyRecord
#         fields = ("habit", "date", "note",)
