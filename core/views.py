import core
import datetime
from django.shortcuts import render, redirect, get_object_or_404
from .models import User, Habit, DailyRecord
from .forms import DailyRecordForm, HabitForm
from django.contrib.auth.decorators import login_required
from django.db.models import Q

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
        {"habit": habit, "pk": pk}
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
def create_record(request, habit_pk, year=None, month=None, day=None):

    if year is None:
        date_for_record = datetime.date.today()
    else:
        date_for_record = datetime.date(year, month, day)
    next_day = date_for_record + datetime.timedelta(days=1)
    prev_day = date_for_record + datetime.timedelta(days=-1)

    daily_record, _ = request.user.daily_records.get_or_create(
        date=date_for_record)
    # meal_plan, _ = MealPlan.objects.get_or_create(user=request.user, date=date_for_plan)
    habit = Habit.objects.filter(pk=habit_pk)

    return render(
        request,
        "core/create_record.html",
        {
            "daily_record": daily_record,
            "habit": habit,
            "date": date_for_record,
            "next_day": next_day,
            "prev_day": prev_day,
        },
    )


@login_required
def list_records(request, pk):
    daily_records = DailyRecord.objects.filter(pk=pk)
    return render(request, "habits/list_records.html", {"daily_records": daily_records, "pk": pk})
