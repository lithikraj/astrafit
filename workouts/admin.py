from django.contrib import admin
from .models import Workout, Exercise, ExerciseSet

class ExerciseSetInline(admin.TabularInline):
    model = ExerciseSet
    extra = 1  # Shows one empty row by default

class ExerciseInline(admin.StackedInline):
    model = Exercise
    extra = 1

@admin.register(Workout)
class WorkoutAdmin(admin.ModelAdmin):
    list_display = ('date', 'name')
    inlines = [ExerciseInline]

@admin.register(Exercise)
class ExerciseAdmin(admin.ModelAdmin):
    list_display = ('name', 'workout')
    inlines = [ExerciseSetInline]

@admin.register(ExerciseSet)
class ExerciseSetAdmin(admin.ModelAdmin):
    list_display = ('exercise', 'set_number', 'weight', 'reps')