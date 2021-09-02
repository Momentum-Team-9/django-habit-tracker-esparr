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
from django.urls import include, path
from core import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('accounts/', include('registration.backends.simple.urls')),
    path("", views.index, name="index"),
    path("habits/", views.list_habits, name="list_habits"),
    path("habits/<int:pk>", views.view_habit, name="view_habit"),
    path("habits/new", views.new_habit, name="new_habit"),
    path("habits/<int:pk>/edit/", views.edit_habit, name="edit_habit"),
    path("habits/<int:pk>/delete/", views.delete_habit, name="delete_habit"),
    path("habits/<int:pk>/record/", views.habit_record, name="habit_record"),
    # path("habits/<int:pk>/year/month/date/",
    #         views.date_record, name="date_record"),
]

if settings.DEBUG:
    import debug_toolbar
    urlpatterns = [
        path('__debug__/', include(debug_toolbar.urls)),

        # For django versions before 2.0:
        # url(r'^__debug__/', include(debug_toolbar.urls)),
    ] + urlpatterns
