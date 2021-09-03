import core
from django.shortcuts import render, redirect, get_object_or_404
from .models import User, Habit, DailyRecord
from .forms import HabitForm
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
def habit_record(request, pk, habit_pk):
    habit = Habit.objects.filter(pk=pk)
    daily_records = DailyRecord.objects.filter(pk=habit_pk)
    ordered_records = daily_records.order_by('-date')
    return render(request, "habits/habit_record.html", {"habit": habit, "daily_records": ordered_records, "pk": pk, "habit_pk": habit_pk})
