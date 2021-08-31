from core.models import DailyRecord, Habit, User
from django.contrib import admin

# Register your models here.
admin.site.register(Habit)
admin.site.register(DailyRecord)
admin.site.register(User)
