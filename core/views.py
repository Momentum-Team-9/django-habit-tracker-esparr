import core
import datetime
from django.shortcuts import render, redirect, get_object_or_404
from .models import User, Habit, DailyRecord
from .forms import DailyRecordForm, HabitForm
from django.contrib.auth.decorators import login_required
from django.db.models import Q
from django.views.generic.dates import DateDetailView

# Create your views here.


def index(request):
    users = User.objects.all()
    if request.user.is_authenticated:
        return redirect("list_habits")
    return render(request, "habits/index.html", {"users": users})


@login_required
def list_habits(request):
    habits = Habit.objects.filter()
    return render(request, "habits/list_habits.html", {"habits": habits})


@login_required
def view_habit(request, pk):
    habit = get_object_or_404(Habit, pk=pk)
    return render(
        request, "habits/view_habit.html",
        {"habit": habit, "pk": pk, "habit_pk": habit.pk}
    )


@login_required
def new_habit(request):
    if request.method == "GET":
        form = HabitForm()
    else:
        form = HabitForm(data=request.POST)
        if form.is_valid():
            habit = form.save(commit=False)
            habit.save()
            return redirect(to="list_habits")

    return render(request, "habits/new_habit.html", {"form": form})


@login_required
def edit_habit(request, pk):
    habit = get_object_or_404(Habit, pk=pk)
    if request.method == "GET":
        form = HabitForm(instance=habit)
    else:
        form = HabitForm(data=request.POST, instance=habit)
        if form.is_valid():
            form.save()
            return redirect(to="list_habits")

    return render(
        request, "habits/edit_habit.html", {
            "form": form, "habit": habit}
    )


@login_required
def delete_habit(request, pk):
    habit = get_object_or_404(Habit, pk=pk)
    if request.method == "POST":
        habit.delete()
        return redirect(to="list_habits")

    return render(request, "habits/delete_habit.html", {"habit": habit})


@login_required
def create_record(request, selected_day, habit_pk):
    if selected_day is None:
        date_record = datetime.date.today()
    else:
        date_record = datetime.datetime.strptime(
            selected_day, '%Y-%M-%d').date()

    habit = get_object_or_404(Habit, pk=habit_pk)
    daily_record = habit.daily_records.filter(
        habit_id=habit.pk).filter(date_record=selected_day)

    daily_record, _ = DailyRecord.objects.get_or_create(
        pk=habit.pk, date=date_record)

    return render(
        request,
        "habits/create_record.html",
        {
            "daily_record": daily_record,
            "habit": habit,
            "pk": habit_pk,
            "date": date_record,
        },
    )

    # if request.method == "GET":
    #     form = DailyRecordForm()
    #     daily_record, _ = DailyRecord.objects.get_or_create(
    #         pk=habit.pk, date="date")
    # else:
    #     form = DailyRecordForm(data=request.POST)
    #     if form.is_valid():
    #         daily_record = form.save(commit=False)
    #         daily_record.habit = habit
    #         daily_record.save()
    #         return redirect(to="list_habits")

    # return render(request, "habits/create_record.html", {"form": form, "daily_record": daily_record, "habit": habit, "pk": habit.pk})


@login_required
def list_records(request, pk):
    habit = get_object_or_404(Habit, pk=pk)
    daily_records = habit.daily_records.all()
    return render(request, "habits/list_records.html", {"daily_records": daily_records, "pk": pk})
