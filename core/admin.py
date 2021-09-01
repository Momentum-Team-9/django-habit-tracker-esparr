from core.models import DailyRecord, Habit, User
from django.contrib import admin

# Register your models here.


@admin.register(Habit)
class HabitAdmin(admin.ModelAdmin):
    pass


@admin.register(DailyRecord)
class DailyRecordAdmin(admin.ModelAdmin):
    pass


@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    pass
