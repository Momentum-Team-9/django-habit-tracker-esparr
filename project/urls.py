"""project URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.conf import settings
from django.urls import include, path, include
from core import views
from django.views.generic.dates import DateDetailView
from core.models import Habit, DailyRecord, User
from rest_framework import routers, serializers, viewsets
from api.views import DailyRecordViewSet, HabitViewSet, RecordCreateViewSet, UserViewSet


router = routers.DefaultRouter()
router.register(r'users', UserViewSet)
router.register(r'habit', HabitViewSet)
router.register(r'daily_record', DailyRecordViewSet)


urlpatterns = [
    path('admin/', admin.site.urls),
    path('accounts/', include('registration.backends.simple.urls')),
    path('api/', include(router.urls)),
    path('api/habit/<int:habit_pk>/records',
         RecordCreateViewSet.as_view(), name="api_create_record"),
    path('api/api-auth/', include('rest_framework.urls', namespace='rest_framework')),
    path("", views.index, name="index"),
    path("habits/", views.list_habits, name="list_habits"),
    path("habits/<int:pk>", views.view_habit, name="view_habit"),
    path("habits/new", views.new_habit, name="new_habit"),
    path("habits/<int:pk>/edit/", views.edit_habit, name="edit_habit"),
    path("habits/<int:pk>/delete/", views.delete_habit, name="delete_habit"),
    path("habits/<int:pk>/records/",
         views.list_records, name="list_records"),
    path("habits/<int:pk>/records/new",
         views.create_record, name='create_record'),
    path("records/<int:record_pk>/edit",
         views.edit_record, name='edit_record'),
    path('auth/', include('djoser.urls')),
    path('auth/', include('djoser.urls.authtoken')),
]

if settings.DEBUG:
    import debug_toolbar
    urlpatterns = [
        path('__debug__/', include(debug_toolbar.urls)),

        # For django versions before 2.0:
        # url(r'^__debug__/', include(debug_toolbar.urls)),
    ] + urlpatterns
